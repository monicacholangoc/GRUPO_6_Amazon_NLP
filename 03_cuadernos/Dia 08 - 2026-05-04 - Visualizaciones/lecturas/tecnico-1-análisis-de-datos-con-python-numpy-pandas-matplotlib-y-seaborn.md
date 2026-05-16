# Análisis de datos con Python, NumPy, Pandas, Matplotlib y Seaborn

Fuente: [freeCodeCamp en español](https://www.freecodecamp.org/espanol/news/tutorial-que-es-analisis-de-datos-como-visualizar-datos-con-python-numpy-pandas-matplotlib-y-seaborn/)  
_Copia local para lectura fuera de línea. El formato original puede verse en la URL._

---

July 17, 2022

/ 

#análisis de datos

Tutorial: ¿Qué es el Análisis de Datos? Cómo visualizar datos con Python, Numpy, Pandas, Matplotlib y Seaborn

Traductor: Andrés Torres

Autor: freeCodeCamp.org (Inglés)

Artículo original: What is Data Analysis? How to Visualize Data with Python, Numpy, Pandas, Matplotlib & Seaborn Tutorial 

El análisis de datos es el proceso de explorar, investigar y recopilar información de los datos utilizando medidas y visualizaciones estadísticas.

El objetivo del análisis de datos es desarrollar una comprensión de los datos al descubrir tendencias, relaciones y patrones. El análisis de datos es tanto una ciencia como un arte. Por un lado, requiere el conocimiento de estadística, técnicas de visualización y paquetes de Python como Numpy, Pandas y Seaborn. 

Por otro lado, requiere que hagas preguntas interesantes para guiar la investigación y luego interpretes los números y cifras para generar ideas útiles. En este tutorial sobre análisis de datos se cubren los siguientes temas:

1.¿Qué es el cálculo numérico? Python y Numpy para principiantes     

2. Cómo analizar datos tabulares usando Python y Pandas     

3. Visualización de datos usando Python, Matplotlib y Seaborn

¿Qué es el cálculo numérico? Python y Numpy para principiantes
Fuente: Elegant Scipy 
Puedes seguir el tutorial y ejecutar el código aquí: https://jovian.ai/aakashns/python-numerical-computing-with-numpy 

Esta sección cubre los siguientes temas:  

Cómo trabajar con datos numéricos en Python     

2. Cómo convertir listas de Python en arreglos Numpy     

3. Arreglos Numpy multidimensionales y sus beneficios     

4. Operaciones con arreglos; transmisión, indexación y división    

5. Cómo trabajar con archivos de datos CSV usando Numpy

Cómo trabajar con datos numéricos en Python

Los "datos" en el análisis de datos, generalmente se refieren a datos numéricos; como precios de acciones, cifras de ventas, mediciones de sensores, puntajes deportivos, tablas de bases de datos, etc. 

La biblioteca Numpy proporciona estructuras de datos especializadas, funciones y otras herramientas para la computación numérica en Python. Analicemos un ejemplo para ver por qué y cómo usar Numpy para trabajar con datos numéricos. 

Supongamos que queremos usar datos climáticos como la temperatura, la lluvia y la humedad para determinar si una región es adecuada para el cultivo de manzanas. 

Un enfoque simple para hacer esto sería formular la relación entre el rendimiento anual de manzanas (toneladas por hectárea) y las condiciones climáticas como la temperatura promedio (en grados Fahrenheit), la lluvia (en milímetros) y la humedad relativa promedio (en porcentaje) como una ecuación lineal.

Rendimiento_manzanas = w1 * temperatura + w2 * lluvia + w3 * humedad 

Estamos expresando el rendimiento de las manzanas como una suma ponderada de la temperatura, la lluvia y la humedad. Esta ecuación es una aproximación, ya que la relación real puede no ser necesariamente lineal y puede haber otros factores involucrados. 

Pero un modelo lineal simple como este suele funcionar bien en la práctica. Con base en algunos análisis estadísticos de datos históricos, podríamos encontrar valores razonables para los pesos w1, w2 y w3 . He aquí un ejemplo de conjunto de valores:

w1, w2, w3 = 0.3, 0.2, 0.5 

Dados algunos datos climáticos para una región, ahora podemos predecir el rendimiento de las manzanas. Aquí hay algunos datos de muestra:

Para comenzar, podemos definir algunas variables para registrar los datos climáticos de la región de Kanto.

kanto_temperatura = 73
kanto_lluvia = 67
kanto_humedad = 43 

Ahora podemos sustituir los valores de estas variables en la ecuación para obtener el rendimiento de las manzanas:

kanto_yield_apples = kanto_temp * w1 + kanto_rainfall * w2 + kanto_humidity * w3
kanto_yield_apples
print("The expected yield of apples in Kanto region is {} tons per hectare.".format(kanto_yield_apples)) 

Para que sea un poco más fácil realizar el cálculo anterior para varias regiones, podemos representar los datos climáticos de cada región como un vector, es decir, una lista de números.

kanto = [73, 67, 43]
johto = [91, 88, 64]
hoenn = [87, 134, 58]
sinnoh = [102, 43, 37]
unova = [69, 96, 70] 

Los tres números en cada vector representan los datos de temperatura, lluvia y humedad, respectivamente. También podemos representar el conjunto de pesos utilizados en la fórmula como un vector. 

pesos=[w1,w2,w3] 

Ahora podemos escribir una función crop_yield para calcular el rendimiento de las manzanas (o cualquier otro cultivo) dados los datos climáticos y los respectivos pesos.

def crop_yield(region, weights):
result = 0
for x, w in zip(region, weights):
result += x * w
return result

crop_yield(kanto, weights)
*# 56.8

crop_yield(johto, weights)
*# 76.9

crop_yield(unova, weights)
*# 74.9 

Cómo convertir listas de Python en arreglos Numpy

El cálculo realizado en la variable crop_yield, implica la multiplicación por elementos de dos vectores y la suma de los resultados. A este proceso matemático se le denomina producto escalar. Puedes obtener mayor información sobre los productos punto aquí .

La biblioteca Numpy proporciona una función integrada para calcular el producto escalar de dos vectores. Sin embargo, primero debemos convertir las listas en arreglos Numpy.

Instalemos la biblioteca Numpy usando el administrador de paquetes pip.

!pip install numpy --upgrade --quiet 

Ahora, importemos el módulo numpy. Es una práctica común importar numpy con el alias np.

import numpy as np 

Ahora podemos usar la función np.array para crear arreglos en Numpy.

kanto = np.array([73, 67, 43])

kanto
# array([73, 67, 43])

weights = np.array([w1, w2, w3])

weights
# array([0.3, 0.2, 0.5]) 

Los arreglos de Numpy poseen la clase ndarray .

type(kanto)
# numpy.ndarray

type(weights)
# numpy.ndarray 

Al igual que las listas, los arrelgos Numpy admiten la notación de indexación [].

weights[0]
# 0.3

kanto[2]
#43 

Operaciones con Arreglos de Numpy 

Ahora podemos calcular el producto de dos vectores usando la función np.dot .

np.dot(kanto, weights)
# 56.8 

El operador * realiza una multiplicación por elementos de dos arreglos si tienen el mismo tamaño. El método sum calcula la suma de números en una matriz.

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr1 * arr2
# array([ 4, 10, 18])

arr2.sum()
# 15 

Los beneficios de usar arreglos en Numpy

Los arreglos en Numpy ofrecen los siguientes beneficios sobre las listas simples de Python. Esto sobre todo en cuanto a operaciones con datos numéricos: 

Son fáciles de usar : Puedes escribir operaciones matemáticas, simples, concisas e intuitivas, como la sumatoria del producto de dos variables (kanto * weights).sum() en lugar de usar un complejo bucle con la variable crop_yield .

Rendimiento : Las operaciones y funciones de Numpy son implementadas internamente en C++,  lo que las vuelve mucho más rápidas que las declaraciones en Python, y por supuesto, que el tiempo de ejecución de sus bucles.

He aquí una comparación del producto de vectores, realizado en un bucle de Python, vs la ejecución en un arreglo de Numpy. Lo interesante de este experimento, es que, cada vector posee un millón de elementos. Muestra más que suficiente para comparar la velocidad entre las dos operaciones. 

# Python lists
arr1 = list(range(1000000))
arr2 = list(range(1000000, 2000000))

# Numpy arrays
arr1_np = np.array(arr1)
arr2_np = np.array(arr2)

%%time
result = 0
for x1, x2 in zip(arr1, arr2):
result += x1*x2
result

# CPU times: user 300 ms, sys: 3.26 ms, total: 303 ms
# Wall time: 302 ms
# 833332333333500000

%%time
np.dot(arr1_np, arr2_np)

# CPU times: user 2.11 ms, sys: 951 µs, total: 3.07 ms
# Wall time: 1.58 ms
# 833332333333500000 

Como puedes ver; al usar np.dot obtenemos una velocidad 100 veces mayor a emplear el bucle for . Esto hace a Numpy muy útil cuando se trabaja con bases de datos de gran tamaño; es decir, de miles o incluso millones de unidades de datos. 

Arreglos multidimensionales con Numpy

Ahora podemos ir un paso más allá y representar los datos climáticos de todas las regiones utilizando una sola matriz Numpy bidimensional.

climate_data = np.array([[73, 67, 43],
[91, 88, 64],
[87, 134, 58],
[102, 43, 37],
[69, 96, 70]])

climate_data
# array([[ 73, 67, 43],
# [ 91, 88, 64],
# [ 87, 134, 58],
# [102, 43, 37],
# [ 69, 96, 70]]) 

Si tienes alguna familiaridad con el álgebra lineal, puedes comprobar el proceso reconociendo la matriz bidimensional anterior como una matriz con cinco filas y tres columnas. Cada fila representa una región y las columnas representan temperatura, lluvia y humedad, respectivamente.

Las arreglos Numpy pueden tener cualquier número de dimensiones y diferentes longitudes a lo largo de cada dimensión. Podemos inspeccionar la longitud a lo largo de cada dimensión. Para esto usamos la propiedad .shape de un arreglo.
Fuente: Elegant Scipy 
# 2D array (matrix)
climate_data.shape
# (5, 3)

weights
# array([0.3, 0.2, 0.5])

# 1D array (vector)
weights.shape
# (3,)

# 3D array 
arr3 = np.array([
[[11, 12, 13], 
[13, 14, 15]], 
[[15, 16, 17], 
[17, 18, 19.5]]])

arr3.shape
# (2, 2, 3) 

Todos los elementos en un arreglo de Numpy poseen el mismo tipo de datos. Puedes verificar el tipo de datos, usando la propiedad .dtype .

weights.dtype
# dtype('float64')

climate_data.dtype
# dtype('int64') 

Si una matriz contiene incluso un solo número en formato flotante ( float ), todos los demás elementos también se convierten en flotantes.

arr3.dtype
# dtype('float64') 

Ahora podemos calcular una predicción con las manzanas en todas las regiones. Esto mediante una simple multiplicación matricial entre climate_data (una matriz 5x3) y weights (un vector de 3 elementos). Observemos este proceso de una forma visual:

Puede aprender sobre arreglos y multiplicación de arreglos mirando los primeros 3 o 4 videos de esta lista de reproducción de YouTube. 

Para efectuar la operación en Numpy, simplemente empleamos la función np.matmul . También puede usarse el operador @ para realizar la multiplicación de arreglos.

np.matmul(climate_data, weights)
# array([56.8, 76.9, 81.9, 57.7, 74.9])

climate_data @ weights
# array([56.8, 76.9, 81.9, 57.7, 74.9]) 

Cómo trabajar con archivos CSV

Numpy también nos provee de funciones auxiliares para a lectura de archivos de texto. En este ejemplo, descarguemos un archivo climate.txt , el cual contiene 10,000 mediciones del clima con tres variables (temperatura, lluvia y humedad) en el siguiente formato:

temperature,rainfall,humidity
25.00,76.00,99.00
39.00,65.00,70.00
59.00,45.00,77.00
84.00,63.00,38.00
66.00,50.00,52.00
41.00,94.00,77.00
91.00,57.00,96.00
49.00,96.00,99.00
67.00,20.00,28.00
... 

Este formato de almacenamiento de datos se conoce como valores separados por comas o CSV.
CSV: un archivo de valores separados por comas (CSV) es un archivo de texto delimitado que utiliza una coma para separar los valores. Cada línea del archivo es un registro de datos. Cada registro consta de uno o más campos, separados por comas. Un archivo CSV generalmente almacena datos tabulares (números y texto) en texto sin formato, en cuyo caso cada línea tendrá la misma cantidad de campos. (Wikipedia) 
Para leer este archivo en un arreglo de Numpy, podemos usar la función genfromtxt .

import urllib.request

urllib.request.urlretrieve(
'https://hub.jovian.ml/wp-content/uploads/2020/08/climate.csv', 
'climate.txt')

climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)

climate_data
# array([[25., 76., 99.],
# [39., 65., 70.],
# [59., 45., 77.],
# ...,
# [99., 62., 58.],
# [70., 71., 91.],
# [92., 39., 76.]])

climate_data.shape
# (10000, 3) 

Ahora podemos realizar una multiplicación de arreglos usando el operador @ para predecir el rendimiento de las manzanas para todo el conjunto de datos usando un conjunto de pesos asignados a las variables.

weights = np.array([0.3, 0.2, 0.5])

yields = climate_data @ weights
yields
# array([72.2, 59.7, 65.2, ..., 71.1, 80.7, 73.4])

yields.shape
# (10000,) 

Añadamos yields a climate_data como una cuarta columna (después de las 3 columnas de temperatura, lluvia y humedad) usando la función np.concatenate .

climate_results = np.concatenate((climate_data, yields.reshape(10000, 1)), axis=1)

climate_results
# array([[25. , 76. , 99. , 72.2],
# [39. , 65. , 70. , 59.7],
# [59. , 45. , 77. , 65.2],
# ...,
# [99. , 62. , 58. , 71.1],
# [70. , 71. , 91. , 80.7],
# [92. , 39. , 76. , 73.4]]) 

Aquí se presentan un par de sutilezas:

Ya que deseamos añadir una nueva columna, usamos el argumento axis=1 para np.concatenate . El argumento axis especifica la dimensión de la concatenación.

Los arreglos deben tener el mismo número de dimensiones, a la vez que la misma extensión. La única excepción es la dimensión empleada para la concatenación. Usamos la función np.reshape para cambiar la forma de yields de (10000,) a (10000,1) .

He aquí una explicación visual de la forma en que funciona np.concatenate junto con axis=1 (A propósito: ¿Puedes adivinar que resultado traería axis=0 ?):

La mejor manera de comprender lo que hace una función Numpy es experimentar con ella y leer la documentación para conocer sus argumentos y valores devueltos. Usa las celdas de arriba para experimentar con np.concatenate y np.reshape .

Escribamos los resultados finales de nuestro calco realizado  usando la función np.savetxt .

np.savetxt('climate_results.txt', 
climate_results, 
fmt='%.2f', 
delimiter=',',
header='temperature,rainfall,humidity,yeild_apples', 
comments='') 

Los resultados están escritos de vuelta en el formato CSV en la fila climate_results.txt .

temperature,rainfall,humidity,yeild_apples
25.00,76.00,99.00,72.20
39.00,65.00,70.00,59.70
59.00,45.00,77.00,65.20
84.00,63.00,38.00,56.80
... 

Numpy provee cientos de funciones para ejecutar operaciones en arreglos, he aquí algunas de las funciones más utilizadas:

Matemáticas: np.sum , np.exp , np.round , operadores aritméticos.

Manipulación de Arreglos: np.reshape , np.stack , np.concatenate , np.split 

Álgebra Lineal: np.matmul , np.dot , np.transpose , np.eigvals 

Estadística: np.mean , np.median , np.std , np.max 

Entonces, ¿cómo encuentras la función que necesitas? La forma más fácil de encontrar la función correcta para una operación o caso de uso específico es realizar una búsqueda en la web. Por ejemplo, la búsqueda de "Cómo unir arreglos numpy" lleva a este tutorial de concatenation .

También puedes encontrar una lista completa de arreglos en la documentación de Numpy .

Operaciones aritméticas numéricas, transmisión y comparación

Los arreglos en Numpy soportan operadores aritméticos como   + , - , * , etc. Lo mejor de todos es que puedes realizar una operación con un simple número (también llamado escalar) o con otro arreglo del mismo tipo.

Estos operadores facilitan la escritura de expresiones matemáticas con arrglos multidimensionales.

arr2 = np.array([[1, 2, 3, 4], 
[5, 6, 7, 8], 
[9, 1, 2, 3]])

arr3 = np.array([[11, 12, 13, 14], 
[15, 16, 17, 18], 
[19, 11, 12, 13]])

# Adding a scalar
arr2 + 3

# array([[ 4, 5, 6, 7],
# [ 8, 9, 10, 11],
# [12, 4, 5, 6]])

# Element-wise subtraction
arr3 - arr2

# array([[10, 10, 10, 10],
# [10, 10, 10, 10],
# [10, 10, 10, 10]])

# Division by scalar
arr2 / 2

# array([[0.5, 1. , 1.5, 2. ],
# [2.5, 3. , 3.5, 4. ],
# [4.5, 0.5, 1. , 1.5]])

# Element-wise multiplication
arr2 * arr3

# array([[ 11, 24, 39, 56],
# [ 75, 96, 119, 144],
# [171, 11, 24, 39]])

# Modulus with scalar
arr2 % 4

# array([[1, 2, 3, 0],
# [1, 2, 3, 0],
# [1, 1, 2, 3]]) 

Broadcasting en un array de Numpy 

Las arreglos Numpy también admiten una acción llamada broadcasting , lo que permite operaciones aritméticas entre dos arreglos con diferentes números de dimensiones pero formas compatibles. Veamos un ejemplo para ver cómo funciona.

arr2 = np.array([[1, 2, 3, 4], 
[5, 6, 7, 8], 
[9, 1, 2, 3]]) 
arr2.shape
# (3, 4)

arr4 = np.array([4, 5, 6, 7])
arr4.shape
# (4,)

arr2 + arr4
# array([[ 5, 7, 9, 11],
# [ 9, 11, 13, 15],
# [13, 6, 8, 10]]) 

Cuando la expresión arr2 + arr4 es evaluada, arr4 (que tiene dimensiones (4,) ) es replicada tres veces para lograr las dimensiones (3, 4) de arr2 . Numpy ejecuta la replicación sin crear tres copias de la dimensión más pequeña del arreglo. Lo que facilita la eficiencia y usa mucha menos memoria.
Fuente: Python Data Science Handbook 
Esto solo funciona si solo funciona si una de los arrelgos se puede replicar para que coincida con la forma de la otra matriz.

arr5 = np.array([7, 8])
arr5.shape
# (2,)

arr2 + arr5
# ValueError: operands could not be broadcast together with shapes (3,4) (2,) 

En el ejemplo precedente, incluso si arr5 es replicado tres veces, no logrará tener las dimensiones de arr2 . Por lo tanto arr2 + arr5 no puede ser evaluado exitosamente. Puedes aprender más aquí acerca de broadcasting .

Comparación de arreglos en Numpy 

Numpy también soporta operadores como == , != , > . El resultado será un arreglo de booleanos.

arr1 = np.array([[1, 2, 3], [3, 4, 5]])
arr2 = np.array([[2, 2, 3], [1, 2, 5]])

arr1 == arr2
# array([[False, True, True],
# [False, False, True]])

arr1 != arr2
# array([[ True, False, False],
# [ True, True, False]])

arr1 >= arr2
# array([[False, True, True],
# [ True, True, True]])

arr1 < arr2
# array([[ True, False, False],
# [False, False, False]]) 

Las comparaciones de arreglos son generalmente utilizadas para contar el número de elementos iguales en dos arreglos, mediante el método sum . Recuerda que True evalúa en 1 y False evalúa en 0 . Esto es así por convención, siempre y cuando trabajes con booleanos.

(arr1 == arr2).sum()
# 3 

Indexing y slicing en Numpy 

Numpy extiende la notación de indexación de listas de Python usando corchetes en múltiples dimensiones de una manera intuitiva. Puede proporcionar una lista de índices o rangos separados por comas para seleccionar un elemento específico o un subarreglo (también llamado segmento) de un arreglo Numpy.

arr3 = np.array([
[[11, 12, 13, 14], 
[13, 14, 15, 19]], 

[[15, 16, 17, 21], 
[63, 92, 36, 18]], 

[[98, 32, 81, 23], 
[17, 18, 19.5, 43]]])

arr3.shape
# (3, 2, 4)

# Single element
arr3[1, 1, 2]

# 36.0

# Subarray using ranges
arr3[1:, 0:1, :2]

# array([[[15., 16.]],
# 
# [[98., 32.]]])

# Mixing indices and ranges
arr3[1:, 1, 3]

# array([18., 43.])

arr3[1:, 1, :3]
# array([[63. , 92. , 36. ],
# [17. , 18. , 19.5]])

# Using fewer indices
arr3[1]

# array([[15., 16., 17., 21.],
# [63., 92., 36., 18.]])

arr3[:2, 1]
# array([[13., 14., 15., 19.],
# [63., 92., 36., 18.]])

# Using too many indices
arr3[1,3,2,1]

# IndexError: too many indices for array: array is 3-dimensional, but 4 were indexed 

La notación y sus resultados pueden parecer confusos al principio, así que reserva un tiempo para experimentar y familiarizarse con ella.

Usa las celdas a continuación para probar algunos ejemplos de indexación y división de arreglos, con diferentes combinaciones de índices y rangos. Aquí hay algunos ejemplos más demostrados visualmente:
Fuente: Scipy Lectures . 
Otros métodos para crear arreglos en Numpy 
Numpy también proporciona algunas funciones útiles para crear arreglos de formas deseadas con valores fijos o aleatorios. Consulta la documentación oficial o utiliza la función de ayuda help para obtener más información.

# All zeros
np.zeros((3, 2))

# array([[0., 0.],
# [0., 0.],
# [0., 0.]])

# All ones
np.ones([2, 2, 3])

# array([[[1., 1., 1.],
# [1., 1., 1.]],
#
# [[1., 1., 1.],
# [1., 1., 1.]]])

# Identity matrix
np.eye(3)

# array([[1., 0., 0.],
# [0., 1., 0.],
# [0., 0., 1.]])

# Random vector
np.random.rand(5)

# array([0.92929562, 0.11301864, 0.64213555, 0.8600434 , 0.53738656])

# Random matrix
np.random.randn(2, 3) # rand vs. randn - what's the difference?

# array([[ 0.09906435, -1.64668094, 0.08073528],
# [ 0.1437016 , 0.80715712, 1.27285476]])

# Fixed value
np.full([2, 3], 42)

# array([[42, 42, 42],
# [42, 42, 42]])

# Range with start, end and step
np.arange(10, 90, 3)

# array([10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58,
# 61, 64, 67, 70, 73, 76, 79, 82, 85, 88])

# Equally spaced numbers in a range
np.linspace(3, 27, 9)

# array([ 3., 6., 9., 12., 15., 18., 21., 24., 27.]) 

Ejercicios 
Prueba los siguientes ejercicios para familiarizarse con los arreglos Numpy y practicar sus habilidades:

Asignación de funciones de matriz Numpy: https://jovian.ml/aakashns/numpy-array-operations 
(Opcional) 100 ejercicios numpy: https://jovian.ml/aakashns/100-numpy-exercises 

Resumen y lecturas adicionales
Con esto, completamos nuestra discusión sobre computación numérica con Numpy. Hemos cubierto los siguientes temas en esta parte del tutorial:

1.Cómo pasar de listas de Python a arreglos Numpy
2.Cómo operar en arreglos Numpy
3.Los beneficios de usar arreglos Numpy sobre listas
4.Arrelgtos Numpy multidimensionales
5.Cómo trabajar con archivos de datos CSV
6.Operaciones aritméticas y radiodifusión
7.Arreglos de indexación y rebanado
8.Otras formas de crear arrelgos Numpy

Consulta los siguientes recursos para obtener más información sobre Numpy:

Tutorial oficial 

Numpy curso en freeCodeCamp 

Numpy avanzado (explorando los detalles) 

Preguntas de revisión para verificar su comprensión

Trata de responder las siguientes preguntas para evaluar su comprensión de los temas tratados en este cuaderno:

¿Qué es un vector?

¿Cómo representas vectores usando una lista de Python? Dar un ejemplo.

¿Qué es un producto escalar de dos vectores?

Escribe una función para calcular el producto escalar de dos vectores.

¿Qué es Numpy?

¿Cómo se instala Numpy?

¿Cómo se importa el módulo numpy?

¿Qué significa importar un módulo con un alias? Dar un ejemplo.

¿Cuál es el alias de uso común para numpy?

¿Qué es una matriz Numpy?

¿Cómo se crea una matriz Numpy? Dar un ejemplo.

¿Cuál es el tipo de arreglos Numpy?

¿Cómo se accede a los elementos de una matriz Numpy?

¿Cómo calculas el producto escalar de dos vectores usando Numpy?

¿Qué sucede si tratas de calcular el producto escalar de dos vectores que tienen diferentes tamaños?

¿Cómo se calcula el producto de elementos de dos arreglos Numpy?

¿Cómo se calcula la suma de todos los elementos en una matriz Numpy?

¿Cuáles son los beneficios de usar arreglos Numpy sobre listas de Python para operar con datos numéricos?

¿Por qué las operaciones de matriz de Numpy tienen un mejor rendimiento en comparación con las funciones y los bucles de Python?

Ilustre la diferencia de rendimiento entre las operaciones de arreglos de Numpy y los bucles de Python mediante un ejemplo.

¿Qué son los arreglos Numpy multidimensionales?

Ilustre cómo crearía arreglos Numpy con 2, 3 y 4 dimensiones.

¿Cómo inspecciona la cantidad de dimensiones y la longitud a lo largo de cada dimensión en una arreglo Numpy?

¿Pueden los elementos de una matriz Numpy tener diferentes tipos de datos?

¿Cómo verifica los tipos de datos de los elementos de un arreglo Numpy?

¿Cuál es el tipo de datos de una matriz Numpy?

¿Cuál es la diferencia entre una matriz y una matriz Numpy 2D?

¿Cómo se realiza la multiplicación de arreglos usando Numpy?

¿Para qué se usa el operador @ en Numpy?

¿Qué es el formato de archivo CSV?

¿Cómo se leen los datos de un archivo CSV usando Numpy?

¿Cómo se concatenan dos arreglos Numpy?

¿Cuál es el propósito del argumento del eje de np.concatenate?

¿Cuándo son compatibles dos arreglos Numpy para la concatenación?

Dé un ejemplo de dos arreglos Numpy que se pueden concatenar.

Dé un ejemplo de dos arreglos Numpy que no se pueden concatenar.

¿Cuál es el propósito de la función np.reshape?

¿Qué significa "remodelar" una matriz Numpy?

¿Cómo se escribe una arreglo numpy en un archivo CSV?

Dé algunos ejemplos de funciones Numpy para realizar operaciones matemáticas.

Proporcione algunos ejemplos de funciones Numpy para realizar la manipulación de arreglos.

Dé algunos ejemplos de funciones Numpy para realizar álgebra lineal.

Dé algunos ejemplos de funciones Numpy para realizar operaciones estadísticas.

¿Cómo encuentra la función Numpy correcta para una operación o caso de uso específico?

¿Dónde puede ver una lista de todas las funciones y operaciones de la matriz Numpy?

¿Cuáles son los operadores aritméticos compatibles con las arreglos Numpy? Ilustrar con ejemplos.

¿Qué es la radiodifusión de matriz? ¿Cómo es útil? Ilustre con un ejemplo.

Proporciona algunos ejemplos de arreglos que sean compatibles para la transmisión.

Dé algunos ejemplos de arreglos que no son compatibles para la transmisión.

¿Cuáles son los operadores de comparación admitidos por las arreglos Numpy? Ilustrar con ejemplos.

¿Cómo accede a un subarreglo o segmento específico de un arreglo Numpy?

Ilustra la indexación y el corte de arreglos en arreglos Numpy multidimensionales con algunos ejemplos.

¿Cómo se crea una matriz Numpy con una forma dada que contiene todos los ceros?

¿Cómo se crea una matriz Numpy con una forma dada que contiene todos unos?

¿Cómo se crea una matriz de identidad de una forma dada?

¿Cómo se crea un vector aleatorio de una longitud dada?

¿Cómo se crea una matriz Numpy con una forma dada con un valor fijo para cada elemento?

¿Cómo se crea una matriz Numpy con una forma dada que contiene elementos inicializados aleatoriamente?

¿Cuál es la diferencia entre np.random.rand y np.random.randn ? Ilustrar con ejemplos.

¿Cuál es la diferencia entre np.arange y np.linspace ? Ilustrar con ejemplos.

Está listo para pasar a la siguiente sección de este tutorial.

Cómo analizar datos tabulares usando Python y Pandas

Sigue y ejecuta el código aquí: https://jovian.ai/aakashns/python-pandas-data-analysis .

Esta sección cubre los siguientes temas:

Cómo leer un archivo CSV en un marco de datos de Pandas

Cómo recuperar datos de marcos de datos de Pandas

Cómo consultar, clasificar y analizar datos

Cómo fusionar, agrupar y agregar datos

Cómo extraer información útil de las fechas

Trazado básico usando gráficos de líneas y barras

Cómo escribir marcos de datos en archivos CSV

Cómo leer un archivo CSV usando Pandas 

Pandas es una biblioteca popular de Python que se utiliza para trabajar con datos tabulares (similares a los datos almacenados en una hoja de cálculo). Proporciona funciones auxiliares para leer datos de varios formatos de archivo como CSV, hojas de cálculo de Excel, tablas HTML, JSON, SQL y más.

Descarguemos el archivo italy-covid-daywise.txt que contiene una gama de datos sobre el Covid-19 en Italia en el siguiente formato:

date,new_cases,new_deaths,new_tests
2020-04-21,2256.0,454.0,28095.0
2020-04-22,2729.0,534.0,44248.0
2020-04-23,3370.0,437.0,37083.0
2020-04-24,2646.0,464.0,95273.0
2020-04-25,3021.0,420.0,38676.0
2020-04-26,2357.0,415.0,24113.0
2020-04-27,2324.0,260.0,26678.0
2020-04-28,1739.0,333.0,37554.0
... 

Este formato de almacenamiento de datos se conoce como valores separados por comas o CSV. Aquí hay un recordatorio en caso de que necesites una definición de lo que es el formato CSV:

CSV: un archivo de valores separados por comas (CSV) es un archivo de texto delimitado que utiliza una coma para separar los valores. Cada línea del archivo es un registro de datos. Cada registro consta de uno o más campos, separados por comas. Un archivo CSV generalmente almacena datos tabulares (números y texto) en texto sin formato, en cuyo caso cada línea tendrá la misma cantidad de campos. (Wikipedia)

Descargaremos este archivo usando la función urlretrieve que proviene del módulo urllib.request .

from urllib.request import urlretrieve

urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/09/italy-covid-daywise.csv', 'italy-covid-daywise.csv') 

Para leer el archivo, podemos usar el método de Pandas read_csv . Pero primero, instalemos la librería de Pandas. 

!pip install pandas --upgrade --quiet 

Ahora podemos importar nuestro módulo pandas , el cual por convención es importado como pd .

import pandas as pd

covid_df = pd.read_csv('italy-covid-daywise.csv') 

Los datos del archivos se almacenan en un objeto DataFrame – una de las estructuras principales en Pandas para almacenar y trabajar con datos tabulares. En el particular caso de los DataFrames; típicamente empleamos el sufijo _df en el nombre de las variables.

type(covid_df)
# pandas.core.frame.DataFrame

covid_df 

Esto es lo que podemos decir al mirar el marco de datos:

El archivo proporciona recuentos de cuatro días para COVID-19 en Italia
Las métricas reportadas son casos nuevos, muertes y pruebas.

Los datos se proporcionan durante 248 días: del 12 de diciembre de 2019 al 3 de septiembre de 2020
Ten en cuenta que estos son números informados oficialmente. El número real de casos y muertes puede ser mayor, ya que no todos los casos se diagnostican.

Podemos observar alguna información básica usando el método .info .

covid_df.info() 

Parece que cada columna contiene valores de un tipo de datos específico. Puedes ver información estadística para columnas numéricas (media, desviación estándar, valores mínimos/máximos y el número de valores no vacíos) usando el método .describe .

covid_df.describe() 

La propiedad columns contiene la lista de las columnas dentro del DataFrame.

covid_df.columns
# Index(['date', 'new_cases', 'new_deaths', 'new_tests'], dtype='object') 

También puedes obtener el número de filas y columnas en el DataFrame usando el método .shape .

covid_df.shape
# (248, 4) 

He aquí un resumen de las funciones y métodos que hemos visto hasta ahora:

pd.read_csv – Lee (y transforma) los datos de un archivo CSV a un objeto de Pandas DataFrame .

.info() – Visualiza información básica acerca de filas columnas y tipo de datos.

.describe() – Visualiza información estadística acerca de los datos almacenados en las columnas.

.columns – Retorna la lista de los nombres de las columnas.

.shape – Obtiene el número de filas y columnas en forma de Tupla.

Re cuperar datos de un DataFrame en Pandas 

La primera cosa que querrás hacer será recuperar datos almacenados en un DataFrame, como el conteo de días específicos, o la lista de valores en una columna particular.

Para hacer esto, debes comprender la representación interna de los datos en un marco de datos. Conceptualmente, puedes pensar en un marco de datos como un diccionario de listas: las claves son nombres de columna y los valores son listas/arreglos que contienen datos para las columnas respectivas.

# El formato de Pandas SÍ es similar a esto:
covid_data_dict = {
'date': ['2020-08-30', '2020-08-31', '2020-09-01', '2020-09-02', '2020-09-03'],
'new_cases': [1444, 1365, 996, 975, 1326],
'new_deaths': [1, 4, 6, 8, 6],
'new_tests': [53541, 42583, 54395, None, None]
} 

Representar los datos en el formato de arriba tiene varios beneficios:

Todos los valores de una columna suelen tener el mismo tipo de valor, por lo que es más eficiente almacenarlos en un único arreglo.

Recuperar los valores de una fila en particular simplemente requiere extraer los elementos en un índice determinado de columnas.

La representación es más compacta (los nombres de las columnas se registran solo una vez) en comparación con otros formatos que usan un diccionario para cada fila de datos (por favor mirar el ejemplo a continuación).

# El formato de Pandas NO es similar a esto
covid_data_list = [
{'date': '2020-08-30', 'new_cases': 1444, 'new_deaths': 1, 'new_tests': 53541},
{'date': '2020-08-31', 'new_cases': 1365, 'new_deaths': 4, 'new_tests': 42583},
{'date': '2020-09-01', 'new_cases': 996, 'new_deaths': 6, 'new_tests': 54395},
{'date': '2020-09-02', 'new_cases': 975, 'new_deaths': 8 },
{'date': '2020-09-03', 'new_cases': 1326, 'new_deaths': 6},
] 

Con la analogía del diccionario de listas en mente, ahora puedes adivinar cómo recuperar datos de un DataFrame. Por ejemplo, podemos obtener una lista de valores de una columna específica utilizando la notación de indexación [].

covid_data_dict['new_cases']
# [1444, 1365, 996, 975, 1326]

covid_df['new_cases']
# 0 0.0
# 1 0.0
# 2 0.0
# 3 0.0
# 4 0.0
# ... 
# 243 1444.0
# 244 1365.0
# 245 996.0
# 246 975.0
# 247 1326.0
# Name: new_cases, Length: 248, dtype: float64 

Cada columna está representada por una estructura de datos llamada   Series , l a cual es esencialmente un arreglo de Numpy con algunos métodos y propiedades adicionales .

type(covid_df['new_cases'])
# pandas.core.series.Series 

Como en los arreglos; puedes recuperar un valor específico con una Series, usando la notación index [] .

covid_df['new_cases'][246]
# 975.0

covid_df['new_tests'][240]
57640.0 

Pandas también nos provee del método .at para recuperar el elemento en una fila y columna específica de forma directa.

covid_df.at[246, 'new_cases']
# 975.0

covid_df.at[240, 'new_tests']
# 57640.0 

En vez de usar la notación de [] , Pandas también nos permite acceder a las columnas como propiedades del DataFrame, usando otro tipo de notación, la notación . . Sin embargo, este método solo funciona para columnas cuyos nombres no contienen espacios o carácteres especiales.

covid_df.new_cases
# 0 0.0
# 1 0.0
# 2 0.0
# 3 0.0
# 4 0.0
# ... 
# 243 1444.0
# 244 1365.0
# 245 996.0
# 246 975.0
# 247 1326.0
# Name: new_cases, Length: 248, dtype: float64 

Además,  también puedes pasar una lista de columnas dentro de la notación index   [] para acceder a un subconjunto del DataFrame con solo las columnas ya presentes.

cases_df = covid_df[['date', 'new_cases']]
cases_df 

El nuevo DataFrame cases_df es simplemente un "primer acercamiento" del DataFrame original covid_df . Ambos apuntan a los mismos datos en la memoria de la computadora. Cambiar cualquier valor dentro de uno de ellos también cambiará los valores respectivos en el otro.

Compartir datos entre DataFrames hace que la manipulación de datos en Pandas sea increíblemente rápida. No necesitas preocuparte por la sobrecarga de copiar miles o millones de filas cada vez que desee crear un nuevo marco de datos al operar en uno existente.

A veces, puede que necesites una copia completa del DataFrame, en este caso puedes usar el método copy .

covid_df_copy = covid_df.copy() 

Los datos dentro de covid_df_copy están ahora completamente separados covid_df , por lo que a partir de ahora, el cambiar los valores al interior de uno, no afectará los valores del otro. 

Para acceder a esta lista específica de datos, Pandas nos brinda el método .loc .

covid_df 

covid_df.loc[243]
# date 2020-08-30
# new_cases 1444.0
# new_deaths 1.0
# new_tests 53541.0
# Name: 243, dtype: object 

Cada columna recuperada es un objeto de una Series .

type(covid_df.loc[243])
# pandas.core.series.Series 

Podemos emplear los métodos .head y .tail para ver los primeros o últimos datos, respectivamente.

covid_df.head(5) 

covid_df.tail(4) 

Nótese que en los resultados de arriba, que pese a que los primeros valores en   new_cases y new_deaths sus columnas son 0 , los valores correspondientes dentro de las columnas new_tests son NaN . Esto es debido a que el archivo CSV no contiene ningún dato en la columa new_tests respecto a fechas específicas (puedes verificar esto mirando al interior del archivo CSV). Estos valores constituyen Missing Data .

covid_df.at[0, 'new_tests']
# nan

type(covid_df.at[0, 'new_tests'])
# numpy.float64 

La diferencia entre 0 y NaN es sutil pero importante . En este conjunto de datos, representa que los números de prueba diarios no se informaron en fechas específicas. Italia comenzó a informar pruebas diarias el 19 de abril de 2020. Ya habían realizado 935,310 pruebas antes del 19 de abril.

Podemos confirmar que el primer índice (Index) no contiene un valor NaN usando el método first_valid_index .

covid_df.new_tests.first_valid_index()
# 111 

Ahora echemos un vistazo a unas cuantas filas antes y después del índice para verificar que los valores NaN han sido cambiados a números reales . Podemos hacer esto definiendo un rango luego de aplicar loc . 

covid_df.loc[108:113] 

Podemos usar el método .sample para recuperar una muestra aleatoria de filas, provenientes de nuestro DataFrame.

covid_df.sample(10) 

Ten en cuenta que aunque hemos tomado una muestra aleatoria, se conserva el índice original de cada fila. Esta es una propiedad útil de los DataFrame.

He aquí un resumen de las funciones y métodos vistos en esta sección:

covid_df['new_cases'] – Recupera las columnas como Series usando el nombre de la columna.

new_cases[243] – Recupera valores de una Series usando la notación index

covid_df.at[243, 'new_cases'] – Recupera un solo valor de un DataFrame específico.

covid_df.copy() – Crea una copia de un DataFrame.

covid_df.loc[243] - Recupera una fila o rango de filas de datos, provenientes de un DataFrame específico.

head , tail , and sample – Recupera múltiples filas de datos de un DataFrame.

covid_df.new_tests.first_valid_index – Encuentra el primer índice no nulo en una Series.

Análisis de Datos de un DataFrame en Pandas.

Let's try to answer some questions about our data.

Q: Cuál es el número total de casos y muertes reportadas por Covid-19 en Italia ? 

Similar a los arreglos de Numpy, una Series de Pandas soporta el método sum para dar respuesta a estas preguntas.

total_cases = covid_df.new_cases.sum()
total_deaths = covid_df.new_deaths.sum()

print('The number of reported cases is {} and the number of reported deaths is {}.'.format(int(total_cases), int(total_deaths)))
# The number of reported cases is 271515 and the number of reported deaths is 35497. 

Q: ¿Cuál es la tasa de mortalidad general (proporción de muertes notificadas a casos notificados) 

death_rate = covid_df.new_deaths.sum() / covid_df.new_cases.sum()

print("The overall reported death rate in Italy is {:.2f} %.".format(death_rate*100))
# The overall reported death rate in Italy is 13.07 %. 

Q: ¿Cuál es el número total de pruebas realizadas? Se realizaron un total de 935,310 pruebas antes de que se informaran los números de pruebas diarias. 

initial_tests = 935310
total_tests = initial_tests + covid_df.new_tests.sum()

total_tests
# 5214766.0 

Q: Qué proporción de los test nos dió un resultado positivo ? 

positive_rate = total_cases / total_tests

print('{:.2f}% of tests in Italy led to a positive diagnosis.'.format(positive_rate*100))
# 5.21% of tests in Italy led to a positive diagnosis. 

Estas preguntas son solo una muestra; puedes continuar realizando preguntas y respondiéndolas con el código.

Cómo consultar y ordenar filas en Pandas

Supongamos que solo queremos dar un vistazo a los días en los que hubieron más de 1000 casos reportados. Podemos emplear una expresión booleana para averiguar cuales filas satisfacen este criterio.

high_new_cases = covid_df.new_cases > 1000

high_new_cases
# 0 False
# 1 False
# 2 False
# 3 False
# 4 False
# ... 
# 243 True
# 244 True
# 245 False
# 246 False
# 247 True
# Name: new_cases, Length: 248, dtype: bool 

La expresión booleana retorna valores enmarcados en los criterios "verdadero" y "falso" True y False , estos representan valores booleanos . Puedes usar esta series para seleccionar un subconjunto de filas del DataFrame original, correspondientes al valor True en las Series.

covid_df[high_new_cases] 

El DataFrame contiene 72 filas, pero solo la primera y las últimas cinco filas se muestran de forma predeterminada con Jupyter por razones de brevedad. Podemos cambiar algunas opciones de visualización para ver todas las filas.

high_cases_df = covid_df[covid_df.new_cases > 1000]

high_cases_df 

from IPython.display import display
with pd.option_context('display.max_rows', 100):
display(covid_df[covid_df.new_cases > 1000]) 
This is just part of the data frame. Check out the rest here . 
También podemos formular consultas más complejas que involucren varias columnas. Como ejemplo, tratemos de determinar los días en que la proporción de casos informados a las pruebas realizadas es más alta que el total. positive_rate .

positive_rate
# 0.05206657403227681

high_ratio_df = covid_df[covid_df.new_cases / covid_df.new_tests > positive_rate]

high_ratio_df 

El resultado de realizar una operación en dos columnas es una nueva serie.

covid_df.new_cases / covid_df.new_tests
# 0 NaN
# 1 NaN
# 2 NaN
# 3 NaN
# 4 NaN
# ... 
# 243 0.026970
# 244 0.032055
# 245 0.018311
# 246 NaN
# 247 NaN
# Length: 248, dtype: float64 

Podemos usar esta nueva series en el DataFrame

covid_df['positive_rate'] = covid_df.new_cases / covid_df.new_tests

covid_df 

Sin embargo, ten en cuenta que a veces puede tomar unos días obtener los resultados de una prueba, por lo que no podemos comparar la cantidad de casos nuevos con la cantidad de pruebas realizadas el mismo día. Cualquier inferencia basada en la columna positive_rate sería probablemente incorrecta.

Es esencial tener cuidado con estas relaciones sutiles que a menudo no se transmiten dentro del archivo CSV y requieren algún contexto externo. Siempre es una buena idea leer la documentación provista con el conjunto de datos o solicitar más información.

Por ahora removamos la columna positive_rate usando el método drop .

covid_df.drop(columns=['positive_rate'], inplace=True) 

Puedes deducir el significado del argumento inplace ?

Cómo ordenar filas usando valores de columnas en Pandas

También puedes ordenar las filas por una columna específica usando .sort_values . Ordenemos para identificar los días con el mayor número de casos, luego encadenémoslo con el método head para presentar los primeros 10 resultados.

covid_df.sort_values('new_cases', ascending=False).head(10) 

Parece que las últimas dos semanas de marzo tuvieron el mayor número de casos diarios. Comparemos esto con los días en los que se registró el mayor número de muertes.

covid_df.sort_values('new_deaths', ascending=False).head(10) 

Parece que las muertes diarias alcanzan un pico casi una semana después del pico de nuevos casos diarios.
Veamos también los días con el menor número de casos. Podríamos esperar ver los primeros días del año en esta lista.

covid_df.sort_values('new_cases').head(10) 

Parece que el recuento de casos nuevos el 20 de junio de 2020 fue -148 , ¡un número negativo! No es algo que podríamos haber esperado, pero esa es la naturaleza de los datos del mundo real. Podría ser un error de ingreso de datos, o el gobierno puede haber emitido una corrección para dar cuenta de errores de conteo en el pasado.

¿Puedes buscar artículos de noticias en línea y averiguar por qué el número fue negativo?

Veamos algunos días antes y después del 20 de junio de 2020.

covid_df.loc[169:175] 

Por ahora, supongamos que esto fue realmente un error de entrada de datos. Podemos usar uno de los siguientes enfoques para tratar con el valor faltante o defectuoso:

Reemplazarlo con 0 .

Reemplazarlo con el promedio de la columna entera.

Reemplazarlo con el promedio de los dos valores de la fecha previa y la siguiente (el punto medio entre su diferencia).

Descartar la columna entera.

Cada enfoque requiere cierto contexto acerca del origen de los datos y la naturaleza del problema.  En este caso, dado que estamos tratando con datos ordenados por fecha; podemos usar el tercer enfoque. 

Puedes usar el método .at para modificar un valor específico dentro del DataFrame. 

covid_df.at[172, 'new_cases'] = (covid_df.at[171, 'new_cases'] + covid_df.at[173, 'new_cases'])/2 

He aquí un resumen de las funciones y métodos que utilizamos en esta sección:

covid_df.new_cases.sum() – Calcula la suma de todos los valores en una columna o series.

covid_df[covid_df.new_cases > 1000] – Realiza una consulta que filtra un subconjunto de filas. Todas estas filas tienen en común el que satisfacen la condición establecida en las expresiones booleanas (> 1000) en este caso.

df['pos_rate'] = df.new_cases/df.new_tests – Añade nuevas columnas mediante la combinación de datos de columnas ya existentes. (como el ratio entre casos y test presentado en este ejemplo).

covid_df.drop('positive_rate') – Remueve una o más columnas del DataFrame.

sort_values – Ordena las filas de un DataFrame usando valores de columnas.

covid_df.at[172, 'new_cases'] = ... – Reemplaza un valor dentro de un DataFrame.

Cómo trabajar con fechas en Pandas 

Si bien hemos analizado los números generales de los casos, las pruebas, la tasa positiva y más, también sería útil estudiar estos números mes a mes.

date  en Pandas provee varias facilidades a la hora de trabajar con fechas. 

covid_df.date
# 0 2019-12-31
# 1 2020-01-01
# 2 2020-01-02
# 3 2020-01-03
# 4 2020-01-04
# ... 
# 243 2020-08-30
# 244 2020-08-31
# 245 2020-09-01
# 246 2020-09-02
# 247 2020-09-03
# Name: date, Length: 248, dtype: object 

El tipo de datos es actualmente un objeto, object , por lo que Pandas "no sabe" que esta columna es una fecha. Hay que convertirlo a una columna datetime usando el método pd.to_datetime .

covid_df['date'] = pd.to_datetime(covid_df.date)

covid_df['date']
# 0 2019-12-31
# 1 2020-01-01
# 2 2020-01-02
# 3 2020-01-03
# 4 2020-01-04
# ... 
# 243 2020-08-30
# 244 2020-08-31
# 245 2020-09-01
# 246 2020-09-02
# 247 2020-09-03
# Name: date, Length: 248, dtype: datetime64[ns] 

Puedes confirmar que ahora tiene el tipo de dato datetime64 . Ahora podemos extraer diferentes partes de los datos en columnas separadas, usando la claseWe can now extract different parts of the data into separate columns, using the DatetimeIndex ( ver doc ).

covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday

covid_df 

Revisemos las métricas generales de mayo. Podemos consultar las filas de mayo, elegir un subconjunto de columnas y usar el método sum para agregar cada uno de los valores de columna seleccionados.

# Query the rows for May
covid_df_may = covid_df[covid_df.month == 5]

# Extract the subset of columns to be aggregated
covid_df_may_metrics = covid_df_may[['new_cases', 'new_deaths', 'new_tests']]

# Get the column-wise sum
covid_may_totals = covid_df_may_metrics.sum()

covid_may_totals
# new_cases 29073.0
# new_deaths 5658.0
# new_tests 1078720.0
# dtype: float64

type(covid_may_totals)
# pandas.core.series.Series 

También podemos combinar las operaciones antes mencionadas en una declaración simple:

covid_df[covid_df.month == 5][['new_cases', 'new_deaths', 'new_tests']].sum()
# new_cases 29073.0
# new_deaths 5658.0
# new_tests 1078720.0
# dtype: float64 

Como otro ejemplo, comprobemos si el número de casos notificados los domingos es superior a la media de casos notificados todos los días. Esta vez, podríamos querer agregar columnas usando el método .mean 

# Overall average
covid_df.new_cases.mean()

# 1096.6149193548388

# Average for Sundays
covid_df[covid_df.weekday == 6].new_cases.mean()

# 1247.2571428571428 

Parece que se informaron más casos los domingos en comparación con otros días.
Intenta hacer y responder algunas preguntas adicionales relacionadas datos y fechas.

Cómo Agrupar y Agregar Datos en Pandas

Como siguiente paso, es posible que deseemos resumir los datos diarios y crear un nuevo DataFrame con datos mensuales. Podemos usar la función groupby para agrupar por mes, seleccionando las columnas que deseamos agrupar (en este caso new_cases, new_deaths y new_tests).

Esto sería la agrupación. Finalmente agregamos todos estos datos usando el método sum .

covid_month_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()

covid_month_df 

El resultado es un nuevo DataFrame que contiene valores únicos de las columnas seleccionadas con groupby nótese que este último también ha funcionado como index. La agrupación y agregación son métodos poderosos para resumir progresivamente los datos en DataFrames más pequeños. 

En lugar de agregar por suma, también podemos agregar por otras medidas como la media (mean). Calculemos el número promedio de casos nuevos diarios, muertes y pruebas para cada mes.

covid_month_mean_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].mean()

covid_month_mean_df 

Además de la agrupación, otra forma de agregación es la suma acumulada. En este caso; la suma acumulada de casos, pruebas o muertes hasta la fecha de cada fila. Podemos usar el método cumsum para calcular la suma acumulada de una columna. 

Añadamos tres columnas: total_cases , total_deaths , and total_tests .

covid_df['total_cases'] = covid_df.new_cases.cumsum()
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()
covid_df['total_tests'] = covid_df.new_tests.cumsum() + initial_tests 

También hemos incluído el el conteo inicial en   total_test para contar los test realizados antes de que empezara el reporte diario por parte de las autoridades.

covid_df 

Nótese como los valores NaN en la columna total_tests permanecen inafectados.

Cómo unir datos desde diferentes fuentes en Pandas 

Para determinar otras métricas como pruebas por millón, casos por millón, etc., necesitamos más información sobre el país, es decir, su población.

Descarguemos otro archivo locations.csv que contiene información relacionada con la salud de muchos países, incluida Italia.

urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 'locations.csv')

locations_df = pd.read_csv('locations.csv')
locations_df 

locations_df[locations_df.location == "Italy"] 

Podemos fusionar estos datos en nuestro marco de datos existente agregando más columnas. Sin embargo, para fusionar dos DataFrames, necesitamos al menos una columna común. Insertemos una columna location en el DataFrame covid_df seleccionando únicamente los valores de Italia, "Italy" .

covid_df['location'] = "Italy"

covid_df 

Ahora podemos añadir las columnas de locations_df en covid_df usando el método .merge .

merged_df = covid_df.merge(locations_df, on="location")

merged_df 
Check out the full data frame here . 
Los datos de ubicación de Italia se adjuntan a cada fila dentro de covid_df . Si el DataFrame covid_df contenía datos para varias ubicaciones, entonces se agregarían los datos de ubicación del país respectivo para cada fila.

Ahora podemos calcular métricas como casos por millón, muertes por millón y pruebas por millón.

merged_df['cases_per_million'] = merged_df.total_cases * 1e6 / merged_df.population
merged_df['deaths_per_million'] = merged_df.total_deaths * 1e6 / merged_df.population
merged_df['tests_per_million'] = merged_df.total_tests * 1e6 / merged_df.population

merged_df 
Check out the full data frame here . 
Cómo volver a escribir datos en archivos de Pandas

Después de completar el análisis y agregar nuevas columnas, debes volver a escribir los resultados en un archivo. De lo contrario, los datos se perderán cuando el portátil Jupyter se apague.
Antes de escribir en el archivo, primero creemos un DataFrame que contenga solo las columnas que deseamos registrar.

result_df = merged_df[['date',
'new_cases', 
'total_cases', 
'new_deaths', 
'total_deaths', 
'new_tests', 
'total_tests', 
'cases_per_million', 
'deaths_per_million', 
'tests_per_million']]

result_df 

Para escribir los datos del DataFrame en un archivo, podemos usar la función to_csv .

result_df.to_csv('results.csv', index=None) 

La función to_csv también incluye una columna adicional para guardar el Index del DataFrame. Esta columna está por defecto. Si pasamos el código index=None eliminaremos esta columna por defecto.Puedes verificar que   results.csv ha sido creada con los datos del DataFrame en el formato CSV:

date,new_cases,total_cases,new_deaths,total_deaths,new_tests,total_tests,cases_per_million,deaths_per_million,tests_per_million
2020-02-27,78.0,400.0,1.0,12.0,,,6.61574439992122,0.1984723319976366,
2020-02-28,250.0,650.0,5.0,17.0,,,10.750584649871982,0.28116913699665186,
2020-02-29,238.0,888.0,4.0,21.0,,,14.686952567825108,0.34732658099586405,
2020-03-01,240.0,1128.0,8.0,29.0,,,18.656399207777838,0.47964146899428844,
2020-03-02,561.0,1689.0,6.0,35.0,,,27.93498072866735,0.5788776349931067,
2020-03-03,347.0,2036.0,17.0,52.0,,,33.67413899559901,0.8600467719897585,
... 

Bonus: Visualización de Datos básica con Pandas 

Generalmente usamos bibliotecas como matplotlib o seaborn para graficar en un notebook de Jupyter. Sin embargo, pandas también provee un método sencillo, .plot para graficar de forma rápida y conveniente.

Hagamos un gráfico lineal que muestre cómo varía el número de casos diarios con el tiempo.

result_df.new_cases.plot(); 

Si bien este gráfico muestra la tendencia general, es difícil saber dónde se produjo el pico, ya que no hay fechas en el eje X. Podemos usar la columna date como el index para el DataFrame. 

result_df.set_index('date', inplace=True)

result_df 

Ten en cuenta que el índice de un DataFrame no tiene que ser numérico. Usar la fecha como índice también nos permite obtener los dato usando .loc .

result_df.loc['2020-09-01']
# new_cases 9.960000e+02
# total_cases 2.696595e+05
# new_deaths 6.000000e+00
# total_deaths 3.548300e+04
# new_tests 5.439500e+04
# total_tests 5.214766e+06
# cases_per_million 4.459996e+03
# deaths_per_million 5.868661e+02
# tests_per_million 8.624890e+04
# Name: 2020-09-01 00:00:00, dtype: float64 

Tracemos los nuevos casos y las nuevas muertes por día como gráficos de líneas.

result_df.new_cases.plot()
result_df.new_deaths.plot(); 

También podemos comparar el total de casos vs. el total de muertes.

result_df.total_cases.plot()
result_df.total_deaths.plot(); 

Veamos cómo la tasa de mortalidad y las tasas de pruebas positivas varían con el tiempo.

death_rate = result_df.total_deaths / result_df.total_cases

death_rate.plot(title='Death Rate'); 

positive_rates = result_df.total_cases / result_df.total_tests

positive_rates.plot(title='Positive Rate'); 

Finalmente, tracemos algunos datos mensuales usando un gráfico de barras para visualizar la tendencia a un nivel superior.

covid_month_df.new_cases.plot(kind='bar'); 

covid_month_df.new_tests.plot(kind='bar') 

Ejercicios en Pandas 

Prueba los siguientes ejercicios para familiarizarse con los marcos de datos de Pandas y practicar sus habilidades:

Evaluación sobre DataFrames 

Ejercicios adicionales en Pandas 

Kaggle 

Resumen y lecturas adicionales

Hemos cubierto los siguientes temas en este tutorial:

Cómo leer un archivo CSV en un marco de datos de Pandas

Cómo recuperar datos de marcos de datos de Pandas

Cómo consultar, clasificar y analizar datos

Cómo fusionar, agrupar y agregar datos

Cómo extraer información útil de las fechas

Trazado básico usando gráficos de líneas y barras

Cómo escribir marcos de datos en archivos CSV

Consulta los siguientes recursos para obtener más información sobre Pandas:

Guía de Pandas 

Python for Data Analysis (Libro del creator of Pandas) 

Preguntas para evaluar tu comprensión

Intenta responder las siguientes preguntas para evaluar tu comprensión de los temas tratados en este capítulo:

1.¿Qué es Pandas? ¿Qué lo hace útil?
2.¿Cómo se instala la biblioteca Pandas?
3.¿Cómo se importa el módulo pandas?
4.¿Cuál es el alias común que se usa al importar el módulo pandas?
5.¿Cómo se lee un archivo CSV usando Pandas? Dar un ejemplo.
6.¿Cuáles son otros formatos de archivo que puede leer con Pandas? Ilustrar con ejemplos.
7.¿Qué son los marcos de datos de Pandas?
8.¿En qué se diferencian los marcos de datos de Pandas de los arreglos de Numpy?
9.¿Cómo encuentra el número de filas y columnas en un marco de datos?
10.¿Cómo se obtiene la lista de columnas en un marco de datos?
11.¿Cuál es el propósito del método de descripción de un marco de datos?
12.¿En qué se diferencian la información y los métodos de marco de datos descritos?
13.¿Es un dataframe de Pandas conceptualmente similar a una lista de diccionarios oa un diccionario de listas? Explique con un ejemplo.
14.¿Qué es una Serie Pandas? ¿En qué se diferencia de una matriz Numpy?
15.¿Cómo accede a una columna desde un marco de datos?
16. ¿Cómo accede a una fila desde un marco de datos?
17. ¿Cómo accede a un elemento en una fila y columna específicas de un marco de datos?
18.¿Cómo se crea un subconjunto de un marco de datos con un conjunto específico de columnas?
19.¿Cómo se crea un subconjunto de un marco de datos con un rango específico de filas?
20. ¿El cambio de un valor dentro de un DataFrame afecta a otros DataFrames creados usando un subconjunto de filas o columnas? ¿Por que es esto entonces?
21.¿Cómo se crea una copia de un DataFrame?
22.¿Por qué debería evitar crear demasiadas copias de un DataFrame?
23.¿Cómo ve las primeras filas de un DataFrame?
24.¿Cómo ve las últimas filas de un DataFrame?
25.¿Cómo ve una selección aleatoria de filas de un DataFrame?
26.¿Qué es el "índice" en un DataFrame? ¿Cómo es útil?
27.¿Qué representa un valor de NaN en un dataframe de Pandas?
28.¿En qué se diferencia Nan de 0?
29.¿Cómo identifica la primera fila no vacía en una serie o columna de Pandas?
30.¿Cuál es la diferencia entre df.loc y df.at?
31.¿Dónde puede encontrar una lista completa de los métodos compatibles con los objetos Pandas DataFrame y Series?
32. ¿Cómo encuentra la suma de números en una columna de un DataFrame?
33. ¿Cómo encuentra la media de los números en una columna de un marco de datos?
34. ¿Cómo encuentra la cantidad de números que no están vacíos en una columna de un DataFrame?
35.¿Cuál es el resultado obtenido al usar una columna Pandas en una expresión booleana? Ilustre con un ejemplo.
36.¿Cómo selecciona un subconjunto de filas donde el valor de una columna específica cumple una condición dada? Ilustre con un ejemplo.
37.¿Cuál es el resultado de la expresión df[df.new_cases > 100]?
38. ¿Cómo se muestran todas las filas de un marco de datos de pandas en una salida de celda Jupyter?
39.¿Cuál es el resultado que se obtiene al realizar una operación aritmética entre dos columnas de un dataframe? Ilustre con un ejemplo.
40. ¿Cómo agrega una nueva columna a un marco de datos combinando valores de dos columnas existentes? Ilustre con un ejemplo.
41.¿Cómo se elimina una columna de un marco de datos? Ilustre con un ejemplo.
42. ¿Cuál es el propósito del argumento in situ en los métodos de marco de datos?
43. ¿Cómo se ordenan las filas de un marco de datos en función de los valores de una columna en particular?
44. ¿Cómo se ordena un marco de datos de pandas utilizando valores de varias columnas?
45. ¿Cómo se especifica si se ordena de forma ascendente o descendente al ordenar un marco de datos de Pandas?
46. ​​¿Cómo cambia un valor específico dentro de un marco de datos?
47.¿Cómo se convierte una columna de marco de datos al tipo de datos de fecha y hora?
48.¿Cuáles son los beneficios de usar el tipo de datos de fecha y hora en lugar del tipo de objeto?
49.¿Cómo se extraen diferentes partes de una columna de fecha como el mes, año, mes, día de la semana, etc. en columnas separadas? Ilustre con un ejemplo.
50. ¿Cómo se agregan varias columnas de un marco de datos?
51.¿Cuál es el propósito del método groupby de un marco de datos? Ilustre con un ejemplo.
52.¿Cuáles son las diferentes formas en que puede agregar los grupos creados por groupby?
53.¿Qué quiere decir con una suma continua o acumulada?
54.¿Cómo se crea una nueva columna que contiene la suma acumulada o acumulada de otra columna?
55.¿Qué otras medidas acumulativas admiten los marcos de datos de Pandas?
56.¿Qué significa fusionar dos marcos de datos? Dar un ejemplo.
57. ¿Cómo especificas las columnas que deben usarse para fusionar dos marcos de datos?
58.¿Cómo se escriben datos de un marco de datos de Pandas en un archivo CSV? Dar un ejemplo.
59. ¿Cuáles son algunos otros formatos de archivo en los que puede escribir desde un marco de datos de Pandas? Ilustrar con ejemplos.
60. ¿Cómo se crea un gráfico de líneas que muestra los valores dentro de una columna de un marco de datos?
61.¿Cómo se convierte una columna de un marco de datos en su índice?
62. ¿Puede el índice de un marco de datos no ser numérico?
63.¿Cuáles son los beneficios de usar un marco de datos no numérico? Ilustre con un ejemplo.
64. ¿Cómo se crea un gráfico de barras que muestra los valores dentro de una columna de un marco de datos?
65. ¿Cuáles son algunos otros tipos de gráficos compatibles con los marcos de datos y las series de Pandas?

¡Tienes lo necesario para la siguiente sección del tutorial!

Data Visualization using Python, Matplotlib, and Seaborn 

Notebook link: https://jovian.ai/aakashns/python-matplotlib-data-visualization 

La visualización de datos es la representación gráfica de los datos. Implica producir imágenes que comuniquen las relaciones entre los datos representados a los espectadores.

La visualización de datos es una parte esencial del análisis de datos y el aprendizaje automático. Usaremos bibliotecas de Python como Matplotlib y Seaborn para aprender y aplicar algunas técnicas populares de visualización de datos. 

Para empezar, installemos las bibliotecas en cuestión. Usaremos el módulo matplotlib.pyplot para gáficos sencillos. A menudo se importa con el alias plt .También usaremos el módulo seaborn para gráficos más avanzados. Este a menudo se importa mediante el alias sns .

!pip install matplotlib seaborn --upgrade --quiet

import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline 

Nótese el comando especial %matplotlib inline para garantizar que nuestros gráficos se muestren e incrusten en el propio cuaderno de Jupyter. Sin este comando, a veces pueden aparecer gráficos en ventanas emergentes.

Cómo crear una gráfica lineal en Python 

El gráfico de líneas es una de las técnicas de visualización de datos más simples y más utilizadas. Un gráfico de líneas muestra información como una serie de puntos de datos o marcadores conectados por líneas rectas.
Puede personalizar la forma, el tamaño, el color y otros elementos estéticos de las líneas y los marcadores para una mejor claridad visual.
Aquí hay una lista de Python que muestra el rendimiento de las manzanas (toneladas por hectárea) durante seis años en un país imaginario llamado Kanto.

yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931] 

Podemos visualizar cómo cambia el rendimiento de las manzanas con el tiempo usando un gráfico de líneas. Para dibujar un gráfico de líneas, podemos usar la función plt.plot .

plt.plot(yield_apples) 

Al llamar la función plt.plot  se traza la línea como se esperaba. también incluye la especificación de la línea [<matplotlib.lines.Line2D at 0x7ff70aa20760>] . podemos añadir ( ; ) al final de la declaración en la celda para evitar mostrar eso último y así solo representar la gráfica. 

plt.plot(yield_apples); 

Mejoremos esta trama paso a paso para que sea más informativa y hermosa.

Cómo personalizar el eje X en MatPlotLib

El eje X de la gráfica actualmente muestra los índices de los elementos de la lista de 0 a 5. La gráfica sería más informativa si pudiéramos mostrar el año para el cual estamos trazando los datos. Podemos hacer esto con dos argumentos plt.plot .

years = [2010, 2011, 2012, 2013, 2014, 2015]
yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]

plt.plot(years, yield_apples) 

Axis Labels in MatPlotLib 

Podemos agregar etiquetas a los ejes para mostrar lo que representa cada eje usando los métodos plt.xlabel y plt.ylabel .

plt.plot(years, yield_apples)
plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)'); 

Cómo trazar líneas múltiples en MatPlotLib

Pueden invocar la función plt.plot en cada variable, para graficar múltiples líneas en la misma gráfica; cómo se muestra a continuación en el ejemplo de manzanas y naranjas en Kanto.

years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]

plt.plot(years, apples)
plt.plot(years, oranges)
plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)'); 

Título de gráfica y leyenda en MatPlotLib 

Para diferenciar entre múltiples líneas, podemos incluir una leyenda dentro del gráfico usando la función plt.legend también podemos ajustar el título mediante la función plt.title .

plt.plot(years, apples)
plt.plot(years, oranges)

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges']); 

Cómo usar marcadores de línea en MatPlotLib

También podemos mostrar marcadores para los puntos de datos en cada línea usando el argumento marcador de   plt.plot .

Matplotlib proporciona muchos marcadores diferentes, como un círculo, una cruz, un cuadrado, un diamante y más. Puedes encontrar la lista completa de tipos de marcadores aquí: https://matplotlib.org/3.1.1/api/markers_api.html .

plt.plot(years, apples, marker='o')
plt.plot(years, oranges, marker='x')

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges']); 

Cómo diseñar líneas y marcadores en MatPlotLib

La función plt.plot soporta varios argumentos para dar estilo a las líneas y marcadores:

color o c – Ajusta el color de la línea ( supported colors )

linestyle o ls – Elije entre una línea sólida o discontinua

linewidth o lw – Establece el ancho de una línea

markersize o ms – Fija el tamaño de los marcadores

markeredgecolor o mec – Establecer el color del borde para los marcadores

markeredgewidth o mew – Establecer el ancho del borde para los marcadores

markerfacecolor o mfc – Establecer el color de relleno para los marcadores

alpha – Opacidad de la gráfica

Puedes ver mayor documentación acerca de Matplotlip y plt.plot aquí: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot .

plt.plot(years, apples, marker='s', c='b', ls='-', lw=2, ms=8, mew=2, mec='navy')
plt.plot(years, oranges, marker='o', c='r', ls='--', lw=3, ms=10, alpha=.5)

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges']); 

fmt = '[marker][line][color]'

plt.plot(years, apples, 's-b')
plt.plot(years, oranges, 'o--r')

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges']); 

El argumento fmt proporciona una abreviatura para especificar la forma del marcador, el estilo de línea y el color de línea. Puede proporcionarlo como tercer argumento para plt.plot.

Puedes usar la función plt.figure para cambiar el tamaño de la figura.

plt.plot(years, oranges, 'or')
plt.title("Yield of Oranges (tons per hectare)"); 

Cómo cambiar el tamaño en las gráficas de MatPlotLib 

Usa la función plt.figure 

plt.figure(figsize=(12, 6))

plt.plot(years, oranges, 'or')
plt.title("Yield of Oranges (tons per hectare)"); 

Cómo mejorar los estilos predeterminados usando Seaborn

Una manera fácil de hacer que tus gráficos se vean hermosos es usar algunos estilos predeterminados de la biblioteca Seaborn. Puede aplicarlos globalmente usando la función sns.set_style. Puede ver una lista completa de estilos predefinidos aquí: https://seaborn.pydata.org/generated/seaborn.set_style.html .

sns.set_style("whitegrid")
plt.plot(years, apples, 's-b')
plt.plot(years, oranges, 'o--r')

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges']); 

sns.set_style("darkgrid")

plt.plot(years, apples, 's-b')
plt.plot(years, oranges, 'o--r')

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges']); 

plt.plot(years, oranges, 'or')
plt.title("Yield of Oranges (tons per hectare)"); 

También puedes editar estilos predeterminados directamente modificando el diccionario matplotlib.rcParams. Aprende más: https://matplotlib.org/3.2.1/tutorials/introductory/customizing.html#matplotlib-rcparams .

import matplotlib

matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000' 

Gráficos de Dispersión en MatPlotLib 

En un diagrama de dispersión, los valores de 2 variables se representan como puntos en una cuadrícula bidimensional. Además, también puede utilizar una tercera variable para determinar el tamaño o el color de los puntos. Probemos un ejemplo.

Usando información de la Iris flower dataset obtenermos  medidas de muestra de sépalos y pétalos para tres especies de flores. El conjunto de datos de Iris se incluye con la biblioteca de Seaborn y puedes cargarlo como un DataFrame de Pandas.

# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")

flowers_df 

flowers_df.species.unique()
# array(['setosa', 'versicolor', 'virginica'], dtype=object) 

Tratemos de visualizar la relación entre la longitud del sépalo y el ancho del sépalo. Nuestro primer instinto podría ser crear un gráfico de líneas usando plt.plot .

plt.plot(flowers_df.sepal_length, flowers_df.sepal_width); 

El resultado no es muy informativo ya que hay demasiadas combinaciones de las dos propiedades dentro del conjunto de datos. No parece haber una relación simple entre ellos.

Podemos usar un diagrama de dispersión para visualizar cómo varía la longitud y el ancho del sépalo usando la función scatterplot de seaborn ( sns ).

sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width); 

Cómo agregar tonos en MatPlotLib

Observa cómo los puntos en el gráfico anterior parecen formar grupos distintos con algunos valores atípicos. Podemos colorear los puntos usando la especie de flor como matiz. También podemos agrandar los puntos usando el argumento s .

sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width, hue=flowers_df.species, s=100); 

Agregar matices hace que la trama sea más informativa. Inmediatamente podemos decir que los iris de Setosa tienen una longitud de sépalo más pequeña pero un ancho de sépalo más alto. Por el contrario, lo contrario es cierto para los lirios Virginica.

Cómo personalizar las gráficas de Seaborn

Dado que Seaborn usa internamente las funciones de trazado de Matplotlib, podemos usar funciones como plt.figure y plt.title para modificar la gráfica.

plt.figure(figsize=(12, 6))
plt.title('Sepal Dimensions')

sns.scatterplot(x=flowers_df.sepal_length, 
y=flowers_df.sepal_width, 
hue=flowers_df.species,
s=100); 

Cómo trazar datos usando marcos de datos de Pandas con Seaborn

Seaborn tiene soporte integrado para marcos de datos de Pandas. En lugar de pasar cada columna como una serie, puede proporcionar nombres de columna y usar el argumento data para especificar un DataFrame.

plt.title('Sepal Dimensions')
sns.scatterplot(x='sepal_length', 
y='sepal_width', 
hue='species',
s=100,
data=flowers_df); 

Histogram a s e n MatPlotLib 

Un histograma representa la distribución de una variable creando contenedores (intervalos) a lo largo del rango de valores y mostrando barras verticales para indicar el número de observaciones en cada contenedor (bin).

Por ejemplo, visualicemos la distribución de valores de ancho de sépalo en el conjunto de datos Iris.Podemos usar la función plt.hist para crear un histograma.

# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")

flowers_df.sepal_width
# 0 3.5
# 1 3.0
# 2 3.2
# 3 3.1
# 4 3.6
# ... 
# 145 3.0
# 146 2.5
# 147 3.0
# 148 3.4
# 149 3.0
# Name: sepal_width, Length: 150, dtype: float64 

plt.title("Distribution of Sepal Width")
plt.hist(flowers_df.sepal_width); 

Inmediatamente podemos ver que los anchos de los sépalos se encuentran en el rango de 2,0 a 4,5, y alrededor de 35 valores están en el rango de 2,9 a 3,1, que parece ser el contenedor más poblado.

Cómo controlar el tamaño y la cantidad de contenedores

Podemos controlar el número de contenedores (bins), así como el tamaño de cada uno usando el argumento bins.

# Specifying the number of bins
plt.hist(flowers_df.sepal_width, bins=5); 

import numpy as np

# Specifying the boundaries of each bin
plt.hist(flowers_df.sepal_width, bins=np.arange(2, 5, 0.25)); 

# Bins of unequal sizes
plt.hist(flowers_df.sepal_width, bins=[1, 3, 4, 4.5]); 

Cómo gestionar múltiples Histogram a s e n MatPlotLib 

Similar a los gráficos de líneas, podemos dibujar varios histogramas en un solo gráfico. Podemos reducir la opacidad de cada histograma para que las barras de un histograma no oculten las de los demás.
Dibujemos histogramas separados para cada especie de flores.

setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']

plt.hist(setosa_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25));
plt.hist(versicolor_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25)); 

También podemos apilar varios histogramas uno encima del otro.

plt.title('Distribution of Sepal Width')

plt.hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width], 
bins=np.arange(2, 5, 0.25), 
stacked=True);

plt.legend(['Setosa', 'Versicolor', 'Virginica']); 

Gráficos de Barra en MatPlotLib 

Los gráficos de barras son bastante similares a los gráficos de líneas, es decir, muestran una secuencia de valores. Sin embargo, se muestra una barra para cada valor, en lugar de puntos conectados por líneas. Podemos usar la función plt.bar para graficarlos.

years = range(2000, 2006)
apples = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]

plt.bar(years, oranges); 

Al igual que en los histogramas; si queremos los resultados de las variables uno encima de otro (color anaranjado y azul). Usamos el argumento bottom de plt.bar para lograrlo.

plt.bar(years, apples)
plt.bar(years, oranges, bottom=apples); 

Gráficos de Barra con promedios en Seaborn 

Veamos otro conjunto de datos de muestra incluido con Seaborn llamado tips . El conjunto de datos contiene información sobre el sexo, la hora del día, la factura total y el monto de la propina para los clientes que visitan un restaurante durante una semana.

tips_df = sns.load_dataset("tips");

tips_df 

Es posible que deseemos dibujar un gráfico de barras para visualizar cómo varía el monto promedio de la factura en los diferentes días de la semana. Una forma de hacer esto sería calcular los promedios diarios y luego usar   plt.bar (puedes intentarlo como ejercicio).

Sin embargo, dado que este es un caso de uso muy común, la biblioteca Seaborn proporciona una función barplot que calcula los promedios automáticamente.

sns.barplot(x='day', y='total_bill', data=tips_df); 

Las líneas que cortan cada barra representan la cantidad de variación en los valores. Por ejemplo, parece que la variación en la factura total es relativamente alta los viernes y baja los sábados.

Podemos también especificar mediante el argumento hue a fin de realizar comparaciones con una tercera categoría, por ejemplo, por género.

sns.barplot(x='day', y='total_bill', hue='sex', data=tips_df); 

Puede hacer que las barras sean horizontales simplemente cambiando los ejes.

sns.barplot(x='total_bill', y='day', hue='sex', data=tips_df); 

Heatmaps e n Seaborn 

Un mapa de calor se usa para visualizar datos bidimensionales como una matriz o una tabla usando colores. La mejor manera de entenderlo es mirando un ejemplo.

Usaremos otro conjunto de datos de muestra de Seaborn, llamado flights , para visualizar el paso mensual de pasajeros en un aeropuerto durante 12 años.

flights_df = sns.load_dataset("flights").pivot("month", "year", "passengers")

flights_df 

flights_df es una matriz con una fila para cada mes y una columna para cada año. Los valores muestran el número de pasajeros (en miles) que visitaron el aeropuerto en un mes específico del año. Podemos usar la función sns.heatmap para visualizar esto.

plt.title("No. of Passengers (1000s)")
sns.heatmap(flights_df); 

Los colores más brillantes indican una pisada más alta en el aeropuerto. Mirando el gráfico, podemos inferir dos cosas:

1.La afluencia en el aeropuerto en un año determinado tiende a ser más alta alrededor de julio y agosto.
2.La afluencia en el aeropuerto en un mes determinado tiende a crecer año tras año.

También podemos mostrar los valores actuales especificando annot=True y usando el argumento cmap para cambiar el color.

plt.title("No. of Passengers (1000s)")
sns.heatmap(flights_df, fmt="d", annot=True, cmap='Blues'); 

Im á ge ne s in MatPlotLib 

También podemos usar Matplotlib para mostrar imágenes. Descarguemos una imagen de internet.

from urllib.request import urlretrieve

urlretrieve('https://i.imgur.com/SkPbq.jpg', 'chart.jpg'); 

Antes de mostrar una imagen, debe leerse en la memoria usando el módulo PIL .

from PIL import Image

img = Image.open('chart.jpg') 

Una imagen cargada con PIL es simplemente una matriz numpy tridimensional que contiene intensidades de píxeles para los canales rojo, verde y azul (RGB) de la imagen. Podemos convertir la imagen en una matriz usando np.array .

img_array = np.array(img)

img_array.shape
# (481, 640, 3) 

Por último, presentamos la imagen usando plt.imshow .

plt.imshow(img); 

Podemos desactivar los ejes y las líneas de cuadrícula y mostrar un título usando las funciones relevantes.

plt.grid(False)
plt.title('A data science meme')
plt.axis('off')
plt.imshow(img); 

Para mostrar una parte de la imagen, simplemente podemos seleccionar un segmento de la matriz numpy.

plt.grid(False)
plt.axis('off')
plt.imshow(img_array[125:325,105:305]); 

Cómo trazar gráficos múltiples en una cuadrícula en MatPlotLib y Seaborn

Matplotlib y Seaborn también admiten el trazado de múltiples gráficos en una cuadrícula, usando plt.subplots , que devuelve un conjunto de ejes para trazar.

Aquí hay una cuadrícula unificada que muestra los diferentes tipos de gráficos que hemos cubierto en este tutorial.

fig, axes = plt.subplots(2, 3, figsize=(16, 8))

# Use the axes for plotting
axes[0,0].plot(years, apples, 's-b')
axes[0,0].plot(years, oranges, 'o--r')
axes[0,0].set_xlabel('Year')
axes[0,0].set_ylabel('Yield (tons per hectare)')
axes[0,0].legend(['Apples', 'Oranges']);
axes[0,0].set_title('Crop Yields in Kanto')

# Pass the axes into seaborn
axes[0,1].set_title('Sepal Length vs. Sepal Width')
sns.scatterplot(x=flowers_df.sepal_length, 
y=flowers_df.sepal_width, 
hue=flowers_df.species, 
s=100, 
ax=axes[0,1]);

# Use the axes for plotting
axes[0,2].set_title('Distribution of Sepal Width')
axes[0,2].hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width], 
bins=np.arange(2, 5, 0.25), 
stacked=True);

axes[0,2].legend(['Setosa', 'Versicolor', 'Virginica']);

# Pass the axes into seaborn
axes[1,0].set_title('Restaurant bills')
sns.barplot(x='day', y='total_bill', hue='sex', data=tips_df, ax=axes[1,0]);

# Pass the axes into seaborn
axes[1,1].set_title('Flight traffic')
sns.heatmap(flights_df, cmap='Blues', ax=axes[1,1]);

# Plot an image using the axes
axes[1,2].set_title('Data Science Meme')
axes[1,2].imshow(img)
axes[1,2].grid(False)
axes[1,2].set_xticks([])
axes[1,2].set_yticks([])

plt.tight_layout(pad=2); 

Para saber más: https://matplotlib.org/3.3.1/api/axes_api.html#the-axes-class .

Gráficas por pares de características con Seaborn

Seaborn usa una función de ayuda sns.pairplot para representar múltiples gráficas por pares de características dentro de un DataFrame.

sns.pairplot(flowers_df, hue='species'); 
See the full output here . 
sns.pairplot(tips_df, hue='sex'); 

Resumen y lectura adicional

Hemos cubierto los siguientes temas en este tutorial:

Cómo crear y personalizar gráficos de líneas usando Matplotlib

Cómo visualizar relaciones entre dos o más variables usando diagramas de dispersión

Cómo estudiar distribuciones de variables utilizando histogramas y gráficos de barras

Cómo visualizar datos bidimensionales usando heatmaps

Cómo mostrar imágenes en Matplotlib mediante plt.imshow 

Cómo graficar múltiples gráficas en Matplotlib y Seaborn.

En este tutorial, cubrimos algunos de los conceptos fundamentales y técnicas populares para la visualización de datos usando Matplotlib y Seaborn. La visualización de datos es un campo muy amplio y apenas hemos arañado la superficie aquí. Consulta estas referencias para aprender y descubrir más:

Visualización de Datos: https://jovian.ml/aakashns/dataviz-cheatsheet 

Seaborn: https://seaborn.pydata.org/examples/index.html 

Matplotlib: https://matplotlib.org/3.1.1/gallery/index.html 

Matplotlib tutorial: https://github.com/rougier/matplotlib-tutorial 

Preguntas de revisión para verificar tu comprensión

Intente responder las siguientes preguntas para evaluar su comprensión de los temas tratados en este cuaderno.:

¿Qué es la visualización de datos?

¿Qué es Matplotlib?

¿Qué es Seaborn?

¿Cómo se instala Matplotlib y Seaborn?

¿Cómo importas Matplotlib y Seaborn? ¿Cuáles son los alias comunes que se utilizan al importar estos módulos?

¿Cuál es el propósito de %matplotlib inline ?

¿Qué es un gráfico de líneas?

¿Cómo se traza un gráfico de líneas en Python? Ilustre con un ejemplo.

¿Cómo se especifican los valores para el eje X de un gráfico de líneas?

¿Cómo se especifican las etiquetas para los ejes de un gráfico?

¿Cómo se trazan gráficos de líneas múltiples en los mismos ejes?

¿Cómo se muestra una leyenda para un gráfico de líneas con varias líneas

¿Cómo se establece un título para un gráfico?

¿Cómo se muestran los marcadores en un gráfico de líneas?

¿Cuáles son las diferentes opciones para diseñar líneas y marcadores en gráficos de líneas? Ilustrar con ejemplos.

¿Cuál es el propósito del argumento fmt para plt.plot ?

¿Donde puedes ver una lista de argumentos que se pueden utilizar en plt.plot ?

¿Cómo cambias el tamaño de una figura en Matplotlib?

¿Cómo aplica los estilos predeterminados de Seaborn globalmente para todos los gráficos?

¿Cuáles son los estilos predefinidos disponibles en Seaborn? Ilustrar con ejemplos.

¿Qué es un diagrama de dispersión?

¿En qué se diferencia un diagrama de dispersión de un gráfico de líneas?

¿Cómo dibujas un diagrama de dispersión usando Seaborn? Ilustre con un ejemplo.

¿Cómo decide cuándo usar un gráfico de dispersión frente a un gráfico de líneas?

¿Cómo se especifican los colores de los puntos en un diagrama de dispersión usando una variable categórica?

¿Cómo se personaliza el título, el tamaño de la figura, la leyenda y el hijo de las tramas de Seaborn?

¿Cómo usas sns.scatterplot en un DataFrame de Pandas?

¿Qué es un Histograma?

¿Cuándo debes usar un histograma vs un gráfico lineal?

¿Cómo se dibuja un histograma usando Matplotlib? Ilustre con un ejemplo.

¿Qué son los "contenedores" en un histograma?

¿Cómo se cambian los tamaños de los contenedores en un histograma?

¿Cómo se cambia el número de contenedores en un histograma?

¿Cómo se muestran varios histogramas en los mismos ejes?

¿Cómo se apilan varios histogramas uno encima del otro?

¿Qué es un gráfico de barras?

¿Cómo se dibuja un gráfico de barras usando Matplotlib? Ilustre con un ejemplo.

¿Cuál es la diferencia entre un gráfico de barras y un histograma?

¿Cuál es la diferencia entre un gráfico de barras y un gráfico de líneas?

¿Cómo se apilan las barras una encima de la otra?

¿Cuál es la diferencia entre plt.bar y sns.barplot ?

¿Qué representan las líneas en las barras de un gráfico de Seaborn?

¿Cómo se muestran gráficos de barras uno al lado del otro?

¿Cómo se dibuja un gráfico de barras horizontales?

¿Qué es un mapa de calor?

¿Qué tipo de datos se visualiza mejor con un mapa de calor?

¿Qué hace el método de pivote de un marco de datos de Pandas?

¿Cómo se dibuja un mapa de calor usando Seaborn? Ilustre con un ejemplo.

¿Cómo se cambia el esquema de color de un mapa de calor?

¿Cómo se muestran los valores originales del conjunto de datos en un mapa de calor?

¿Cómo se descargan imágenes de una URL en Python?

¿Cómo abres una imagen para procesarla en Python?

¿Cuál es el propósito del módulo PIL en Python?

¿Cómo convierte una imagen cargada usando PIL en una matriz Numpy?

¿Cuántas dimensiones tiene una matriz Numpy para una imagen? ¿Qué representa cada dimensión?

¿Qué son los "canales de color" en una imagen?

¿Qué es RGB?

¿Cómo se muestra una imagen usando Matplotlib?

¿Cómo se desactivan los ejes y las líneas de cuadrícula en un gráfico?

¿Cómo se muestra una parte de una imagen usando Matplotlib?

¿Cómo traza múltiples gráficos en una cuadrícula usando Matplotlib y Seaborn? Ilustrar con ejemplos.

¿Cuál es el propósito de la función plt.subplots ?

¿Qué son las parcelas de pares en Seaborn? Ilustra con un ejemplo.

¿Cómo se exporta un gráfico a un archivo de imagen PNG usando Matplotlib?

¿Dónde puede obtener información sobre los diferentes tipos de gráficos que puede crear con Matplotlib y Seaborn?

¡Felicitaciones por llegar al final de este tutorial! Ahora puedes aplicar estas habilidades para analizar conjuntos de datos del mundo real de fuentes como Kaggle .

Traductor: Andrés Torres

Leer más publicaciones .

Autor: freeCodeCamp.org (Inglés)

Learn to code. Build projects. Earn certifications—All for free.

Si este artículo fue de ayuda, compártelo .

Aprende a codificar de forma gratuita. El plan de estudios de código abierto de freeCodeCamp ha ayudado a más de 40,000 personas a obtener trabajos como desarrolladores. Empezar 

ANUNCIO
