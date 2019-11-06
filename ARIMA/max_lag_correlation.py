import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sys
sys.path.append("..")
sys.path.append("/dataset")

# default settings
MIN_LAG = 2
MAX_LAG = 24
MAX_LAG_SEQUENCE = range(MIN_LAG, MAX_LAG+1)

# import dataset
ds = pd.read_csv("/home/olga/Projects/CPI/dataset/CI_2015_2018.csv", header=None)
ds.head()
values = ds.to_numpy(dtype=float)[:, 1]  # .reshape((45,1))
values = values[::-1]  # the newest data is the first in the list

# data about correlation in 1 and 2 method
corr_data = np.zeros((MAX_LAG-MIN_LAG+1, 3))
for lag in MAX_LAG_SEQUENCE:
    # save lag value
    corr_data[lag - MIN_LAG, 0] = lag

    # method 1: data
    time_series_1 = []
    for i in range(lag):
        time_series_1.append(values[i:values.shape[0] - lag + i])
    time_series_1 = np.array(time_series_1)
    # method 1: correlation
    corr_data[lag - MIN_LAG, 1] = np.corrcoef(time_series_1[0, :], time_series_1[1, :])[1, 0]

    # method 2: data
    time_series_2 = [[] for _ in range(lag)]
    index_out_of_bounds_flag = False
    for i in range(0, values.shape[0], lag):
        for j in range(lag):
            if i+j >= values.shape[0]:
                index_out_of_bounds_flag = True
                break
            time_series_2[j].append(values[i+j])
        if index_out_of_bounds_flag:
            break
    shape = max([len(series) for series in time_series_2])
    for i in range(len(time_series_2)):
        time_series_2[i] = np.array(time_series_2[i] + [0]*(shape-len(time_series_2[i])))
    time_series_2 = np.array(time_series_2)
    # method 2: correlation
    corr_data[lag - MIN_LAG, 2] = np.corrcoef(time_series_2[0, :], time_series_2[1, :])[1, 0]

# save correlation data
df = pd.DataFrame(corr_data, columns=['lag', 'corr_1', 'corr_2'])
df.to_csv("corr_delta_1.csv")

# plot the correlations
plt.subplot(211)
plt.plot(df['lag'], df['corr_1'])
plt.xlabel('max lag value')
plt.ylabel('corr(X[t], X[t-1])')
plt.title('Method 1')
plt.minorticks_on()
plt.grid(which='major', color='k', linestyle=':')
plt.grid(which='minor', color='k', linestyle=':')

plt.subplot(212)
plt.plot(df['lag'], df['corr_2'])
plt.xlabel('max lag value')
plt.ylabel('corr(X[t], X[t-1])')
plt.title('Method 2')
plt.minorticks_on()
plt.grid(which='major', color='k', linestyle=':')
plt.grid(which='minor', color='k', linestyle=':')

plt.show()
