# Día 1 · Kick-off del seminario — Notas del profesor

**Fecha:** Martes 21 de abril de 2026 · **Duración:** 2h30 sincrónicas (150 min)

---

## Antes de empezar (15 min antes de la sesión)

Abre el repositorio `CursoPythonDatos_2026` en VS Code con el terminal listo. Ten una segunda pestaña de Chrome con el `index.html` de Día 1 abierto, por si necesitas mostrar el programa visualmente. Ten a mano el listado de los 15 casos del repo `casos/`.

Verifica que la cámara del Zoom/Meet esté prendida, el micrófono funciona, y la pestaña de chat está visible. Si compartes pantalla, prepárate para cambiar rápido entre VS Code, el navegador (GitHub) y tu notebook.

Lleva contigo una lista mental de los nombres de los estudiantes. Si puedes, revisa quiénes se matricularon en las últimas 48 horas. El primer día empieza bien cuando reconoces al menos un nombre por persona.

**Energía interna:** Hoy no vas a enseñar Python. Vas a vender el curso. La primera clase decide cuánta atención te dan las siguientes 16. Suena raro, pero es así. Prepárate con un discurso claro de 3 minutos que responda: qué van a construir, por qué deberían importarse, qué pierden si no participan activamente. Si no te convence a ti, no los va a convencer a ellos.

---

## Arco general del día

Este es el único día donde no hay "tema" que enseñar. Es alineación pura. El 60% del tiempo son tú hablando o facilitando. El 40% son ellos instalando cosas y eligiendo caso/equipo.

La trampa del primer día es perderse en la logística y olvidar transmitir la visión. La otra trampa es hablar 2 horas sin hacer nada práctico. Equilibrio: toca la visión varias veces, pero ábrela con una mini-actividad en los primeros 20 minutos para que no sea un monólogo.

Objetivo al cierre:
- Todos con Python funcional en su máquina
- Los 15 casos presentados rápidamente
- Equipos de 3 formados con roles asignados
- Caso elegido (aunque sea preliminar)
- Repo GitHub creado con el README del equipo

Si alguno de esos 5 no pasa, tienes un problema para el Día 2.

---

## Minuto a minuto

### 0–5 min · Apertura (saludo + escaneo)

Entra al Zoom 2 minutos antes. Deja que vayan llegando. No empieces tarde. A los 2 minutos, empieza aunque falten 3 personas — las tardanzas crónicas se cultivan el primer día.

Abre con una frase directa, corta:

> "Bienvenidos. Tengo muchas ganas de empezar este seminario con ustedes. En las próximas cuatro semanas vamos a construir un producto de software completo — dashboard, API, todo — a partir de datos reales. Pero eso es después. Hoy los quiero conocer."

No leas los objetivos todavía. Deja que la apertura sea humana, no una diapositiva.

### 5–15 min · Check-in rápido (mini-actividad)

Pide que cada uno, en 30 segundos, diga:
1. Su nombre
2. Carrera/semestre
3. **Una cosa que esperan poder hacer al final del curso** (no "aprender Python" — algo concreto)

Esto cumple tres funciones: rompe el hielo, tú ves energías y niveles, y obtienes expectativas reales para ajustar el discurso. Toma nota mental de las respuestas.

**Tiempo estricto:** 30s por persona. Si son 15 personas, son 7.5 min. Bien. Si alguien se extiende, córtalo con humor: "Perfecto, anota eso, lo retomamos". No dejes que el primer turno se vuelva de 2 minutos, porque todos los demás van a calibrar hacia arriba y pierdes 20 minutos.

### 15–35 min · El "por qué" del seminario y cómo funciona

Comparte pantalla con el `index.html` de Día 1 o con el README principal. Recorre:

- **Qué van a construir:** muéstrales una captura real de un dashboard en Streamlit con un API sirviendo un modelo. Si puedes, ten un ejemplo de entrega de una cohorte anterior o construye uno de juguete. Un dashboard visible en 60 segundos vale más que 10 minutos de explicación.
- **Cómo está organizado:** 17 sesiones, 4 semanas, 4 entregables (S1, S2, S3, Final). Muestra la tabla del README.
- **Cómo se evalúa:** los 4 entregables + defensa oral. No hay exámenes. Sí hay rúbricas. La rúbrica de cada entrega sale el día que les corresponde.
- **Cómo trabajan en el día a día:** las 2h30 sincrónicas son talleres. Ellos vienen con el material leído. En clase escribimos código juntos. Después de clase terminan los ejercicios y suben el notebook.

**Qué decir sobre la "dificultad":**

> "Este curso es exigente y es justo. Si vienen con ganas, lo terminan. Si vienen a ver qué pasa, se van a quedar atrás rápido. La buena noticia es que el material está organizado para que si entregan cada semana, al final tienen un producto que pueden poner en su portafolio. Ese producto vale más que la nota."

Evita el tono de amenaza ("si no hacen esto se reprueban"). Usa el tono de compromiso mutuo ("si cumplen, yo cumplo").

### 35–60 min · Los 15 casos disponibles

Esta es la parte que más vas a repetir en los siguientes días, así que hazla bien hoy. Abre la carpeta `casos/` del repo.

**Plan táctico:** agrupa los 15 casos en 5 clusters temáticos (~3 casos cada uno) y dedica 3 minutos por cluster. No describas caso por caso — agrupa y resalta.

Clusters sugeridos (ajusta según tu curso):
1. **Retail y e-commerce** (Airbnb, vehículos usados, reseñas)
2. **Servicios y movilidad** (turismo, vuelos, movilidad urbana)
3. **Salud y seguridad pública** (salud pública, sismos)
4. **Contenido y recomendación** (música, StackOverflow, recomendación de películas)
5. **Finanzas y deportes** (banca, deportes)

Para cada cluster, muestra:
- Qué datos hay (origen, tamaño aprox)
- Un ejemplo de pregunta de negocio potente
- Qué tipo de modelo podría resolverla

**Lo que NO hagas:** leer las 15 descripciones del README. Te demorarías 45 minutos y los pierdes.

**Lo que SÍ hagas:** decir al final "cada caso tiene un README detallado en `casos/nombre_del_caso/`. La elección final la hacen hoy, pero tienen hasta el día 4 (entrega S1) para cambiar si se dan cuenta que el caso no tiene lo que necesitan."

### 60–65 min · Pausa (5 min)

Diles:

> "Cinco minutos. Estiren las piernas. Vayan por agua. A las [hora exacta] seguimos con la parte divertida: formar los equipos."

Deja la pestaña compartida para que regresen con foco. Usa estos 5 minutos para tomar nota mental de cómo está el grupo hasta ahora. ¿Quién se ve perdido? ¿Quién se ve enganchado? ¿Alguien aún no prende cámara?

### 65–100 min · Formación de equipos y elección de caso (35 min)

Este bloque es crítico. Si sale mal, arrastras problemas toda la semana.

**Paso 1 — Roles (5 min):** explica los tres roles del equipo.

> "Cada equipo son 3 personas con tres roles. **Data Lead:** se preocupa por el pipeline — que los datos entren, estén limpios y estructurados. **Model Lead:** EDA y modelado — estadística, hipótesis, primer modelo. **Product Lead:** dashboard, API, documentación, presentación. Los roles no son compartimentos — todos tocan todo —, pero cada rol tiene ownership de una parte del entregable final."

Aclara: los roles pueden rotar si el equipo lo decide, pero para la entrega de la S4 debe haber un responsable claro por cada rol. Eso evita el "pensé que lo hacías tú" del día 16 a las 10 PM.

**Paso 2 — Auto-organización (20 min):** abre breakout rooms de 3 personas asignadas aleatoriamente. Dales 20 minutos con estas instrucciones (también escríbelas en el chat):

1. Preséntense. Que cada uno diga qué experiencia previa tiene con programación (no solo Python — cualquier cosa).
2. Elijan un caso del `casos/` que les guste a los tres.
3. Asignen roles (Data / Model / Product Lead).
4. Creen un Google Doc compartido con: nombre del equipo, integrantes (nombres + correos), caso elegido, roles.

**Si el grupo es impar:** un equipo puede ser de 4 con dos Model Leads o uno de 2 (solo si hay justificación — enfermedad, cruce horario). Equipos de 2 cargan más. Equipos de 4 a veces se diluyen. 3 es el óptimo.

**Qué hacer mientras están en breakout:**
- Entra rápido a cada sala (1 min por sala máx)
- Pregunta: "¿cómo van?" y "¿ya tienen caso?"
- Si alguien está en silencio total, activa a esa persona directamente: "[Nombre], ¿qué les parece el caso X?"
- Si alguien está dominando la conversación, no lo frenes pero inicia una pregunta que obligue a otro a hablar.

**Paso 3 — Puesta en común (10 min):** reabre la sala principal. Cada equipo, 1 minuto:
- Nombres
- Caso elegido
- Roles

Si un caso lo están eligiendo dos equipos, está bien (las preguntas de negocio serán distintas). No fuerces diversidad.

### 100–135 min · Setup del entorno (35 min)

Este bloque es donde más se atascan, y es el más predecible. Ten una guía lista.

**Orden de instalación:**
1. Python 3.11 o 3.12 desde python.org (¡marcar "Add to PATH" en Windows!)
2. VS Code + extensiones "Python" y "Jupyter"
3. Git (en Windows: Git for Windows; en Mac: `xcode-select --install`)
4. Cuenta en GitHub (si no tienen)

**Comparte tu pantalla y haz el setup en vivo**, aunque ya lo tengas instalado. Abre una terminal y corre:

```bash
python --version
git --version
code --version
```

Explica qué hace cada comando. La primera vez que ven un terminal es un mini choque cultural — dedica 30 segundos a normalizarlo ("es solo una forma de darle órdenes al computador sin hacer clic").

**Mientras ellos instalan, divide la atención:**
- Deja la pantalla compartida con el proceso de instalación
- Ve al chat y responde preguntas puntuales
- Si varios tienen el mismo error, pausa y explícalo para todos

**Errores comunes y respuesta rápida:**
- `python no es reconocido como un comando interno o externo` → no marcó "Add to PATH" en el instalador. Solución: desinstalar y reinstalar marcando la casilla.
- `command not found: python` (Mac) → prueba `python3 --version`. Mac usa `python3` por default.
- VS Code no encuentra el intérprete → `Cmd+Shift+P` → "Python: Select Interpreter" → elegir el que tiene "Python 3.11".
- Jupyter no arranca → la extensión Jupyter no está instalada. Installar desde el marketplace de VS Code.

**Plan B:** si alguien no logra instalar local en los 35 min, diles que usen **Google Colab** como fallback temporal. Ya tienen el link en el README. El objetivo es que puedan trabajar mañana, no que sufran hoy.

### 135–150 min · Primer commit + cierre (15 min)

**Último push del día:** cada equipo crea su repositorio en GitHub. Pueden usar un fork del repo del curso o un repo nuevo — lo importante es:
1. Un repo público (o privado con los 3 integrantes + tú como colaboradores)
2. Un `README.md` con: nombre del equipo, integrantes, caso elegido, roles
3. Un primer commit con ese README

Dales 10 minutos para esto. Al minuto 8, comparte en el chat los nombres de los equipos que ya tienen repo visible.

**Cierre (últimos 5 min):**

Cambia de tono. Cámara prendida, mira a la cámara, habla despacio. Di algo como:

> "Hoy hicieron el trabajo más aburrido de todo el curso: instalar herramientas y formar equipos. Si están aquí, sobrevivieron. Mañana empezamos con Python de verdad. Lean la celda de apertura del notebook del Día 2 antes de mañana — no se demora. Y si algo no funcionó hoy — instalación, GitHub, cualquier cosa — escríbanme antes de las 6pm. No lleguen mañana arrastrando un problema de instalación."

Termina con una frase que les dé sentido:

> "En 4 semanas van a tener un producto que funciona. No un notebook perdido en Google Drive — un producto. Eso es lo que vamos a construir. Nos vemos mañana."

**No hagas resumen tipo "lo que aprendimos hoy fue X, Y, Z"**. Hoy no aprendieron nada técnico. Aprendieron logística. Un resumen sonaría falso.

---

## Después de la sesión (20 min de tu tiempo)

1. **Verifica los repos:** abre los 4-5 repos que crearon. Que el README tenga lo que pediste. Si falta algo, envía un mensaje directo al Product Lead del equipo.
2. **Lista de alertas:** identifica a 1-3 estudiantes que viste en riesgo (cámara apagada todo el día, no participaron, se veían perdidos). Envíales un mensaje individual discreto: "Hola [nombre], ¿todo bien con la instalación? Si necesitas ayuda antes de mañana, aquí estoy."
3. **Ajusta Día 2:** si viste que hay mucha variación de nivel (gente que ya sabe vs. gente que nunca programó), prepara tiempos de ejercicios más elásticos para mañana.
4. **Sube las grabaciones** (si grabaste) a la carpeta del curso. Los que faltaron las necesitan.

---

## Banderas rojas que justifican intervención

- **Equipo sin caso elegido al minuto 100** → entra al breakout y decide por ellos. "Pongan X, después lo pueden cambiar."
- **Alguien sin Python al minuto 135** → dile que use Colab mañana y te reúnes con él/ella el fin de semana para instalar.
- **Dos personas pelean por el mismo rol en un equipo** → sugiere que roten: primera semana uno, segunda semana el otro. Nunca lo conviertas en debate público.
- **Alguien se conecta tarde (30+ min) y pierde la formación de equipos** → asignalo al final a un equipo que tenga 2. Habla con él después de clase para ponerlo al día.

---

## Tips de mentor

**Sobre la energía:** el primer día todos están nerviosos, incluyéndote. La forma de bajar la tensión no es ser súper formal, es ser tú. Usa tus modismos. Cuenta una anécdota breve de un proyecto real tuyo. Hace que el seminario se sienta como algo que sabes, no como algo que leíste en un libro.

**Sobre los silencios:** habrá silencios incómodos, sobre todo cuando preguntes "¿alguien tiene dudas?". No llenes todos los silencios con más explicación. Cuenta hasta 5. A veces alguien habla. Si nadie habla, sigue — no tortures al grupo con "vamos, alguien debe tener una duda".

**Sobre la palabra "obvio":** nunca la uses. "Esto es obvio" significa "si no lo entiendes eres tonto". Usa "esto es conocido" o "esto lo saben" o, mejor, solo explica y deja que quien ya sepa se aburra un segundo.

**Sobre el orden de los casos:** algunos casos son más "sexy" (música, Airbnb) y otros suenan secos (banca, salud pública). Los que suenan secos frecuentemente tienen datos más limpios y son mejores proyectos. Si puedes, crea un argumento para los casos secos — no los hundas solos.

**Sobre las preguntas difíciles:** si alguien pregunta algo técnico complejo (p.ej., "¿podemos usar redes neuronales?"), responde honesto:

> "El curso cubre hasta modelos lineales. Si quieren ir más allá, pueden — pero no lo voy a enseñar yo ni es parte de la rúbrica. Los rúbrica premia claridad, no sofisticación."

No prometas lo que no vas a entregar.

---

## Material auxiliar del día (por si te piden)

- `index.html` del Día 1 — tiene el plan visual
- `README.md` del repo principal — tabla de las 17 sesiones
- `casos/` — carpeta con los 15 casos
- Guía de instalación para Windows/Mac/Linux (link en el README)
- Video de introducción a Jupyter (opcional, para los que necesiten refuerzo asincrónico)

---

## Al cierre del día, reflexiona

- ¿Todos los equipos tienen caso?
- ¿Todos tienen Python + Git + GitHub?
- ¿Hay alguien en riesgo que necesita seguimiento?
- ¿Qué ajustaría mañana?

Escribe dos líneas en tu diario del curso. Al final de las 4 semanas, esas notas valen oro para la siguiente cohorte.
