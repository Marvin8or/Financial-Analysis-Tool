# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 16:59:43 2025

@author: gabri
"""
import os
import argparse
import yfinance as yf
from datetime import datetime


def get_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--ticker", required=True, type=str, help="Stock or ETF ticker"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = get_arguments()
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    data = yf.download(args.ticker, period="max")

    if not data.empty:
        print(f"Successfully downloaded data for {args.ticker}.")
        print(data.head())

        filename = f"{args.ticker}_{timestamp}.csv"
        data.to_csv(os.path.join("datasets", filename))

        print(f"\nData saved to '{filename}' in folder 'datasets'.")
