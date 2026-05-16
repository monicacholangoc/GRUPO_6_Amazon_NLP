# Día 4 · Planteamiento del proyecto — ENTREGA S1 — Notas del profesor

**Fecha:** Viernes 24 de abril de 2026 · **Duración:** 2h30 sincrónicas (150 min)

---

## Antes de empezar (20 min antes)

Este día **no es clase, es taller con mentor**. Tú no enseñas contenido nuevo. Tú mentorizas 5-6 equipos simultáneamente mientras cada uno pule su entrega S1.

Prepara:

1. **La rúbrica S1** impresa mentalmente. Repásala una vez más:
   - Pregunta de negocio clara, específica, medible
   - 10–15 historias de usuario (formato "Como [rol] quiero [acción] para [beneficio]")
   - Ficha del dataset: origen, tamaño (filas × columnas), calidad inicial, limitaciones conocidas
   - Repo GitHub con README completo (sección del equipo, caso elegido, pregunta, historias, ficha)

2. **Tu matriz de equipos y casos** en papel o nota. Apunta junto al nombre de cada equipo:
   - Caso elegido
   - Quién es Data / Model / Product Lead
   - Estado de los últimos 2 notebooks (subido sí/no)
   - Alertas de la semana

3. **Una plantilla del README de entrega** abierta. Si no tienes una, hoy es el día de tenerla. Al inicio del día compártela en el chat.

**Energía interna:** hoy no te quemas con el contenido, te quemas con la rotación. Vas a pasar 10 minutos con cada equipo, 5 equipos, dos rondas. Esa es la sesión. Calibra energía como un terapeuta en consultas de 20 minutos: presente, enfocado, desconectado del anterior.

---

## Arco general del día

Los estudiantes entregan la S1 esta noche (viernes 24 abr, antes de medianoche). Hoy es el último taller antes de la entrega.

**Estructura del día:**
- 20 min: revisión grupal de la rúbrica + expectativa de entrega
- 90 min: dos rondas de mentoría a los equipos (45 min cada ronda)
- 30 min: trabajo silencioso final + ajustes
- 10 min: cierre de la semana

**Tu rol:** mentor rotativo, no profesor frontal. Los equipos hacen el trabajo. Tú catalizas.

**Trampa principal del día:** que un equipo se quede parado porque no saben qué pregunta de negocio elegir. Tu trabajo es ayudarlos a decidir, no a decidir por ellos.

**Trampa secundaria:** que un equipo te monopolice por 40 minutos mientras los otros 4 te esperan. Tiempo estricto por equipo.

Objetivo al cierre:
- Los 5-6 equipos tienen pregunta de negocio definida
- Los 5-6 equipos tienen al menos 10 historias de usuario borrador
- Los 5-6 equipos tienen ficha del dataset completada
- El README del equipo tiene la estructura correcta
- **Todos entregan antes de medianoche** (verificar a las 10 PM)

---

## Minuto a minuto

### 0–10 min · Apertura y encuadre

Empieza puntual. Abre con claridad de expectativa:

> "Hoy no hay clase. Hoy es taller. Ustedes trabajan en equipos, yo voy pasando. Pregúntenme todo lo que necesiten — es literalmente para lo que sirve esta sesión."

Muestra la rúbrica S1 en pantalla. Lee cada punto en voz alta, con ejemplos cortos:

**Pregunta de negocio:**

> "Una pregunta de negocio es una pregunta que un ejecutivo podría hacerles si trabajaran en esta empresa. Es específica y se puede responder con datos. Mala pregunta: '¿Cómo funciona nuestro negocio?'. Buena pregunta: '¿Qué variables predicen mejor si un usuario va a cancelar su suscripción en los próximos 30 días?'."

**Historias de usuario:**

> "Cada historia tiene este formato: 'Como [rol], quiero [acción], para [beneficio]'. Ejemplo: 'Como gerente de marketing, quiero ver la tasa de cancelación por segmento, para priorizar campañas de retención'. Diez historias mínimo, quince ideal. No son 10 variaciones de la misma. Son 10 necesidades distintas del mismo proyecto."

**Ficha del dataset:**

> "Tres cosas: origen (de dónde sale, quién lo produjo, bajo qué licencia), forma (filas × columnas, tamaño en MB, rango de fechas), y calidad (cuántos nulos, qué columnas sospechan que están rotas, qué le falta). No tienen que resolver los problemas hoy — tienen que identificarlos."

**Repo GitHub con README completo:**

> "El repo que crearon el Día 1 ya debe estar. Hoy le añaden el README con toda la información del proyecto. Si el repo está privado, añádanme como colaborador."

### 10–20 min · Plan del taller

> "Voy a pasar por cada equipo dos veces. Primera ronda, 10 minutos por equipo — veo su pregunta de negocio y sus historias borradoras. Segunda ronda, 5-8 minutos — veo la ficha del dataset y el README."

> "Mientras no estoy con su equipo, trabajen. No me esperen. La forma en que este día funciona es que ustedes avanzan y yo los destrabo."

Si usas Zoom: breakout rooms por equipo, tú con permiso de entrar a cualquiera. Si es presencial: equipos en mesas, tú caminas.

**Tip:** comparte un cronograma tipo "ronda 1: 20–65, ronda 2: 75–115". Así cada equipo sabe aprox. cuándo les tocas.

Abre los breakouts. Cuenta 60 segundos mientras empiezan. Vete a la primera sala.

### 20–65 min · Ronda 1 de mentoría (~9 min por equipo × 5 equipos)

**Estructura de la visita a cada equipo:**

1. **Minuto 0-1 — Check-in:** "¿Cómo están? ¿En qué están trabajando?". Si responden un tema concreto (pregunta de negocio), enfócate ahí. Si dicen "estamos viendo qué hacer", no entras suave — entras directo: "OK, ¿cuál es su caso? ¿Qué es lo que más les llama de ese caso?".

2. **Minuto 1-4 — Pregunta de negocio:** pídeles que te la digan **en voz alta**. No la leas de una pantalla compartida. Obligarlos a verbalizarla es el 50% del trabajo. Escucha con cuidado. ¿Es específica? ¿Es responsable con datos? ¿No es una simple descripción?

   Si es muy vaga ("queremos saber qué pasa con los usuarios"), retrocédelos: "OK, concrétenla. ¿Qué usuarios? ¿Qué quieren saber de ellos? ¿Si pudieran tomar una decisión con la respuesta, cuál decisión sería?". No les des la respuesta. Pregunta hasta que la respondan ellos.

3. **Minuto 4-7 — Historias de usuario:** "Léanme tres de las historias que tengan". Si tienen menos de 3, asesora: "¿Quién es un usuario real del sistema que van a construir? Su jefe, su cliente, el analista de otro equipo. Piensen en esas personas."

4. **Minuto 7-9 — Compromiso:** "Para cuando vuelva a ustedes en ~50 minutos, quiero ver su ficha del dataset empezada y el README con esta estructura (link)". Les das concreción.

**Variantes según lo que encuentres:**

- **Equipo ya adelantado (ya tienen pregunta + 10 historias bien):** "Excelente. Usen el tiempo para la ficha del dataset. Descarguen el dataset, hagan `df.info()`, `df.describe()`, y escriban sus hallazgos. Los veo en la ronda 2."

- **Equipo atascado en elegir caso:** "¿Qué les preocupa de [caso A]? ¿Y de [caso B]?". Si no pueden decidir, decide tú: "Van con A. Si en 30 días ven que no sirve, cambiamos. Avancen."

- **Equipo con conflicto interno:** nota la tensión. No la resuelvas en los 9 min. Dile al Product Lead en privado (DM después): "Hola, los vi con tensión. ¿Todo bien? Dime si necesitan que medie."

- **Equipo silencioso cuando entras:** pregunta directo a uno por uno. "[Nombre], ¿tú qué opinas de la pregunta que tienen?". Activa a los silenciosos explícitamente.

**Reloj mental:** 9 minutos por equipo × 5 equipos = 45 min. Si te atrasas en uno, acorta en el siguiente. No robes el tiempo del equipo que sigue.

### 65–75 min · Pausa grupal (10 min)

Reúne al grupo principal:

> "Pausa de 10 minutos. Estiren, tomen agua. Cuando regresen, ronda 2. Les cuento: en la ronda 1 vi 3 cosas recurrentes — [menciónalas]. Traten de ajustarlas antes de que los vuelva a visitar."

Las "3 cosas recurrentes" son las observaciones que hayas visto que se repiten. Ejemplos:
- "Muchas preguntas de negocio son demasiado vagas. Hagan la prueba del gerente: si el gerente pregunta esto, ¿sabría qué hacer con la respuesta?".
- "Las historias de usuario no tienen `para [beneficio]`. Completen esa parte."
- "Nadie descargó todavía el dataset. Descárguenlo antes de la ronda 2."

Sé específico con el feedback colectivo, no abstracto. El feedback general genérico no sirve — el específico sí.

### 75–125 min · Ronda 2 de mentoría (~10 min por equipo)

Segunda visita a cada equipo. Enfoque:

1. **Minuto 0-1:** "¿Qué hicieron con lo que les dije?". Evalúa si ajustaron.
2. **Minuto 1-5:** revisa la ficha del dataset. Pídeles que te muestren `df.info()`, `df.head()`, `df.isna().sum()`. Si no lo han hecho, hazlos hacerlo en el momento:

   ```python
   import pandas as pd
   df = pd.read_csv("tu_dataset.csv")
   print(df.info())
   print(df.head())
   print(df.isna().sum())
   ```

   (Sí, todavía no han visto pandas formalmente — pero `read_csv`, `.info()`, `.head()` son suficientemente simples para hoy, y mañana comienzan con pandas de lleno.)

3. **Minuto 5-8:** revisa el README del repo. Debe tener:
   - Nombre del proyecto
   - Equipo y roles
   - Pregunta de negocio
   - Historias de usuario (como bullets)
   - Ficha del dataset (como tabla o lista)
   - Cómo correr el proyecto (aunque sea instrucciones básicas)

4. **Minuto 8-10:** últimos ajustes. "Para las 10 PM quiero ver el commit final. Si hay algo que no está resuelto, ponlo en la sección 'Pendientes' del README. Es mejor ser honesto que ocultarlo."

**Errores comunes que vas a ver en ronda 2:**

- **Pregunta de negocio "arreglada" pero igual de vaga.** Si pasa, sé directo: "Esto todavía no responde qué decisión se toma con la respuesta. Les propongo: [ejemplo concreto]. Ajústenlo así o más específico aún."

- **Dataset descargado pero no exploración.** "Vamos, abran un notebook, copien esto [les das el snippet]. No pueden entregar una ficha sin haber visto los datos."

- **README vacío o con la plantilla intacta.** "Esto está vacío. Cierren la aplicación que estén usando y ábranlo ahora. Les doy 10 minutos más en la siguiente pausa — pero esto tiene que estar para cuando cerremos."

- **Historias de usuario que son tareas del equipo (no necesidades del usuario).** "Esta es una tarea de desarrollo ('limpiar datos'), no una necesidad. Una historia es qué quiere un usuario del producto — no qué van a hacer ustedes internamente."

### 125–140 min · Trabajo silencioso + revisión cruzada (15 min)

Reúne el grupo:

> "Últimos 15 minutos de trabajo. Dos opciones: sigan puliendo su entrega, o hagan una revisión cruzada — intercambien links de README con otro equipo y denle feedback de 5 minutos cada uno."

Si el grupo está maduro, la revisión cruzada funciona muy bien. Si el grupo es tímido, quédense trabajando individualmente.

Durante estos 15 min, tú:
- Revisas los repos desde tu computador
- Haces una lista mental de 2-3 equipos que parecen en riesgo de no entregar bien
- Envías DMs puntuales: "Equipo X, vi que falta ficha del dataset — tienen 4 horas antes de la entrega, ¿necesitan más ayuda?"

### 140–150 min · Cierre de la semana (10 min)

Cierre importante. Cámara prendida, mira a la cámara.

**Primero, confirmación operativa:**

> "Entrega hoy antes de medianoche. El link del repo con el commit final. Todo lo que hayan puesto en el README cuenta como entrega. Voy a revisar mañana por la mañana y les envío feedback individual el domingo — tendrán tiempo de ajustar antes del Lunes."

**Segundo, cierre de la semana:**

> "Hoy cerramos la semana 1. En cuatro días pasaron de no haber escrito una línea de Python (algunos de ustedes) a tener un proyecto definido, un equipo, un dataset identificado y un repo profesional. Eso es más de lo que muchos cursos hacen en un mes."

**Tercero, preparación para la semana 2:**

> "La semana que viene empezamos con NumPy y pandas. Es donde se pone serio. Los que tengan tiempo el fin de semana, miren la documentación de pandas — no tienen que entenderla, solo familiarizarse con las palabras. `DataFrame`, `Series`, `iloc`, `loc`. Las van a ver mucho."

**Cuarto, agradecimiento real:**

> "Aprecio que estén aquí. Esto se construye juntos — si algo no está funcionando (ritmo, contenido, el formato), díganme. No tengo que averiguarlo por adivinanza."

Termina. No alargues.

---

## Durante la noche (10 PM — verificación de entregas)

A las 10 PM abre una tab con los repos de los 5-6 equipos. Verifica:

- [ ] README del repo tiene la estructura correcta
- [ ] Pregunta de negocio está presente y específica
- [ ] Historias de usuario (≥10) están presentes
- [ ] Ficha del dataset está presente
- [ ] Último commit es del día

Si a las 10 PM falta un equipo, envía DM: "Hey [Product Lead], no veo el commit final. ¿Todo bien? Si necesitan 2 horas más, avísenme — pero díganme ahora." Da margen razonable.

A las 11:30 PM haz un barrido final. Si falta un equipo, registra el retraso y sigue — el feedback se da igual el sábado.

---

## Durante el fin de semana (feedback de S1)

Sábado-domingo: revisa cada entrega en detalle (30 min por equipo, ~3 horas total). Para cada uno, un feedback individual por DM:

**Formato de feedback:**

```
Equipo [Nombre],

Revisé su S1. Tres cosas:

✓ Lo que está bien: [1-2 líneas específicas]
△ Lo que podrían pulir: [1-2 líneas con acción concreta]
✗ Lo que tienen que corregir: [si aplica — solo si es crítico]

Tienen hasta el lunes a las 8 AM para ajustar. Si está bien como está, no necesitan hacer nada.

[Tu nombre]
```

**No pongas calificación numérica en el DM.** Eso va en el sistema. El DM es formativo, no evaluativo.

---

## Banderas rojas del día

- **Equipo que no ha elegido caso a las 10 AM** → DM al Product Lead antes del taller para alinear. Si llegan sin caso, decides tú.
- **Dos equipos eligieron mismo caso y preguntan si es un problema** → "Para nada. Van a hacer preguntas distintas con los mismos datos." No fuerces diferenciación.
- **Un estudiante que no aparece en el día de la entrega** → DM urgente. "Hola, no te vi hoy. La entrega es hoy. Avísame qué necesitas."
- **Conflicto de equipo en el momento** → pausa 5 min con ellos en una sala aparte. Lleva preguntas simples: "¿Qué esperan de esta semana? ¿Qué necesitan del otro para estar bien?". No resuelvas tú — facilita.
- **Equipo que decide cambiar de caso el día de la entrega** → "Pueden cambiar. La rúbrica no cambia. Hagan la S1 con el caso nuevo hoy mismo — llego hasta las 11 PM disponible por chat."

---

## Tips de mentor

**Sobre la pregunta de negocio:** el error más común es mezclar pregunta de negocio con pregunta técnica. Pregunta de negocio = la que haría un ejecutivo. Pregunta técnica = "¿qué modelo debo usar?". El curso hace lo segundo al servicio de lo primero.

**Sobre las historias de usuario:** muchos nunca han escrito historias. El formato es mecánico al principio pero útil. Si alguien te dice "esto se siente forzado", contesta: "Al principio sí. Después te das cuenta que obliga a pensar en quién usa tu producto, no solo en el producto."

**Sobre el dataset:** idealmente han descargado un subset del dataset para esta sesión. Si vienen con el dataset completo (varios GB), diles: "Trabajen con los primeros 100.000 registros hasta que sepan qué quieren hacer. Full dataset cuando estén seguros del pipeline."

**Sobre equipos que piden "qué modelo vamos a usar":** corta: "No es la pregunta todavía. Primero tenemos que saber qué pregunta responden. El modelo sale naturalmente de la pregunta. En la semana 3 decidimos."

**Sobre tu propia rotación entre equipos:** ponte alarma del teléfono (silencio) a los 9 minutos en cada equipo. Ayuda mucho. Sin alarma, los equipos buenos te retienen y los equipos que necesitan ayuda se quedan sin ti.

**Sobre el balance de los equipos:** si notas que un equipo está muy débil (tres estudiantes que no hicieron ni un notebook completo), es probable que no entreguen bien. Ponlos en tu radar de la semana 2. No los sueltes.

**Sobre entregar tarde:** lo normal en un curso así es que 1-2 entregas lleguen tarde la primera semana. Dales 24 horas de gracia con pérdida mínima de nota (20% menos, por ejemplo). Si se hace costumbre, endurece a partir de la S2.

---

## Material auxiliar

- `clase_04.ipynb` — plantilla del notebook de entrega S1 (humanizado)
- `index.html` Día 4 — rúbrica visible para estudiantes
- Ejemplo de README de una entrega pasada (si tienes)
- Plantilla de historias de usuario (en el repo principal)
- Guía de exploración inicial de un dataset (documento de 1 página con los comandos básicos de pandas — les será útil hoy mismo)

---

## Al cierre del día, reflexiona

- ¿Los 5-6 equipos van a entregar hoy? ¿Cuál es el riesgo?
- ¿Qué pregunta de negocio fue la más sólida? ¿Cuál la más débil? (para referencia la próxima cohorte)
- ¿Qué hice bien como mentor? ¿Qué podría mejorar la próxima semana?
- ¿Hay alguien al borde de abandonar? ¿Cómo lo abordo?

Anota 3-4 líneas. Cierre de la semana 1 es un buen momento para una retrospectiva más larga — dedícale 15 min el domingo si puedes.

---

## Checklist de la semana (para tu control)

Al final del viernes deberías poder marcar:

- [ ] Los 5-6 equipos tienen caso y pregunta definidos
- [ ] Todos los estudiantes tienen Python funcional
- [ ] Todos los notebooks del Día 2 y Día 3 están subidos (con retraso aceptable)
- [ ] Los repos de los equipos tienen README profesional
- [ ] Todas las S1 están entregadas (o con extensión explícita)
- [ ] Tengo una lista de 2-3 estudiantes a seguir de cerca en la semana 2
- [ ] Mi energía está bien para arrancar el lunes con NumPy

Si hay alguno sin marcar, decide qué hacer el fin de semana. La semana 2 comienza el lunes — mejor llegar con todo cerrado.
