# Día 6 · Pandas I – Series, DataFrames y carga de datos

**Fecha:** Martes 28 de abril de 2026  
**Módulo:** Módulo 2 · Manipulación y análisis de datos  
**Duración:** 2 horas 30 minutos sincrónicas  

---

## Introducción

Pandas es la herramienta más usada para manipulación de datos tabulares en Python. Hoy vamos a aprender a cargar datos desde distintos formatos, seleccionar, filtrar y ordenar con soltura.

## Objetivos de aprendizaje

Al finalizar esta sesión serás capaz de:

- Cargar CSV, Excel, JSON y SQL con Pandas.
- Usar `loc` e `iloc` sin confundirlos.
- Filtrar y ordenar DataFrames con claridad.

## Contenidos de la sesión

### 1. Series y DataFrames

Una `Series` es una columna con índice; un `DataFrame` es una tabla 2D con índice de filas y columnas.

### 2. Carga de datos

- `pd.read_csv(path, sep, encoding, parse_dates, dtype, usecols, skiprows, nrows)`.
- `pd.read_excel(path, sheet_name, skiprows)`.
- `pd.read_json(path)`.
- `pd.read_sql(query, conn)`.

### 3. Exploración rápida

`df.head()`, `df.tail()`, `df.sample(5)`, `df.info()`, `df.describe(include="all")`, `df.nunique()`, `df.columns`, `df.index`.

### 4. Selección: loc vs. iloc

- `df.loc[filas, columnas]`: por **etiquetas**.
- `df.iloc[filas, columnas]`: por **posiciones enteras**.
Ejemplo: `df.loc[df["ciudad"] == "Quito", ["precio", "area"]]`.

### 5. Filtrado por condiciones

Máscaras booleanas y combinación con `&`, `|`, `~`. Uso de `.isin()` y `.between()`.

### 6. Ordenamiento

`df.sort_values(by=["col"], ascending=False)` y `df.sort_index()`.

## Actividad práctica

En `notebooks/04_pandas_carga.ipynb`:

1. Carga el CSV `tips.csv` (provisto por el docente).
2. Muestra las propinas superiores al promedio.
3. Obtén los 5 registros con mayor propina relativa (`tip / total_bill`).

## Trabajo en grupo sobre el caso asignado

En su dataset del caso:

- Confirmen que los parámetros de `read_*` son los correctos (separador, encoding, fechas).
- Completen la **ficha de exploración** con: n° de registros, tipos de dato, % de nulos por columna y tres observaciones iniciales.

## Entregable del día

Notebook `04_pandas_carga.ipynb` + ficha de exploración en `docs/ficha_dataset.md`.

## Recursos recomendados

- Pandas – 10 minutes to Pandas: https://pandas.pydata.org/docs/user_guide/10min.html
- Comparación con SQL: https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html

---


