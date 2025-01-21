
import numpy as np
import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as print
import yfinance as yf

def get_financial_statement(ticker_symbol, statement_type):
    """
    Retrieve the specified financial statement for a given ticker.
    Args:
    - ticker_symbol: The ticker symbol of the company (e.g., 'MSFT').
    - statement_type: The financial statement to retrieve ('balance_sheet', 'income_stmt', 'cashflow').

    Returns:
    - The requested financial statement as a Pandas DataFrame.
    """
    company = yf.Ticker(ticker_symbol)
    year=company.balance_sheet.columns

    if statement_type == 'balance_sheet':
        return company.balance_sheet
    elif statement_type == 'income_stmt':
        return company.financials
    elif statement_type == 'cashflow':
        return company.cashflow
    else:
        raise ValueError("Invalid statement_type. Choose from 'balance_sheet', 'income_stmt', or 'cashflow'.")

def get_financial_statement_update(ticker_symbol, statement_type, n):
    """
    Retrieve the specified financial statement for a given ticker.
    Args:
    - ticker_symbol: The ticker symbol of the company (e.g., 'MSFT').
    - statement_type: The financial statement to retrieve ('balance_sheet', 'income_stmt', 'cashflow').
    - n: Index of the desired financial statement period.

    Returns:
    - The requested financial statement as a Pandas Series or DataFrame.
    """
    company = yf.Ticker(ticker_symbol)

    # Select the statement type
    if statement_type == 'balance_sheet':
        statement = company.balance_sheet
    elif statement_type == 'income_stmt':
        statement = company.financials
    elif statement_type == 'cashflow':
        statement = company.cashflow
    else:
        raise ValueError("Invalid statement_type. Choose from 'balance_sheet', 'income_stmt', or 'cashflow'.")

    # Get available dates
    available_dates = statement.columns

    # Validate the index
    if n >= len(available_dates):
        raise IndexError(f"Index {n} is out of range. Available indices are 0 to {len(available_dates) - 1}.")

    # Retrieve the data for the requested date
    return statement[available_dates[n]]

    
def rows(ticker_symbol, statement_type):
    company = yf.Ticker(ticker_symbol)

    if statement_type == 'balance_sheet':
        return company.balance_sheet.index.tolist()
    elif statement_type == 'income_stmt':
        return company.income_stmt.index.tolist()
    elif statement_type == 'cashflow':
        return company.cashflow.index.tolist()
    else:
        raise ValueError("Invalid statement_type. Choose from 'balance_sheet', 'income_stmt', or 'cashflow'.")