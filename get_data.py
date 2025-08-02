# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 16:59:43 2025

@author: gabri
"""
import yfinance as yf

# Download historical data for Apple (AAPL)
data = yf.download("AAPL", start="2020-01-01", end="2023-01-01")

# Display the first 5 rows of the data
print(data.head())
