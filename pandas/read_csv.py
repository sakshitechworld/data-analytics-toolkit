import pandas as pd

df = pd.read_csv('pandas/data/annual-enterprise-survey-2023-financial-year-provisional-size-bands.csv')  #Loading the dataset
print(df.iloc[1:10])