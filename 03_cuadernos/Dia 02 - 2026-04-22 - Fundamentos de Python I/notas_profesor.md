# Día 2 · Fundamentos de Python I — Notas del profesor

**Fecha:** Miércoles 22 de abril de 2026 · **Duración:** 2h30 sincrónicas (150 min)

---

## Antes de empezar (15 min antes)

Abre el notebook `clase_02.ipynb` en Jupyter y el `index.html` del Día 2 en una pestaña aparte. Ten listo un notebook en blanco para escribir en vivo — **hoy se programa frente a ellos**, no se lee código preparado.

Revisa rápido la lista de alertas que dejaste ayer. ¿Los estudiantes en riesgo se conectaron? ¿Todos los equipos tienen GitHub funcional? Si alguien te escribió ayer con problemas de instalación, verifica que estén resueltos o ten listo Colab como plan B.

**Energía interna:** hoy hacen las primeras líneas de código. Es el día más importante del curso para la motivación. Si alguien sale de esta sesión pensando "Python no es para mí", es muy difícil recuperarlo después. Tu trabajo no es meter mucho contenido — es hacer que todos escriban código que funciona y lo entiendan. Baja el ritmo si hace falta.

---

## Arco general del día

Hoy cubrimos tipos primitivos (int, float, str, bool), operadores (aritméticos, relacionales, lógicos) y formateo de strings. Es contenido que muchos conocen superficialmente, pero que casi nadie tiene claro al nivel que necesitan para pandas la semana entrante.

La trampa de hoy: pasar por encima porque "es básico". El Día 7 cuando pandas les reviente con un error de tipos (`TypeError: can only concatenate str to str, not int`) van a volver a este día mental.

La otra trampa: querer cubrir demasiado. Si terminas solo el ejercicio guiado y el aplicado, está bien. Si el desafío lo hacen en casa, está bien. **Mejor profundo y lento que rápido y confuso.**

Objetivo al cierre:
- Todos han ejecutado Python en su máquina (no solo leído)
- Todos entienden la diferencia entre `=` y `==`
- Todos pueden explicar por qué `"5" + 5` falla y `5 + 5.0` no
- Todos hicieron al menos el ejercicio guiado y el aplicado
- Todos subieron el notebook al repo del equipo

---

## Minuto a minuto

### 0–10 min · Apertura y conexión con ayer

Empieza puntual. Abre con una frase corta que conecte:

> "Ayer formamos equipos e instalamos cosas. Hoy escribimos código. Python funciona. Sus máquinas funcionan. Vamos."

Pregunta rápido:
- "¿Alguien tuvo problemas con la instalación que no logró resolver?" (cámara/mano levantada, no chat — necesitas identificar rápido)

Si hay 1-2 personas con problemas, asignalas a Colab por hoy y diles que al cierre del día te quedas 10 minutos con ellos. Si hay más de 3, reprograma y dedica los primeros 20 min a instalación grupal.

**NO** leas los objetivos del día en voz alta. Abre el notebook `clase_02.ipynb`, mantén la cámara de tu lado, y comparte pantalla con el notebook.

### 10–15 min · Setup ejecutado (primera celda de código)

Pídeles que abran `clase_02.ipynb` en su Jupyter local (o Colab). Todos juntos, ejecutan la primera celda de código (setup con imports y SEED). Tiempo estimado: 2-3 minutos de ejecución, 2 minutos de "no me corre".

Errores comunes:
- `ModuleNotFoundError: No module named 'numpy'` → en Colab no pasa. En local: `pip install numpy pandas matplotlib seaborn`. Si no saben dónde ejecutar `pip`, muéstrales cómo abrir terminal en VS Code (`Ctrl+ñ` o View → Terminal).
- Kernel no selecciona Python 3 → clic en "Select Kernel" arriba a la derecha → elegir Python 3.11+.

Cuando todos tengan `Setup completo ✓`, sigue.

### 15–45 min · Tipos primitivos + operadores (live coding)

**No expliques todos los tipos en abstracto.** Escribe en vivo. Abre una celda nueva y teclea:

```python
edad = 27
altura = 1.72
nombre = "Juli"
activo = True

print(type(edad), type(altura), type(nombre), type(activo))
```

Ejecuta. Señala los nombres `int`, `float`, `str`, `bool`. Pregunta en voz alta:

> "¿Por qué creen que no usamos comillas en el 27 pero sí en el 'Juli'?"

Deja silencio de 5 segundos. Si alguien responde, amplifica la respuesta. Si no, dilo tú: "Los números son el valor directo. Los strings son texto, y Python necesita las comillas para saber dónde empiezan y dónde acaban."

Sigue con operadores. Escribe en vivo:

```python
# Aritméticos
print(5 + 3, 5 - 3, 5 * 3, 5 / 3)
print(5 // 3)   # división entera
print(5 % 3)    # módulo (resto)
print(5 ** 3)   # potencia
```

Ejecuta. Explica `//` y `%` con un ejemplo concreto:

> "Si tengo 17 huevos y quiero empacarlos en cartones de 6 — `17 // 6` me dice cuántos cartones completos puedo hacer, y `17 % 6` me dice cuántos huevos quedan sueltos."

Esa frase la recuerdan más que la definición formal.

Sigue con comparaciones (`==`, `!=`, `<`, `>`, `<=`, `>=`) y lógicos (`and`, `or`, `not`). Para cada uno, una línea:

```python
edad = 27
es_mayor_de_edad = edad >= 18
tiene_licencia = True
puede_conducir = es_mayor_de_edad and tiene_licencia
print(puede_conducir)
```

**Momento clave:** el `=` vs `==`. Escribe en vivo:

```python
x = 5       # asignación: x ahora vale 5
x == 5      # comparación: devuelve True
```

Dales 10 segundos para que registren. Luego:

> "Si mañana escriben `if x = 5:` Python les va a decir `SyntaxError`. Es el error más común del curso. Ya lo saben."

### 45–50 min · Pausa corta (5 min)

> "Cinco minutos. Regresen a tiempo. A las [hora] vemos strings."

### 50–75 min · Strings y f-strings (25 min)

Strings merecen su propio bloque. Escribe en vivo:

```python
saludo = "Hola"
nombre = "Ecuador"
mensaje = saludo + ", " + nombre + "!"
print(mensaje)
```

Muestra el método de concatenación con `+`. Luego contrasta con f-strings:

```python
mensaje_v2 = f"{saludo}, {nombre}!"
print(mensaje_v2)
```

**Aquí toma una opinión fuerte:**

> "Hay tres formas de formatear strings en Python: concatenación con `+`, el método `.format()`, y f-strings. Las tres funcionan. Usen f-strings. Son más legibles, más cortas, y no vamos a discutirlo."

A los que pregunten "pero en un libro vi esto otro" — diles que ambas funcionan, pero que en el curso usamos f-strings porque es el estándar moderno. No pierdas 10 min en un debate.

Muestra slicing rápido:

```python
texto = "Ecuador"
print(texto[0])       # 'E'
print(texto[-1])      # 'r'
print(texto[0:3])     # 'Ecu'
print(texto[::2])     # 'Euad'
```

Explica indices en 30 segundos: el 0 es el primer carácter, el -1 es el último. El `[inicio:fin]` es un rango. Si no ponen `fin`, va hasta el final. Si no ponen `inicio`, empieza desde 0.

No pretendas que entiendan `[::2]` en el momento. Diles "esto lo vamos a usar en pandas. Hoy solo reconozcan que existe."

### 75–95 min · Ejercicio 1 (guiado) (20 min)

Abre el ejercicio guiado en el notebook. Léelo en voz alta:

> "Prueba esto. Tengo la estructura, tú pones la lógica."

Deja que lo hagan solos durante 10 minutos. **No camines con ellos por el código**. Ese es el error más grande del primer día — quieren ayuda inmediata y si se las das, nunca aprenden a debuggear.

Camina la sala virtual: mira el chat, responde preguntas puntuales. Si 3+ personas se atascan en el mismo punto, pausa y explícalo para todos.

Al minuto 15, pregunta: "¿A cuántos les pasó el assert?". Cuenta manos. Si es la mayoría, sigue. Si es menos de la mitad, muestra la solución en tu pantalla y explica dónde se atascaron.

**Cómo mostrar la solución:** no leas el código. Ejecútalo línea por línea y pregunta "¿qué creen que hace esta línea?" antes de explicar.

### 95–100 min · Pausa corta (5 min)

Úsala para cambiar el aire. Si el grupo está callado, pide que en el chat pongan una palabra que describa cómo van hasta ahora. Te da señal.

### 100–130 min · Ejercicio 2 (aplicado) (30 min)

Este es el ejercicio con peso real. Léelo en voz alta también, pero **sin mostrar la estructura**. Déjales 20 minutos para que lo hagan.

Mientras tanto:
- Abre breakout rooms por equipo (los mismos de ayer). Dales 15 minutos en equipo.
- Los Leads se ayudan entre sí. Si uno del equipo ya terminó, ayuda a los otros dos.
- **Tú entras a los breakouts**, 1-2 minutos por sala, preguntas "¿cómo van?". No resuelvas por ellos. Si están atascados, pregúntales qué han intentado.

**Regla de oro del profesor:** si te hacen una pregunta técnica, responde con otra pregunta. "¿Qué te sale cuando lo ejecutas?". "¿Qué parte del error no entiendes?". "¿Qué tipo tiene la variable que estás pasando?".

A los 20 minutos, reúne la sala principal. Pide a un equipo que comparta pantalla y muestre su solución. Comenta el código: qué está bien, qué podría mejorar. No destroces. Celebra lo que esté bien.

### 130–140 min · Checkpoint (10 min)

Este es el mini-test honesto. Pregunta verbal a todo el grupo (no con AskUserQuestion ni Slido — directa, a todos):

1. "Sin ver el código, ¿cuál es la diferencia entre `=` y `==`?"
2. "¿Qué tipo devuelve `type(3.14)`?"
3. "¿Cómo formateo `'El precio es $5'` con una variable `precio = 5`?"

Deja silencios. Pregunta a personas específicas si nadie responde. "Juan, ¿qué dirías?". Es el momento de detectar quién no está entendiendo.

Si hay incomodidad con el silencio, diles:

> "Este no es un examen. Estoy tomando pulso al grupo. Si no lo saben, mejor que me lo digan ahora. No hay castigo."

### 140–145 min · Ejercicio 3 (desafío) — instrucciones (5 min)

Esto **casi nunca** se termina en clase. Lo presentas, lo explicas, y se va a casa.

> "El ejercicio 3 es más abierto. No tiene esqueleto. Léanlo antes de mañana, intenten atacarlo. Si se atascan, la solución está comentada en la celda siguiente — pero de verdad intenten antes de mirarla. Si me escriben con dudas hoy en la tarde, les respondo."

No lo hagas en clase. Usa el tiempo en algo más útil.

### 145–150 min · Cierre (5 min)

Reúne al grupo. Cámara tuya prendida. Habla despacio:

> "Hoy vieron tipos, operadores, strings. No parece mucho, pero es la base de todo lo demás. Cada vez que pandas les tire un error de tipos, este día es la respuesta."

> "Suban el notebook al repo del equipo antes de mañana. No necesitan terminar el desafío para subir — suban lo que tengan, lo miro."

> "Mañana: control de flujo, funciones, estructuras. Es el día con más contenido técnico de la semana. Descansen bien."

Termina. No alargues.

---

## Después de la sesión (20-30 min de tu tiempo)

1. **Revisa los notebooks que suban hoy.** Busca dos cosas:
   - ¿El assert del ejercicio guiado pasó?
   - ¿Hay celdas sin ejecutar? (significa que copiaron sin probar)
2. **Alertas:** ¿alguien no subió nada? Envía mensaje directo amable. "Hola, no vi tu notebook en el repo — ¿todo bien?"
3. **Nivel del grupo:** de las respuestas del checkpoint, calibra si Día 3 debe ir más lento (más tiempo en funciones) o puede mantener ritmo.
4. **Prepara el notebook del Día 3:** asegúrate que el hook conecte con lo que ya hicieron ("Ayer escribimos código lineal. Hoy le damos estructura.").

---

## Banderas rojas

- **Alguien con Colab aún** (no logra instalación local) → ofrécele 15 min después de clase para instalar en vivo contigo.
- **Alguien cuyo equipo trabaja sin él** → el riesgo real del curso. Habla aparte con el Product Lead del equipo y con el estudiante por separado. Entiende qué pasa.
- **Grupo en silencio total, cámaras apagadas** → para una sesión y reconocelo. "Los veo silencio hoy. ¿Estoy yendo muy rápido? ¿Muy lento?". A veces es energía baja del día, a veces es que no entienden y no lo dicen. Tómalo en serio.
- **Alguien que ya sabe todo y se aburre** → dale un rol de mentor. "Oye, a Juan le está costando el ejercicio 2 — ¿puedes pasar 5 min con él?". Convertís aburrimiento en activo.

---

## Tips de mentor

**Sobre el live coding:** si tecleas mal y te sale un error, NO lo borres disimulado. Léelo en voz alta y explica qué falló. Es lo más útil que pueden ver. Los estudiantes creen que los profesionales no cometen errores — enseñarles a debuggear en vivo es 10x más valioso que un código perfecto preparado.

**Sobre los errores en vivo:**

> "Miren, me salió `NameError: name 'Edad' is not defined`. ¿Por qué? Porque la definí como `edad` con minúscula. Python es case-sensitive. Este es el error más común del curso."

**Sobre la profundidad:** no abras temas que no puedas cerrar. Si alguien pregunta por mutabilidad, listas vs. tuplas, o estructuras de datos, diles: "excelente pregunta, la veremos mañana". Si lo abres hoy, se extiende 15 min y no terminas lo que viene.

**Sobre la inequidad de nivel:** algunos ya programan en JavaScript o C. Para ellos, todo esto es aburrido. Dales ejercicios bonus ("haz el desafío con mapeo funcional") o el rol de mentores de sala. No les digas "esto es fácil para ti" — reconoce su nivel y úsalo.

**Sobre el ritmo:** si al minuto 90 solo llegaste al ejercicio guiado, NO te apures por cubrir todo. El curso tiene margen. Es peor cubrir todo mal que cubrir menos bien. Ajusta.

**Sobre las preguntas fuera de scope:** "profe, ¿esto se usa en inteligencia artificial?". Respuesta honesta: "Es base. Pandas usa esto debajo. Sklearn usa pandas. Todos los modelos que vamos a ver salen de aquí." No prometas IA-IA si no está en el programa.

---

## Material auxiliar

- `clase_02.ipynb` — notebook del día (ya debe estar humanizado)
- `index.html` Día 2 — referencia escrita
- Cheatsheet de f-strings (opcional, link en el README de la carrera)
- PEP 8 — mención rápida, no exigencia todavía

---

## Al cierre del día, reflexiona

- ¿Cuántos terminaron el ejercicio aplicado?
- ¿Hubo silencios incómodos? ¿Por qué?
- ¿Qué pregunta no supe responder bien y debo pulir?
- ¿A quién quiero revisar individualmente antes del Día 3?

Anota 2-3 líneas. Mañana Python II es más pesado — sé honesto contigo sobre qué dejar más claro.
