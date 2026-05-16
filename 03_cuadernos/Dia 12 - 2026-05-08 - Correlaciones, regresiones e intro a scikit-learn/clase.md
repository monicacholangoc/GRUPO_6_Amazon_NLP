# Día 12 · Correlaciones, regresiones e introducción a scikit-learn

**Fecha:** Viernes 8 de mayo de 2026  
**Módulo:** Módulo 3 · Visualización y análisis exploratorio de datos  
**Duración:** 2 horas sincrónicas  

---

## Introducción

Cerramos el módulo 3 con el primer modelo predictivo del proyecto. No esperamos un modelo perfecto: la meta es tener un **baseline** honesto que servirá de punto de comparación en el módulo 4.

## Objetivos de aprendizaje

Al finalizar esta sesión serás capaz de:

- Interpretar correlaciones y sus límites.
- Entrenar y evaluar un modelo simple de regresión o clasificación.
- Adoptar el flujo estándar de scikit-learn.

## Contenidos de la sesión

### 1. Correlaciones

**Pearson** (lineal, variables continuas). **Spearman** (monotónica, robusta a no linealidades). **Kendall** (similar a Spearman, útil con muchos empates). La correlación ≠ causalidad.

### 2. Visualizar correlaciones

`sns.heatmap(df.corr(), annot=True, cmap="RdBu_r", center=0)`. Pairplots para explorar relaciones.

### 3. Regresión lineal

Modelo: y = β₀ + β₁x₁ + ... + βₙxₙ + ε. Interpretación de coeficientes. Supuestos: linealidad, independencia, homocedasticidad, normalidad de residuales.

### 4. Regresión logística

Para clasificación binaria. Función sigmoide transforma la combinación lineal en probabilidad.

### 5. API de scikit-learn

Patrón universal:
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)
score = model.score(X_test, y_test)
```

### 6. Preprocesamiento

`StandardScaler`, `MinMaxScaler`, `OneHotEncoder`, `OrdinalEncoder`. `ColumnTransformer` para aplicar distintas transformaciones por tipo de columna.

### 7. Pipelines

`Pipeline([("prep", preprocessor), ("model", LogisticRegression())])`. Evitan fugas de datos entre entrenamiento y test.

## Actividad práctica

Entrena en `notebooks/10_modelo_base.ipynb`:

1. Regresión lineal sobre California Housing para predecir el precio.
2. Regresión logística sobre Titanic para predecir supervivencia.

Para cada uno: reporta coeficientes/importancias y la métrica principal.

## Trabajo en grupo sobre el caso asignado

Entrenen el **primer modelo del caso** con evaluación inicial (RMSE si es regresión, Accuracy si es clasificación). Guarden el modelo con `joblib.dump(model, "models/baseline.joblib")`. Preparen la presentación de la Semana 3 del lunes.

## Entregable del día

Notebook `10_modelo_base.ipynb` + modelo serializado en `models/`.

## Recursos recomendados

- scikit-learn – User Guide: https://scikit-learn.org/stable/user_guide.html
- "An Introduction to Statistical Learning" (libro gratuito): https://www.statlearning.com/

---


