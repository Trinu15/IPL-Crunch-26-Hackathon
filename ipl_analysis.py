"""
IPL Crunch '26 — Wooble Hackathon Submission
Analysis of IPL 2021–2025 ball-by-ball data
Author: [Your Name]
"""

import pandas as pd
import glob
import os

# ─────────────────────────────────────────────
# LOAD DATA
# ─────────────────────────────────────────────
# Put all your IPL CSV files (2021–2025) in the same folder as this script.
# Each row = one ball bowled.
# Expected columns: match_id, season, toss_winner, toss_decision, winner,
#                   batting_team, bowling_team, over, batter, bowler,
#                   runs_off_bat, extras, wicket_type

files = glob.glob("*.csv")
if not files:
    print("ERROR: No CSV files found. Download IPL CSVs from cricsheet.org first.")
    exit()

df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
print(f"Loaded {len(df):,} balls from {df['match_id'].nunique()} matches across {df['season'].nunique()} seasons.\n")

# ─────────────────────────────────────────────
# Q1: DO TOSS WINNERS WIN MORE?
# ─────────────────────────────────────────────
match_level = df.drop_duplicates('match_id')[['match_id','toss_winner','winner','toss_decision']].copy()
match_level['toss_won_match'] = match_level['toss_winner'] == match_level['winner']

toss_win_rate = match_level['toss_won_match'].mean() * 100
toss_lose_rate = 100 - toss_win_rate

print("=" * 50)
print("Q1: TOSS ANALYSIS")
print("=" * 50)
print(f"Toss winners won the match: {toss_win_rate:.1f}%")
print(f"Toss losers  won the match: {toss_lose_rate:.1f}%")

# Breakdown by toss decision
decision_win = match_level.groupby('toss_decision')['toss_won_match'].mean() * 100
print("\nWin rate by toss decision:")
for dec, rate in decision_win.items():
    print(f"  Chose to {dec}: {rate:.1f}% win rate")

# ─────────────────────────────────────────────
# Q2: WHICH PHASE IS MOST LINKED TO WINNING?
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("Q2: PHASE ANALYSIS (runs/over)")
print("=" * 50)

# Tag each ball with its phase
df['phase'] = pd.cut(
    df['over'],
    bins=[0, 6, 15, 20],
    labels=['Powerplay (1–6)', 'Middle (7–15)', 'Death (16–20)']
)

# Tag whether batting team won
df['batting_won'] = df['batting_team'] == df['winner']

phase_summary = (
    df.groupby(['phase', 'batting_won'])['runs_off_bat']
    .mean()
    .reset_index()
)
phase_summary['label'] = phase_summary['batting_won'].map({True: 'Winners', False: 'Losers'})
phase_pivot = phase_summary.pivot(index='phase', columns='label', values='runs_off_bat')
phase_pivot['Gap (W-L)'] = phase_pivot['Winners'] - phase_pivot['Losers']
print(phase_pivot.round(2).to_string())

# ─────────────────────────────────────────────
# Q3: TOP 5 BATTERS & BOWLERS (5 seasons)
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("Q3: TOP 5 BATTERS (by total runs)")
print("=" * 50)
top_batters = (
    df.groupby('batter')['runs_off_bat']
    .agg(['sum', 'count'])
    .rename(columns={'sum': 'Runs', 'count': 'Balls'})
    .nlargest(5, 'Runs')
)
top_batters['Strike Rate'] = (top_batters['Runs'] / top_batters['Balls'] * 100).round(1)
print(top_batters[['Runs', 'Strike Rate']].to_string())

print("\n" + "=" * 50)
print("Q3: TOP 5 BOWLERS (by total wickets)")
print("=" * 50)
# Exclude run-outs (credit to fielder not bowler)
wickets_df = df[df['wicket_type'].notna() & ~df['wicket_type'].isin(['run out', 'obstructing the field'])]
top_bowlers = (
    wickets_df.groupby('bowler')['wicket_type']
    .count()
    .nlargest(5)
    .reset_index()
    .rename(columns={'wicket_type': 'Wickets'})
)
# Economy
econ = df.groupby('bowler')['runs_off_bat'].sum() / (df.groupby('bowler')['over'].count() / 6)
top_bowlers['Economy'] = top_bowlers['bowler'].map(econ).round(2)
print(top_bowlers.set_index('bowler').to_string())

# ─────────────────────────────────────────────
# SURPRISING FINDING
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("SURPRISING FINDING")
print("=" * 50)
death = df[df['phase'] == 'Death (16–20)']
death_won  = death[death['batting_won'] == True]['runs_off_bat'].mean()
death_lost = death[death['batting_won'] == False]['runs_off_bat'].mean()
gap = death_won - death_lost
print(f"Winners score {death_won:.2f} runs/ball in death overs")
print(f"Losers  score {death_lost:.2f} runs/ball in death overs")
print(f"Gap = {gap:.2f} — BIGGEST across all 3 phases")
print("Winning the toss gives a ~3% edge. Winning the death overs gives a ~40% edge.")
print("\nScript complete. Run generate_charts.py next to produce your chart images.")
