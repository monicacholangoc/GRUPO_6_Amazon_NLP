[← Día 09](../Dia%2009%20-%202026-05-05%20-%20SQL%20con%20Python%20-%20ENTREGA%20SEMANA%202/) · [🏠 Índice](../README.md) · [Día 11 →](../Dia%2011%20-%202026-05-07%20-%20Hip%C3%B3tesis%20y%20pruebas%20estad%C3%ADsticas/)

<a href="https://colab.research.google.com/github/we-human-centric/CursoPythonDatos_2026/blob/main/Dia%2010%20-%202026-05-06%20-%20Visualizaciones%20avanzadas/clase_10.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  &nbsp; [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/we-human-centric/CursoPythonDatos_2026/blob/main/Dia%2010%20-%202026-05-06%20-%20Visualizaciones%20avanzadas/clase_10.ipynb)

---

# Día 10 · Visualizaciones avanzadas con Seaborn y Plotly

**Fecha:** Miércoles 6 de mayo de 2026  
**Módulo:** Módulo 3 · Visualización y análisis exploratorio de datos  
**Duración:** 2 horas sincrónicas  

---

## 🗓️ Plan de la Semana 3

| Día | Fecha | Tema |
|-----|-------|------|
| 10 | Mié 6 may | Visualizaciones avanzadas |
| 11 | Jue 7 may | Hipótesis y pruebas estadísticas |
| 12 | Vie 8 may | Correlaciones, regresiones e intro a scikit-learn |
| **13** | **Lun 11 may** | **Métricas y comparación de modelos — ENTREGA S3** |

### Entregable de cierre: Semana 3

Al cierre del **Día 13 (lunes 11 de mayo)** cada equipo entrega la **exploración completa + primer modelo**:

- EDA completo: descripción estadística y visualizaciones avanzadas.
- Hipótesis formuladas y validadas con pruebas estadísticas.
- Correlaciones clave identificadas y documentadas.
- Primer modelo predictivo con scikit-learn y evaluación inicial (RMSE, Accuracy, etc.).

---

## Introducción

Arrancamos el módulo 3 con visualizaciones que cuentan historias. Pasamos de los gráficos básicos de Seaborn a composiciones más ricas y, sobre todo, a gráficos **interactivos** con Plotly, que luego embutiremos en el dashboard final.

## Objetivos de aprendizaje

Al finalizar esta sesión serás capaz de:

- Construir visualizaciones compuestas con Seaborn.
- Producir gráficos interactivos con Plotly Express.
- Escoger el gráfico adecuado para cada tipo de pregunta.

## Contenidos de la sesión

### 1. Seaborn avanzado

`FacetGrid` y `catplot` para comparar subgrupos. `jointplot` (bivariado con marginales). `lmplot` para regresiones visuales. Uso de `hue`, `col`, `row` para múltiples dimensiones.

### 2. Plotly Express

API de alto nivel: `px.scatter`, `px.line`, `px.bar`, `px.box`, `px.histogram`, `px.treemap`, `px.sunburst`. Gráficos interactivos con hover, zoom y selección.

### 3. Plotly Graph Objects

Cuando Express no alcanza: `go.Figure` con `subplots`, anotaciones (`fig.add_annotation`), formas (`fig.add_shape`), configuración de layout.

### 4. Mapas

`px.scatter_mapbox` y `px.choropleth_mapbox` para análisis geoespacial. Requiere token gratuito de Mapbox o `open-street-map` como estilo sin token.

### 5. Paletas y accesibilidad

Paletas cualitativas, secuenciales y divergentes. Considerar daltonismo (paletas *colorblind-safe*). Contraste para impresión blanco y negro.

### 6. Dataviz storytelling

Cada gráfico responde una pregunta. Título que resume el hallazgo. Ejes etiquetados. Si es posible, destaca el punto clave.

## Actividad práctica

Crea 3 visualizaciones avanzadas de tu dataset en `notebooks/07_viz_avanzadas.ipynb`. Cada una debe:

- Responder una **pregunta específica**.
- Tener título que resuma el hallazgo.
- Estar correctamente rotulada.

## Trabajo en grupo sobre el caso asignado

Inicien `notebooks/08_eda_profundo.ipynb` organizado por **preguntas de análisis**. Cada sección: pregunta → gráfico(s) → interpretación en texto. Es el documento más importante del módulo 3.

## Entregable del día

Notebook `07_viz_avanzadas.ipynb` con al menos 5 gráficos avanzados comentados.

## Recursos recomendados

- Plotly Express – Tutorial: https://plotly.com/python/plotly-express/
- Chart chooser (From Data to Viz): https://www.data-to-viz.com/

---

---

[← Día 09](../Dia%2009%20-%202026-05-05%20-%20SQL%20con%20Python%20-%20ENTREGA%20SEMANA%202/) · [🏠 Índice](../README.md) · [Día 11 →](../Dia%2011%20-%202026-05-07%20-%20Hip%C3%B3tesis%20y%20pruebas%20estad%C3%ADsticas/)

> *Seminario EDA · Abril–Mayo 2026 · [we-human-centric](https://github.com/we-human-centric)*
