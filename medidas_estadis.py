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
