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

    def visualise_daily_percentage_change(self):
        