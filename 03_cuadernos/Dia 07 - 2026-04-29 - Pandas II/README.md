[← Día 06](../Dia%2006%20-%202026-04-28%20-%20Pandas%20I/) · [🏠 Índice](../README.md) · [Día 08 →](../Dia%2008%20-%202026-05-04%20-%20Estad%C3%ADstica%20descriptiva%20y%20visualizaci%C3%B3n%20inicial/)

<a href="https://colab.research.google.com/github/we-human-centric/CursoPythonDatos_2026/blob/main/Dia%2007%20-%202026-04-29%20-%20Pandas%20II/clase_07.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  &nbsp; [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/we-human-centric/CursoPythonDatos_2026/blob/main/Dia%2007%20-%202026-04-29%20-%20Pandas%20II/clase_07.ipynb)

---

# Día 7 · Pandas II – Limpieza y transformación de datos

**Fecha:** Miércoles 29 de abril de 2026  
**Módulo:** Módulo 2 · Manipulación y análisis de datos  
**Duración:** 2 horas 30 minutos sincrónicas  

---

## Introducción

El 80% del tiempo de un proyecto de datos se va en limpieza. Hoy aprendemos las herramientas que harán que ese 80% sea rápido y reproducible. Al final de la clase empezamos a mover el código del notebook a un pipeline en `src/pipeline.py`.

## Objetivos de aprendizaje

Al finalizar esta sesión serás capaz de:

- Detectar y tratar nulos, duplicados y outliers.
- Convertir tipos y crear variables derivadas.
- Agrupar, pivotar y unir tablas.
- Iniciar un pipeline reproducible.

## Contenidos de la sesión

### 1. Valores nulos

`df.isna().sum()`, `df.dropna()`, `df.fillna(valor)`. Criterio para decidir entre imputar vs. eliminar.

### 2. Duplicados

`df.duplicated()`, `df.drop_duplicates(subset=[...], keep="first")`. Diferenciar duplicados reales de legítimos.

### 3. Outliers

Detección con IQR (`Q1 - 1.5·IQR`, `Q3 + 1.5·IQR`) y con z-score. *Winsorization* con `clip()`.

### 4. Conversión de tipos

`astype()`, `pd.to_datetime()`, `pd.to_numeric(errors="coerce")`. Manejo de categóricos con `category`.

### 5. Variables derivadas

`df.assign()`, `df["col"].apply(func)`, `df["col"].map(dict)`, expresiones con columnas.

### 6. Groupby y agregaciones

`df.groupby("col").agg({"otra": "mean", "tercera": ["sum", "count"]})`. `transform` para devolver resultados del mismo tamaño que el DataFrame original.

### 7. Pivot y melt

`pivot_table(index, columns, values, aggfunc)` para reorganizar. `melt(id_vars, value_vars)` para pasar de formato ancho a largo.

### 8. Merge y concat

`pd.merge(a, b, on="id", how="left")`, tipos de join. `pd.concat([a, b])` para apilar.

## Actividad práctica

En `notebooks/05_limpieza.ipynb` limpia el CSV "sucio" provisto por el docente y documenta cada decisión:

1. Nulos: ¿imputar o eliminar?
2. Duplicados: ¿por qué existen?
3. Outliers: ¿son errores o casos reales?
4. Tipos: conversiones aplicadas.

## Trabajo en grupo sobre el caso asignado

Inicien `src/pipeline.py` con las funciones:

```python
def load_raw(path: str) -> pd.DataFrame: ...
def clean(df: pd.DataFrame) -> pd.DataFrame: ...
def transform(df: pd.DataFrame) -> pd.DataFrame: ...
def save_processed(df: pd.DataFrame, path: str) -> None: ...
```

Apliquen el pipeline a su dataset y guarden el resultado en `data/processed/`.

## Entregable del día

Notebook `05_limpieza.ipynb` + esqueleto de `src/pipeline.py` + dataset procesado guardado.

## Recursos recomendados

- Pandas – Working with missing data: https://pandas.pydata.org/docs/user_guide/missing_data.html
- Pandas – Group by: https://pandas.pydata.org/docs/user_guide/groupby.html

---

---

[← Día 06](../Dia%2006%20-%202026-04-28%20-%20Pandas%20I/) · [🏠 Índice](../README.md) · [Día 08 →](../Dia%2008%20-%202026-05-04%20-%20Estad%C3%ADstica%20descriptiva%20y%20visualizaci%C3%B3n%20inicial/)

> *Seminario EDA · Abril–Mayo 2026 · [we-human-centric](https://github.com/we-human-centric)*
