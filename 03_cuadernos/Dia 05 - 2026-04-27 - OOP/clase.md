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

---

## Introducción

Hoy damos el salto conceptual más importante de la semana: **Programación Orientada a Objetos (OOP)**. Las librerías del ecosistema Python (Pandas, scikit-learn, Matplotlib) están construidas con clases y objetos. Cuando escribes `df.describe()` o `model.fit(X, y)`, estás llamando métodos de un objeto. Hoy entenderás cómo funciona eso por dentro.

## Objetivos de aprendizaje

Al finalizar esta sesión serás capaz de:

- Definir clases con atributos y métodos propios.
- Usar el constructor `__init__` y `self` con confianza.
- Aplicar herencia para crear jerarquías de clases.
- Usar polimorfismo para código genérico y reutilizable.
- Implementar encapsulamiento con atributos privados y `@property`.
- Usar métodos mágicos para integrar objetos con Python.

## Contenidos de la sesión

### 1. ¿Qué es OOP? Clases y Objetos

La diferencia entre clase (molde) e instancia (objeto). Atributos y métodos. La relación con módulos y librerías.

### 2. Constructor `__init__` y `self`

Cómo se inicializa un objeto. Por qué `self` siempre es el primer parámetro. Estado propio de cada objeto.

### 3. Herencia

Crear subclases especializadas. `super()` para reutilizar el padre. Sobreescribir métodos.

### 4. Polimorfismo

Diferentes clases respondiendo al mismo método. Código genérico que no depende del tipo exacto.

### 5. Encapsulamiento

Atributos privados (`__atributo`). `@property` y `@setter` para acceso controlado.

### 6. Métodos mágicos (Dunder)

`__str__`, `__repr__`, `__len__`, `__eq__`, `__lt__`, `__add__`. Integración nativa con Python.

## Actividad práctica

En `clase_05.ipynb`:

1. Ejercicio guiado: `Persona`, `Estudiante`, `Profesor` con herencia.
2. Ejercicio aplicado: `Rectangulo` con métodos mágicos.
3. Desafío 1: Sistema de inventario (dos clases interactuando).
4. Desafío 2: Figuras geométricas con polimorfismo.
5. Desafío 3: `DatasetSimple` — mini-Pandas con OOP.

## Recursos recomendados

- Video: [POO en Python — mouredev](https://www.youtube.com/watch?v=Tje_s_j7Suk)
- Docs: [Python Classes](https://docs.python.org/3/tutorial/classes.html)

---
