from pydantic import BaseModel
import pandas as pd


class IncomeStatement(BaseModel):
    revenue: float
    expense: float
    profit: float
    margin: float

    @classmethod
    def from_dataframe(cls, df: pd.DataFrame) -> "IncomeStatement":
        # Filter data for income and expense accounts
        income_credit = df[
            (df["account_nature"] == "income") & (df["transaction_type"] == "credit")
        ]
        income_debit = df[
            (df["account_nature"] == "income") & (df["transaction_type"] == "debit")
        ]
        expense_credit = df[
            (df["account_nature"] == "expense") & (df["transaction_type"] == "credit")
        ]
        expense_debit = df[
            (df["account_nature"] == "expense") & (df["transaction_type"] == "debit")
        ]

        # Calculate Revenues, Expenses, Profits, and Margin
        revenues = round(
            float((income_credit["amount"].sum() - income_debit["amount"].sum())), 2
        )
        expenses = round(
            float((expense_credit["amount"].sum() - expense_debit["amount"].sum())), 2
        )
        profits = round(float(revenues + expenses), 2)
        margin = round(float((profits / revenues) * 100) if revenues != 0 else 0, 1)

        return cls(revenue=revenues, expense=expenses, profit=profits, margin=margin)
