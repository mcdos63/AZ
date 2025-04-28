import pandas as pd

df = pd.read_csv('World-happiness-report-2024.csv')
print(df.head())
print(df.info())
print(df.describe())

df2=pd.read_csv('dz.csv')

df2.dropna(inplace=True) # убираю непонятные строки
print(df2)
print(df2.groupby('City')['Salary'].mean().reset_index())