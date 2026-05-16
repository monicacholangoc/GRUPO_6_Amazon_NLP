[← Día 04](../Dia%2004%20-%202026-04-24%20-%20Planteamiento%20del%20proyecto/) · [🏠 Índice](../README.md) · [Día 06 →](../Dia%2006%20-%202026-04-28%20-%20Pandas%20I/)

<a href="https://colab.research.google.com/github/we-human-centric/CursoPythonDatos_2026/blob/main/Dia%2005%20-%202026-04-27%20-%20OOP/clase_05.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

---

# Día 5 · Programación Orientada a Objetos (OOP)

**Fecha:** Lunes 27 de abril de 2026  
**Módulo:** Módulo 1 · Fundamentos de Python  
**Duración:** 2 horas 30 minutos sincrónicas  

---

## 🗓️ Plan de la Semana 2

| Día | Fecha | Tema |
|-----|-------|------|
| **5** | **Lun 27 abr** | **OOP – Programación Orientada a Objetos** |
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

Hoy damos el salto conceptual más importante de la semana: **Programación Orientada a Objetos (OOP)**. Comprender OOP no es solo aprender una sintaxis nueva — es entender *por qué* Pandas, scikit-learn y Matplotlib están diseñados como están. Cuando escribes `df.describe()` o `model.fit(X, y)`, estás usando objetos y métodos. Hoy entenderás la mecánica detrás de eso.

## Objetivos de aprendizaje

Al finalizar esta sesión serás capaz de:

- Definir clases con atributos y métodos propios.
- Usar el constructor `__init__` y `self` con confianza.
- Aplicar herencia para crear jerarquías de clases relacionadas.
- Usar polimorfismo para escribir código genérico y reutilizable.
- Implementar encapsulamiento con atributos privados y `@property`.
- Usar métodos mágicos (`__str__`, `__len__`, `__eq__`, etc.) para integrar objetos con Python.

## Contenidos de la sesión

### 1. ¿Qué es OOP? Clases y Objetos

La diferencia entre clase (molde) e instancia (objeto). Atributos y métodos. La relación con módulos y librerías.

### 2. Constructor `__init__` y `self`

Cómo se inicializa un objeto. Por qué `self` siempre es el primer parámetro. Atributos de instancia vs. atributos de clase.

### 3. Herencia

Crear subclases que heredan de una clase base. Usar `super()` para llamar al constructor del padre. Sobreescribir métodos.

### 4. Polimorfismo

Diferentes clases respondiendo al mismo método. Código que funciona con cualquier objeto que tenga la interfaz correcta.

### 5. Encapsulamiento

Atributos privados (`__atributo`). Propiedades con `@property` y `@setter`. Por qué proteger el estado interno.

### 6. Métodos mágicos (Dunder)

`__str__`, `__repr__`, `__len__`, `__eq__`, `__lt__`, `__add__`. Cómo integrar tus objetos con Python.

## Actividad práctica

En el notebook `clase_05.ipynb`:

1. Ejercicio guiado: clases `Persona`, `Estudiante`, `Profesor` con herencia y propiedades.
2. Ejercicio aplicado: clase `Rectangulo` con métodos mágicos para comparación y ordenamiento.
3. Desafío 1: Sistema de inventario con dos clases interactuando.
4. Desafío 2: Jerarquía de figuras geométricas con polimorfismo puro.
5. Desafío 3: Clase `DatasetSimple` — anticipa lo que hace Pandas.

## Recursos recomendados

- Video: [POO en Python — mouredev](https://www.youtube.com/watch?v=Tje_s_j7Suk)
- Documentación oficial: [Python Classes Tutorial](https://docs.python.org/3/tutorial/classes.html)
- Real Python: [Object-Oriented Programming in Python 3](https://realpython.com/python3-object-oriented-programming/)

---

[← Día 04](../Dia%2004%20-%202026-04-24%20-%20Planteamiento%20del%20proyecto/) · [🏠 Índice](../README.md) · [Día 06 →](../Dia%2006%20-%202026-04-28%20-%20Pandas%20I/)

> *Seminario EDA · Abril–Mayo 2026 · [we-human-centric](https://github.com/we-human-centric)*
