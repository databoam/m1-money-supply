import pandas as pd

df = pd.read_csv('m1_comp_raw.csv')

df['m1'] = df.iloc[:, 1:].sum(axis=1)

df.to_csv('m1_comp_processed.csv', index=False)