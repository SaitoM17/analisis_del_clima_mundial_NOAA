# 📊 TROLL A: Análisis de los datos meteorológicos del año 2024
# Limpieza de Datos (Enfoque en Limpieza + Pandas)

Este proyecto se centra en la limpieza, exploración y visualización de datos meteorológicos históricos de la estación **TROLL A OIL PLATAFORM NO** para el año 2024, utilizando el conjunto de datos **Global Summary of the Day (GSOD)** proporcionado por el NOAA. El objetivo principal es explorar y comprender los patrones de temperatura, velocidad del viento y otras variables climáticas relevantes en esta ubicación específica, aplicando técnicas de limpieza, análisis exploratorio y análisis estadístico con Python, Pandas, Matplotlib y Seaborn.

---

## 📚 Tabla de Contenidos

- [📂 Estructura del proyecto](#estructura-del-proyecto)
- [🎯 Propósito](#-propósito)
- [📦 Conjunto de Datos](#-conjunto-de-datos)
- [🧪 Pasos del Proyecto](#-pasos-del-proyecto)
- [🛠️ Tecnologías](#-tecnologías)
- [⚙️ Instalación](#-instalación)
- [🚀 Uso](#-uso)
- [📈 Conclusiones y Recomendaciones](#-conclusiones-y-recomendaciones)
- [👤 Autor](#-autor)
- [📝 Licencia](#-licencia)

---
## 📂Estructura del proyecto
```
📂 analisis_del_clima_mundial_NOAA/
│── 📂 data/           
│   ├── 📂 raw/         # Datos originales sin modificar
│   └── 📂 processed/   # Datos limpios/listos para análisis
│
│── 📂 notebooks/       # Contiene los Jupyter Notebooks para explorar los datos
│── 📂 scripts/         # Guarda scripts de Python para limpieza, modelos, etc.
│── 📂 reports/         # Contiene gráficos y reportes generados
│── 📂 models/          # Si usas machine learning, guarda los modelos aquí
│── 📂 docs/            # Documentación del proyecto
│── requirements.txt    # Lista de paquetes necesarios (para instalar en otro PC)
│── README.md           # Documentación principal
│── LICENSE             # LICENSE del proyecto
|── .gitignore          # Archivos excluidos
```
---

## 🎯 Propósito

- Analizar en profundidad las tendencias de temperatura y otras variables meteorológicas en la plataforma Troll A durante el año 2024.
- Aplicar técnicas de limpieza y análisis exploratorio de datos para comprender las condiciones climáticas específicas de esta ubicación.
- Utilizar conceptos estadísticos y de probabilidad para validar hipótesis sobre el clima en Troll A.
- Reforzar habilidades en Python, Pandas, Matplotlib, Seaborn y NumPy.

---

## 📦 Conjunto de Datos

El conjunto de datos utilizado contiene las siguientes columnas:

troll_a_2024.csv:
* **`STATION`**: Identificador único de la estación meteorológica (en este caso, `01087799999`).
* **`DATE`**: Fecha de la observación meteorológica en formato `mm/dd/aaaa`.
* **`LATITUDE`**: Latitud de la estación en grados decimales.
* **`LONGITUDE`**: Longitud de la estación en grados decimales.
* **`ELEVATION`**: Elevación de la estación en metros.
* **`NAME`**: Nombre de la estación meteorológica (TROLL A OIL PLATFORM, NO).
* **`TEMP`**: Temperatura media diaria en décimas de grado Fahrenheit.
* **`TEMP_ATTRIBUTES`**: Número de observaciones utilizadas para calcular la temperatura media.
* **`DEWP`**: Punto de rocío medio diario en décimas de grado Fahrenheit.
* **`DEWP_ATTRIBUTES`**: Número de observaciones utilizadas para calcular el punto de rocío medio.
* **`SLP`**: Presión media a nivel del mar en décimas de milibar (mb).
* **`SLP_ATTRIBUTES`**: Número de observaciones utilizadas para calcular la presión media a nivel del mar.
* **`STP`**: Presión media de la estación en décimas de milibar (mb).
* **`STP_ATTRIBUTES`**: Número de observaciones utilizadas para calcular la presión media de la estación.
* **`VISIB`**: Visibilidad media diaria en décimas de milla.
* **`VISIB_ATTRIBUTES`**: Número de observaciones utilizadas para calcular la visibilidad media.
* **`WDSP`**: Velocidad media del viento diaria en décimas de nudo.
* **`WDSP_ATTRIBUTES`**: Número de observaciones utilizadas para calcular la velocidad media del viento.
* **`MXSPD`**: Velocidad máxima sostenida del viento diaria en nudos.
* **`GUST`**: Ráfaga máxima de viento diaria en nudos.
* **`MAX`**: Temperatura máxima diaria en décimas de grado Fahrenheit.
* **`MAX_ATTRIBUTES`**: Indicador de cómo se obtuvo la temperatura máxima (explícitamente o de datos horarios).
* **`MIN`**: Temperatura mínima diaria en décimas de grado Fahrenheit.
* **`MIN_ATTRIBUTES`**: Indicador de cómo se obtuvo la temperatura mínima (explícitamente o de datos horarios).
* **`PRCP`**: Precipitación total diaria en centésimas de pulgada.
* **`PRCP_ATTRIBUTES`**: Indicador de la fuente de los datos de precipitación.
* **`SNDP`**: Profundidad de la nieve diaria en décimas de pulgada.
* **`FRSHTT`**: Indicadores (1 = sí, 0 = no) de la ocurrencia de niebla, lluvia, nieve, granizo, tormenta y tornado.

Fuente: [Global Summary of the Day (GSOD)](https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/2024/).

---

## 🧪 Pasos del Proyecto

1. **Importación y limpieza de datos.**
2. **Análisis exploratorio con visualizaciones.**
3. **Aplicación de estadística descriptiva e inferencial.**
4. **Conclusiones y hallazgos clave.**

---

## 🛠️ Tecnologías

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook / Google Colab
- [Otras herramientas que uses, como Scikit-learn, Plotly, etc.]

---

## ⚙️ Instalación

### 1. Clonar este repositorio:
```bash
git clone https://github.com/SaitoM17/analisis_del_clima_mundial_NOAA.git
```
### 2. Uso de un Entorno Virtual para Aislar Dependencias

Para evitar conflictos con versiones de librerías, se recomienda usar entornos virtuales.

####  Crear y Activar un Entorno Virtual

##### Crear el entorno virtual:
```
python -m venv venv
```
##### Activar el entorno:
* #### En Windows:

    ```
    venv\Scripts\activate
    ```

* #### En Mac/Linux::

    ```
    source venv/bin/activate
    ```
#### 3. Instalar dependencias dentro del entorno:
* #### Opición 1:
    ```
    pip install -r requirements.txt
    ```

* #### Opción 2 (De forma manual):
    ```
    pip install numpy pandas matplotlib seaborn scikit-learn
    ```
---

## 🚀 Uso
Por definir

---

## 📈 Conclusiones y Recomendaciones

- [Insight 1]
- [Insight 2]
- [Recomendación práctica o estratégica basada en los datos]

---

## 👤 Autor

**Said Mariano Sánchez** – *smariano170@gmail.com*  
Este proyecto forma parte de mi portafolio como analista de datos Jr.

---

## 📝 Licencia

Este proyecto está licenciado bajo la **Licencia MIT**. Puedes usarlo, modificarlo y distribuirlo libremente, siempre que menciones al autor original.

---