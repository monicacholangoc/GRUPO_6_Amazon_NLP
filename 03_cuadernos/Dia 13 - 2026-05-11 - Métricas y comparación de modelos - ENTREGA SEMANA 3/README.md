[← Día 12](../Dia%2012%20-%202026-05-08%20-%20Correlaciones%2C%20regresiones%20e%20intro%20a%20scikit-learn/) · [🏠 Índice](../README.md) · [Día 14 →](../Dia%2014%20-%202026-05-12%20-%20Dashboards%20con%20Streamlit/)

<a href="https://colab.research.google.com/github/we-human-centric/CursoPythonDatos_2026/blob/main/Dia%2013%20-%202026-05-11%20-%20M%C3%A9tricas%20y%20comparaci%C3%B3n%20de%20modelos%20-%20ENTREGA%20SEMANA%203/clase_13.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  &nbsp; [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/we-human-centric/CursoPythonDatos_2026/blob/main/Dia%2013%20-%202026-05-11%20-%20M%C3%A9tricas%20y%20comparaci%C3%B3n%20de%20modelos%20-%20ENTREGA%20SEMANA%203/clase_13.ipynb)

---

# Día 13 · Métricas y comparación de modelos · ENTREGA SEMANA 3

**Fecha:** Lunes 11 de mayo de 2026  
**Módulo:** Módulo 4 · Ciencia de datos aplicada y escalabilidad  
**Duración:** 2 horas sincrónicas  

---

## Introducción

Entramos al módulo 4. La pregunta ya no es *"¿cuál es mi modelo?"* sino *"¿es el mejor modelo y cómo lo sé?"*. Hoy vemos métricas, validación cruzada y cómo comparar modelos sin engañarnos.

## Objetivos de aprendizaje

Al finalizar esta sesión serás capaz de:

- Seleccionar la métrica adecuada según el problema.
- Hacer validación cruzada correcta.
- Comparar dos o más modelos con rigor.

## Contenidos de la sesión

### 1. Métricas de regresión

- **MAE** (error absoluto medio): fácil de interpretar, en las unidades de y.
- **MSE / RMSE**: penalizan más los errores grandes. RMSE también en unidades de y.
- **R²**: proporción de varianza explicada; puede ser negativo si el modelo es peor que predecir la media.

### 2. Métricas de clasificación

- **Accuracy**: útil cuando las clases están balanceadas.
- **Precision**: de los que predije positivos, cuántos lo eran.
- **Recall**: de los positivos reales, cuántos capturé.
- **F1**: media armónica de precision y recall.
- **ROC-AUC**: capacidad de ordenar positivos sobre negativos.
- **Matriz de confusión**: base para interpretar todo lo anterior.

### 3. Validación cruzada

`KFold` (general), `StratifiedKFold` (clasificación con clases desbalanceadas), `TimeSeriesSplit` (series temporales). Usar `cross_val_score` y `cross_validate`.

### 4. Sobreajuste y subajuste

Síntomas: score alto en train / bajo en test → sobreajuste. Score bajo en ambos → subajuste. Curvas de aprendizaje para diagnóstico.

### 5. Ajuste de hiperparámetros

`GridSearchCV` (exhaustivo) y `RandomizedSearchCV` (muestreo aleatorio, más rápido para espacios grandes).

### 6. Benchmarking

Siempre comparar contra un **baseline trivial**: media (regresión) o clase mayoritaria (clasificación) con `DummyRegressor` / `DummyClassifier`.

## Actividad práctica

Compara dos modelos sobre un mismo dataset (por ejemplo, Logistic Regression vs. Random Forest sobre Titanic). Reporta: baseline trivial, scores por fold, media y desviación, intervalo de confianza informal.

## Trabajo en grupo sobre el caso asignado

**ENTREGABLE SEMANA 3**:
- EDA completo (07_viz_avanzadas, 08_eda_profundo, 09_hipotesis).
- Primer modelo con métricas.
- Presentación de 5 minutos por equipo.

Después de presentar, entrenen un **segundo modelo** para comparar en los próximos días.

## Entregable del día

Entregables S3 consolidados + segundo modelo en `models/`.

## Recursos recomendados

- scikit-learn – Model evaluation: https://scikit-learn.org/stable/modules/model_evaluation.html
- "Beyond Accuracy": https://neptune.ai/blog/evaluation-metrics-binary-classification

---

---

[← Día 12](../Dia%2012%20-%202026-05-08%20-%20Correlaciones%2C%20regresiones%20e%20intro%20a%20scikit-learn/) · [🏠 Índice](../README.md) · [Día 14 →](../Dia%2014%20-%202026-05-12%20-%20Dashboards%20con%20Streamlit/)

> *Seminario EDA · Abril–Mayo 2026 · [we-human-centric](https://github.com/we-human-centric)*
