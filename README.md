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
