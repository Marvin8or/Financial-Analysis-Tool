import os
import numpy as np
import pandas as pd
from typing import List, Dict


class AnalyticalEngine:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.features: List = list(data.columns)
        self.result_dict = {}

    def calculate_moving_averages(self, column="Close", windows=[5, 20, 50]):
        moving_avg_df = pd.DataFrame(index=self.data.index)

        for window in windows:
            ma_label = f"MA_{window}"
            moving_avg_df[ma_label] = (
                self.data[column].rolling(window=window).mean()
            )

        self.result_dict["moving_avg_df"] = moving_avg_df
        return moving_avg_df


    def calculate_daily_percentage_change(self, feature: str) -> Dict:
        data_as_numpy = self.data[feature].values
        mask = np.array([0, 1])
        dperc_change = np.empty(len(data_as_numpy))
        dperc_change[0] = np.nan
        idx = 1
        while mask[-1] < len(data_as_numpy):
            values = data_as_numpy[mask]
            values_diff = np.diff(values)
            dperc_change[idx] = values_diff[0] / values[0]
            idx += 1
            mask += 1

        dperc_change = dperc_change * 100
        self.result_dict[f"daily_percentage_change_{feature}"] = dperc_change


    def calculate_cumulative_returns(self, column="Close"):
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
