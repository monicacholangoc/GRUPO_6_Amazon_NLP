# Día 5 · NumPy – Arrays y operaciones vectorizadas

**Fecha:** Lunes 27 de abril de 2026  
**Módulo:** Módulo 2 · Manipulación y análisis de datos  
**Duración:** 2 horas 30 minutos sincrónicas  

---

## 🗓️ Plan de la Semana 2

| Día | Fecha | Tema |
|-----|-------|------|
| 5 | Lun 27 abr | NumPy – Arrays y operaciones vectorizadas |
| 6 | Mar 28 abr | Pandas I – DataFrames y selección |
| 7 | Mié 29 abr | Pandas II – Agrupaciones y limpieza |
| 8 | Lun 4 may | Estadística descriptiva y visualización inicial |
| **9** | **Mar 5 may** | **SQL con Python — ENTREGA S2** |

### Entregable de cierre: Semana 2

Al cierre del **Día 9 (martes 5 de mayo)** cada equipo entrega el **pipeline completo** corriendo con `python -m src.pipeline`:

- Ingesta desde al menos una fuente real (CSV, Excel, API o base de datos).
- Transformación: nulos, duplicados, outliers y tipos de datos.
- Estructuración: variables derivadas, normalización y categorización.
- Validación de calidad: tests de integridad básicos con pytest.

---

## Introducción

Entramos al módulo 2. NumPy es la base numérica de todo el ecosistema científico de Python. Pandas se apoya en NumPy, scikit-learn también. Si dominas arrays y vectorización, tu código será más rápido y más legible.

## Objetivos de aprendizaje

Al finalizar esta sesión serás capaz de:

- Crear y manipular arrays n-dimensionales.
- Aplicar operaciones vectorizadas y entender el broadcasting.
- Elegir entre bucles Python y operaciones NumPy con criterio.

## Contenidos de la sesión

### 1. El objeto ndarray

Arrays 1D, 2D y nD. Atributos: `.shape`, `.dtype`, `.size`, `.ndim`.

### 2. Creación de arrays

`np.array`, `np.arange`, `np.linspace`, `np.zeros`, `np.ones`, `np.random.rand`, `np.random.randn`, `np.eye`.

### 3. Indexación y slicing

Indexación básica (`a[0, 1]`), slicing por dimensiones (`a[:, 1:3]`), máscaras booleanas (`a[a > 0]`) y *fancy indexing* con listas de índices.

### 4. Operaciones vectorizadas

Operaciones elemento a elemento, funciones universales (`np.sqrt`, `np.log`, `np.exp`). Evitar bucles Python en datos numéricos.

### 5. Agregaciones

`sum`, `mean`, `std`, `min`, `max`, `argmax` con el parámetro `axis`. Entender bien `axis=0` (por columnas) vs. `axis=1` (por filas).

### 6. Broadcasting

Cómo NumPy opera entre arrays de diferentes shapes. Ejemplo: centrar una matriz restándole la media por columna con una sola línea.

## Actividad práctica

En `notebooks/02_numpy.ipynb`:

1. Crea un array 10×5 con datos aleatorios (`np.random.rand(10, 5)`).
2. Normaliza cada columna restando la media y dividiendo por la desviación (sin bucles).
3. Calcula la distancia euclídea entre dos arrays de puntos 2D usando operaciones vectorizadas.

## Trabajo en grupo sobre el caso asignado

Descarguen el dataset del caso y cárguenlo en un DataFrame. En `notebooks/03_dataset.ipynb` reporten:
- `shape` y `dtypes`.
- Primeras 5 filas.
- Porcentaje de nulos por columna.
- Cualquier observación inicial relevante.

## Entregable del día

Notebooks `02_numpy.ipynb` y `03_dataset.ipynb` versionados en Git.

## Recursos recomendados

- NumPy – Absolute Beginners: https://numpy.org/doc/stable/user/absolute_beginners.html
- Visualización de broadcasting: https://numpy.org/doc/stable/user/basics.broadcasting.html

---


