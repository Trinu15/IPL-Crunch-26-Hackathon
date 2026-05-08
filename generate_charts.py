"""
IPL Crunch '26 — Chart Generator
Produces chart1_toss.png and chart2_phases.png
Run this script: python generate_charts.py
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': True,
    'grid.alpha': 0.25,
    'grid.linestyle': '--'
})

# ─────────────────────────────────────────────
# CHART 1 — TOSS WIN RATE
# ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 4.5))

categories  = ['Toss Winners\n(chose to field)', 'Toss Winners\n(chose to bat)', 'Toss Losers']
values      = [58.1, 47.9, 47.2]
colors      = ['#3266ad', '#7fa8d8', '#73726c']

bars = ax.bar(categories, values, color=colors, width=0.5, zorder=3, edgecolor='white', linewidth=1.2)

for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.4,
            f'{val}%', ha='center', va='bottom', fontsize=13, fontweight='bold',
            color='#222')

ax.set_ylim(40, 65)
ax.set_ylabel('Win Rate (%)', fontsize=12)
ax.set_title('Do toss winners win more?\nIPL 2021–2025 (5 seasons, ~370 matches)',
             fontsize=13, fontweight='bold', pad=12)
ax.axhline(50, color='red', linewidth=1, linestyle=':', alpha=0.6, label='50% (coin flip)')
ax.legend(fontsize=10)
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)

plt.tight_layout()
plt.savefig('chart1_toss.png', dpi=180, bbox_inches='tight')
plt.close()
print("✓ chart1_toss.png saved")


# ─────────────────────────────────────────────
# CHART 2 — PHASE-WISE RUNS
# ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 4.5))

phases  = ['Powerplay\n(Overs 1–6)', 'Middle Overs\n(Overs 7–15)', 'Death Overs\n(Overs 16–20)']
winners = [8.6, 8.3, 11.4]
losers  = [8.1, 7.9,  9.6]
gaps    = [w - l for w, l in zip(winners, losers)]

x = np.arange(len(phases))
width = 0.35

b1 = ax.bar(x - width/2, winners, width, label='Winners', color='#1D9E75',
            zorder=3, edgecolor='white', linewidth=1)
b2 = ax.bar(x + width/2, losers,  width, label='Losers',  color='#D4537E',
            zorder=3, edgecolor='white', linewidth=1)

for bar, val in zip(b1, winners):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
            f'{val}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='#1D9E75')

for bar, val in zip(b2, losers):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
            f'{val}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='#D4537E')

# Gap annotation
for i, (w, l, g) in enumerate(zip(winners, losers, gaps)):
    mid = (w + l) / 2
    ax.annotate(f'Gap: +{g:.1f}', xy=(x[i], mid + 0.2),
                ha='center', va='bottom', fontsize=9,
                color='#555', fontstyle='italic')

ax.set_ylim(6, 13.5)
ax.set_xticks(x)
ax.set_xticklabels(phases, fontsize=10)
ax.set_ylabel('Average Runs per Over', fontsize=12)
ax.set_title('Which phase decides IPL matches?\nWinners vs Losers — IPL 2021–2025',
             fontsize=13, fontweight='bold', pad=12)
ax.legend(fontsize=11)

plt.tight_layout()
plt.savefig('chart2_phases.png', dpi=180, bbox_inches='tight')
plt.close()
print("✓ chart2_phases.png saved")


# ─────────────────────────────────────────────
# BONUS: TOP PERFORMERS BAR CHART
# ─────────────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

# Top batters
batters = ['Virat Kohli', 'Ruturaj Gaikwad', 'Sai Sudharsan', 'Shubman Gill', 'SKY']
runs    = [3146, 2427, 2219, 2184, 1987]
colors_b = ['#3266ad'] + ['#7fa8d8'] * 4

bars = ax1.barh(batters[::-1], runs[::-1], color=colors_b[::-1],
                zorder=3, edgecolor='white')
for bar, val in zip(bars, runs[::-1]):
    ax1.text(val + 30, bar.get_y() + bar.get_height()/2,
             f'{val:,}', va='center', fontsize=10, fontweight='bold')
ax1.set_xlim(0, 3600)
ax1.set_xlabel('Total Runs', fontsize=11)
ax1.set_title('Top 5 Batters\nIPL 2021–2025', fontsize=12, fontweight='bold')
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)

# Top bowlers
bowlers = ['Y. Chahal', 'J. Bumrah', 'P. Krishna', 'Harshal Patel', 'Arshdeep']
wickets = [112, 98, 91, 88, 85]
colors_w = ['#6B21A8'] + ['#a855f7'] * 4

bars2 = ax2.barh(bowlers[::-1], wickets[::-1], color=colors_w[::-1],
                 zorder=3, edgecolor='white')
for bar, val in zip(bars2, wickets[::-1]):
    ax2.text(val + 1, bar.get_y() + bar.get_height()/2,
             f'{val}', va='center', fontsize=10, fontweight='bold')
ax2.set_xlim(0, 130)
ax2.set_xlabel('Total Wickets', fontsize=11)
ax2.set_title('Top 5 Bowlers\nIPL 2021–2025', fontsize=12, fontweight='bold')
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)

plt.suptitle('IPL 2021–2025 · Top Performers', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('chart3_performers.png', dpi=180, bbox_inches='tight')
plt.close()
print("✓ chart3_performers.png saved")
print("\nAll charts generated! Upload chart1_toss.png, chart2_phases.png to Wooble.")
