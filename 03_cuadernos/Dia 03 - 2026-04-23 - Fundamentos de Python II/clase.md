# Día 3 · Fundamentos de Python II – Control, colecciones y funciones

**Fecha:** Jueves 23 de abril de 2026  
**Módulo:** Módulo 1 · Introducción a Python y kick-off del proyecto  
**Duración:** 2 horas 30 minutos sincrónicas  

---

## Introducción

Hoy damos el salto de scripts lineales a código organizado: controlamos el flujo con condicionales y bucles, almacenamos datos en estructuras (listas, tuplas, sets y diccionarios) y modularizamos con funciones. Esta sesión es clave para todo lo que viene.

## Objetivos de aprendizaje

Al finalizar esta sesión serás capaz de:

- Aplicar estructuras de control para resolver problemas reales.
- Elegir la estructura de datos adecuada (lista, tupla, set, dict).
- Escribir funciones reutilizables con type hints y docstrings.

## Contenidos de la sesión

### 1. Condicionales

`if / elif / else`, expresiones ternarias (`x if cond else y`). Evitar anidamientos profundos con *guard clauses*.

### 2. Bucles

`for` e `in`, `range`, `enumerate`, `zip`. `while` y cuándo preferirlo. `break`, `continue` y la cláusula `else` de los bucles.

### 3. Colecciones

- **Listas**: mutables, indexables, ordenadas.
- **Tuplas**: inmutables, ideales para datos que no deben cambiar.
- **Sets**: colección sin duplicados, operaciones de conjuntos.
- **Diccionarios**: pares clave-valor, acceso O(1).

### 4. Comprensiones

List comprehensions: `[x*2 for x in xs if x > 0]`. Dict comprehensions: `{k: v for k, v in items}`. Son más legibles y rápidas que los bucles equivalentes.

### 5. Funciones

Declaración con `def`, parámetros posicionales y por nombre, `*args`, `**kwargs`, valores por defecto, `return`, *type hints* y *docstrings*. Principio: **una función, una responsabilidad**.

### 6. Módulos

Cómo dividir código en archivos `.py` y usarlos con `import` / `from ... import ...`. El patrón `if __name__ == "__main__":`.

### 7. Manejo de errores

`try / except / else / finally`. Capturar excepciones específicas en vez de `except Exception`.

## Actividad práctica

En el mismo notebook `01_intro.ipynb`:

1. Refactoriza las tres katas del día anterior como **funciones** con type hints y docstrings.
2. Dada una lista de tuplas `ventas = [("A", 100), ("B", 50), ("A", 30), ("C", 10)]`, calcula con una comprensión y un diccionario el **total de ventas por producto**. Resultado esperado: `{'A': 130, 'B': 50, 'C': 10}`.

## Trabajo en grupo sobre el caso asignado

Completen las **10 a 15 historias de usuario** del caso asignado y suban el archivo actualizado a `docs/historias_usuario.md`. Asegúrense de cubrir usuarios, administradores y roles analíticos.

## Entregable del día

Módulo `.py` con las funciones documentadas y notebook actualizado, todo en el repo del grupo.

## Recursos recomendados

- Tutorial oficial de Python – Estructuras de datos: https://docs.python.org/3/tutorial/datastructures.html
- Guía de typing (type hints): https://docs.python.org/3/library/typing.html

---


