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

    def export_moving_averages_to_csv(
        self, filename="moving_averages.csv", folder="datasets"
    ):
        moving_avg_df = self.result_dict.get("moving_avg_df")

        if moving_avg_df is None:
            raise ValueError(
                "You must calculate moving averages before exporting."
            )

        os.makedirs(folder, exist_ok=True)
        filepath = os.path.join(folder, filename)
        moving_avg_df.to_csv(filepath)
        print(f"Moving averages saved to '{filepath}'")

    def calculate_daily_percentage_change(self, feature: str) -> Dict:
        pass


if __name__ == "__main__":
    data = pd.read_csv(
        "C:/Projects/Quant Analysis/quant_analysis/src/datasets/I500.DE_20250802-210754.csv"
    )
    aeng = AnalyticalEngine(data)
