# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 21:33:39 2025

@author: gabri
"""
import matplotlib.pyplot as plt
from typing import Dict

ResultsDict = Dict


class VisualisationEngine:
    def __init__(self, data: ResultsDict):
        self.results_dict = data
