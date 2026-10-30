import pandas as pd

data_dictionary = pd.read_excel('../data/LCDataDictionary.xlsx')
df = pd.read_csv('../data/loan.csv')

print(data_dictionary)
print("////////////////////////\n")
print(df.columns)