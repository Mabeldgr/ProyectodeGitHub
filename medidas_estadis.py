# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 10:41:44 2018

@author: mariaguadalupe
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats

data = pd.read_csv("C:/Users/mariaguadalupe/Downloads/MinDa/Code/salaries_nyrb.csv")
col = 'Salary'

print('Statistics for ',col)
dataCol = np.array(data[col].values)
print(dataCol)
print('Minimun = ',np.min(dataCol))
print('Maximun = ',np.max(dataCol))
print('First quartile = ',np.percentile(dataCol,25))
print('Median = ',np.median(dataCol))
print('Mean = ',np.mean(dataCol))
print('Third quartile = ',np.percentile(dataCol,75))
iqr = np.percentile(dataCol,75)-np.percentile(dataCol,25)
print('IQR = ',iqr)
plt.boxplot(dataCol)

plt.figure()
per = 0.1
trim_data = stats.trimboth(data[col],per)
print('Statics for ',col,'Trimmed at ',per)
print('Minimun = ',np.min(trim_data))
print('Maximun = ',np.max(trim_data))
print('First quartile = ',np.percentile(trim_data,25))
print('Median = ',np.median(trim_data))
print('Mean = ',np.mean(trim_data))
print('Third quartile = ',np.percentile(trim_data,75))
iqr = np.percentile(trim_data,75)-np.percentile(trim_data,25)
print('IQR = ',iqr)
plt.boxplot(trim_data)