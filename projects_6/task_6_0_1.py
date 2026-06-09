import pandas as pd

df = pd.read_csv('C:\Users\Polin\OneDrive\Рабочий стол/wild_boars.csv')
print(df['tusk_length_cm'])
print(df['tusk_length_cm'].max())
print(df['tusk_length_cm'].min())