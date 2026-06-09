import pandas as pd
df = pd.read_csv('wild_boars.csv')

grouped = df.groupby('gender')['tusk_length_cm']

with open('tusk_length.txt', 'w') as file:
    for gender, values in grouped:
        mean_value = values.mean()
        std_value = values.std()
        variation_coeff = std_value / mean_value * 100

        file.write(f'{gender}: {variation_coeff:.2f}%\n')