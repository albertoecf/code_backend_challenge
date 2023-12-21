from data_processing import (
    process_raw_files,
    df_preproceesing,
    group_year_month_metrics,
)
from models import IncomeStatement


class GenerateReport:
    """
    A class responsible for generating a financial report based on raw data.

    Methods:
        generate_report(): Generates and returns a financial report given the target month and year.
        Saves the provided DataFrame to the result file in CSV format.
    """

    def __init__(self, bookings_path, accounts_path, result_path):
        """
        Initializes the GenerateReport instance.

        Args:
            bookings_path (str): The file path to the bookings data.
            accounts_path (str): The file path to the chart of accounts data.
            result_path (str): The file path to store the generated report.
        """
        self.bookings_path = bookings_path
        self.accounts_path = accounts_path
        self.result_path = result_path

    def generate_report(self):
        """
        Generates a financial report, saves it into self.result_path and return the str of result_path

        """

        try:
            # Process raw files and generate the report
            merged_df = process_raw_files(self.bookings_path, self.accounts_path)

            # todo: accept as parameters
            target_month = 5
            target_year = 2020

            # preprocess given df and targets
            preproceesed = df_preproceesing(merged_df)
            income_statment_df = group_year_month_metrics(
                preproceesed, target_year, target_month
            )

            # create IncomeStatement instance from df
            income_statement = IncomeStatement.from_dataframe(income_statment_df)
            return income_statement
            # todo save the file
            # return file_path

        except Exception as e:
            # todo raise better exceptions
            raise e
