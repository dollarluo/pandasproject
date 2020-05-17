import pandas as pd
from openpyxl.workbook import Workbook

df_excel = pd.read_excel('../Exercise Files/regions.xlsx') 
df_csv = pd.read_csv('../Exercise Files/Names.csv')
df_txt = pd.read_csv('../Exercise Files/data.txt')

print(df_txt)
