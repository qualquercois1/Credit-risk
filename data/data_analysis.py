import pandas as pd

data_dictionary = pd.read_excel('../data/LCDataDictionary.xlsx')
df = pd.read_csv('../data/loan.csv')

colunas = ['loan_status','term','revol_util','pub_rec','annual_inc','loan_amnt','dti','delinq_2yrs','open_acc','emp_length','home_ownership']

print(data_dictionary[data_dictionary['LoanStatNew'].isin(colunas)])
print("////////////////////////\n")



print(df[colunas])