import os
import numpy as np
import pandas as pd
from typing import List, Dict


class AnalyticalEngine:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.features: List = list(data.columns)
        self.result_dict = {}

    def calculate_moving_averages(self, column="Close", window = 20):
        ma_label = f"MA_{window}"
        moving_avg = self.data[column].rolling(window=window).mean()
        self.result_dict[ma_label] = moving_avg

        return moving_avg

    def calculate_daily_percentage_change(
        self, feature: str = "Close"
    ) -> None:
        data_as_numpy = self.data[feature].values
        dperc_change = np.empty(len(data_as_numpy))
        dperc_change[0] = np.nan
        dperc_change[1:] = np.diff(data_as_numpy) / data_as_numpy[:-1]
        self.result_dict[f"daily_percentage_change_{feature}"] = dperc_change
        return dperc_change

    def calculate_closing_price_volatility(self, time_frame: int = 252):
        # Daily returns
        data_as_numpy = self.data["Close"].values
        daily_returns = np.log(data_as_numpy[1:] / data_as_numpy[:-1])
        daily_returns_std = np.std(daily_returns)

        rel_volatility = float(daily_returns_std * np.sqrt(time_frame) * 100)
        self.result_dict[f"relative_volatility_{time_frame}"] = rel_volatility
        return rel_volatility

    def calculate_cumulative_returns(self, column: str = "Close"):
        price_series = self.data[column]
        initial_price = price_series.iloc[0]

        cumulative_returns = (price_series / initial_price) - 1

        self.result_dict["cumulative_returns"] = cumulative_returns
        return cumulative_returns


if __name__ == "__main__":
    data = pd.read_csv(
        "C:/Projects/Quant Analysis/quant_analysis/src/datasets/I500.DE_20250802-210754.csv"
    )
    aeng = AnalyticalEngine(data)
    aeng.calculate_daily_percentage_change("Close")
    aeng.calculate_closing_price_volatility()
