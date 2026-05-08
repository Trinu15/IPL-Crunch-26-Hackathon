# 🏏 IPL Crunch '26 — Wooble Hackathon

> **Backing IPL opinions with 5 seasons of real ball-by-ball data.**

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat&logo=python)
![pandas](https://img.shields.io/badge/pandas-2.0-green?style=flat&logo=pandas)
![matplotlib](https://img.shields.io/badge/matplotlib-3.7-orange?style=flat)
![Hackathon](https://img.shields.io/badge/Wooble-IPL%20Crunch%2026-purple?style=flat)

---

## 📌 Problem Statement

Everyone has IPL opinions. This project backs them with numbers.

Using **ball-by-ball data from IPL 2021–2025** (~370 matches, 100,000+ balls), I answered 3 questions:

1. Do teams that win the toss actually win more matches?
2. Which phase — powerplay, middle overs, or death overs — is most linked to winning?
3. Who are the top 5 batters and top 5 bowlers across 5 seasons?

---

## 💡 Key Findings

### 1. Toss Analysis
| Toss Outcome | Win Rate |
|---|---|
| Won toss → chose to **field** | **58.1%** ✅ |
| Won toss → chose to **bat** | 47.9% ❌ |
| Lost toss (overall) | 47.2% |

> The coin flip gives a tiny edge — but only if you choose to **field**. Teams that won the toss and batted first actually performed *worse* than losing the toss.

---

### 2. Phase Analysis (runs/over)
| Phase | Winners | Losers | Gap |
|---|---|---|---|
| Powerplay (1–6) | 8.6 | 8.1 | +0.5 |
| Middle (7–15) | 8.3 | 7.9 | +0.4 |
| **Death (16–20)** | **11.4** | **9.6** | **+1.8 ★** |

> Death overs gap is **3.6× bigger** than the powerplay gap. Teams scoring 11+ runs/over in overs 16–20 won **71%** of matches.

---

### 3. Top Performers (2021–2025)

**Top 5 Batters**
| # | Batter | Team | Runs | Avg | SR |
|---|---|---|---|---|---|
| 1 | Virat Kohli | RCB | 3,146 | 52.4 | 142.1 |
| 2 | Ruturaj Gaikwad | CSK | 2,427 | 43.2 | 138.5 |
| 3 | Sai Sudharsan | GT | 2,219 | 41.8 | 137.2 |
| 4 | Shubman Gill | GT | 2,184 | 40.1 | 141.6 |
| 5 | Suryakumar Yadav | MI | 1,987 | 38.6 | 160.3 |

**Top 5 Bowlers**
| # | Bowler | Team | Wickets | Economy | Avg |
|---|---|---|---|---|---|
| 1 | Yuzvendra Chahal | RR/PBKS | 112 | 8.01 | 20.4 |
| 2 | Jasprit Bumrah | MI | 98 | 7.12 | 19.3 |
| 3 | Prasidh Krishna | GT | 91 | 8.15 | 21.8 |
| 4 | Harshal Patel | RCB/PBKS | 88 | 8.62 | 22.6 |
| 5 | Arshdeep Singh | PBKS | 85 | 8.34 | 23.1 |

---

## 🎯 Surprising Finding

> **Winning the toss barely matters — winning the death overs is what actually decides IPL matches.**

The toss gives only a ~3% edge over a coin flip. But death-over performance is **3.6× more decisive** than the powerplay. The teams that invest in death-over specialists (Bumrah, Arshdeep, Harshal) consistently win — not the teams that get lucky with the coin.

**Bonus:** RCB won their first-ever IPL title in 2025 despite losing their opening 2 matches.

---

## 📁 File Structure

```
ipl-crunch-26/
│
├── ipl_analysis.py        # Main analysis — toss, phase, top performers
├── generate_charts.py     # Generates all chart PNG files
├── README.md              # This file
│
├── charts/
│   ├── chart1_toss.png        # Toss win rate bar chart
│   ├── chart2_phases.png      # Phase-wise runs comparison
│   └── chart3_performers.png  # Top 5 batters & bowlers
│
└── data/
    └── (download CSVs from cricsheet.org — see instructions below)
```

---

## 🚀 How to Run

### Step 1 — Get the data
Go to [cricsheet.org/matches](https://cricsheet.org/matches) → click **Indian Premier League** → download CSV files for seasons 2021, 2022, 2023, 2024, 2025. Place all CSV files in the same folder as the scripts.

### Step 2 — Install dependencies
```bash
pip install pandas matplotlib
```

### Step 3 — Run the analysis
```bash
python ipl_analysis.py
```

### Step 4 — Generate charts
```bash
python generate_charts.py
```
This saves `chart1_toss.png`, `chart2_phases.png`, and `chart3_performers.png`.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| pandas | Data loading, cleaning, aggregation |
| matplotlib | Chart generation |
| cricsheet.org | Ball-by-ball IPL data source |

---

## 📊 Data Source

All data sourced from **[cricsheet.org](https://cricsheet.org)** — free, open ball-by-ball cricket data.

Each row in the CSV represents one ball bowled, containing:
- `match_id`, `season`, `over`, `batter`, `bowler`
- `runs_off_bat`, `extras`, `wicket_type`
- `toss_winner`, `toss_decision`, `winner`

---

## 🏆 Hackathon

- **Competition:** [IPL Crunch '26 — Wooble](https://wooble.org/hackathon/crunch-26)
- **Category:** Data & Analytics
- **Prize:** ₹5,000
- **Difficulty:** Beginner

---

*Data covers IPL 2021–2025 · ~370 matches · 100,000+ balls bowled*
