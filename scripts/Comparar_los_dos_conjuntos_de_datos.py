# Comparar los dos conjuntos de datos para asegurar de que tiene el mismo tipo de datos
import pandas as pd

df_con_ountliers = pd.read_csv('../data/processed/troll_a_2024_con_outliers.csv')
df_sin_ountliers = pd.read_csv('../data/processed/troll_a_2024_sin_outliers.csv')


print(df_con_ountliers.head(5))


print(df_sin_ountliers.head(5))


