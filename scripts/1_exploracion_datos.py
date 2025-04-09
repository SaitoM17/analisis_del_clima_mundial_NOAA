# %% [markdown]
# ##### **PLANIFICAR:**
# Cargar el conjunto de datos troll_a_2024.csv para conocer conocer como esta estructurado, el tipo de datos que contiene y detectar posibles problemas

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# ##### **Analisis exploratorio de datos:**
# Realizamos un analisis exploratorio para conocer más sobre el conjunto troll_a_2024.csv

# %%
# Cargamos el conjunto de datos y visualizamos los primeros 20 datos
df_troll_a_2024 = pd.read_csv('../data/raw/troll_a_2024.csv')

#Mostrar todas las columnas
pd.set_option('display.max_columns', None)

df_troll_a_2024.head(20)

# %%
# Conocer los tipos de datos que conforman el conjunto de datos
df_troll_a_2024.info()

# %% [markdown]
# Por lo que se ve en la información la fecha tiene es de tipo object cuando deberia de ser de tipo datetime

# %%
# Identificar valores nulos
print('Valores faltantes por columnas')
print(df_troll_a_2024.isnull().sum())

# %% [markdown]
# No se encontraron datos faltantes

# %%
# Verificar valores duplicados
print(df_troll_a_2024.duplicated().sum())

# %% [markdown]
# No se encontraron valores duplicados

# %%
# Consistencia de los datos
# (Aquí verificamos si hay valores únicos inesperados en la columna 'NAME')
print("Valores únicos en la columna 'NAME':")
print(f'{df_troll_a_2024['NAME'].unique()} {df_troll_a_2024['NAME'].value_counts().unique()}')

# %%
# Identificación de valores atípicos usando el método IQR
def deteccion_outliers_iqr(data):
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)
    iqr = q3 - q1
    outliers = data[(data < q1 - 1.5 * iqr) | (data > q3 + 1.5 * iqr)]
    return outliers

# %%
def detectar_y_graficar_outliers(df, columnas_interes):
    outliers_dict = {}

    for col in columnas_interes:
        if col not in df.columns:
            print(f'⚠ Advertencia: la columna {col} no esta en el DataFrame.')

        serie = df[col].dropna() # Evitar errores por NaN    
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr

        outliers = serie[(serie < limite_inferior) | (serie > limite_superior)]

        if not outliers.empty:
            outliers_dict[col] = {
                'cantidad': len(outliers),
                'índices': outliers.index.tolist(),
                'valores': outliers.tolist()
            }
        # Gráfico
        plt.figure(figsize=(6,4))
        sns.boxplot(x = serie)
        plt.title(f'Boxplot de {col} (con outliers)')
        plt.xlabel(col)
        plt.grid(True)
        plt.show()

    return outliers_dict

# %%
columnas_meteorologicas = ['TEMP', 'DEWP', 'SLP', 'STP', 'VISIB', 'WDSP', 'MXSPD', 'GUST', 'MAX', 'MIN']

outliers_detectados = detectar_y_graficar_outliers(df_troll_a_2024, columnas_meteorologicas)

# Mostrar resultados
if outliers_detectados:
    print("🔎 Valores atípicos detectados:")
    for col, info in outliers_detectados.items():
        print(f"\n📌 Columna: {col}")
        print(f"  - Cantidad: {info['cantidad']}")
        print(f"  - Índices: {info['índices']}")
else:
    print("✅ No se detectaron valores atípicos en las columnas seleccionadas.")

# %%
# Calcula la matriz de correlación para columnas relevantes
correlation_matrix = df_troll_a_2024[['VISIB', 'WDSP', 'GUST', 'MAX', 'MIN', 'TEMP', 'DEWP', 'SLP', 'STP']].corr()

# Visualiza la matriz de correlación con un mapa de calor
plt.figure(figsize=(10, 8))  # Ajusta el tamaño según sea necesario
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de correlación')
plt.show()


