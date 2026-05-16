[← Día 07](../Dia%2007%20-%202026-04-29%20-%20Pandas%20II/) · [🏠 Índice](../README.md) · [Día 09 →](../Dia%2009%20-%202026-05-05%20-%20SQL%20con%20Python%20-%20ENTREGA%20SEMANA%202/)

<a href="https://colab.research.google.com/github/we-human-centric/CursoPythonDatos_2026/blob/main/Dia%2008%20-%202026-05-04%20-%20Estad%C3%ADstica%20descriptiva%20y%20visualizaci%C3%B3n%20inicial/clase_08.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  &nbsp; [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/we-human-centric/CursoPythonDatos_2026/blob/main/Dia%2008%20-%202026-05-04%20-%20Estad%C3%ADstica%20descriptiva%20y%20visualizaci%C3%B3n%20inicial/clase_08.ipynb)

---

# Día 8 · Estadística descriptiva y visualización inicial (Matplotlib / Seaborn)

**Fecha:** Lunes 4 de mayo de 2026  
**Módulo:** Módulo 2 · Manipulación y análisis de datos  
**Duración:** 2 horas 30 minutos sincrónicas  

---

## Introducción

Después del feriado retomamos con la parte más "exploratoria" del EDA: resumir numéricamente el dataset y traducir esos números en gráficos que cuenten una historia. Piensa cada gráfico como una respuesta a una pregunta específica.

## Objetivos de aprendizaje

Al finalizar esta sesión serás capaz de:

- Resumir variables con estadística descriptiva adecuada.
- Producir visualizaciones iniciales claras y honestas.
- Identificar los primeros hallazgos del caso.

## Contenidos de la sesión

### 1. Tendencia central y dispersión

Media, mediana, moda. Varianza, desviación estándar, rango, IQR. Cuándo usar media vs. mediana.

### 2. Distribuciones

Cuartiles y percentiles. Histogramas, KDE, gráficos Q-Q.

### 3. Exploración con Pandas

`df.describe()`, `df["col"].value_counts(normalize=True)`, `pd.crosstab(a, b)`.

### 4. Matplotlib

Anatomía: figure, axes, artists. Gráficos básicos: `plot`, `bar`, `scatter`, `hist`, `boxplot`. Configuración de títulos, ejes, leyendas y estilos.

### 5. Seaborn

API de alto nivel basada en Matplotlib. `histplot`, `boxplot`, `countplot`, `heatmap`, `pairplot`. Paletas de color y temas.

### 6. Principios de dataviz

Escala apropiada, no distorsionar, incluir contexto, un mensaje por gráfico.

## Actividad práctica

En `notebooks/06_eda_inicial.ipynb` produce **6 gráficos** sobre tu dataset, incluyendo al menos:

- 1 histograma o boxplot por cada variable numérica clave.
- 1 `countplot` de la variable categórica principal.
- 1 `heatmap` de correlaciones.
- 1 `pairplot` de las 4 variables más importantes.

## Trabajo en grupo sobre el caso asignado

Agreguen al pipeline validaciones de integridad. Opciones:

- `assert` simples dentro de `transform` (mínimo viable).
- Librería `pandera` o `great_expectations` (recomendado).

Ejemplo con asserts:

```python
assert df["precio"].ge(0).all(), "precios negativos detectados"
assert df["fecha"].notna().all(), "fechas nulas"
```

## Entregable del día

Notebook `06_eda_inicial.ipynb` + validaciones integradas al pipeline.

## Recursos recomendados

- Seaborn – Tutorial: https://seaborn.pydata.org/tutorial.html
- Matplotlib – Anatomía de una figura: https://matplotlib.org/stable/gallery/showcase/anatomy.html

---

---

[← Día 07](../Dia%2007%20-%202026-04-29%20-%20Pandas%20II/) · [🏠 Índice](../README.md) · [Día 09 →](../Dia%2009%20-%202026-05-05%20-%20SQL%20con%20Python%20-%20ENTREGA%20SEMANA%202/)

> *Seminario EDA · Abril–Mayo 2026 · [we-human-centric](https://github.com/we-human-centric)*
