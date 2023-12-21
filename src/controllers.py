import pandas as pd
from src.models import IncomeStatement


class GenerateReport:
    """
    A class responsible for generating a financial report based on raw data.

    Methods:
        generate_report(): Generates and returns a financial report given the target month and year.
        Saves the provided DataFrame to the result file in CSV format.
    """

    def __init__(self, bookings_file_path, chart_of_accounts_file_path):
        """
        Initializes the GenerateReport instance.

        Args:
            bookings_path (str): The file path to the bookings data.
            accounts_path (str): The file path to the chart of accounts data.
            result_path (str): The file path to store the generated report.
        """
        self.bookings_file_path = bookings_file_path
        self.chart_of_accounts_file_path = chart_of_accounts_file_path

    def generate_report(self, target_period=None):
        """
        Generates a financial report, saves it into self.result_path and return the str of result_path

        Args:
            target_period (dict): Dictionary containing 'year' and 'month' for the target period.

        Returns:
            IncomeStatement: The generated financial report.
        """
        # Validate target_period
        if target_period is None or not isinstance(target_period, dict):
            raise ValueError("Invalid target_period. Please provide a dictionary.")

        year = target_period.get("year")
        month = target_period.get("month")

        if not isinstance(year, int) or not (1900 <= year <= 2100):
            # we could get min and max year from existing df
            raise ValueError("Invalid year. Please provide a 4-digit integer.")

        if not isinstance(month, int) or not (1 <= month <= 12):
            raise ValueError(
                "Invalid month. Please provide an integer between 1 and 12."
            )

        # Process raw files
        merged_df = self._process_raw_files()

        # Preprocess DataFrame
        processed_df = self._df_preprocessing(merged_df)

        # Generate report for the specified period
        grouped_df = self._group_year_month_metrics(processed_df, year, month)

        # Convert to IncomeStatement object
        income_statement = IncomeStatement.from_dataframe(grouped_df)

        return income_statement

    def _process_raw_files(self):
        # Read CSV files into DataFrames
        bookings_df = pd.read_csv(self.bookings_file_path)
        chart_of_accounts_df = pd.read_csv(self.chart_of_accounts_file_path)

        # Merge DataFrames
        merged_df = pd.merge(
            bookings_df, chart_of_accounts_df, on="account_code", how="inner"
        )

        return merged_df

    def _df_preprocessing(self, df):
        # DataFrame preprocessing
        df["amount"] = pd.to_numeric(
            df["amount"].str.replace(",", "."), errors="coerce"
        )
        df["transaction_date"] = pd.to_datetime(
            df["transaction_date"], format="%Y-%m-%d"
        )
        df.drop(columns=["account_code"], inplace=True)
        df["month"] = df["transaction_date"].dt.month
        df["year"] = df["transaction_date"].dt.year

        return df

    def _group_year_month_metrics(self, df, target_year, target_month):
        # Group metrics by year and month
        reduce = df[df["month"] == target_month]
        filtered_df = reduce[reduce["year"] == target_year]
        grouped_df = (
            filtered_df.groupby(["account_nature", "transaction_type"])["amount"]
            .sum()
            .reset_index()
        )
        return grouped_df

    def compare_income_statements(self, statement_a, statement_b):
        """
        Compares two income statements and returns the comparison results.

        Args:
            statement_a (IncomeStatement): The first income statement.
            statement_b (IncomeStatement): The second income statement.

        Returns:
            dict: A dictionary containing the comparison results.
        """
        # Calculate absolute and percentage differences for each metric
        comparison_results = {
            "Revenues": self._compare_metrics(statement_a.revenue, statement_b.revenue),
            "Expenses": self._compare_metrics(statement_a.expense, statement_b.expense),
            "Profits": self._compare_metrics(statement_a.profit, statement_b.profit),
            "Margins": self._compare_metrics(statement_a.margin, statement_b.margin),
        }

        return comparison_results

    def _compare_metrics(self, metric_a, metric_b):
        """
        Compares two metrics and returns the comparison results.

        Args:
            metric_a (float): The first metric.
            metric_b (float): The second metric.

        Returns:
            dict: A dictionary containing the absolute and percentage differences.
        """
        absolute_difference = metric_a - metric_b
        percentage_difference = (
            absolute_difference / abs(metric_b) * 100 if abs(metric_b) != 0 else 0
        )

        return {
            "Absolute": round(absolute_difference, 2),
            "Percentage": round(percentage_difference, 1),
        }
