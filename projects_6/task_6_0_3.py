import pandas as pd
df = pd.read_csv('wild_boars.csv')

with open('projects_6/task_6_0/mediana.txt', 'w') as fl:
    fl.write(df.drop(columns='boar_id').median(numeric_only=True).to_string())

median_weight = df['weight_kg'].median()
print(f"Boars median weight is {median_weight:.2f}")    