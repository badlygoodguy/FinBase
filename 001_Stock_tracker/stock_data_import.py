import yfinance as yf #Needed for stock data retrieval
import pandas as pd #Needed for data manipulation
import sqlite3 #Needed for database connection

# Get from 01 Jan 1990 for Apple if available
aapl_ticker = yf.Ticker("AAPL")
aapl_hist = aapl_ticker.history(start="1990-01-01")

# from 01 Jan 1990 for LVMH if available
lvmh_ticker = yf.Ticker("MC.PA")
lvmh_hist = lvmh_ticker.history(start="1990-01-01")

# from 01 Jan 1990 for SAP if available
sap_ticker = yf.Ticker("SAP.DE")
sap_hist = sap_ticker.history(start="1990-01-01")

# Get from 01 Jan 1990 for Toyota if available
toyota_ticker = yf.Ticker("7203.T")
toyota_hist = toyota_ticker.history(start="1990-01-01")

# Get data from 01 Jan 1990 for Lloyds if available
lloyds_ticker = yf.Ticker("LLOY.L")
lloyds_hist = lloyds_ticker.history(start="1990-01-01")

# Define a list of the DataFrames and their corresponding table names
dfs_to_save = {
    'AAPL': aapl_hist,
    'LVMH': lvmh_hist,
    'SAP': sap_hist,
    'TOYOTA': toyota_hist,
    'LLOYDS': lloyds_hist
}

# Create a database connection
conn = sqlite3.connect('stock_prices.db')
# This will create a file named 'stock_prices.db' if it doesn't already exist

# Use a loop to write each DataFrame to its own table in the database
for ticker, df in dfs_to_save.items():
    try:
        df.to_sql(ticker, conn, if_exists='replace', index=True)
        print(f"Successfully saved {ticker} data to the database.")
    except Exception as e:
        print(f"Failed to save {ticker} data: {e}")

# Close the connection when you're done
conn.close()

print("All data has been saved and the database connection is closed.")