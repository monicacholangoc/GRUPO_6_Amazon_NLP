# Día 11 · Hipótesis y pruebas estadísticas

**Fecha:** Jueves 7 de mayo de 2026  
**Módulo:** Módulo 3 · Visualización y análisis exploratorio de datos  
**Duración:** 2 horas sincrónicas  

---

## Introducción

Hoy convertimos intuiciones en afirmaciones estadísticas verificables. Formular hipótesis y validarlas con rigor distingue a un análisis "eyeball" de un análisis profesional. No te asustes: la matemática es mínima; lo difícil es elegir bien la prueba.

## Objetivos de aprendizaje

Al finalizar esta sesión serás capaz de:

- Formular H₀ y H₁ para tus preguntas de negocio.
- Escoger la prueba adecuada según tipo de variables y tamaño de muestra.
- Interpretar p-valores correctamente.

## Contenidos de la sesión

### 1. Marco general

Hipótesis nula (H₀) vs. alternativa (H₁). Nivel de significancia α (usualmente 0.05). p-valor: probabilidad de observar algo tan extremo o más si H₀ es verdadera.

### 2. Pruebas paramétricas

- **t-test de una muestra**: comparar media con un valor de referencia.
- **t-test de dos muestras**: comparar medias entre dos grupos.
- **t-test pareado**: mismas unidades medidas antes/después.
- **ANOVA**: comparar medias entre 3+ grupos.

### 3. Pruebas no paramétricas

Cuando los datos no son normales o la muestra es pequeña:
- **Mann–Whitney U** (reemplaza t-test de dos muestras).
- **Wilcoxon** (reemplaza t-test pareado).
- **Kruskal–Wallis** (reemplaza ANOVA).

### 4. Independencia entre categóricas

**Chi-cuadrado** sobre tabla de contingencia (`scipy.stats.chi2_contingency`).

### 5. Tests de normalidad

Shapiro–Wilk (n < 5000), Kolmogorov–Smirnov. Complementan con gráficos Q-Q.

### 6. Interpretación

p < α → rechazamos H₀. p ≥ α → no hay evidencia suficiente para rechazar H₀. **Nunca** se "acepta" H₀. Reportar también tamaño de efecto, no solo p-valor.

### 7. Librerías

`scipy.stats` para la mayoría de pruebas. `statsmodels` cuando necesitas intervalos de confianza o regresión explicativa.

## Actividad práctica

Sobre `tips.csv`, valida en `notebooks/09_hipotesis.ipynb` dos hipótesis:

1. ¿La propina media es mayor en cenas que en almuerzos?
2. ¿El día de la semana influye en la propina?

Para cada una: formula H₀ y H₁, elige la prueba, ejecuta, interpreta.

## Trabajo en grupo sobre el caso asignado

Formulen **3 hipótesis** relevantes para la pregunta de negocio del caso y valídenlas sobre su dataset. Documenten en `notebooks/09_hipotesis.ipynb` con la estructura: hipótesis → prueba → resultado → interpretación → decisión.

## Entregable del día

Notebook `09_hipotesis.ipynb` con código, salidas e interpretación de cada prueba.

## Recursos recomendados

- SciPy Stats – Reference: https://docs.scipy.org/doc/scipy/reference/stats.html
- "The Hacker's Guide to Statistical Inference" (recurso gratuito online).

---


