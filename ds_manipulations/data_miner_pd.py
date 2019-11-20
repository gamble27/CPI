import pandas as pd


# read the data
with open("dataset/ukrstat_dno/values.txt") as f:
    vals = f.read().split(sep='\n')
for i in range(len(vals)):
    vals[i] = float(vals[i].replace(',', '.'))
vals = vals[::-1]

# create CI series
ds = pd.Series(vals)

# save dataset to csv
ds.to_csv("CI_2015_2018.csv")
