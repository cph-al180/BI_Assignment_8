import numpy as np
import pandas as pd
from scipy import stats

dataSet = "brain_size.csv"
brainData = pd.read_csv(dataSet, sep=';')

def ttest(data):
    data = pd.DataFrame(data)
    danishMeanHeight = 71
    americanMeanHeight = 68.4
    dataHeight = data["Height"]
    dataHeight = pd.DataFrame(dataHeight)
    dataHeight = dataHeight[dataHeight.Height != "."]
    heights = []

    i = 0
    for row in dataHeight.iterrows():
        entry = dataHeight.iloc[i]["Height"]
        entryToFloat = float(entry)
        heights.append(entryToFloat)
        i = i + 1
    
    dkttest = stats.ttest_1samp(heights, danishMeanHeight)
    usttest = stats.ttest_1samp(heights, americanMeanHeight)
    print 'Danish T-Test: ', '\n', dkttest
    print 'America T-Test: ', '\n', usttest

def run():
    ttest(brainData)
    print 'done'

run()
