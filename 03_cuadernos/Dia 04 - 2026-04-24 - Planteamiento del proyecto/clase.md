# Día 4 · Planteamiento del proyecto analítico y estructura del repositorio · ENTREGA SEMANA 1

**Fecha:** Viernes 24 de abril de 2026  
**Módulo:** Módulo 1 · Introducción a Python y kick-off del proyecto  
**Duración:** 2 horas 30 minutos sincrónicas  

---

## Introducción

Cerramos la primera semana montando la estructura profesional del proyecto y formulando la pregunta de negocio. Un proyecto de datos bien planteado ahorra semanas de trabajo; uno mal planteado se descarrila en la fase de modelado. Hoy es el día para definirlo bien.

## Objetivos de aprendizaje

Al finalizar esta sesión serás capaz de:

- Formular una pregunta de negocio clara para tu caso.
- Estructurar el repositorio siguiendo buenas prácticas.
- Caracterizar el dataset con origen, tamaño, calidad y limitaciones.

## Contenidos de la sesión

### 1. CRISP-DM vs. el flujo del seminario

Entendimiento del negocio → Entendimiento de los datos → Preparación → Modelado → Evaluación → Despliegue. Veremos cómo se mapea a los 4 módulos del curso.

### 2. Pregunta de negocio

Tres familias: **medir** (KPIs, reportes), **explicar** (qué factores influyen) y **predecir** (estimar valores futuros o clasificar). Ejemplo para retail: "¿Qué clientes están en riesgo de abandonar en los próximos 30 días?".

### 3. Estructura de carpetas recomendada

```
seminario-eda/
├─ data/
│  ├─ raw/          # datos originales, nunca modificar
│  └─ processed/    # datos limpios
├─ notebooks/       # .ipynb numerados 01_, 02_, ...
├─ src/             # código reutilizable
├─ reports/         # figuras y documentos generados
├─ tests/           # pytest
├─ README.md
├─ requirements.txt
└─ .gitignore
```

### 4. README profesional

Debe responder en 1 minuto: ¿qué hace el proyecto?, ¿cómo se instala?, ¿cómo se ejecuta?, ¿quién lo mantiene? Use badges, capturas y ejemplos.

### 5. Entorno virtual y dependencias

`python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`. Nunca instalen paquetes fuera del venv.

### 6. Ficha del dataset

Documento corto con: URL/origen, licencia, fecha de extracción, número de registros y columnas, tipos por columna, % de nulos, limitaciones conocidas.

## Actividad práctica

En equipo:

1. Creen el entorno virtual y levanten la estructura de carpetas descrita arriba.
2. Escriban la **pregunta de negocio** del caso y justifiquen en 1 párrafo por qué es relevante.
3. Carguen el dataset, ejecuten `df.head()`, `df.info()`, `df.shape` y `df.describe()`.
4. Escriban la ficha del dataset en `docs/ficha_dataset.md`.

## Trabajo en grupo sobre el caso asignado

**ENTREGABLE SEMANA 1** (se evalúa hoy):
- Pregunta de negocio + justificación.
- 10–15 historias de usuario.
- Ficha del dataset (origen, tamaño, calidad, limitaciones).
- Repositorio GitHub con la estructura base y README completo.

## Entregable del día

Presentación de 5 minutos por equipo al final de la sesión + enlace al repositorio. Recibirán retroalimentación del docente para ajustar durante el fin de semana si es necesario.

## Recursos recomendados

- Cookiecutter Data Science: https://cookiecutter-data-science.drivendata.org/
- Escribir buenos README: https://www.makeareadme.com/
- CRISP-DM en 1 página: https://www.datascience-pm.com/crisp-dm-2/

---


