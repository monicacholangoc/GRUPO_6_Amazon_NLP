# Día 3 · Fundamentos de Python II — Notas del profesor

**Fecha:** Jueves 23 de abril de 2026 · **Duración:** 2h30 sincrónicas (150 min)

---

## Antes de empezar (15 min antes)

Abre el notebook `clase_03.ipynb` y ten a mano un notebook en blanco. Repasa rápido cómo explicar estos tres conceptos sin mirar apuntes, porque vas a querer pizarra mental ágil:

1. **Condicional** con `elif` anidado
2. **Función** con parámetros por defecto
3. **Diccionario** vs lista vs tupla — cuándo usar cada uno

Mira los notebooks que subieron ayer al repo (5 minutos). Identifica dos cosas:
- ¿Quiénes NO subieron? (lista mental)
- ¿Cuáles fueron los errores comunes? (prepárate para referenciarlos hoy)

**Energía interna:** hoy es el día más denso de la semana en contenido técnico. Tres bloques gordos: control de flujo, estructuras de datos, funciones. Si los tres los cubres bien, pandas la próxima semana fluye. Si solo cubres dos, pandas sufre. Elige qué sacrificar si tienes que sacrificar — el orden de prioridad es: **funciones > estructuras > control de flujo**. Las tres son importantes pero funciones es lo que menos podrán sacar de leer la documentación.

---

## Arco general del día

Tres temas pesados:
1. **Control de flujo:** `if/elif/else`, `for`, `while`, `break`, `continue`.
2. **Estructuras de datos:** listas, tuplas, diccionarios, sets — con los métodos más comunes.
3. **Funciones:** definir, parámetros, return, scope, docstrings.

La trampa: enseñar los tres en abstracto y no mostrar cómo se combinan. Al final del día deberían ver (y practicar) una función que reciba una lista, la recorra con un `for`, y devuelva un diccionario — porque eso es el 60% de lo que van a escribir en pandas.

Objetivo al cierre:
- Todos pueden escribir un `for` con `if` dentro
- Todos entienden la diferencia entre listas y diccionarios (y cuándo usar cada uno)
- Todos pueden definir una función con parámetros y entender qué es `return`
- Todos terminan el ejercicio guiado + aplicado
- Todos suben el notebook al repo antes de mañana

---

## Minuto a minuto

### 0–10 min · Apertura y repaso de ayer

Abre con contexto:

> "Ayer Python ya es un lenguaje que conocen. Hoy lo organizamos. Mañana ese conocimiento organiza los datos del proyecto."

Menciona explícitamente los errores que viste en los notebooks de ayer:

> "Ví en varios notebooks de ayer que `x == 5` a veces lo escribieron como `x = 5`. Si su assert no pasó, revisen eso primero."

Esto dice: "yo miro sus notebooks, no los subo para nada". Refuerza el hábito de entregar.

Pregunta rápido: "¿Alguien se quedó atascado en el desafío del día 2 y no pudo con él?". Si es <3 personas, 2 min de explicación colectiva. Si es más, promete resolverlo al cierre del día o pasa a un canal asincrónico.

Ejecuta el setup de `clase_03.ipynb` con ellos (2 min).

### 10–40 min · Control de flujo (30 min)

**If / elif / else** primero. Live coding:

```python
nota = 85

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("F")
```

Explica qué hace cada línea. **Énfasis en la indentación:**

> "Python usa indentación como sintaxis, no como decoración. Si no indentan, el programa no corre. Cuatro espacios es el estándar. VS Code lo hace automático si presionas tab."

Muestra el error común: indentar mal y ver `IndentationError`. Hazlo deliberadamente:

```python
if nota >= 90:
print("A")   # ERROR: debe estar indentado
```

Ejecuta, lee el error en voz alta, explica. Diles: "Este error lo van a ver muchas veces. Ahora saben qué significa."

**For loops** después. Muestra la sintaxis con una lista concreta:

```python
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")
```

Pregunta: "¿cuántas veces se ejecuta este print?". Silencio. Alguien dice 3. Amplifica.

Muestra `range()`:

```python
for i in range(5):
    print(i)
```

Explica: `range(5)` genera `0, 1, 2, 3, 4`. Cinco números, pero empieza en 0. Resalta que **Python siempre empieza en 0** (listas, strings, ranges — todo).

Combina `for` con `if`:

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
print(pares)
```

**Señala que esto es el patrón más común de todos.** Recorrer, filtrar, acumular. Es la base de pandas.

**While loops** muy rápido. Un ejemplo corto:

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

No profundices. Diles: "While lo usan cuando no saben cuántas iteraciones. For cuando sí. En data science, `for` es el 95% de los casos."

Menciona `break` y `continue` en una frase: "`break` sale del loop, `continue` salta a la siguiente iteración. Los van a necesitar raramente."

### 40–45 min · Pausa (5 min)

> "Cinco minutos. A las [hora] vemos estructuras de datos."

### 45–80 min · Estructuras de datos (35 min)

Este es el bloque con más contenido. Pero hay que hacerlo bien porque el resto del curso depende.

**Listas** (10 min). Live coding:

```python
paises = ["Ecuador", "Colombia", "Perú", "Chile"]

print(paises[0])         # Ecuador
print(paises[-1])        # Chile
print(len(paises))       # 4

paises.append("Bolivia")
paises.remove("Perú")
print(paises)
```

Muestra los métodos más comunes: `.append()`, `.remove()`, `.sort()`, `.reverse()`. Explica que las listas son **mutables**: puedes cambiarlas después de crearlas.

**Tuplas** (3 min rápido):

```python
coordenadas = (-0.18, -78.47)  # Quito
print(coordenadas[0])
# coordenadas[0] = 0  # ERROR: tuplas son inmutables
```

Explica en una frase: "Las tuplas son como listas, pero no se pueden modificar. Úsenlas cuando tengan datos que no deben cambiar, como coordenadas GPS o fechas."

**Diccionarios** (15 min — aquí es donde se queda el grupo). Este es EL concepto más importante del día. Pandas es esencialmente diccionarios en esteroides.

```python
estudiante = {
    "nombre": "Ana",
    "edad": 22,
    "carrera": "Software",
    "semestre": 8
}

print(estudiante["nombre"])
print(estudiante.get("nombre"))

estudiante["edad"] = 23       # Modificar
estudiante["ciudad"] = "Quito"  # Agregar

print(estudiante.keys())
print(estudiante.values())
print(estudiante.items())
```

**Aquí pausa el live coding y pregunta:**

> "¿Cuál es la diferencia entre una lista y un diccionario? ¿Cuándo usarían cada uno?"

Deja silencio. Espera 10 segundos. Alguien dirá "lista es ordenada" o "diccionario tiene claves". Amplifica y llévalos al punto:

> "Las listas son para **secuencias** — cosas ordenadas donde cada elemento es del mismo tipo (una lista de precios, una lista de nombres). Los diccionarios son para **registros** — un conjunto de campos que describen una entidad (un estudiante, un producto, un pedido). Piensen en una tabla Excel: cada fila es un diccionario, la tabla completa es una lista de diccionarios."

Muestra ese último concepto con código:

```python
estudiantes = [
    {"nombre": "Ana", "edad": 22},
    {"nombre": "Beto", "edad": 25},
    {"nombre": "Cata", "edad": 21},
]

for e in estudiantes:
    print(f"{e['nombre']} tiene {e['edad']} años")
```

Esto es un DataFrame antes del DataFrame. Diles explícitamente: "La semana que viene con pandas, van a ver que un DataFrame es básicamente esto pero más rápido y con mejor sintaxis. Si entienden esto hoy, pandas va a ser fácil."

**Sets** (5 min muy rápido):

```python
tags = {"python", "data", "python", "viz"}
print(tags)  # solo valores únicos
```

Diles: "Sets son para cuando necesitan valores únicos. No los van a usar mucho en el curso, pero sepan que existen."

### 80–85 min · Pausa (5 min)

### 85–110 min · Funciones (25 min)

Este es el otro pilar. Live coding despacio:

```python
def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo.

    Args:
        base: La base en metros.
        altura: La altura en metros.

    Returns:
        El área en metros cuadrados.
    """
    area = base * altura
    return area

resultado = calcular_area_rectangulo(5, 3)
print(resultado)
```

Desglosa línea por línea:
- `def` define una función
- El nombre: verbo + qué hace. Descriptivo.
- Los parámetros: lo que la función necesita para trabajar
- Docstring (el `"""..."""`): qué hace la función. **No es opcional en este curso.**
- El cuerpo: lo que hace la función
- `return`: lo que devuelve

**Pregunta:** "¿Qué pasa si no pongo `return`?". Déjalos pensar. Respuesta: la función devuelve `None`. Muestra:

```python
def sin_return(x):
    print(x * 2)

r = sin_return(5)
print(r)  # None
```

**Parámetros por defecto:**

```python
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}"

print(saludar("Ana"))
print(saludar("Ana", saludo="Buenos días"))
```

**Scope (concepto difícil, mantenlo simple):**

```python
x = 10  # variable global

def cambiar():
    x = 20  # variable local
    print("Dentro:", x)

cambiar()
print("Fuera:", x)
```

Explica: "Las variables dentro de una función son locales. No afectan las de fuera. Esto es bueno — evita que una función rompa algo en otro lado." No abras el tema de `global` — ni siquiera lo menciones, se van a confundir.

### 110–140 min · Ejercicios (30 min)

Explica los tres ejercicios rápido:

1. **Guiado:** función que reciba una lista de números y devuelva un diccionario con `max`, `min`, `promedio`.
2. **Aplicado:** función que reciba una lista de diccionarios (estudiantes) y devuelva los estudiantes mayores de 20 años.
3. **Desafío:** función que agrupe estudiantes por carrera en un diccionario.

**Plan:**
- 5 min: explicar los 3 y leer los enunciados
- 20 min en breakouts de equipo
- 5 min: un equipo comparte su solución del aplicado

En los breakouts, entra a cada sala 1 min. Pregunta qué están haciendo. No resuelvas.

Si un equipo termina los 3 antes de los 20 min, dales bonus: "¿Pueden refactorizar el desafío usando solo list/dict comprehensions?". Es un gancho para los que avanzan rápido sin que los otros se sientan apurados.

### 140–145 min · Checkpoint corto (5 min)

Tres preguntas al aire:
1. "¿Qué devuelve una función si no tiene `return`?"
2. "¿Cuál es la diferencia entre una lista y un diccionario?"
3. "¿Qué es un docstring y para qué sirve?"

Si hay silencio, pregunta directo a alguien. Anota mentalmente quién no responde bien — son los que necesitan seguimiento.

### 145–150 min · Cierre (5 min)

Cámara tuya, mira al grupo:

> "Hoy vieron los fundamentos que se repiten en todo lo demás. Funciones, loops y diccionarios son el 80% de lo que van a escribir en el resto del curso. Si algo no quedó claro, mejor preguntarlo mañana que tragárselo."

> "Mañana es la primera entrega: S1 — Planteamiento del proyecto. Vengan con su pregunta de negocio medio pensada. Van a usar la clase entera para pulirla en equipo conmigo rondando."

> "Suban el notebook al repo antes de mañana. Terminen el desafío si alcanzan; si no, suban lo que tengan."

Corta ahí. No alargues.

---

## Después de la sesión (30 min de tu tiempo)

1. **Revisar notebooks subidos:** foca en si los ejercicios aplicado y desafío los resolvieron como función o como código suelto. Los que no usaron `def` no captaron el concepto — envía mensaje individual.
2. **Alertas subiendo:** si alguien no ha subido ni el Día 2 ni el Día 3, es zona roja. Llámalo directamente (DM, no grupo).
3. **Preparación Día 4:** la sesión de mañana es casi enteramente trabajo en equipo, tú como mentor rotativo. Prepara la rúbrica de la S1 (pregunta de negocio + 10-15 historias de usuario + ficha de dataset) y tenla lista para compartir como referencia.
4. **Envía recordatorio por chat del curso:** "Mañana S1. Vengan con la pregunta de negocio medio pensada. No tiene que ser perfecta, yo les ayudo a pulirla."

---

## Banderas rojas

- **Alguien que escribió el aplicado sin usar `def`** → no captó la abstracción de función. Importante arreglarlo antes del Día 5 (NumPy). Sesión individual de 15 min.
- **Equipo donde uno no participa en breakouts** → dinámica a atajar antes de la S1 de mañana. Habla con el Product Lead en privado.
- **Un estudiante que "ya sabe todo esto"** → dale rol de mentor + dale un bonus real (list comprehensions, decoradores simples). Evita que se desconecte.
- **Grupo entero lento en diccionarios** → NO sigas a funciones. Dedica otros 10 min a diccionarios con un ejemplo más. Pandas sin diccionarios = naufragio.

---

## Tips de mentor

**Sobre los errores de indentación:** los primeros 2-3 días se van a encontrar con `IndentationError` varias veces. No les digas "ten cuidado con la indentación" — muéstrales cómo configurar VS Code para que autoindente. Ctrl/Cmd + `,` → buscar "indent" → asegurar que "Editor: Tab Size" sea 4 y "Insert Spaces" esté activo.

**Sobre la retención conceptual:** funciones y diccionarios son los dos que se olvidan. A la mitad del curso muchos todavía van a escribir `estudiante.nombre` en vez de `estudiante["nombre"]` (herencia de otros lenguajes). No los corrijas con sarcasmo — solo recuerda.

**Sobre el overload:** si sientes que los estás perdiendo a la mitad del día, corta contenido. Funciones es lo último que no se puede saltar. Loops básicos, dicts básicos, funciones — si llegan con eso, mañana funcionan. El resto lo recuperan en casa.

**Sobre la pregunta "¿usaremos POO?":** la respuesta es "sí, en la semana 4. Hoy no". No abras el tema.

**Sobre enseñar funciones a gente que nunca las ha visto:** usa analogías. "Una función es una máquina: recibe ingredientes (parámetros), hace algo adentro, y saca un resultado (return). Como una licuadora: recibe frutas, las procesa, y da un jugo. El `return` es lo que sale por la boca."

**Sobre los equipos que avanzan muy rápido:** NUNCA los aburras. Dales ownership — "¿puedes explicarle el ejercicio 3 a [otro equipo] en 5 minutos?". Enseñar es la prueba definitiva de haber aprendido.

---

## Material auxiliar

- `clase_03.ipynb` — notebook humanizado del día
- `index.html` Día 3 — referencia escrita
- Cheatsheet de métodos comunes de listas y dicts (opcional)
- Link a la documentación oficial de Python (functions) por si alguien pide referencia

---

## Al cierre del día, reflexiona

- ¿El grupo entiende funciones? (criterio práctico: ¿escribieron `def` en los ejercicios?)
- ¿El grupo entiende diccionarios? (criterio: ¿hicieron el aplicado sin pedir ayuda de sintaxis?)
- ¿Todos están listos para la entrega de mañana?
- ¿Hay alguien que necesita rescate antes de mañana?

Anota 2-3 líneas. Mañana es la primera entrega — si alguien llega sin fundamentos, va a naufragar en la S1.
