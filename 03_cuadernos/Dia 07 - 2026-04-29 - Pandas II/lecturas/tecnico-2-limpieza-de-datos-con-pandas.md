# Limpieza de datos con Pandas

Fuente: [Codificando Bits](https://codificandobits.com/tutorial/limpieza-de-datos-con-pandas/)  
_Copia local para lectura fuera de línea. El formato original puede verse en la URL._

---

Limpieza de datos con Pandas

En este tutorial veremos de forma práctica cómo hacer uso de varias herramientas de Pandas para realizar la limpieza de un set de datos, una fase esencial en cualquier proyecto de Ciencia de Datos y Machine Learning.

Al final del tutorial se encuentra el enlace para descargar el set de datos y el código fuente.

El problema a resolver

En este tutorial vamos a suponer que una entidad bancaria contrata a una empresa de marketing encargada de contactar telefónicamente a posibles clientes para determinar si están interesados o no en adquirir un certificado de depósito a término con el banco.

Y vamos a suponer que la pregunta que queremos resolver tras este análisis es: ¿qué perfil tienen los clientes con mayor potencial de conversión?

Esta pregunta será el punto de partida para ver cómo realizar la limpieza del set de datos que usaremos en este tutorial.

Un requisito para este tutorial es tener algo de familiaridad con el uso de Pandas, la librería de Python más usada para el procesamiento de datos tabulares. Si quieres aprender a usar esta librería te sugiero los 3 cursos de Pandas disponibles acá en la Academia Online: Pandas Nivel Básico , Pandas Nivel Intermedio y Pandas Nivel Avanzado .

El set de datos

La información recolectada por la empresa de mercadeo se encuentra en un archivo CSV («dataset_banco.csv») con 45215 filas y 17 columnas.

Cada registro contiene 16 características (las primeras 16 columnas) y una categoría («yes» o «no» dependiendo de si la persona está o no interesada en adquirir el producto). Las columnas son:

«age»: edad (numérica)

«job»: tipo de trabajo (categórica: «admin.», «unknown», «unemployed», «management», «housemaid», «entrepreneur», «student», «blue-collar»,»self-employed», «retired», «technician», «services»)

«marital»: estado civil (categórica: «married», «divorced», «single»)

«education»: nivel educativo (categórica: «unknown», «secondary», «primary», «tertiary»)

«default»: si dejó de pagar sus obligaciones (categórica: «yes», «no»)

«balance»: saldo promedio anual en euros (numérica)

«housing»: ¿tiene o no crédito hipotecario? (categórica: «yes», «no»)

«loan»: ¿tiene créditos de consumo? (categórica: «yes», «no»)

«contact»: medio a través del cual fue contactado (categórica: «unknown», «telephone», «cellular»)

«day»: último día del mes en el que fue contactada (numérica)

«month»: último mes en el que fue contactada (categórica: «jan», «feb», «mar», …, «nov», «dec»)

«duration»: duración (en segundos) del último contacto (numérica)

«campaign»: número total de veces que fue contactada durante la campaña (numérica)

«pdays»: número de días transcurridos después de haber sido contactado antes de la campaña actual (numérica. -1 indica que no fue contactado previamente)

«previous»: número de veces que ha sido contactada antes de esta campaña (numérica)

«poutcome»: resultado de la campaña de marketing anterior (categórica: «unknown», «other», «failure», «success»)

«y»: categoría ¿el cliente se suscribió a un depósito a término? (categórica: «yes», «no»)

Teniendo clara la estructura general de nuestro set de datos, hagamos uso de Pandas para leerlo y realizar una primera exploración.

Lectura y exploración inicial del set de datos

Comencemos importando las librerías requeridas:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

Usaremos Pandas para implementar las fases de lectura y procesamiento y las librerías Matplotlib y Seaborn para visualizar los datos.

Ahora usamos el método «read_csv» de Pandas para realizar la lectura del dataset:

data = pd.read_csv("dataset_banco.csv") 

Usando el método «shape» podemos verificar el tamaño del set de datos:

print(data.shape) 

Y en este caso vemos que la tabla de datos contiene 45.215 filas y 17 columnas.

Usemos ahora el método «head()» para imprimir en pantalla las primeras 5 filas del set de datos, lo que nos permitirá tener una idea general de las características de esta tabla:

data.head() 

lo cual nos arroja un resultado similar a este:

Las primeras 5 filas del set de datos a usar en este tutorial 

Podemos verificar que las primeras 16 columnas («age», «job», …, «poutcome») corresponden a las variables predictoras (o características) mientras que la última columna («y») es la variable que nos indica si el cliente se suscribió o no a un depósito a término con la entidad bancaria.

Una parte esencial en esta exploración inicial es entender los tipos de variables que tenemos (es decir el tipo de dato usado para almacenar la información en cada columna de nuestra tabla). Esto lo podemos verificar usando el método «info()»:

data.info() 

lo cual nos arroja este resultado:

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 45215 entries, 0 to 45214
Data columns (total 17 columns):
# Column Non-Null Count Dtype 
--- ------ -------------- ----- 
0 age 45215 non-null int64 
1 job 45213 non-null object 
2 marital 45214 non-null object 
3 education 45214 non-null object 
4 default 45215 non-null object 
5 balance 45213 non-null float64
6 housing 45215 non-null object 
7 loan 45215 non-null object 
8 contact 45215 non-null object 
9 day 45215 non-null int64 
10 month 45215 non-null object 
11 duration 45214 non-null float64
12 campaign 45215 non-null int64 
13 pdays 45214 non-null float64
14 previous 45215 non-null int64 
15 poutcome 45215 non-null object 
16 y 45215 non-null object 
dtypes: float64(3), int64(4), object(10)
memory usage: 5.9+ MB 

En la línea 2 podemos ver el número total de registros (o filas) que tiene nuestro set de datos (45.215) y luego podemos contrastar esta información con el número de registros «no nulos» (o datos completos) en cada una de las columnas.

Así por ejemplo podemos ver que las columnas «job», «marital», «education», «balance», «duration» y «pdays» no contienen exactamente 45.215 sino un poco menos, lo cual nos indica que estas columnas contienen datos faltantes.

Esto quiere decir que como parte de la limpieza que llevaremos a cabo tendremos que realizar el manejo de estos datos faltantes .

Así que habiendo realizado esta exploración inicial del set de datos veamos la parte central de este tutorial: el proceso de limpieza.

Limpieza del set de datos

En este proceso de limpieza haremos uso de diferentes herramientas de Pandas que nos permitirán abordar las situaciones que más comúnmente encontraremos en un set de datos tabular, como son:

El manejo de datos faltantes (que como lo acabamos de ver están presentes en nuestro set de datos)

La eliminación de columnas irrelevantes (es decir, columnas que no contienen información relacionada con el problema que queremos resolver)

El manejo de registros (filas) repetidos

El manejo de valores extremos (u «outliers») para el caso de las variables (columnas) numéricas

La limpieza de errores tipográficos que puedan existir en las variables categóricas

Y al final de este proceso de limpieza deberíamos tener un set de datos íntegro, listo para la fase de Análisis Exploratorio.

Así que veamos cómo implementar cada una de estas fases de limpieza.

Detección y manejo de datos faltantes

Como lo vimos en la exploración inicial del set de datos, algunas columnas («job», «marital», «education», «balance», «duration» y «pdays») no contienen exactamente 45.215 sino unos pocos menos. 

En esencia existen dos técnicas para realizar este manejo de datos faltantes: la eliminación (que consiste en simplemente borrar las filas que tengan datos incompletos) o la imputación (que consiste en estimar el dato faltante con base en la información conocida).

Como en este caso tenemos tan pocos datos faltantes (entre 1 y 2 registros) podemos simplemente optar por la eliminación pues no perderemos gran parte de la información.

Cuando tenemos un dato faltante en Pandas este dato es marcado como «NaN» (o «Not A Number») y por tanto podemos implementar la eliminación de estas filas usando el método «dropna()» de Pandas:

data.dropna(inplace=True) 

donde hemos usado el parámetro «inplace = True» para sobre-escribir el DataFrame original («data»).

Para verificar que se han eliminado correctamente los registros incompletos podemos usar nuevamente el método «info()» obteniendo este resultado:

<class 'pandas.core.frame.DataFrame'>
Int64Index: 45207 entries, 0 to 45214
Data columns (total 17 columns):
# Column Non-Null Count Dtype 
--- ------ -------------- ----- 
0 age 45207 non-null int64 
1 job 45207 non-null object 
2 marital 45207 non-null object 
3 education 45207 non-null object 
4 default 45207 non-null object 
5 balance 45207 non-null float64
6 housing 45207 non-null object 
7 loan 45207 non-null object 
8 contact 45207 non-null object 
9 day 45207 non-null int64 
10 month 45207 non-null object 
11 duration 45207 non-null float64
12 campaign 45207 non-null int64 
13 pdays 45207 non-null float64
14 previous 45207 non-null int64 
15 poutcome 45207 non-null object 
16 y 45207 non-null object 
dtypes: float64(3), int64(4), object(10)
memory usage: 6.2+ MB 

Vemos que ahora el DataFrame contiene 45.207 filas y que todas las columnas tienen exactamente 45.207 datos completos. Así que en este punto ya tenemos una tabla sin datos faltantes.

Vamos a la siguiente fase: la eliminación de columnas irrelevantes.

Eliminación de columnas irrelevantes

En esta fase de limpieza eliminaremos aquellas columnas que no aportan información relevante para el análisis que queremos realizar.

En particular, en esta etapa de pre-procesamiento consideraremos que una columna es irrelevante si:

No contiene información relacionada con el problema que queremos resolver. Por ejemplo en este caso podría ser una columna que no guarde relación con el posible perfil del cliente (deporte favorito, hobbies, comida favorita, etc.)

Una columna categórica pero con un sólo nivel. Por ejemplo si en la columna «job» solo tuviésemos el nivel «unknown» esta columna no aporta información que nos permita diferenciar un perfil de cliente de otro

Una columna numérica pero con un sólo valor. Por ejemplo si en la columna «edad» todos los valores fuesen iguales a 50 ocurriría algo similar al caso anterior, pues no aportaría información para diferencial unos clientes de otros

Columnas con información redundante. Por ejemplo si además de las columnas «month» y «day» tuviésemos la columna «month-day», esta última columna no aportaría información adicional al análisis

Sin embargo, puede haber situaciones en las cuales no tendremos claro si una columna puede resultar siendo relevante o no. En este caso la recomendación es dejar la columna y es posible que más adelante en posteriores etapas (por ejemplo si realizamos el Análisis Exploratorio o si construimos un modelo para generar predicciones) podamos decidir si preservamos o no dicha columna.

Si volvemos a la exploración que hicimos inicialmente podemos concluir que en principio todas las columnas podrían aportar información que nos permita definir los diferentes perfiles de cliente.

Sin embargo, debemos verificar que no haya columnas categóricas con un sólo nivel, o columnas numéricas con un sólo valor.

Comencemos analizando entonces las columnas categóricas. Primero definamos una lista de Python que contenga los nombres de estas columnas:

cols_cat = ['job', 'marital', 'education', 'default', 'housing',
'loan', 'contact', 'month', 'poutcome', 'y'] 

Y ahora hagamos uso del método «nunique()» aplicado a cada columna. Este método nos permite determinar los diferentes niveles de cada variable categórica:

for col in cols_cat:
print(f'Columna {col}: {data[col].nunique()} subniveles') 

Al ejecutar esta porción de código obtenemos este resultado:

Columna job: 18 subniveles
Columna marital: 6 subniveles
Columna education: 10 subniveles
Columna default: 2 subniveles
Columna housing: 2 subniveles
Columna loan: 6 subniveles
Columna contact: 5 subniveles
Columna month: 12 subniveles
Columna poutcome: 6 subniveles
Columna y: 2 subniveles 

Y con esto podemos verificar que todas las columnas categóricas tienen más de 1 sub-nivel, así que no eliminaremos ninguna.

Hagamos algo similar pero para las variables numéricas. En este caso podemos usar el método «describe()» que nos mostrará en pantalla una tabla sintetizando algunos parámetros estadísticos básicos de dichas variables numéricas (como la media, el rango intercuartiles y la desviación estándar, entre otras).

Así, una variable numérica que contenga un sólo valor nos arrojará una desviación estándar igual a cero y podría ser eliminada:

data.describe() 

Tras ejecutar el código anterior obtenemos este resultado:

Resultado de usar el método «describe» de Pandas en el set de datos que estamos limpiando 

Y al observar la fila «std» (que contiene las diferentes desviaciones estándar) podemos verificar que ninguno de los valores es iguales a cero. Así que en este caso tampoco eliminaremos ninguna columna numérica.

Veamos ahora cómo realizar la detección y manejo de filas repetidas.

Detección y manejo de registros repetidos

La presencia de filas repetidas es una situación que en ocasiones podremos encontrar en nuestros sets de datos.

Como su nombre lo indica, las filas repetidas son aquellas donde todos sus registros son idénticos.

En estos casos la idea es preservar únicamente uno de estos registros repetidos y eliminar los restantes, para lo cual podemos usar el método «drop_duplicates()» de Pandas, que permite realizar la detección y eliminación en una sóla línea de código.

Hagamos entonces uso de este método, para lo cual vamos a imprimir primero en pantalla el número total de filas antes de la eliminación de registros duplicados. Después de esto realizaremos la eliminación y posteriormente imprimiremos nuevamente el tamaño del set de datos resultante:

print(f'Tamaño del set antes de eliminar las filas repetidas: {data.shape}')
data.drop_duplicates(inplace=True)
print(f'Tamaño del set después de eliminar las filas repetidas: {data.shape}') 

donde en la línea 2 del código anterior hemos usado nuevamente el argumento «inplace = True» para sobre-escribir el resultado de la limpieza en el set de datos original («data»). Tras ejecutar el código anterior obtenemos este resultado:

Tamaño del set antes de eliminar las filas repetidas: (45207, 17)
Tamaño del set después de eliminar las filas repetidas: (45203, 17) 

y con esto podemos verificar que en efecto hemos pasado de un set que contenía 45.207 filas a uno con 45.203 registros. Esto quiere decir que se han eliminado 4 registros repetidos.

Continuando con esta limpieza del set de datos veamos ahora cómo realizar la detección y el manejo de valores extremos.

Detección y manejo de valores extremos

Los valores extremos (u «outliers») son aquellos datos atípicos que se salen del rango «normal» de la mayoría de los datos. Y estos valores extremos pueden estar presentes tanto en las variables numéricas como en las variables categóricas.

Por ejemplo, un valor extremo en una variable como la edad (columna «age») podría ser por ejemplo un valor negativo (¡pues la edad no puede ser una cantidad negativa!) o podría ser también una edad de, por ejemplo, 150 años.

Y en una variable categórica como la columna «job» (tipo de trabajo) podría ser un tipo de trabajo poco frecuente, es decir que aparezca muy pocas veces en la totalidad del set de datos.

El uso de gráficos de caja (o «boxplots») es una herramienta que fácilmente permite detectar la presencia de «outliers» en variables numéricas.

Así que usaremos estos «boxplots» para verificar si existen valores extremos en las variables numéricas de nuestro set de datos. Comencemos definiendo una lista de Python con estas variables numéricas:

cols_num = ['age', 'balance', 'day', 'duration', 'campaign',
'pdays', 'previous'] 

Y ahora usemos la función «boxplot()» de la librería Seaborn para generar un gráfico de caja para cada una de las variables numéricas:

fig, ax = plt.subplots(nrows=7, ncols=1, figsize=(8,30))
fig.subplots_adjust(hspace=0.5)

for i, col in enumerate(cols_num):
sns.boxplot(x=col, data=data, ax=ax[i])
ax[i].set_title(col) 

Al ejecutar el código anterior obtenemos los gráficos de caja de cada una de las variables especificadas:

Gráficos de caja («boxplots») de las variables numéricas para el set de datos que estamos limpiando 

En este caso vemos que cada gráfico contiene precisamente una caja (de allí el nombre de «boxplots») de color azul. Los límites de esta caja corresponden a los cuartiles 1 y 3 entre los cuales se encuentra el 50% de los datos.

Además, más allá de estos límites de la caja, a izquierda y derecha, encontramos los «whiskers» o «bigotes» que son los límites por debajo y por encima de los cuales tendremos precisamente valores extremos (estos «whiskers» se ven claramente por ejemplo en los gráficos para las variables «day» y «duration»).

Y estos valores extremos son esencialmente los puntos que aparecen por fuera de estos «bigotes». Así que interpretando el contenido de estos gráficos de caja podemos observar lo siguiente:

Para la variable «age» tenemos valores extremos que corresponden a edades mucho mayores a 100 años

Para la variable «duration» (la duración del depósito a término adquirida por el cliente) existen valores negativos

Y en la variable «previous» (que indica el número de veces que la persona ha sido contactada antes de esta campaña) se tiene un valor extremadamente alto (cercano a 300)

Estos son precisamente valores extremos que debemos manejar. Y en este caso existen dos alternativas:

La eliminación de estos registros

El recorte, que implica cambiar los valores extremos para llevarlos al rango «normal» de valores

La imputación usando información de registros similares

Como en este caso tenemos muy pocos valores extremos en cada una de las variables mencionadas, resulta suficiente usar la técnica de eliminación.

Comencemos eliminando los valores extremos en la variable edad (columna «age») lo cual equivale a preservar únicamente los sujetos cuyas edades sean, por ejemplo, menores o iguales a 100. Vamos a imprimir el tamaño del dataset antes y después de la eliminación para verificar los cambios en la cantidad total de datos:

print(f'Tamaño del set antes de eliminar registros de edad: {data.shape}')
data = data[data['age']<=100]
print(f'Tamaño del set después de eliminar registros de edad: {data.shape}') 

donde en la línea 2 hemos simplemente establecido la condición «data[‘age’]<=100» para preservar únicamente los registros que se encuentran en el rango normal. Antes de ejecutar esta línea de código teníamos 45.203 registros y después del manejo de estos valores extremos tendremos 45.195 (es decir, hemos eliminado 8 registros).

Usemos una sintaxis similar pero para preservar duraciones (columna «duration») mayores a cero:

print(f'Tamaño del set antes de eliminar registros de duración: {data.shape}')
data = data[data['duration']>0]
print(f'Tamaño del set después de eliminar registros de duración: {data.shape}') 

Y en este caso hemos pasado de 45.195 a 45.190 registros después de la eliminación de estos «outliers».

Y finalmente eliminemos las filas cuyo valor en la columna «previos» es mayor que 100 (lo cual equivale a preservar los registros con valores menores o iguales a 100):

print(f'Tamaño del set antes de eliminar registros de previous: {data.shape}')
data = data[data['previous']<=100]
print(f'Tamaño del set después de eliminar registros de previous: {data.shape}') 

Y en este último caso partimos de 45.190 para tras la eliminación obtener 45.189.

Así que en este punto ya hemos realizado el manejo de valores extremos y únicamente nos resta corregir posibles errores tipográficos o la presencia de equivalencias que pueda haber en las variables categóricas. Veamos cómo implementar esta fase de la limpieza.

Corrección de errores tipográficos o equivalencias

Los errores tipográficos pueden corresponder a sub-niveles dentro de una variable categórica que estén escritos incorrectamente. Por ejemplo, podríamos tener un nivel como «mobile» en la variable «contact» y un sub-nivel similar pero escrito incorrectamente, como por ejemplo «mobiiile».

Por otra parte, pueden aparecer sub-niveles como «unknown» y «UNK» que para nosotros son equivalentes pero que para nuestro programa parecerían diferentes.

Así que debemos normalizar todos estos sub-niveles para que tengan las mismas representaciones. Y para hacer esto debemos analizar, por cada variable categórica, los sub-niveles que están presentes y por inspección visual determinar posibles inconsistencias.

Así que podemos usar el método «value_counts()» aplicado sobre cada columna para imprimir en pantalla todos sus sub-niveles:

for col in cols_cat:
print(data[col].value_counts())
print('-'*20) 

con lo cual obtenemos este resultado:

job
blue-collar 9727
management 9451
technician 7592
admin. 5165
services 4151
retired 2262
self-employed 1577
entrepreneur 1486
unemployed 1303
housemaid 1240
student 937
unknown 288
administrative 3
Management 2
MANAGEMENT 2
Self-employed 1
Services 1
Retired 1
Name: count, dtype: int64
--------------------
marital
married 27200
single 12781
divorced 5194
div. 7
Single 4
DIVORCED 3
Name: count, dtype: int64
--------------------
education
secondary 23181
tertiary 13297
primary 6845
unknown 1855
SECONDARY 3
Primary 2
sec. 2
UNK 2
Secondary 1
Tertiary 1
Name: count, dtype: int64
--------------------
default
no 44374
yes 815
Name: count, dtype: int64
--------------------
housing
yes 25111
no 20078
Name: count, dtype: int64
--------------------
loan
no 37941
yes 7238
No 5
YES 2
NO 2
Yes 1
Name: count, dtype: int64
--------------------
contact
cellular 29271
unknown 13011
telephone 2901
phone 3
mobile 3
Name: count, dtype: int64
--------------------
month
may 13748
jul 6895
aug 6246
jun 5341
nov 3970
apr 2931
feb 2648
jan 1402
oct 738
sep 579
mar 477
dec 214
Name: count, dtype: int64
--------------------
poutcome
unknown 36939
failure 4898
other 1837
success 1509
UNK 4
Success 2
Name: count, dtype: int64
--------------------
y
no 39904
yes 5285
Name: count, dtype: int64
-------------------- 

En primer lugar podemos observar que hay sub-niveles con el mismo nombre pero escritos en minúscula, en mayúscula o con la primera letra en mayúscula (por ejemplo en la variable «job» donde tenemos «self-employed» y «Self-employed» o «management» y «MANAGEMENT»).

Unifiquemos esta representación inicialmente representando todo el texto en minúsculas usando el método «str.lower()»:

for column in data.columns:
# Representar en minúsculas sólo si la columna es categórica
if column in cols_cat:
data[column] = data[column].str.lower() 

Ejecutemos el bloque de código anterior nuevamente para verificar que estos cambios ya aparecen reflejados en los sub-niveles de cada variable categórica:

for col in cols_cat:
print(data[col].value_counts())
print('-'*20) 

Y podemos verificar que ya hemos corregido estas inconsistencias:

job
blue-collar 9727
management 9455
technician 7592
admin. 5165
services 4152
retired 2263
self-employed 1578
entrepreneur 1486
unemployed 1303
housemaid 1240
student 937
unknown 288
administrative 3
Name: count, dtype: int64
--------------------
marital
married 27200
single 12785
divorced 5197
div. 7
Name: count, dtype: int64
--------------------
education
secondary 23185
tertiary 13298
primary 6847
unknown 1855
sec. 2
unk 2
Name: count, dtype: int64
--------------------
default
no 44374
yes 815
Name: count, dtype: int64
--------------------
housing
yes 25111
no 20078
Name: count, dtype: int64
--------------------
loan
no 37948
yes 7241
Name: count, dtype: int64
--------------------
contact
cellular 29271
unknown 13011
telephone 2901
phone 3
mobile 3
Name: count, dtype: int64
--------------------
month
may 13748
jul 6895
aug 6246
jun 5341
nov 3970
apr 2931
feb 2648
jan 1402
oct 738
sep 579
mar 477
dec 214
Name: count, dtype: int64
--------------------
poutcome
unknown 36939
failure 4898
other 1837
success 1511
unk 4
Name: count, dtype: int64
--------------------
y
no 39904
yes 5285
Name: count, dtype: int64
-------------------- 

Ahora analicemos cada variable de manera individual para verificar otras posibles inconsistencias:

«job»: se tienen equivalencias entre «admin.» y «administrative» 

«marital»: se tienen equivalencias entre «divorced» y «div.»

«education»: se tienen equivalencias entre «secondary» y «sec.» y entre «unknown» y «unk.»

«contact»: se tienen equivalencias entre «cellular» y «mobile» y entre «telephone» y «phone»

Así que lo que nos resta es corregir estas equivalencias. Comencemos con la variable «job» donde reemplazarmos «admin.» por «administrative» usando nuevamente el método «str.replace()»:

data['job'] = data['job'].str.replace('admin.','administrative', regex=False) 

Hagamos algo similar para la columna «marital», reemplazando «div.» por «divorced»:

data['marital'] = data['marital'].str.replace('div.','divorced', regex=False) 

Y también usaremos una sintaxis similar para reemplazar «sec.» por «secondary» en la columna «education»:

data['education'] = data['education'].str.replace('sec.','secondary', regex=False) 

Y si en esta misma columna queremos reemplazar «unk» por «unknown» podríamos usar el mismo enfoque anterior o esta alternativa (usando el método «loc»):

data.loc[data['education']=='unk','education'] = 'unknown' 

Y usemos este mismo enfoque para reemplazar «phone» por «telephone» y «mobile» por «cellular» en la columna «contact»:

data.loc[data['contact']=='phone','contact'] = 'telephone'
data.loc[data['contact']=='mobile','contact'] = 'cellular' 

«job»: «self-employed» y «Self-employed», «retired» y «Retired» y «management» y «MANAGEMENT»

¡Y listo, en este punto ya hemos completado todas las fases de limpieza de datos!

En este punto ya podemos decir que tenemos un set de datos íntegro que nos permite continuar con fases posteriores del análisis, como por ejemplo el Análisis Exploratorio de los Datos o la creación de algún modelo predictivo.

Enlaces de descarga set de datos y código fuente

▼ El set de datos de este tutorial 

▼ El código fuente de este tutorial 

Conclusión

Muy bien, en este tutorial hemos visto cómo hacer uso de diferentes herramientas que nos ofrece la librería Pandas para implementar varias de las técnicas que más comúnmente encontraremos en proyectos reales al momento de llevar a cabo la limpieza de datos.

Aunque cada set de datos tiene sus particularidades considero que estas técnicas nos permiten abordar los inconvenientes que más comúnmente encontraremos al momento de procesar los datos, como son por ejemplo el manejo de datos faltantes, de valores extremos y de registros repetidos así como la eliminación de columnas irrelevantes y la estandarización de las variables categóricas.

Recuerda que puedes acceder tutoriales exclusivos suscribiéndote a la Academia Online. Y con esta suscripción también tendrás acceso a todos los cursos y proyectos disponibles en la Academia.

Volver a la página de tutoriales
