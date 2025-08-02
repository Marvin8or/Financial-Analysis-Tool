import pandas as pd
import os

class AnalyticalEngine:
    def __init__(self, data: pd.DataFrame):
        self.data = data.copy()
        self.result_dict = {}

    def calculate_moving_averages(self, column='Close', windows=[5, 20, 50]):
        moving_avg_df = pd.DataFrame(index=self.data.index)

        for window in windows:
            ma_label = f"MA_{window}"
            moving_avg_df[ma_label] = self.data[column].rolling(window=window).mean()

        self.result_dict["moving_avg_df"] = moving_avg_df
        return moving_avg_df

    def export_moving_averages_to_csv(self, filename='moving_averages.csv', folder='datasets'):
        moving_avg_df = self.result_dict.get("moving_avg_df")

        if moving_avg_df is None:
            raise ValueError("You must calculate moving averages before exporting.")

        os.makedirs(folder, exist_ok=True)
        filepath = os.path.join(folder, filename)
        moving_avg_df.to_csv(filepath)
        print(f"Moving averages saved to '{filepath}'")
