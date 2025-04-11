# %%
# Impotamos las librerias necesariar para la limpieza de los datos
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# ##### Analisis (EDA)

# %%
# Cargamos el Data Set y mostralos los primeros 20 elementos

df_troll_2024 = pd.read_csv('../data/raw/troll_a_2024.csv')
#Para que nos muestre todas las columnas
pd.set_option('display.max_columns', None)
df_troll_2024.head(20)

# %%
# Concer la información del DataFrame
print(df_troll_2024.info())

# %% [markdown]
# df_troll_2024.info nos dio infomración importante de como esta compuesto el DataFrame, en este DataFrame la columna que se tendria que cambiar seria DATE de object a datetime

# %%
# Cambiar el tipo de dato a la columnas DATE (se necesita el formato datetime para realizar operación más adelante en este archivo)
df_troll_2024['DATE'] = pd.to_datetime(df_troll_2024['DATE'], format='%Y-%m-%d')
df_troll_2024.info()

# %%
# Identificación de valores nulos 
df_troll_2024.isnull().sum()

# %% [markdown]
# **No se encontraron valores nulos en las columnas**

# %%
# Buscar valores duplicados 
print(df_troll_2024.duplicated().sum())

# %% [markdown]
# **No se encontro ningun dato duplicado**

# %%
# Consistencia de los datos
# (Aquí verificamos si hay valores únicos inesperados en la columna 'NAME')
print("Valores únicos en la columna 'NAME':")
print(f'{df_troll_2024['NAME'].unique()} {df_troll_2024['NAME'].value_counts().unique()}')

# %% [markdown]
# **No se encontraron valores inusuales en la columnas NAME** (Errores tipográficos)

# %% [markdown]
# #### Para el proyecto estas son las tablas de nuestro interes:
# Unidades de Medida:
# * TEMP (Temperatura media diaria):
#     * Grados Fahrenheit.
# * DEWP (Punto de rocío medio diario):
#     * Grados Fahrenheit.
# * SLP (Presión media a nivel del mar):
#     * Hectopascales (hPa).
# * STP (Presión media de la estación):
#     * Hectopascales (hPa).
# * VISIB (Visibilidad media diaria):
#     * Décimas de milla.
# * WDSP (Velocidad media del viento diaria):
#     * Nudos.
# * MXSPD (Velocidad máxima sostenida del viento diaria):
#     * Nudos.
# * GUST (Ráfaga máxima de viento diaria):
#     * Nudos.
# * MAX (Temperatura máxima diaria):
#     * Grados Fahrenheit.
# * MIN (Temperatura mínima diaria):
#     * Grados Fahrenheit.

# %% [markdown]
# ##### Tranformación de datos (Unidad de medida)

# %%
# Tranformar TEMP, DEWP, MAX, MIN de Grados Fahrenheit (°F) a Grados Celsius (°C).
temp_cols = ['TEMP', 'DEWP', 'MAX', 'MIN' ]
for col in temp_cols:
    if col in temp_cols:
        df_troll_2024[col] = (df_troll_2024[col] - 32) * 5/9

# %%
# Tranformar VISIB de Décimas de milla a Kilómetros
if 'VISIB' in df_troll_2024.columns:
    df_troll_2024['VISIB'] = df_troll_2024['VISIB'] * 0.160934

# %%
# Transformar nudos a kilómetros por hora
wind_cols = ['WDSP', 'MXSPD', 'GUST']
for col in wind_cols:
    if col in df_troll_2024.columns:
        df_troll_2024[col] = df_troll_2024[col] * 1.852

# %%
# Verificar la transformación de los datos
df_troll_2024[['TEMP', 'DEWP', 'MAX', 'MIN', 'VISIB', 'WDSP', 'MXSPD', 'GUST']].head(20)

# %% [markdown]
# #### Detectar valores atípicos 

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

outliers_detectados = detectar_y_graficar_outliers(df_troll_2024, columnas_meteorologicas)

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
# Revisar que los cambios se hayan guardado
df_troll_2024.info()

# %% [markdown]
# ##### Guardar los datos con outliers y sin outliers (se guardaran solo las columnas de nuestro interes para el proyecto)
# 
# * STATION (Número de la estación)	
# * DATE	(Fecha)
# * LATITUDE	(Coordenadas)
# * LONGITUDE	(Coordenadas)
# * ELEVATION	(Elevación)
# * NAME (Nombre de la estación)
# * TEMP (Temperatura media diaria):
#     * Grados Fahrenheit.
# * DEWP (Punto de rocío medio diario):
#     * Grados Fahrenheit.
# * SLP (Presión media a nivel del mar):
#     * Hectopascales (hPa).
# * STP (Presión media de la estación):
#     * Hectopascales (hPa).
# * VISIB (Visibilidad media diaria):
#     * Décimas de milla.
# * WDSP (Velocidad media del viento diaria):
#     * Nudos.
# * MXSPD (Velocidad máxima sostenida del viento diaria):
#     * Nudos.
# * GUST (Ráfaga máxima de viento diaria):
#     * Nudos.
# * MAX (Temperatura máxima diaria):
#     * Grados Fahrenheit.
# * MIN (Temperatura mínima diaria):
#     * Grados Fahrenheit.

# %%
# Guardar los datos con outliers
df_troll_2024_con_outliers = df_troll_2024[['STATION', 'DATE', 'LATITUDE', 'LONGITUDE', 'ELEVATION', 'NAME', 'TEMP', 'DEWP', 'SLP', 'STP', 'VISIB', 'WDSP', 'MXSPD', 'GUST', 'MAX', 'MIN']]
df_troll_2024_con_outliers.to_csv('../data/processed/troll_a_2024_con_outliers.csv', index=False)

# %%
df = pd.read_csv('../data/processed/troll_a_2024_con_outliers.csv')
df.info()

# %%
# Eliminar Outliers
indices_eliminar = {
    'VISIB': [20, 27, 32, 48, 49, 50, 93, 95, 97, 120, 124, 126, 127, 140, 141, 187, 189, 227, 232, 233, 241, 255, 256, 285, 297, 300, 322, 323, 327, 340, 346],
    'WDSP': [327],
    'GUST': [12, 15, 17, 20, 21, 22, 24, 25, 30, 31, 32, 33, 43, 51, 78, 96, 99, 106, 152, 173, 177, 180, 217, 232, 246, 248, 264, 276, 283, 287, 293, 312, 313, 315, 316, 317, 327, 336, 337, 338, 341, 343, 352],
    'MAX': [103, 243, 300],
    'MIN': [103, 300, 331]
}

df_troll_2024_sin_outliers = df_troll_2024.copy()

# Consolidar todos los índices únicos
indices_unicos = []
for lista_indices in indices_eliminar.values():
    indices_unicos.extend(lista_indices)
indices_unicos = list(set(indices_unicos)) # Obtener índices únicos    

# Eliminar filas usando los índices únicos
indices_existentes = [indice for indice in indices_unicos if indice in df_troll_2024_sin_outliers.index]
    
if indices_existentes:
    df_troll_2024_sin_outliers = df_troll_2024_sin_outliers.drop(indices_existentes)
    print(f'Indice {indices_existentes} eliminado')
else:
    print(f'No se encontro índices para la columnas ')



# %%
# Verificamos los outliers
columnas_meteorologicas = ['TEMP', 'DEWP', 'SLP', 'STP', 'VISIB', 'WDSP', 'MXSPD', 'GUST', 'MAX', 'MIN']

outliers_detectados = detectar_y_graficar_outliers(df_troll_2024_sin_outliers, columnas_meteorologicas)

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
df_troll_2024_sin_outliers['DATE'] = pd.to_datetime(df_troll_2024_sin_outliers['DATE'].astype(np.int64))
df_troll_2024_sin_outliers.info()

# %%
plt.figure(figsize=(8,5))
sns.scatterplot(x='DATE', y='VISIB', data=df_troll_2024_sin_outliers)
plt.title('VISIB (Con Outliers)')
plt.xlabel('Fecha')
plt.ylabel('VISB')

plt.show()

# %%
plt.figure(figsize=(8,5))
sns.histplot(df_troll_2024_sin_outliers['VISIB'], kde=True, color='b')
plt.title('Histograma de VISIB')
plt.xlabel('VISIB ')
plt.show()

# %%
plt.figure(figsize=(8,5))
sns.scatterplot(x='DATE', y='WDSP', data=df_troll_2024_sin_outliers)
plt.title('WDSP (Con Outliers)')
plt.xlabel('Fecha')
plt.ylabel('WDSP')
plt.show()

# %%
plt.figure(figsize=(8,5))
sns.histplot(df_troll_2024_sin_outliers['WDSP'], kde=True, color='b')
plt.title('Boxplot de WDSP')
plt.xlabel('WDSP (Nudos)')
plt.show()

# %%
# Remplzar los valores atípicos en una columnas con columna con la mediana 
def imputar_outliers(df, columna):
    mediana = df[columna].median()
    q1 = df[columna].quantile(0.25)
    q3 = df[columna].quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    df[columna] = np.where(
        (df[columna] < limite_inferior) | (df[columna] > limite_superior),
        mediana,
        df[columna],
    )
    return df

df_troll_2024_sin_outliers = imputar_outliers(df_troll_2024_sin_outliers, "VISIB")
df_troll_2024_sin_outliers = imputar_outliers(df_troll_2024_sin_outliers, "WDSP")

# %%
# Verificamos los outliers
columnas_meteorologicas = ['TEMP', 'DEWP', 'SLP', 'STP', 'VISIB', 'WDSP', 'MXSPD', 'GUST', 'MAX', 'MIN']

outliers_detectados = detectar_y_graficar_outliers(df_troll_2024_sin_outliers, columnas_meteorologicas)

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
# Guardar los datos sin outliers
df_troll_2024_sin_outliers = df_troll_2024_sin_outliers[['STATION','DATE', 'LATITUDE', 'LONGITUDE', 'ELEVATION', 'NAME', 'TEMP', 'DEWP', 'SLP', 'STP', 'VISIB', 'WDSP', 'MXSPD', 'GUST', 'MAX', 'MIN']]
df_troll_2024_sin_outliers.to_csv('../data/processed/troll_a_2024_sin_outliers.csv', index=False)

# %%
# Verficamos de que se ayan guardado los datos
df_troll_2024_sin_outliers = pd.read_csv('../data/processed/troll_a_2024_sin_outliers.csv')
df_troll_2024_sin_outliers.head(5)

# %%
df_troll_2024_sin_outliers.info()


