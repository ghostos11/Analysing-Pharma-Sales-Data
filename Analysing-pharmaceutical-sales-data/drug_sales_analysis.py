
import pandas as pd


# Load data

daily = pd.read_csv("salesdaily.csv")
daily["datum"] = pd.to_datetime(daily["datum"], format="%m/%d/%Y")

ATC_COLS = ["M01AB", "M01AE", "N02BA", "N02BE", "N05B", "N05C", "R03", "R06"]


# 1. Total sales quantity for each drug category

def total_sales_by_category(df):
    return df[ATC_COLS].sum().sort_values(ascending=False)



# 2. Highest-selling individual "drug brand"
#    (no brand column exists -> same result as category totals)


def highest_selling_category(df):
    totals = total_sales_by_category(df)
    return totals.index[0], totals.iloc[0]


# 3. Top 3 categories for specific year/month combinations


def top3_for_month(df, year, month):
    mask = (df["Year"] == year) & (df["Month"] == month)
    return df.loc[mask, ATC_COLS].sum().sort_values(ascending=False).head(3)



# 4. Category sold most often in 2017
#    - "most" by total quantity, and by frequency (days with any sales)

def most_sold_in_year(df, year):
    sub = df[df["Year"] == year]
    by_quantity = sub[ATC_COLS].sum().sort_values(ascending=False)
    by_frequency = (sub[ATC_COLS] > 0).sum().sort_values(ascending=False)
    return by_quantity, by_frequency


# 5. Category with the highest average daily sales

def highest_average_daily_sales(df):
    return df[ATC_COLS].mean().sort_values(ascending=False)


# 6. Seasonality check for R03 (respiratory drugs)

def r03_seasonality(df):
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    result = df.groupby("Month")["R03"].agg(["sum", "mean"]).round(2)
    result.index = month_names
    return result.sort_values("sum", ascending=False)


# Run everything and print results

if __name__ == "__main__":
    print("=== 1. Total sales by category (full period) ===")
    print(total_sales_by_category(daily), "\n")

    print("=== 2. Highest-selling category ('brand') ===")
    cat, qty = highest_selling_category(daily)
    print(f"{cat}: {qty:.2f} total units\n")

    print("=== 3. Top 3 categories by month ===")
    for year, month, label in [(2015, 1, "January 2015"),
                                (2016, 7, "July 2016"),
                                (2017, 9, "September 2017")]:
        print(f"--- {label} ---")
        print(top3_for_month(daily, year, month), "\n")

    print("=== 4. Most-sold category in 2017 ===")
    by_qty, by_freq = most_sold_in_year(daily, 2017)
    print("By total quantity:")
    print(by_qty, "\n")
    print("By frequency (days with nonzero sales):")
    print(by_freq, "\n")

    print("=== 5. Highest average daily sales by category ===")
    print(highest_average_daily_sales(daily), "\n")

    print("=== 6. R03 sales by calendar month (seasonality) ===")
    print(r03_seasonality(daily))