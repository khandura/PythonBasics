import pandas as pd
import os

DESTI_DIR = r'D:\CODEBASE\files\dest\Lu_Portfolio_20200425.csv'

df = pd.read_csv(DESTI_DIR)

print(df)
# idx = list(df.columns).index('COL12')
# print('index of col1 ', idx)
# print('col1 : \n', df['COL1'])

df['COL1'].replace('VAL1', '', inplace=True)
print(df)
df.loc[:, 'COL1'] = ""
print(df)

df.to_csv(path_or_buf= r'D:\CODEBASE\files\dest\Lu_Portfolio_20200425.csv', index=False)
