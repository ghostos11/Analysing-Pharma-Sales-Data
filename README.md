# Analysing-Pharma-Sales-Data


Analysis of pharmacy sales data by drug category (ATC code), answering six questions about total sales, top sellers, seasonal trends, and more.

## Files

| File | Description |
|---|---|
| `drug_sales_analysis.py` | Plain Python script. Run with `python3 drug_sales_analysis.py`. |
| `drug_sales_analysis.ipynb` | Same analysis as a Jupyter notebook, with markdown explanations and pre-run outputs. |
| `salesdaily.csv` | **Not included** — place your own copy in the same folder before running (see below). |

## Data

This analysis expects `salesdaily.csv`, with one row per day and these columns:

- `datum` — date (`M/D/YYYY`)
- `M01AB`, `M01AE`, `N02BA`, `N02BE`, `N05B`, `N05C`, `R03`, `R06` — daily sales quantity per drug category (ATC code)
- `Year`, `Month`, `Hour`, `Weekday Name` — pre-split date parts

### ATC code reference

| Code | Category |
|---|---|
| M01AB, M01AE | Anti-inflammatory / anti-rheumatic drugs |
| N02BA, N02BE | Analgesics (N02BE includes paracetamol) |
| N05B, N05C | Anxiolytics / sedatives-hypnotics |
| R03 | Drugs for obstructive airway diseases (asthma/COPD) |
| R06 | Antihistamines |

**Note:** the dataset tracks sales by category only — there is no individual drug-brand or product-name column in the source data. Questions about "drugs" or "brands" are therefore answered at the category level, since that's the finest detail the data supports.

## Setup

pip install pandas
# for the notebook:
pip install jupyter nbconvert

Place `salesdaily.csv` in the same folder as the script/notebook.

## Running

**Script:**

python3 drug_sales_analysis.py

**Notebook:**

jupyter notebook drug_sales_analysis.ipynb

or open it directly in VS Code / JupyterLab and run all cells.

## Questions answered

1. Total sales quantity for each drug category
2. Highest-selling category ("brand")
3. Top 3 categories by sales in January 2015, July 2016, and September 2017
4. Category sold most often in 2017 (by total quantity and by frequency)
5. Category with the highest average daily sales
6. Seasonality of R03 (respiratory drug) sales by calendar month

## Key findings

- **N02BE** is the top-selling category overall, by total quantity, by average daily sales, and in every individual month checked — it's not close, outselling the next category by roughly 3x.
- **N02BE** and **N05B** take the top two spots in January 2015, July 2016, and September 2017; the third-place category


https://roadmap.sh/projects/pharmaceutical-sales-data
