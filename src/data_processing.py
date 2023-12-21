#todo, refactor into controllers as methods
import pandas as pd

def process_raw_files(bookings_file_path, chart_of_accounts_file_path):
    # Read CSV files into DataFrames
    bookings_df = pd.read_csv(bookings_file_path)
    chart_of_accounts_df = pd.read_csv(chart_of_accounts_file_path)

    merged_df = pd.merge(
        bookings_df, chart_of_accounts_df, on="account_code", how="inner"
    )

    return merged_df


def df_preproceesing(df: pd.DataFrame) -> pd.DataFrame:
    df["amount"] = pd.to_numeric(df["amount"].str.replace(",", "."), errors="coerce")
    df["transaction_date"] = pd.to_datetime(df["transaction_date"], format="%Y-%m-%d")
    df.drop(columns=["account_code"], inplace=True)
    df["month"] = df["transaction_date"].dt.month
    df["year"] = df["transaction_date"].dt.year
    return df


def group_year_month_metrics(
    df: pd.DataFrame, target_year: int, target_month: int
) -> pd.DataFrame():
    reduce = df[df["month"] == target_month]
    filtered_df = reduce[reduce["year"] == target_year]
    grouped_df = (
        filtered_df.groupby(["account_nature", "transaction_type"])["amount"]
        .sum()
        .reset_index()
    )
    return grouped_df
