[← Día 08](../Dia%2008%20-%202026-05-04%20-%20Estad%C3%ADstica%20descriptiva%20y%20visualizaci%C3%B3n%20inicial/) · [🏠 Índice](../README.md) · [Día 10 →](../Dia%2010%20-%202026-05-06%20-%20Visualizaciones%20avanzadas/)

<a href="https://colab.research.google.com/github/we-human-centric/CursoPythonDatos_2026/blob/main/Dia%2009%20-%202026-05-05%20-%20SQL%20con%20Python%20-%20ENTREGA%20SEMANA%202/clase_09.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  &nbsp; [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/we-human-centric/CursoPythonDatos_2026/blob/main/Dia%2009%20-%202026-05-05%20-%20SQL%20con%20Python%20-%20ENTREGA%20SEMANA%202/clase_09.ipynb)

---

# Día 9 · Conexión a bases de datos con SQL y Python · ENTREGA SEMANA 2

**Fecha:** Martes 5 de mayo de 2026  
**Módulo:** Módulo 2 · Manipulación y análisis de datos  
**Duración:** 2 horas 30 minutos sincrónicas  

---

## Introducción

Cerramos el módulo 2 cruzando Pandas con SQL. No todo dato vive en un CSV: muchas veces está en una base de datos. Hoy aprendemos a conectarnos, a consultar, y a persistir los resultados de nuestro pipeline.

## Objetivos de aprendizaje

Al finalizar esta sesión serás capaz de:

- Ejecutar consultas SQL desde Python.
- Usar SQLAlchemy y sqlite3 con criterio.
- Ingerir datos desde APIs REST.
- Entregar el pipeline completo de la Semana 2.

## Contenidos de la sesión

### 1. Repaso de SQL

`SELECT col FROM tabla WHERE cond GROUP BY x HAVING agg > n ORDER BY col LIMIT k`. `JOIN` interno, izquierdo y cruzado.

### 2. sqlite3

```python
import sqlite3
conn = sqlite3.connect("datos.db")
df.to_sql("ventas", conn, if_exists="replace", index=False)
out = pd.read_sql("SELECT * FROM ventas WHERE total > 100", conn)
```

### 3. SQLAlchemy

`create_engine("sqlite:///datos.db")` para desacoplarse del driver. Mismo patrón con PostgreSQL o MySQL cambiando el URI.

### 4. APIs REST con requests

`requests.get(url, params, headers, timeout)`; convertir JSON a DataFrame con `pd.DataFrame(response.json())` o `pd.json_normalize(...)`. Control de errores y *rate limits*.

### 5. Persistencia

CSV vs. Parquet vs. SQLite. Parquet comprime bien y conserva tipos; úsenlo para datasets grandes.

### 6. Ejecutar scripts

Estructura: `python -m src.pipeline` desde la raíz del proyecto. Ventajas sobre ejecutar `.ipynb` a mano.

### 7. Tests básicos con pytest

`tests/test_pipeline.py` con funciones `test_*`. Ejecutar con `pytest -q`.

## Actividad práctica

1. Carguen su DataFrame limpio a una base SQLite local con `to_sql`.
2. Escriban 3 consultas SQL útiles para el caso y ejecútenlas con `read_sql`.
3. Agreguen `tests/test_pipeline.py` con al menos un test de integridad (ej. "no hay precios negativos").

## Trabajo en grupo sobre el caso asignado

**ENTREGABLE SEMANA 2**:
- Pipeline que corre end-to-end con `python -m src.pipeline`.
- Ingesta desde ≥1 fuente real (CSV, Excel, API o BD).
- Transformación (nulos, duplicados, outliers, tipos).
- Estructuración (variables derivadas, normalización, categorización).
- Validación de calidad (tests en `tests/`).
- Presentación de 5 minutos por equipo.

## Entregable del día

Repo actualizado + base SQLite generada + tests pasando.

## Recursos recomendados

- SQLAlchemy – Quickstart: https://docs.sqlalchemy.org/en/20/orm/quickstart.html
- Requests – Quickstart: https://requests.readthedocs.io/en/latest/user/quickstart/

---

---

[← Día 08](../Dia%2008%20-%202026-05-04%20-%20Estad%C3%ADstica%20descriptiva%20y%20visualizaci%C3%B3n%20inicial/) · [🏠 Índice](../README.md) · [Día 10 →](../Dia%2010%20-%202026-05-06%20-%20Visualizaciones%20avanzadas/)

> *Seminario EDA · Abril–Mayo 2026 · [we-human-centric](https://github.com/we-human-centric)*
