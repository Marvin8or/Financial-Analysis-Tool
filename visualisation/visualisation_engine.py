# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 21:33:39 2025

@author: gabri
"""
import os
import matplotlib.pyplot as plt
from typing import Dict

ResultsDict = Dict


class VisualisationEngine:
    def __init__(self, raw_data: pd.DataFrame, data: ResultsDict, results_path):
        self.raw_data = raw_data
        self.results_dict = data
        self.results_path = results_path
        
        os.makedirs(self.results_path, exist_ok=True)

    def visualise_moving_averages(self):
        ma_keys = [key for key in self.results_dict if key.startswith("MA_")]

        if not ma_keys:
            print("No moving averages found in results_dict.")
            return

        for ma_key in ma_keys:
            try:
                _, col_name, window_str = ma_key.split("_")
                window = int(window_str)
            except ValueError:
                print(f"Skipping invalid key: {ma_key}")
                continue

            if col_name not in self.raw_data.columns:
                print(f"Column '{col_name}' not found in raw data. Skipping {ma_key}.")
                continue

            plt.figure(figsize=(12, 6))

            plt.plot(self.raw_data[col_name], label=col_name, linewidth=1.5)
            plt.plot(self.results_dict[ma_key], label=f"MA {window}", linestyle='--')

            plt.title(f"{col_name} with {window}-Day Moving Average")
            plt.xlabel("Date")
            plt.ylabel("Value")
            plt.legend()
            plt.grid(True)

            filename = os.path.join(self.results_path, f"{ma_key}.png")
            plt.savefig(filename)
            plt.close()

            print(f"Saved plot: {filename}")
            return


    def visualise_daily_percentage_change(self):
        pass