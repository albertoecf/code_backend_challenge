# Helu.io - Code challenge for Backend Engineering 2022

## Context
The objective of this challenge is to calculate a simplified version of an income statement (a.k.a. profit and loss, or
P&L for short). Which is one of the main financial statements used to report the activities, position and
performance of a business. [More info](https://corporatefinanceinstitute.com/resources/knowledge/accounting/three-financial-statements/)


## Data
In order to be able to calculate the values for the P&L, we need first the raw material data provided by two csv files:
* bookings.csv : Journal entries are the record of the financial transactions we are going to use to calculate the totals.
  [More info](https://en.wikipedia.org/wiki/Bookkeeping)
* chart-of-accounts.csv : Chart of accounts (CoA) is where the accounts are categorized by its purpose and nature.
  [More info](https://en.wikipedia.org/wiki/Chart_of_accounts)

With the information contained in these two files, you have all the information you need to build the P&L report.  
**Note**: If there are some bookings in *bookings.csv* for accounts that are not listed in *chart-of-accounts.csv* - just ignore them.

## The challenge
Process the entries from the given files (bookings.csv and chart-of-accounts.csv) and calculate the results in order to
obtain the same result in such a way the test is passing. Meaning, providing the results throughout a REST endpoint.
We'll consider the quality of the code as a "production ready", not only a PoC.  
You are allowed to add/change any part of the code as long as it passes the test case.
### Results logistic
Please send the final solution in .zip archive (add your name to the archive name, so it is not messed up with other solutions). 
Please, do not include venv, pycache or any other not required folders and files to keep the zip file small.

## Formulas
`Revenues = (income credit) - (income debit)`  
`Expenses = (expense credit) - (expense debit)`  
`Profits = Revenues + Expenses`  we already inverted the values when calculating expenses  
`Margin = Profits / Revenues * 100`  
`Comparison between A and B = [Absolute = A - B, Percentage = Absolute / abs(B) * 100]`


## Run the app
`make up`

## Run tests
`make test`  

# Solution 

## Video
[Here](https://www.loom.com/share/70e2856b317e48e8a22561c8d592fd35?t=1&sid=5a9f33e8-8b01-4dc4-83c9-f5596ba59024)

## Repo
[Here](https://github.com/albertoecf/code_backend_challenge)


## Model-View-Controller (MVC) Approach
This project follows the Model-View-Controller (MVC) design pattern for structuring the application. The key components are as follows:

- **Model (models.py):** Defines the data model using Pydantic. The `IncomeStatement` class represents the financial statement.

- **View (main.py):** Implements the FastAPI application to expose endpoints for generating and downloading financial reports. The endpoint `/report` allows users to download the financial report in CSV format.

- **Controller (controllers.py):** Contains the `GenerateReport` class responsible for processing raw data, generating financial reports, and comparing income statements.

## Main Functionalities of Model and Controllers
### Model (models.py):
The `IncomeStatement` model has the following functionalities:

- **from_dataframe(cls, df):** Creates an `IncomeStatement` object from a given DataFrame.

### Controllers (controllers.py):
The `GenerateReport` class provides the following main functionalities:

- **generate_report(target_period):** Generates a financial report for the specified target period.

- **compare_income_statements(statement_a, statement_b):** Compares two income statements and returns the comparison results.

- **generate_and_save_report(new_period, old_period):** Generates and saves the financial report for new and old periods.


## ⚠️ Pending Improvements
Due to time constrain, the state of the current implementation, the output of `/report` is missing the comparison between June and May 2020 (%).


