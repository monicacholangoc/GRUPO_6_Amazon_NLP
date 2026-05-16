# Día 2 · Fundamentos de Python I – Sintaxis y tipos primitivos

**Fecha:** Miércoles 22 de abril de 2026  
**Módulo:** Módulo 1 · Introducción a Python y kick-off del proyecto  
**Duración:** 2 horas 30 minutos sincrónicas  

---

## Introducción

Arrancamos con la base del lenguaje. El objetivo hoy es que puedas leer y escribir pequeños scripts con fluidez: variables, operadores, strings y el ciclo básico de entrada/salida. Todo el curso se apoya en estos fundamentos, así que tómate el tiempo de practicar.

## Objetivos de aprendizaje

Al finalizar esta sesión serás capaz de:

- Dominar los tipos primitivos de Python (int, float, str, bool, None).
- Usar operadores y cadenas con soltura, incluyendo f-strings.
- Escribir scripts simples siguiendo PEP 8.

## Contenidos de la sesión

### 1. Variables y tipos primitivos

Asignación, tipado dinámico, `type()`, conversión entre tipos con `int()`, `float()`, `str()`, `bool()`.

### 2. Operadores

Aritméticos (`+ - * / // % **`), de comparación (`== != < > <= >=`), lógicos (`and or not`) y de asignación (`+=`, `-=`, etc.).

### 3. Cadenas (strings)

Concatenación, slicing (`s[1:5]`), métodos más usados (`upper`, `lower`, `strip`, `replace`, `split`, `join`, `startswith`, `endswith`). F-strings: `f"Hola {nombre}"`.

### 4. Entrada/salida

`print()` con `sep` y `end`, `input()` para leer desde consola. Siempre convertir lo que devuelve `input` al tipo necesario.

### 5. PEP 8 y estilo

Nombres en `snake_case`, líneas ≤ 79 caracteres, espacios alrededor de operadores, docstrings con triple comilla.

## Actividad práctica

Resuelve las tres katas siguientes en un notebook `01_intro.ipynb`:

1. **Conversor de temperatura**: lee una temperatura en °C y muestra el equivalente en °F.
2. **Calculadora de propina**: dada una factura y un porcentaje, calcula la propina y el total.
3. **Validador simple de email**: recibe una cadena y devuelve `True` si contiene exactamente un `@` y al menos un `.` después del `@`.

## Trabajo en grupo sobre el caso asignado

Redacten las **3 primeras historias de usuario** del caso, en el formato:

> Como **<rol>**, quiero **<acción>** para **<beneficio>**.

Guárdenlas en `docs/historias_usuario.md` dentro del repositorio.

## Entregable del día

Notebook `01_intro.ipynb` con las 3 katas resueltas y commit en el repo del grupo.

## Recursos recomendados

- PEP 8 (guía de estilo): https://peps.python.org/pep-0008/
- Documentación oficial de strings: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

---


