[← Día 15](../Dia%2015%20-%202026-05-13%20-%20APIs%20con%20FastAPI/) · [🏠 Índice](../README.md) · [Día 17 →](../Dia%2017%20-%202026-05-15%20-%20Presentaciones%20finales/)

<a href="https://colab.research.google.com/github/we-human-centric/CursoPythonDatos_2026/blob/main/Dia%2016%20-%202026-05-14%20-%20Buenas%20pr%C3%A1cticas%20y%20portafolio/clase_16.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  &nbsp; [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/we-human-centric/CursoPythonDatos_2026/blob/main/Dia%2016%20-%202026-05-14%20-%20Buenas%20pr%C3%A1cticas%20y%20portafolio/clase_16.ipynb)

---

# Día 16 · Buenas prácticas, testing, documentación y portafolio

**Fecha:** Jueves 14 de mayo de 2026  
**Módulo:** Módulo 4 · Ciencia de datos aplicada y escalabilidad  
**Duración:** 2 horas 30 minutos sincrónicas  

---

## Introducción

A un día de presentar, dedicamos la sesión a lo que distingue un proyecto de clase de un proyecto profesional: modularidad, tests, linting, documentación y cómo publicar el trabajo en tu portafolio.

## Objetivos de aprendizaje

Al finalizar esta sesión serás capaz de:

- Modularizar el código del proyecto con claridad.
- Escribir tests unitarios mínimos y pasar el linter.
- Dejar el README listo para entregar.
- Preparar el proyecto para el portafolio personal.

## Contenidos de la sesión

### 1. Modularización

Separación clara por responsabilidad:

```
src/
├─ data/        # cargas e ingesta
├─ features/    # transformaciones
├─ models/      # entrenamiento y evaluación
├─ api/         # FastAPI
└─ app/         # Streamlit
```

### 2. Configuración externa

Valores que cambian (paths, URLs, parámetros) en `config.yaml` o variables de entorno (`.env`). Nunca commitear credenciales.

### 3. Gestión de dependencias

`pip freeze > requirements.txt` al final. Fijar versiones (`pandas==2.2.0`) asegura reproducibilidad.

### 4. Tests con pytest

Tests unitarios por función crítica. Fixtures reutilizables con `@pytest.fixture`. Correr con `pytest -q`. Cobertura con `pytest-cov`.

### 5. Linting y formateo

`black .` formatea automáticamente. `ruff check .` detecta errores y estilo. Considerar pre-commit hooks.

### 6. Documentación

README.md con: descripción, instalación, uso, estructura de carpetas, resultados y licencia. Docstrings en todas las funciones públicas.

### 7. CI/CD básico (opcional)

GitHub Actions: un workflow que corre tests y linter en cada push.

### 8. Portafolio

LinkedIn post con el proyecto, GitHub Pages para servir el README como sitio, video corto (1–2 min) con la demo. Pitch de 60 segundos: problema → qué hiciste → resultados → impacto.

## Actividad práctica

En el repo del grupo:

1. Escriban **3 tests unitarios** para funciones críticas del pipeline.
2. Pasen `black` y `ruff` a todo el código.
3. Completen el README con todas las secciones.
4. Ensayen la presentación final (10 min exposición + 5 min preguntas).

## Trabajo en grupo sobre el caso asignado

Ensayo general en vivo. Cada integrante habla al menos una parte. Revisen demos en vivo de **dashboard** y **API** para evitar sorpresas el viernes.

## Entregable del día

Repositorio limpio con README completo, `requirements.txt`, tests pasando y estructura modular.

## Recursos recomendados

- pytest – Getting started: https://docs.pytest.org/en/stable/getting-started.html
- Black: https://black.readthedocs.io/
- Ruff: https://docs.astral.sh/ruff/

---

---

[← Día 15](../Dia%2015%20-%202026-05-13%20-%20APIs%20con%20FastAPI/) · [🏠 Índice](../README.md) · [Día 17 →](../Dia%2017%20-%202026-05-15%20-%20Presentaciones%20finales/)

> *Seminario EDA · Abril–Mayo 2026 · [we-human-centric](https://github.com/we-human-centric)*
