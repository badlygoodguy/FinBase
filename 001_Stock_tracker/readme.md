Stock Tracker

Project Purpose

This script is designed to download historical stock data and store it in a local database for analysis.

Prerequisites

To run this script, you need to have the following Python libraries installed:

• `yfinance`
• `pandas`


You can install them using pip:

```
`pip install yfinance pandas`
```

How to Use

1. Configure the script: Open the `stock_data_import.py` file and modify the list of stock tickers and the date range to suit your needs.
2. The currently included stock tickers are Apple, LVMH, SAP, Toyota and Lloyds. The data collection start date is set to 01 Jan 1990
3. Run the script: Execute the script from your terminal.


```
`python stock_data_import.py`
```

4. Database File: The script will automatically create a file named `stock_prices.db` in the same directory. This is your local database containing the downloaded stock data. This file is not intended to be shared on GitHub and is excluded via the `.gitignore` file.
