# Pandas desde cero: tutorial completo

Fuente: [Jose R. Zapata (joserzapata.github.io)](https://joserzapata.github.io/courses/python-ciencia-datos/pandas/)  
_Copia local para lectura fuera de línea. El formato original puede verse en la URL._

---

PANDAS - Manipulación de Datos con Python

Por Jose R. Zapata 

Ultima actualizacion: 2/Noviembre/2024 - Pandas 2.2.2

Pandas es una herramienta de manipulación de datos de alto nivel desarrollada por Wes McKinney . En su inicio es construido sobre Numpy y ahora compatible con Arrow y permite el análisis de datos que cuenta con las estructuras de datos que necesitamos para limpiar los datos en bruto y que sean aptos para el análisis (por ejemplo, tablas). Pandas permite realizar tareas importantes, como alinear datos para su comparación, fusionar conjuntos de datos, gestión de datos perdidos, etc., se ha convertido en una librería muy importante para procesar datos a alto nivel en Python (es decir, estadísticas ). Pandas fue diseñada originalmente para gestionar datos financieros, y como alternativo al uso de hojas de cálculo (es decir, Microsoft Excel).

Los principales tipos de datos que pueden representarse con pandas son:

Datos tabulares con columnas de tipo heterogéneo con etiquetas en columnas y filas.

Series temporales

Pandas proporciona herramientas que permiten:

leer y escribir datos en diferentes formatos: CSV, JSON, Excel, bases SQL, parquet y HDF5 entre otros

seleccionar y filtrar de manera sencilla tablas de datos en función de posición, valor o etiquetas

fusionar y unir datos

transformar datos aplicando funciones tanto en global como por ventanas

manipulación de series temporales

hacer gráficas

En pandas existen 2 tipos básicos de objetos todos ellos basados a su vez en Numpy y ahora en Arrow:

Series (listas, 1D)

DataFrame (tablas, 2D)

Por lo tanto, Pandas nos proporciona las estructuras de datos y funciones necesarias para el análisis de datos.

Instalar Pandas

Pandas ya esta preinstalado si se usa Google Collaboratory, si va realizar una instalacion en su computador

PIP

pip install pandas 

Pandas con librerias para leer archivos de excel

pip install "pandas[excel]" 

Pandas para leer archivos de Arrow (Parquet)

pip install "pandas[pyarrow]" 

Para ver otras opciones ir al siguiente link otras instalaciones de pandas 

Importando Pandas

La libreria Pandas se importa de la siguiente manera

import numpy as np # Importación estándar de la librería NumPy 
import pandas as pd # Importación estándar de la librería Pandas 

pd . __version__ 

'2.2.2'

Series

Una serie es el primer tipo de datos de pandas y es muy similar a una matriz NumPy (de hecho está construida sobre el objeto de matriz NumPy). Lo que diferencia un arreglo NumPy de una serie, es que una serie puede tener etiquetas en los ejes, lo que significa que puede ser indexada por una etiqueta, en lugar de solo una ubicación numérica. Tampoco necesita contener datos numéricos, puede contener cualquier Objeto de Python arbitrario.

Creando una Serie

Puede convertir una lista, una matriz numpy o un diccionario en una serie, usando el método pd.Series:

# Crear diferentes tipos de datos 
labels = [ "a" , "b" , "c" ] # lista de etiquetas 
my_list = [ 10 , 20 , 30 ] # lista con valores 
arr = np . array ([ 10 , 20 , 30 ]) # Convertir lista de valores en arreglo NumPy 
d = { "a" : 10 , "b" : 20 , "c" : 30 } # Creación de un diccionario 

Desde Listas

# Convertir una lista en series usando el método pd.Series 
# observe que se crean los nombres con las posiciones de cada elemento 
pd . Series ( data = my_list ) 

0 10
1 20
2 30
dtype: int64

# Convertir una lista en series usando el método pd.Series 
# se puede ingresar el nombre de las posiciones 
pd . Series ( data = my_list , index = labels ) 

a 10
b 20
c 30
dtype: int64

# No es necesario ingresar la palabra de 'data ='' en el argumento 
pd . Series ( my_list , labels ) 

a 10
b 20
c 30
dtype: int64

Desde Arreglos NumPy

# Convertir un arreglo en series usando el método pd.Series 
pd . Series ( arr ) 

0 10
1 20
2 30
dtype: int64

# Convertir un arreglo en series indicando también los valores del index 
pd . Series ( arr , labels ) 

a 10
b 20
c 30
dtype: int64

Desde un Diccionario

# Convertir un diccionario en series usando el método pd.Series 
# Como el diccionario ya tiene clave entonces se le asigna como valor de la posición 
pd . Series ( d ) 

a 10
b 20
c 30
dtype: int64

Datos en una Series

Una serie de pandas puede contener una variedad de tipos de objetos:

# Creando una serie basado solo en una lista de letras 
pd . Series ( data = labels ) 

0 a
1 b
2 c
dtype: object

Indexacion

La clave para usar una serie es entender su índice. Pandas hace uso de estos nombres o números de índice al permitir búsquedas rápidas de información (funciona como una tabla hash o diccionario).

Veamos algunos ejemplos de cómo obtener información de una serie. Vamos a crear dos series, ser1 y ser2:

# Creación de una serie con sus labels o indices 
ser1 = pd . Series ([ 1 , 2 , 3 , 4 ], index = [ "USA" , "Alemania" , "Italia" , "Japon" ]) 

ser1 

USA 1
Alemania 2
Italia 3
Japon 4
dtype: int64

# Creación de una serie con sus labels o indices 
ser2 = pd . Series ([ 1 , 2 , 5 , 4 ], index = [ "USA" , "Alemania" , "Colombia" , "Japon" ]) 

ser2 

USA 1
Alemania 2
Colombia 5
Japon 4
dtype: int64

# La búsqueda en una serie es igual como en un diccionario 
ser1 [ "USA" ] 

1

# La búsqueda en una serie es igual como en un diccionario 
ser2 [ "Colombia" ] 

5

Las operaciones también se realizan según el índice:

# Observe los resultados de los países que solo están en una serie y no en las dos 
ser1 + ser2 

Alemania 4.0
Colombia NaN
Italia NaN
Japon 8.0
USA 2.0
dtype: float64

DataFrames

Los DataFrames son la estructura mas importante en pandas y están directamente inspirados en el lenguaje de programación R. Se puede pensar en un DataFrame como un conjunto de Series reunidas que comparten el mismo índice.
En los DataFrame tenemos la opción de especificar tanto el index (el nombre de las filas) como columns (el nombre de las columnas).

# Importar la función de NumPy para crear arreglos de números enteros 
from numpy.random import randn 

np . random . seed ( 101 ) # Inicializar el generador aleatorio 

# Forma rápida de crear una lista de python desde strings 
"A B C D E F" . split () 

['A', 'B', 'C', 'D', 'E', 'F']

# Crear un dataframe con números aleatorios de 4 Columnas y 5 Filas 
# Crear listas rápidamente usando la función split 'A B C D E'.split() 
# Esto evita tener que escribir repetidamente las comas 

df = pd . DataFrame ( randn ( 6 , 4 ), index = "A B C D E F" . split (), columns = "W X Y Z" . split ()) 

df 

W X Y Z 

A 2.706850 0.628133 0.907969 0.503826 

B 0.651118 -0.319318 -0.848077 0.605965 

C -2.018168 0.740122 0.528813 -0.589001 

D 0.188695 -0.758872 -0.933237 0.955057 

E 0.190794 1.978757 2.605967 0.683509 

F 0.302665 1.693723 -1.706086 -1.159119 

Descripcion general del dataframe

Numero de Filas y Columnas

df . shape # retorna un Tuple asi: (filas, col) 

(6, 4)

información General de los datos

# información general de los datos de cada columna 
# Indica el numero de filas del dataset 
# Muestra el numero de datos No Nulos por columna (valores validos) 
# Tipo de dato de cada columna 
# Tamaño total del dataset 
df . info () 

<class 'pandas.core.frame.DataFrame'>
Index: 6 entries, A to F
Data columns (total 4 columns):
# Column Non-Null Count Dtype
--- ------ -------------- -----
0 W 6 non-null float64
1 X 6 non-null float64
2 Y 6 non-null float64
3 Z 6 non-null float64
dtypes: float64(4)
memory usage: 240.0+ bytes

# Tipos de datos que existen en las columnas del dataframe 
df . dtypes 

W float64
X float64
Y float64
Z float64
dtype: object

Resumen de estadistica descriptiva General

el método .describe() de los dataframes presenta un resumen de la estadistica descriptiva general de las columnas numericas del dataframe, presenta la información de:

Promedio (mean)

Desviacion estandard (std)

Valor minimo

Valor maximo

Cuartiles (25%, 50% y 75%)

df . describe () # No muestra la información de las columnas categóricas 

W X Y Z 

count 6.000000 6.000000 6.000000 6.000000 

mean 0.336992 0.660424 0.092558 0.166706 

std 1.503744 1.075862 1.571280 0.839534 

min -2.018168 -0.758872 -1.706086 -1.159119 

25% 0.189220 -0.082455 -0.911947 -0.315794 

50% 0.246730 0.684127 -0.159632 0.554896 

75% 0.564005 1.455323 0.813180 0.664123 

max 2.706850 1.978757 2.605967 0.955057 

Ver Primeros elementos del dataframe

df . head () 

W X Y Z 

A 2.706850 0.628133 0.907969 0.503826 

B 0.651118 -0.319318 -0.848077 0.605965 

C -2.018168 0.740122 0.528813 -0.589001 

D 0.188695 -0.758872 -0.933237 0.955057 

E 0.190794 1.978757 2.605967 0.683509 

Ver Ultimos elementos del dataframe

df . tail () 

W X Y Z 

B 0.651118 -0.319318 -0.848077 0.605965 

C -2.018168 0.740122 0.528813 -0.589001 

D 0.188695 -0.758872 -0.933237 0.955057 

E 0.190794 1.978757 2.605967 0.683509 

F 0.302665 1.693723 -1.706086 -1.159119 

Ver elementos aleatorios del dataframe

df . sample ( 3 ) 

W X Y Z 

B 0.651118 -0.319318 -0.848077 0.605965 

D 0.188695 -0.758872 -0.933237 0.955057 

C -2.018168 0.740122 0.528813 -0.589001 

Seleccion y Indexacion

Existen diversos métodos para tomar datos de un DataFrame

# Regresara todos los datos de la columna W 
df [ "W" ] 

A 2.706850
B 0.651118
C -2.018168
D 0.188695
E 0.190794
F 0.302665
Name: W, dtype: float64

# Seleccionar dos o mas columnas 
# Pasar una lista con los nombres de las columnas 

df [[ "W" , "Z" ]] 

W Z 

A 2.706850 0.503826 

B 0.651118 0.605965 

C -2.018168 -0.589001 

D 0.188695 0.955057 

E 0.190794 0.683509 

F 0.302665 -1.159119 

# Seleccionar dos o mas columnas 
# Pasar una lista con los nombres de las columnas 
# Puedo indicar el orden de las columnas 

df [[ "X" , "W" , "Z" ]] 

X W Z 

A 0.628133 2.706850 0.503826 

B -0.319318 0.651118 0.605965 

C 0.740122 -2.018168 -0.589001 

D -0.758872 0.188695 0.955057 

E 1.978757 0.190794 0.683509 

F 1.693723 0.302665 -1.159119 

Las columnas de un DataFrame Columns son solo Series

type ( df [ "W" ]) # Tipos de datos 

pandas.core.series.Series

Creando una Nueva Columna

# Nueva columna igual a la suma de otras dos 
# operación vectorial 
df [ "new" ] = df [ "W" ] + df [ "Y" ] 
df 

W X Y Z new 

A 2.706850 0.628133 0.907969 0.503826 3.614819 

B 0.651118 -0.319318 -0.848077 0.605965 -0.196959 

C -2.018168 0.740122 0.528813 -0.589001 -1.489355 

D 0.188695 -0.758872 -0.933237 0.955057 -0.744542 

E 0.190794 1.978757 2.605967 0.683509 2.796762 

F 0.302665 1.693723 -1.706086 -1.159119 -1.403420 

Eliminando Columnas

df . drop ( "new" , axis = "columns" ) 

W X Y Z 

A 2.706850 0.628133 0.907969 0.503826 

B 0.651118 -0.319318 -0.848077 0.605965 

C -2.018168 0.740122 0.528813 -0.589001 

D 0.188695 -0.758872 -0.933237 0.955057 

E 0.190794 1.978757 2.605967 0.683509 

F 0.302665 1.693723 -1.706086 -1.159119 

# No se aplica a el dataframe a menos que se especifique. 
# Como se ve la operación pasada no quedo grabada 
df 

W X Y Z new 

A 2.706850 0.628133 0.907969 0.503826 3.614819 

B 0.651118 -0.319318 -0.848077 0.605965 -0.196959 

C -2.018168 0.740122 0.528813 -0.589001 -1.489355 

D 0.188695 -0.758872 -0.933237 0.955057 -0.744542 

E 0.190794 1.978757 2.605967 0.683509 2.796762 

F 0.302665 1.693723 -1.706086 -1.159119 -1.403420 

# Para que quede grabado se puede hacer de dos formas 
# df = df.drop('new',axis='columns') # Forma 1 

df . drop ( "new" , axis = "columns" , inplace = True ) # Forma 2 
df 

W X Y Z 

A 2.706850 0.628133 0.907969 0.503826 

B 0.651118 -0.319318 -0.848077 0.605965 

C -2.018168 0.740122 0.528813 -0.589001 

D 0.188695 -0.758872 -0.933237 0.955057 

E 0.190794 1.978757 2.605967 0.683509 

F 0.302665 1.693723 -1.706086 -1.159119 

df 

W X Y Z 

A 2.706850 0.628133 0.907969 0.503826 

B 0.651118 -0.319318 -0.848077 0.605965 

C -2.018168 0.740122 0.528813 -0.589001 

D 0.188695 -0.758872 -0.933237 0.955057 

E 0.190794 1.978757 2.605967 0.683509 

F 0.302665 1.693723 -1.706086 -1.159119 

También se puede sacar filas de esta manera:

df . drop ( "E" , axis = "index" ) 

W X Y Z 

A 2.706850 0.628133 0.907969 0.503826 

B 0.651118 -0.319318 -0.848077 0.605965 

C -2.018168 0.740122 0.528813 -0.589001 

D 0.188695 -0.758872 -0.933237 0.955057 

F 0.302665 1.693723 -1.706086 -1.159119 

df 

W X Y Z 

A 2.706850 0.628133 0.907969 0.503826 

B 0.651118 -0.319318 -0.848077 0.605965 

C -2.018168 0.740122 0.528813 -0.589001 

D 0.188695 -0.758872 -0.933237 0.955057 

E 0.190794 1.978757 2.605967 0.683509 

F 0.302665 1.693723 -1.706086 -1.159119 

# Otra manera de borrar las columnas es 
del df [ "X" ] # Esta función es INPLACE 
df 

W Y Z 

A 2.706850 0.907969 0.503826 

B 0.651118 -0.848077 0.605965 

C -2.018168 0.528813 -0.589001 

D 0.188695 -0.933237 0.955057 

E 0.190794 2.605967 0.683509 

F 0.302665 -1.706086 -1.159119 

Obtener los nombres de las columnas y los indices (index):

df . columns # nombres de las columnas 

Index(['W', 'Y', 'Z'], dtype='object')

df . index # nombres de los indices 

Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')

Seleccionando Filas y Columnas

las dos formas de seleccion principal son:

DataFrame.loc[etiqueta_fila, etiqueta_columna] <- por etiquetas

DataFrame.iloc[indice_fila, indice_columna] <- por indices

# la función loc busca por medio de los nombres de los indices y columnas 
df . loc [ "A" ] # se selecciona todos los valores de la fila 'A' 

W 2.706850
Y 0.907969
Z 0.503826
Name: A, dtype: float64

O basado en la posición (index) en vez de usar la etiqueta

df . iloc [ 2 ] # Se seleccionan los valores de la fila con indice 2 
# recordar que los index empiezan en cero 

W -2.018168
Y 0.528813
Z -0.589001
Name: C, dtype: float64

Seleccionar un subconjunto de filas y columnas

# Mediante etiquetas 
# se selecciona el elemento que esta en la fila=B Col=Y 
df . loc [ "B" , "Y" ] # con etiquetas 

-0.8480769834036315

# Mediante etiquetas 
# se selecciona un subconjunto de datos que están entre 
# filas = A, B Cols= W, Y 
df . loc [[ "A" , "B" ], [ "W" , "Y" ]] 

W Y 

A 2.706850 0.907969 

B 0.651118 -0.848077 

df . loc [[ "B" , "A" ], [ "Y" , "W" ]] 

Y W 

B -0.848077 0.651118 

A 0.907969 2.706850 

Seleccion Condicional o Filtros

Una característica importante de pandas es la selección condicional usando la notación de corchetes, muy similar a NumPy:

df 

W Y Z 

A 2.706850 0.907969 0.503826 

B 0.651118 -0.848077 0.605965 

C -2.018168 0.528813 -0.589001 

D 0.188695 -0.933237 0.955057 

E 0.190794 2.605967 0.683509 

F 0.302665 -1.706086 -1.159119 

# Devuelve una serie con booleans 
# según si se cumple o no la condición 
df [ "W" ] > 0 

A True
B True
C False
D True
E True
F True
Name: W, dtype: bool

# seleccionar todas las filas del dataframe donde el valor 
# que esta en la columna 'W' sea mayor que cero 
df [ df [ "W" ] > 0 ] 

W Y Z 

A 2.706850 0.907969 0.503826 

B 0.651118 -0.848077 0.605965 

D 0.188695 -0.933237 0.955057 

E 0.190794 2.605967 0.683509 

F 0.302665 -1.706086 -1.159119 

# Seleccionar las filas donde 'W' sea mayor que cero 
# y de esas filas escoger los valores de la columna 'Y' 
df [ df [ "W" ] > 0 ][ "Y" ] 

A 0.907969
B -0.848077
D -0.933237
E 2.605967
F -1.706086
Name: Y, dtype: float64

# Seleccionar las filas donde 'W' sea mayor que cero 
# y de esas filas escoger los valores de las columna 'Y' y 'X' 
df [ df [ "W" ] > 0 ][[ "Y" , "Z" ]] 

Y Z 

A 0.907969 0.503826 

B -0.848077 0.605965 

D -0.933237 0.955057 

E 2.605967 0.683509 

F -1.706086 -1.159119 

Para dos condiciones, se usa los booleanos de esta forma

| en vez de or 

& en vez de and 

~ en vez de not 

Por amor a Dios, recuerde usar paréntesis:

# Seleccionar las filas donde 'W' sea mayor que cero 
# y también donde 'Y' sea mayor que 0.5 
limite_x = 0 
limite_y = 0.5 
df [( df [ "W" ] > limite_x ) & ( df [ "Y" ] > limite_y )] 

W Y Z 

A 2.706850 0.907969 0.503826 

E 0.190794 2.605967 0.683509 

.query() Busqueda condicional

Los terminos de busqueda condicional o filtros se entregan al método como tipo ‘string’

df 

W Y Z 

A 2.706850 0.907969 0.503826 

B 0.651118 -0.848077 0.605965 

C -2.018168 0.528813 -0.589001 

D 0.188695 -0.933237 0.955057 

E 0.190794 2.605967 0.683509 

F 0.302665 -1.706086 -1.159119 

# seleccionar todas las filas donde el valor 
# que esta en la columna 'W' sea mayor que cero 

# df[df['W']>0] 
df . query ( "W>0" ) 

W Y Z 

A 2.706850 0.907969 0.503826 

B 0.651118 -0.848077 0.605965 

D 0.188695 -0.933237 0.955057 

E 0.190794 2.605967 0.683509 

F 0.302665 -1.706086 -1.159119 

# Seleccionar las filas donde 'W' sea mayor que cero 
# y de esas filas escoger los valores de la columna 'Y' 

# df[df['W']>0]['Y'] 
df . query ( "W>0" )[ "Y" ] 

A 0.907969
B -0.848077
D -0.933237
E 2.605967
F -1.706086
Name: Y, dtype: float64

# Seleccionar las filas donde 'W' sea mayor que cero 
# y de esas filas escoger los valores de las columna 'Y' y 'X' 

# df[df['W']>0][['Y','Z']] 
df . query ( "W>0" )[[ "Y" , "Z" ]] 

Y Z 

A 0.907969 0.503826 

B -0.848077 0.605965 

D -0.933237 0.955057 

E 2.605967 0.683509 

F -1.706086 -1.159119 

Para dos condiciones, puede usar | = or y & = and con paréntesis:

# Seleccionar las filas donde 'W' sea mayor que cero 
# y también donde 'Y' sea mayor que 0.5 

# df[(df['W']>0) & (df['Y'] > 0.5)] 
df . query ( "W>0 and Y>0.5" ) 

W Y Z 

A 2.706850 0.907969 0.503826 

E 0.190794 2.605967 0.683509 

Cambio de columna de Indexacion

Analicemos algunas características más de la indexación, incluido el restablecimiento del índice o el establecimiento de parámetros.

df 

W Y Z 

A 2.706850 0.907969 0.503826 

B 0.651118 -0.848077 0.605965 

C -2.018168 0.528813 -0.589001 

D 0.188695 -0.933237 0.955057 

E 0.190794 2.605967 0.683509 

F 0.302665 -1.706086 -1.159119 

Se puede reiniciar el indice con numeros consecutivos

df . reset_index () # reset el indice 

# el index anterior se convierte en una columna 

index W Y Z 

0 A 2.706850 0.907969 0.503826 

1 B 0.651118 -0.848077 0.605965 

2 C -2.018168 0.528813 -0.589001 

3 D 0.188695 -0.933237 0.955057 

4 E 0.190794 2.605967 0.683509 

5 F 0.302665 -1.706086 -1.159119 

Se puede Redefinir el indice con los valores de otra columna

# Es importante tener valores que no sean duplicados 
df [ "States" ] = [ "CA" , "NY" , "WY" , "OR" , "CO" , "FL" ] 
df 

W Y Z States 

A 2.706850 0.907969 0.503826 CA 

B 0.651118 -0.848077 0.605965 NY 

C -2.018168 0.528813 -0.589001 WY 

D 0.188695 -0.933237 0.955057 OR 

E 0.190794 2.605967 0.683509 CO 

F 0.302665 -1.706086 -1.159119 FL 

# Redefinir la columna states como el indice 
df = df . set_index ( "States" , drop = True ) 
df 

W Y Z 

States 

CA 2.706850 0.907969 0.503826 

NY 0.651118 -0.848077 0.605965 

WY -2.018168 0.528813 -0.589001 

OR 0.188695 -0.933237 0.955057 

CO 0.190794 2.605967 0.683509 

FL 0.302665 -1.706086 -1.159119 

Groupby (Agrupacion por filas)

El método groupby le permite agrupar filas de datos y llamar a funciones agregadas

# Crear dataframe desde un diccionario 
data = { 
"Company" : [ "GOOG" , "GOOG" , "MSFT" , "MSFT" , "FB" , "FB" , "GOOG" , "MSFT" , "FB" ], 
"Person" : [ 
"Sam" , 
"Charlie" , 
"Amy" , 
"Vanessa" , 
"Carl" , 
"Sarah" , 
"John" , 
"Randy" , 
"David" , 
], 
"Sales" : [ 200 , 120 , 340 , 124 , 243 , 350 , 275 , 400 , 180 ], 
} 
# conversion del diccionario a dataframe 
df = pd . DataFrame ( data ) 
df 

Company Person Sales 

0 GOOG Sam 200 

1 GOOG Charlie 120 

2 MSFT Amy 340 

3 MSFT Vanessa 124 

4 FB Carl 243 

5 FB Sarah 350 

6 GOOG John 275 

7 MSFT Randy 400 

8 FB David 180 

Se puede usar el método .groupby() para agrupar filas en función de un nombre de columna. Por ejemplo, vamos a agruparnos a partir de la Compañía. Esto creará un objeto DataFrameGroupBy : 

# agrupar por Company 
df . groupby ( "Company" ) 

<pandas.core.groupby.generic.DataFrameGroupBy object at 0x724ca5feb6d0>

utilizar los métodos agregados del objeto:

# agrupar por compañía y calcular el promedio por cada una 
df . groupby ( "Company" ) . mean ( numeric_only = True ) 

Sales 

Company 

FB 257.666667 

GOOG 198.333333 

MSFT 288.000000 

Más ejemplos de métodos agregados:

# agrupar por compañía y calcular la desviación estándar 
df . groupby ( "Company" ) . std ( numeric_only = True ) 

Sales 

Company 

FB 85.943780 

GOOG 77.513440 

MSFT 145.161978 

# agrupar por compañía y calcular el mínimo 
df . groupby ( "Company" ) . min () 

Person Sales 

Company 

FB Carl 180 

GOOG Charlie 120 

MSFT Amy 124 

# agrupar por compañía y calcular el máximo 
df . groupby ( "Company" ) . max () 

Person Sales 

Company 

FB Sarah 350 

GOOG Sam 275 

MSFT Vanessa 400 

# agrupar por compañía y sumar los elementos que hay excluyendo los NaN 
df . groupby ( "Company" ) . count () 

Person Sales 

Company 

FB 3 3 

GOOG 3 3 

MSFT 3 3 

# Una de las funciones mas usadas para descripción estadística de un dataframe 
# Genera estadísticas descriptivas que resumen la tendencia central, 
# la dispersión y la forma de la distribución de un conjunto de datos, 
# excluyendo los valores `` NaN``. 
# by_comp.describe(include = 'all') # incluir todo 
df . groupby ( "Company" ) . describe () 

Sales 

count mean std min 25% 50% 75% max 

Company 

FB 3.0 257.666667 85.943780 180.0 211.5 243.0 296.5 350.0 

GOOG 3.0 198.333333 77.513440 120.0 160.0 200.0 237.5 275.0 

MSFT 3.0 288.000000 145.161978 124.0 232.0 340.0 370.0 400.0 

# Una de las funciones mas usadas para descripción estadística de un dataframe 
# Genera estadísticas descriptivas que resumen la tendencia central, la dispersión 
# y la forma de la distribución de un conjunto de datos, 
# excluyendo los valores `` NaN``. 

# Transponer la descripción 
df . groupby ( "Company" ) . describe () . transpose () 

Company FB GOOG MSFT 

Sales count 3.000000 3.000000 3.000000 

mean 257.666667 198.333333 288.000000 

std 85.943780 77.513440 145.161978 

min 180.000000 120.000000 124.000000 

25% 211.500000 160.000000 232.000000 

50% 243.000000 200.000000 340.000000 

75% 296.500000 237.500000 370.000000 

max 350.000000 275.000000 400.000000 

# Descripción estadística de los datos de la compañía GOOG 
df . groupby ( "Company" ) . describe () . transpose ()[ "GOOG" ] 

Sales count 3.000000
mean 198.333333
std 77.513440
min 120.000000
25% 160.000000
50% 200.000000
75% 237.500000
max 275.000000
Name: GOOG, dtype: float64

Pivot Tables

La funciónlidad “Pivot_table” es muy utilizada y popular en las conocidas “hojas de cálculo” tipo, OpenOffice, LibreOffice, Excel, Lotus, etc. Esta funcionalidad nos permite agrupar, ordenar, calcular datos y manejar datos de una forma muy similar a la que se hace con las hojas de cálculo.
mas informacion 

La principal función del “Pivot_table” son las agrupaciones de datos a las que se les suelen aplicar funciones matemáticas como sumatorios, promedios, etc

import seaborn as sns # importar la librería seaborn 

# cargar dataset del titanic 
titanic = sns . load_dataset ( "titanic" ) 
titanic . head () 

survived pclass sex age sibsp parch fare embarked class who adult_male deck embark_town alive alone 

0 0 3 male 22.0 1 0 7.2500 S Third man True NaN Southampton no False 

1 1 1 female 38.0 1 0 71.2833 C First woman False C Cherbourg yes False 

2 1 3 female 26.0 0 0 7.9250 S Third woman False NaN Southampton yes True 

3 1 1 female 35.0 1 0 53.1000 S First woman False C Southampton yes False 

4 0 3 male 35.0 0 0 8.0500 S Third man True NaN Southampton no True 

Haciendo el Pivot table a mano para obtener el promedio de personas que sobrevivieron por genero

# 1. Agrupar por genero 
# 2. Obtener los sobrevivientes 
# 3. Calcular el promedio 
titanic . groupby ( "sex" )[[ "survived" ]] . mean () 

survived 

sex 

female 0.742038 

male 0.188908 

promedio de cuantos sobrevivieron por genero divididos por clase

# 1. Agrupar por genero y clase 
# 2. Obtener los sobrevivientes 
# 3. Calcular el promedio 
# 4. Poner el resultado como una tabla (.unstack) 
titanic . groupby ([ "sex" , "class" ], observed = True )[ "survived" ] . mean () . unstack () 

class First Second Third 

sex 

female 0.968085 0.921053 0.500000 

male 0.368852 0.157407 0.135447 

Usando Pivot tables

titanic . pivot_table ( "survived" , index = "sex" , columns = "class" , observed = True ) 

class First Second Third 

sex 

female 0.968085 0.921053 0.500000 

male 0.368852 0.157407 0.135447 

titanic . pivot_table ( 
"survived" , index = "sex" , columns = "class" , margins = True , observed = True 
) 

class First Second Third All 

sex 

female 0.968085 0.921053 0.500000 0.742038 

male 0.368852 0.157407 0.135447 0.188908 

All 0.629630 0.472826 0.242363 0.383838 

Concatenar, Fusionar (Concatenating y Merging)

Las formas principales de combinar DataFrames: concatenar y fusionar

df1 = pd . DataFrame ( 
{ 
"A" : [ "A0" , "A1" , "A2" , "A3" ], 
"B" : [ "B0" , "B1" , "B2" , "B3" ], 
"C" : [ "C0" , "C1" , "C2" , "C3" ], 
"D" : [ "D0" , "D1" , "D2" , "D3" ], 
}, 
index = [ 0 , 1 , 2 , 3 ], 
) 

df2 = pd . DataFrame ( 
{ 
"A" : [ "A4" , "A5" , "A6" , "A7" ], 
"B" : [ "B4" , "B5" , "B6" , "B7" ], 
"C" : [ "C4" , "C5" , "C6" , "C7" ], 
"D" : [ "D4" , "D5" , "D6" , "D7" ], 
}, 
index = [ 4 , 5 , 6 , 7 ], 
) 

df3 = pd . DataFrame ( 
{ 
"A" : [ "A8" , "A9" , "A10" , "A11" ], 
"B" : [ "B8" , "B9" , "B10" , "B11" ], 
"C" : [ "C8" , "C9" , "C10" , "C11" ], 
"D" : [ "D8" , "D9" , "D10" , "D11" ], 
}, 
index = [ 8 , 9 , 10 , 11 ], 
) 

df1 

A B C D 

0 A0 B0 C0 D0 

1 A1 B1 C1 D1 

2 A2 B2 C2 D2 

3 A3 B3 C3 D3 

df2 

A B C D 

4 A4 B4 C4 D4 

5 A5 B5 C5 D5 

6 A6 B6 C6 D6 

7 A7 B7 C7 D7 

df3 

A B C D 

8 A8 B8 C8 D8 

9 A9 B9 C9 D9 

10 A10 B10 C10 D10 

11 A11 B11 C11 D11 

Concatenación (Concatenation)

La concatenación básicamente combina DataFrames. Tenga en cuenta que las dimensiones deben coincidir a lo largo del eje con el que se está concatenando.

la Concatenación se hace con dataframes de diferentes indices

Puede usar .concat() y pasar una lista de DataFrames para concatenar juntos:

# Concatenar cada dataframe verticalmente, 
# ya que coinciden los nombres de las columnas 

pd . concat ([ df1 , df2 , df3 ], axis = "index" ) 

A B C D 

0 A0 B0 C0 D0 

1 A1 B1 C1 D1 

2 A2 B2 C2 D2 

3 A3 B3 C3 D3 

4 A4 B4 C4 D4 

5 A5 B5 C5 D5 

6 A6 B6 C6 D6 

7 A7 B7 C7 D7 

8 A8 B8 C8 D8 

9 A9 B9 C9 D9 

10 A10 B10 C10 D10 

11 A11 B11 C11 D11 

# concatenar dataframe horizontalmente, 
# como no coinciden los index observar lo que ocurre 

pd . concat ([ df1 , df2 , df3 ], axis = "columns" ) 

A B C D A B C D A B C D 

0 A0 B0 C0 D0 NaN NaN NaN NaN NaN NaN NaN NaN 

1 A1 B1 C1 D1 NaN NaN NaN NaN NaN NaN NaN NaN 

2 A2 B2 C2 D2 NaN NaN NaN NaN NaN NaN NaN NaN 

3 A3 B3 C3 D3 NaN NaN NaN NaN NaN NaN NaN NaN 

4 NaN NaN NaN NaN A4 B4 C4 D4 NaN NaN NaN NaN 

5 NaN NaN NaN NaN A5 B5 C5 D5 NaN NaN NaN NaN 

6 NaN NaN NaN NaN A6 B6 C6 D6 NaN NaN NaN NaN 

7 NaN NaN NaN NaN A7 B7 C7 D7 NaN NaN NaN NaN 

8 NaN NaN NaN NaN NaN NaN NaN NaN A8 B8 C8 D8 

9 NaN NaN NaN NaN NaN NaN NaN NaN A9 B9 C9 D9 

10 NaN NaN NaN NaN NaN NaN NaN NaN A10 B10 C10 D10 

11 NaN NaN NaN NaN NaN NaN NaN NaN A11 B11 C11 D11 

Fusion (Merging)

La función merge() le permite fusionar DataFrames juntos utilizando una lógica similar a la combinación de Tablas SQL. Por ejemplo:

# DataFrames de ejemplo para merging 
left = pd . DataFrame ( 
{ 
"Producto" : [ "Arepas" , "Banano" , "Cafe" ], 
"Tienda" : [ 1 , 2 , 1 ], 
"Ventas" : [ 100 , 200 , 50 ], 
} 
) 

right = pd . DataFrame ( 
{ 
"Producto" : [ "Arepas" , "Banano" , "Cafe" ], 
"Tienda" : [ 1 , 2 , 1 ], 
"Inventario" : [ 50 , 100 , 75 ], 
} 
) 

left 

Producto Tienda Ventas 

0 Arepas 1 100 

1 Banano 2 200 

2 Cafe 1 50 

right 

Producto Tienda Inventario 

0 Arepas 1 50 

1 Banano 2 100 

2 Cafe 1 75 

# how='inner' utilice la intersección de las claves de ambos marcos, 
# similar a una combinación interna de SQL; las keys son comunes 

pd . merge ( left , right , how = "inner" , on = "Producto" ) 

Producto Tienda_x Ventas Tienda_y Inventario 

0 Arepas 1 100 1 50 

1 Banano 2 200 2 100 

2 Cafe 1 50 1 75 

Un ejemplo mas complicado:

Natural join: para mantener solo las filas que coinciden con los marcos de datos, especifique el argumento how = ‘inner’.

Full outer join: para mantener todas las filas de ambos dataframe, especifique how = ‘OUTER’.

Left outer join: para incluir todas las filas de su dataframe x y solo aquellas de y que coincidan, especifique how=‘left’.

Right outer join: para incluir todas las filas de su dataframe y y solo aquellas de x que coincidan, especifique how=‘right’.

left = pd . DataFrame ( 
{ 
"Producto" : [ "Arepas" , "Leche" , "Cafe" ], 
"Tienda" : [ 1 , 2 , 1 ], 
"Ventas" : [ 100 , 200 , 50 ], 
} 
) 

right = pd . DataFrame ( 
{ 
"Producto" : [ "Arepas" , "Banano" , "Cafe" ], 
"Tienda" : [ 1 , 2 , 1 ], 
"Inventario" : [ 50 , 100 , 75 ], 
} 
) 

left 

Producto Tienda Ventas 

0 Arepas 1 100 

1 Leche 2 200 

2 Cafe 1 50 

right 

Producto Tienda Inventario 

0 Arepas 1 50 

1 Banano 2 100 

2 Cafe 1 75 

# fusionando comparando las mismas claves que tengan comunes 
pd . merge ( left , right , on = [ "Producto" ]) 

Producto Tienda_x Ventas Tienda_y Inventario 

0 Arepas 1 100 1 50 

1 Cafe 1 50 1 75 

# fusionando totalmente las dos tablas con las claves 
pd . merge ( left , right , how = "outer" , on = [ "Producto" ]) 

Producto Tienda_x Ventas Tienda_y Inventario 

0 Arepas 1.0 100.0 1.0 50.0 

1 Banano NaN NaN 2.0 100.0 

2 Cafe 1.0 50.0 1.0 75.0 

3 Leche 2.0 200.0 NaN NaN 

# fusionando usando las claves de la tabla right 
pd . merge ( left , right , how = "right" , on = [ "Producto" ]) 

Producto Tienda_x Ventas Tienda_y Inventario 

0 Arepas 1.0 100.0 1 50 

1 Banano NaN NaN 2 100 

2 Cafe 1.0 50.0 1 75 

# fusionando usando las claves de la tabla left 
pd . merge ( left , right , how = "left" , on = [ "Producto" ]) 

Producto Tienda_x Ventas Tienda_y Inventario 

0 Arepas 1 100 1.0 50.0 

1 Leche 2 200 NaN NaN 

2 Cafe 1 50 1.0 75.0 

Datos Categoricos

La busqueda en datos categoricos es mucho mas rapida

Ocupan Menos memoria que si los datos estan como string

Se pueden tener datos categoricos Ordinales

Mas información de datos categoricos:

https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html 

Creacion

# Creación de una serie de datos categóricos 
cate = pd . Series ([ "manzana" , "banano" , "corozo" , "manzana" , "pera" ], dtype = "category" ) 
cate 

0 manzana
1 banano
2 corozo
3 manzana
4 pera
dtype: category
Categories (4, object): ['banano', 'corozo', 'manzana', 'pera']

cate . dtypes 

CategoricalDtype(categories=['banano', 'corozo', 'manzana', 'pera'], ordered=False, categories_dtype=object)

cate . describe () 

count 5
unique 4
top manzana
freq 2
dtype: object

# Creando primero los datos y luego convirtiéndolos en categóricos 
df_cate = pd . DataFrame ({ "Fruta" : [ "manzana" , "banano" , "corozo" , "manzana" , "pera" ]}) 
df_cate 

Fruta 

0 manzana 

1 banano 

2 corozo 

3 manzana 

4 pera 

# Observar los tipos de datos en el data frame 
df_cate . dtypes 

Fruta object
dtype: object

df_cate [ "Fruta2" ] = df_cate [ "Fruta" ] . astype ( "category" ) 
df_cate 

Fruta Fruta2 

0 manzana manzana 

1 banano banano 

2 corozo corozo 

3 manzana manzana 

4 pera pera 

# Observar los tipos de datos en el dataframe 
df_cate . dtypes 

Fruta object
Fruta2 category
dtype: object

# Crear los datos categóricos desde a declaración de los datos 
df_cate = pd . DataFrame ({ "A" : list ( "abca" ), "B" : list ( "bccd" )}, dtype = "category" ) 
df_cate 

A B 

0 a b 

1 b c 

2 c c 

3 a d 

df_cate . dtypes 

A category
B category
dtype: object

df_cate . describe () 

A B 

count 4 4 

unique 3 3 

top a c 

freq 2 2 

Categoricos Ordinales

# creación de dataframe con datos 
df_cate = pd . DataFrame ({ "A" : list ( "abca" ), "B" : list ( "bccd" )}) 
df_cate 

A B 

0 a b 

1 b c 

2 c c 

3 a d 

df_cate . dtypes 

A object
B object
dtype: object

# definición de los tipos de datos y que están en orden 
df_cate [ "A" ] = pd . Categorical ( 
df_cate [ "A" ], categories = [ "a" , "b" , "c" , "d" ], ordered = True 
) 
df_cate 

A B 

0 a b 

1 b c 

2 c c 

3 a d 

df_cate [ "A" ] 

0 a
1 b
2 c
3 a
Name: A, dtype: category
Categories (4, object): ['a' < 'b' < 'c' < 'd']

# Los datos no tienen que ser strings para que sean categóricos 
s = pd . Series ([ 1 , 2 , 3 , 1 ], dtype = "category" ) 
s 

0 1
1 2
2 3
3 1
dtype: category
Categories (3, int64): [1, 2, 3]

s = s . cat . set_categories ([ 2 , 3 , 1 ], ordered = True ) 
s 

0 1
1 2
2 3
3 1
dtype: category
Categories (3, int64): [2 < 3 < 1]

Correcion de tipos de datos (Casting)

Cuando se trabaja con datos, es posible que se encuentre con un DataFrame donde el tipo de datos de una columna no es la correcta. los tipos de datos son principalmente: numericos, categoricos nominales, categoricos ordinales, booleanos, fechas y tiempos, texto .

Se debe convertir los tipos de datos para que sean apropiados para el tipo de datos que representan. Por ejemplo, es posible que desee convertir una columna de strings que representan números en números enteros o flotantes. O puede tener una columna de números que representan fechas, pero que pandas no reconoce como fechas.

Nota: al convertir los datos a su forma correcta, normalmente hace que los DataFrames sean mucho más pequeños en la memoria, lo que los hace más eficientes de usar.

import seaborn as sns # importar la librería seaborn 

titanic = sns . load_dataset ( "titanic" ) 
titanic . info () 

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 15 columns):
# Column Non-Null Count Dtype
--- ------ -------------- -----
0 survived 891 non-null int64
1 pclass 891 non-null int64
2 sex 891 non-null object
3 age 714 non-null float64
4 sibsp 891 non-null int64
5 parch 891 non-null int64
6 fare 891 non-null float64
7 embarked 889 non-null object
8 class 891 non-null category
9 who 891 non-null object
10 adult_male 891 non-null bool
11 deck 203 non-null category
12 embark_town 889 non-null object
13 alive 891 non-null object
14 alone 891 non-null bool
dtypes: bool(2), category(2), float64(2), int64(4), object(5)
memory usage: 80.7+ KB

titanic . sample ( 5 ) 

survived pclass sex age sibsp parch fare embarked class who adult_male deck embark_town alive alone 

139 0 1 male 24.0 0 0 79.2000 C First man True B Cherbourg no True 

548 0 3 male 33.0 1 1 20.5250 S Third man True NaN Southampton no False 

32 1 3 female NaN 0 0 7.7500 Q Third woman False NaN Queenstown yes True 

36 1 3 male NaN 0 0 7.2292 C Third man True NaN Cherbourg yes True 

724 1 1 male 27.0 1 0 53.1000 S First man True E Southampton yes False 

Casting variables Categoricas nominales

# convertir la columna sex, embarked, who, embark_town en categóricas 
cols_categoricas_nom = [ "sex" , "embarked" , "who" , "embark_town" ] 

# ver los datos únicos de las columnas_categoricas_nom 
for columna in cols_categoricas_nom : 
print ( f "Valores únicos en { columna } : { titanic [ columna ] . unique () } " ) 

Valores únicos en sex: ['male' 'female']
Valores únicos en embarked: ['S' 'C' 'Q' nan]
Valores únicos en who: ['man' 'woman' 'child']
Valores únicos en embark_town: ['Southampton' 'Cherbourg' 'Queenstown' nan]

titanic [ cols_categoricas_nom ] = titanic [ cols_categoricas_nom ] . astype ( "category" ) 

# ver los datos únicos de las columnas_categoricas_nom 
for columna in cols_categoricas_nom : 
print ( f "Valores únicos en { columna } : { titanic [ columna ] . unique () } " ) 

Valores únicos en sex: ['male', 'female']
Categories (2, object): ['female', 'male']
Valores únicos en embarked: ['S', 'C', 'Q', NaN]
Categories (3, object): ['C', 'Q', 'S']
Valores únicos en who: ['man', 'woman', 'child']
Categories (3, object): ['child', 'man', 'woman']
Valores únicos en embark_town: ['Southampton', 'Cherbourg', 'Queenstown', NaN]
Categories (3, object): ['Cherbourg', 'Queenstown', 'Southampton']

Casting variables Categoricas Ordinales

cols_categoricas_ord = [ "pclass" , "deck" ] 

for columna in cols_categoricas_ord : 
print ( f "Valores únicos en { columna } : { titanic [ columna ] . unique () } " ) 

Valores únicos en pclass: [3 1 2]
Valores únicos en deck: [NaN, 'C', 'E', 'G', 'D', 'A', 'B', 'F']
Categories (7, object): ['A', 'B', 'C', 'D', 'E', 'F', 'G']

titanic [ "pclass" ] = pd . Categorical ( 
titanic [ "pclass" ], categories = [ 3 , 2 , 1 ], ordered = True 
) 
titanic [ "deck" ] = pd . Categorical ( 
titanic [ "deck" ], categories = list ( "ABCDEFG" ), ordered = True 
) 

for columna in cols_categoricas_ord : 
print ( f "Valores únicos en { columna } : { titanic [ columna ] . unique () } " ) 

Valores únicos en pclass: [3, 1, 2]
Categories (3, int64): [3 < 2 < 1]
Valores únicos en deck: [NaN, 'C', 'E', 'G', 'D', 'A', 'B', 'F']
Categories (7, object): ['A' < 'B' < 'C' < 'D' < 'E' < 'F' < 'G']

Casting variables booleanas

columnas_bool = [ "alive" , "alone" , "survived" ] 

titanic [ columnas_bool ] = titanic [ columnas_bool ] . astype ( "bool" ) 

Resulado Casting

titanic . info () 

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 15 columns):
# Column Non-Null Count Dtype
--- ------ -------------- -----
0 survived 891 non-null bool
1 pclass 891 non-null category
2 sex 891 non-null category
3 age 714 non-null float64
4 sibsp 891 non-null int64
5 parch 891 non-null int64
6 fare 891 non-null float64
7 embarked 889 non-null category
8 class 891 non-null category
9 who 891 non-null category
10 adult_male 891 non-null bool
11 deck 203 non-null category
12 embark_town 889 non-null category
13 alive 891 non-null bool
14 alone 891 non-null bool
dtypes: bool(4), category(7), float64(2), int64(2)
memory usage: 38.7 KB

Datos Faltantes (Missing data)

Métodos para Manejar datos faltantes en pandas:

# data frame con algunos datos faltantes 
# NaN = Not a Number 
df = pd . DataFrame ({ "A" : [ 1 , 2 , np . nan ], "B" : [ 5 , np . nan , np . nan ], "C" : [ 1 , 2 , 3 ]}) 
df 

A B C 

0 1.0 5.0 1 

1 2.0 NaN 2 

2 NaN NaN 3 

Detectar si Faltan datos

# verificar cuales valores son NaN o nulos (Null) 
df . isna () 

A B C 

0 False False False 

1 False True False 

2 True True False 

# Verificar si hay datos faltantes por columna 
df . isna () . any () 

A True
B True
C False
dtype: bool

Numero de datos faltantes

Calcular el numero de datos nulos que hay por columna

# Numero de datos faltantes por columna 
df . isna () . sum () 

A 1
B 2
C 0
dtype: int64

Eliminar datos Faltantes

# Eliminar todas las filas que tengan datos faltantes 
df . dropna ( axis = "index" ) # cuando son filas no es necesario escribir axis='index' 

A B C 

0 1.0 5.0 1 

# Eliminar todas las columnas que tengan datos faltantes 
df . dropna ( axis = "columns" ) 

C 

0 1 

1 2 

2 3 

# eliminar las filas que tengas 2 o mas valores NaN 
df . dropna ( thresh = 2 ) 

A B C 

0 1.0 5.0 1 

1 2.0 NaN 2 

Reemplazar los datos faltantes

# Llenar los datos faltantes con el dato que nos interese 
df . fillna ( value = "Llenar Valores" ) # llenar los espacios con un string 
# puede ser una palabra, numero , etc 

A B C 

0 1.0 5.0 1 

1 2.0 Llenar Valores 2 

2 Llenar Valores Llenar Valores 3 

# Llenar los datos faltantes con el dato que nos interese 
df . fillna ( value = 99 ) # llenar los espacios con un numero 

A B C 

0 1.0 5.0 1 

1 2.0 99.0 2 

2 99.0 99.0 3 

# Llenar los datos faltantes con el promedio de esa columna 
df [ "A" ] . fillna ( value = df [ "A" ] . mean ()) 

0 1.0
1 2.0
2 1.5
Name: A, dtype: float64

# Llenar los datos faltantes con el promedio de cada columna 
df . fillna ( value = df . mean ()) 

A B C 

0 1.0 5.0 1 

1 2.0 5.0 2 

2 1.5 5.0 3 

Datos unicos (Unique Values)

# crear un dataframe 
df = pd . DataFrame ( 
{ 
"col1" : [ 1 , 2 , 3 , 4 ], 
"col2" : [ 444 , 555 , 666 , 444 ], 
"col3" : [ "abc" , "def" , "ghi" , "xyz" ], 
} 
) 
df 

col1 col2 col3 

0 1 444 abc 

1 2 555 def 

2 3 666 ghi 

3 4 444 xyz 

# valores únicos de la columna col2 
df [ "col2" ] . unique () 

array([444, 555, 666])

# Numero de valores únicos en el dataframe 
df [ "col2" ] . nunique () 

3

# contar cuanto se repiten cada uno de los valores 
df [ "col2" ] . value_counts () 

col2
444 2
555 1
666 1
Name: count, dtype: int64

Datos Duplicados

Se puede borrar los registros que son exactamente iguales en todos los valores de las columnas

datos = { 
"nombre" : [ "Jaime" , "Juan" , "Roberto" , "Juan" ], 
"edad" : [ 18 , 20 , 22 , 20 ], 
"trabajo" : [ "Asistente" , "Manager" , "Cientifico" , "Manager" ], 
} 
df_dup = pd . DataFrame ( datos ) 
df_dup 

nombre edad trabajo 

0 Jaime 18 Asistente 

1 Juan 20 Manager 

2 Roberto 22 Cientifico 

3 Juan 20 Manager 

# método para detectar los datos duplicados 
# me sirve para ver si existen registros duplicados 
df_dup . duplicated () 

0 False
1 False
2 False
3 True
dtype: bool

# Contar cuantos datos duplicados existen 
df_dup . duplicated () . sum () 

1

# Para remover los datos duplicados 
df_dup . drop_duplicates () 

nombre edad trabajo 

0 Jaime 18 Asistente 

1 Juan 20 Manager 

2 Roberto 22 Cientifico 

# El método drop_duplicates entrega el data frame sin duplicados 
# Pero la función no es inplace, osea que el dataframe original sigue igual 
df_dup 

nombre edad trabajo 

0 Jaime 18 Asistente 

1 Juan 20 Manager 

2 Roberto 22 Cientifico 

3 Juan 20 Manager 

df_dup . drop_duplicates ( inplace = True ) 
df_dup 

nombre edad trabajo 

0 Jaime 18 Asistente 

1 Juan 20 Manager 

2 Roberto 22 Cientifico 

Duplicados por Columna

Se pueden borrar los valores que se repitan solamente verificando la columna

frame_datos = { 
"nombre" : [ "Jaime" , "Juan" , "Roberto" , "Juan" ], 
"edad" : [ 18 , 20 , 22 , 21 ], 
"trabajo" : [ "Asistente" , "Manager" , "Cientifico" , "Profesor" ], 
} 
df_dup = pd . DataFrame ( frame_datos ) 
df_dup 

nombre edad trabajo 

0 Jaime 18 Asistente 

1 Juan 20 Manager 

2 Roberto 22 Cientifico 

3 Juan 21 Profesor 

el valor de jason esta duplicado en la columna name

# recordar que estas funciones no son inplace 
df_dup . drop_duplicates ([ "nombre" ]) 

nombre edad trabajo 

0 Jaime 18 Asistente 

1 Juan 20 Manager 

2 Roberto 22 Cientifico 

Outliers

Una de las formas de eliminar los outliers es identificando cual sera el rango en el que queremos nuestros datos y limitar los datos entre ese rango

edad = titanic [ "age" ] 
edad 

0 22.0
1 38.0
2 26.0
3 35.0
4 35.0
...
886 27.0
887 19.0
888 NaN
889 26.0
890 32.0
Name: age, Length: 891, dtype: float64

# Cual es la edad maxima 
edad . max () 

80.0

# Cual es la edad Minima 
edad . min () 

0.42

Solo por hacer el ejercicio se delimitaran las edades entre 1 y 70 años

esto se puede hacer con el método .clip(lower = Valor mas bajo, upper = valor mas alto) 

edad = edad . clip ( lower = 1 , upper = 70 ) 

edad . max () 

70.0

edad . min () 

1.0

Tablas de Contingencia (two way tables)

# Crear Datos 
data = pd . DataFrame ( 
{ 
"gender" : [ 
"male" , 
"male" , 
"female" , 
"female" , 
"male" , 
"female" , 
"male" , 
"female" , 
], 
"education_level" : [ 
"high school" , 
"college" , 
"college" , 
"graduate" , 
"high school" , 
"graduate" , 
"college" , 
"graduate" , 
], 
"city" : [ 
"Boston" , 
"Boston" , 
"Miami" , 
"Boston" , 
"Miami" , 
"Boston" , 
"Miami" , 
"Miami" , 
], 
"score" : [ 75 , 82 , 88 , 95 , 69 , 92 , 78 , 85 ], 
} 
) 
data 

gender education_level city score 

0 male high school Chicago 75 

1 male college Chicago 82 

2 female college New York 88 

3 female graduate Chicago 95 

4 male high school New York 69 

5 female graduate Chicago 92 

6 male college New York 78 

7 female graduate New York 85 

# Tabla de contingencia por Genero y nivel de educación 
pd . crosstab ( data [ "gender" ], data [ "education_level" ], margins = True ) 

education_level college graduate high school All 

gender 

female 1 3 0 4 

male 2 0 2 4 

All 3 3 2 8 

# Tabla de contingencia de Genero, nivel de educación y ciudad 
pd . crosstab ([ data [ "gender" ], data [ "education_level" ]], data [ "city" ], margins = True ) 

city Chicago New York All 

gender education_level 

female college 0 1 1 

graduate 2 1 3 

male college 1 1 2 

high school 1 1 2 

All 4 4 8 

pd . crosstab ( 
data [ "gender" ], data [ "education_level" ], values = data [ "score" ], aggfunc = "mean" 
) 

education_level college graduate high school 

gender 

female 88.0 90.666667 NaN 

male 80.0 NaN 72.0 

# con los valores normalizados 
pd . crosstab ( data [ "gender" ], data [ "education_level" ], normalize = True , margins = True ) 

education_level college graduate high school All 

gender 

female 0.125 0.375 0.00 0.5 

male 0.250 0.000 0.25 0.5 

All 0.375 0.375 0.25 1.0 

métodos y funciones en Pandas

Todos los métodos de los dataframe de pandas se pueden encontrar en:

http://pandas.pydata.org/pandas-docs/stable/reference/frame.html 

Duplicados por Columna

Se pueden borrar los valores que se repitan solamente verificando la columna

# crear un dataframe 
df = pd . DataFrame ( 
{ 
"col1" : [ 1 , 2 , 3 , 4 ], 
"col2" : [ 444 , 555 , 666 , 444 ], 
"col3" : [ "mama " , " papa" , " HIJO " , "HiJa" ], 
} 
) 
df . head () # solamente mostrar los primeros elementos del dataframe 

col1 col2 col3 

0 1 444 mama 

1 2 555 papa 

2 3 666 HIJO 

3 4 444 HiJa 

métodos Basicos Pandas

Ejemplos simples de los métodos de los dataframe de pandas

Para información completa de los métodos de computacion y estadisticos ver:

http://pandas.pydata.org/pandas-docs/stable/reference/frame.html#computations-descriptive-stats 

# Suma total de cada Columna, si es categórico no lo suma 
df . sum () 

col1 10
col2 2109
col3 mama papa HIJO HiJa
dtype: object

# método en una sola columna 
df [ "col1" ] . sum () 

10

# método en varias columnas 
df [[ "col1" , "col2" ]] . sum () 

col1 10
col2 2109
dtype: int64

# Valor Mínimo cada Columna 
df . min () 

col1 1
col2 444
col3 HIJO
dtype: object

# Valor Máximo cada Columna 
df . max () 

col1 4
col2 666
col3 mama
dtype: object

métodos de información General

# Cargar la base de datos 'mpg' de la librería seaborn 
import seaborn as sns 

# los datos se cargan en un dataframe 
data = sns . load_dataset ( "mpg" ) 

data . info () 

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 398 entries, 0 to 397
Data columns (total 9 columns):
# Column Non-Null Count Dtype
--- ------ -------------- -----
0 mpg 398 non-null float64
1 cylinders 398 non-null int64
2 displacement 398 non-null float64
3 horsepower 392 non-null float64
4 weight 398 non-null int64
5 acceleration 398 non-null float64
6 model_year 398 non-null int64
7 origin 398 non-null object
8 name 398 non-null object
dtypes: float64(4), int64(3), object(2)
memory usage: 28.1+ KB

data . head () 

mpg cylinders displacement horsepower weight acceleration model_year origin name 

0 18.0 8 307.0 130.0 3504 12.0 70 usa chevrolet chevelle malibu 

1 15.0 8 350.0 165.0 3693 11.5 70 usa buick skylark 320 

2 18.0 8 318.0 150.0 3436 11.0 70 usa plymouth satellite 

3 16.0 8 304.0 150.0 3433 12.0 70 usa amc rebel sst 

4 17.0 8 302.0 140.0 3449 10.5 70 usa ford torino 

data . describe () # ver datos estadísticos de las columnas numéricas 

mpg cylinders displacement horsepower weight acceleration model_year 

count 398.000000 398.000000 398.000000 392.000000 398.000000 398.000000 398.000000 

mean 23.514573 5.454774 193.425879 104.469388 2970.424623 15.568090 76.010050 

std 7.815984 1.701004 104.269838 38.491160 846.841774 2.757689 3.697627 

min 9.000000 3.000000 68.000000 46.000000 1613.000000 8.000000 70.000000 

25% 17.500000 4.000000 104.250000 75.000000 2223.750000 13.825000 73.000000 

50% 23.000000 4.000000 148.500000 93.500000 2803.500000 15.500000 76.000000 

75% 29.000000 8.000000 262.000000 126.000000 3608.000000 17.175000 79.000000 

max 46.600000 8.000000 455.000000 230.000000 5140.000000 24.800000 82.000000 

data . describe ( include = "all" ) # ver todos los datos incluidos los categóricos 

mpg cylinders displacement horsepower weight acceleration model_year origin name 

count 398.000000 398.000000 398.000000 392.000000 398.000000 398.000000 398.000000 398 398 

unique NaN NaN NaN NaN NaN NaN NaN 3 305 

top NaN NaN NaN NaN NaN NaN NaN usa ford pinto 

freq NaN NaN NaN NaN NaN NaN NaN 249 6 

mean 23.514573 5.454774 193.425879 104.469388 2970.424623 15.568090 76.010050 NaN NaN 

std 7.815984 1.701004 104.269838 38.491160 846.841774 2.757689 3.697627 NaN NaN 

min 9.000000 3.000000 68.000000 46.000000 1613.000000 8.000000 70.000000 NaN NaN 

25% 17.500000 4.000000 104.250000 75.000000 2223.750000 13.825000 73.000000 NaN NaN 

50% 23.000000 4.000000 148.500000 93.500000 2803.500000 15.500000 76.000000 NaN NaN 

75% 29.000000 8.000000 262.000000 126.000000 3608.000000 17.175000 79.000000 NaN NaN 

max 46.600000 8.000000 455.000000 230.000000 5140.000000 24.800000 82.000000 NaN NaN 

# Descripción de una sola columna 
data [ "cylinders" ] . describe () 

count 398.000000
mean 5.454774
std 1.701004
min 3.000000
25% 4.000000
50% 4.000000
75% 8.000000
max 8.000000
Name: cylinders, dtype: float64

data [ "mpg" ] . describe () 

count 398.000000
mean 23.514573
std 7.815984
min 9.000000
25% 17.500000
50% 23.000000
75% 29.000000
max 46.600000
Name: mpg, dtype: float64

data [ "cylinders" ] . dtypes 

dtype('int64')

Estadistica Descriptiva

métodos de Estadistica Descriptiva, de medida central, simetria, momentos, etc. para mas informacion:
http://pandas.pydata.org/pandas-docs/stable/reference/frame.html#computations-descriptive-stats 

Los calculos de las medidas estadisticas se hacen siempre en columnas, es algo predeterminado, si se quiere hacer por filas, se debe especificar dentro de los métodos el parametro axis=1.

Ejemplo:

Calculo de la media por columnas (predeterminado) = df.mean() 

Calculo de la media por filas = df.mean(axis='columns') 

Esto funciona con los otros tipos de medidas estadisticas

# Se tomara la columna 'mpg' para realizar los cálculos 
X = data [ "mpg" ] 
type ( X ) 

pandas.core.series.Series

Medidas de centralizacion

estas funciones se aplican sobre un dataframe de pandas

Media

# Media Aritmética 
X . mean () 

23.514572864321607

# Media aritmética en un dataframe 
data . mean ( numeric_only = True ) 

mpg 23.514573
cylinders 5.454774
displacement 193.425879
horsepower 104.469388
weight 2970.424623
acceleration 15.568090
model_year 76.010050
dtype: float64

Mediana

# Mediana 
X . median () 

23.0

# Mediana en un dataframe 
data . median ( numeric_only = True ) 

mpg 23.0
cylinders 4.0
displacement 148.5
horsepower 93.5
weight 2803.5
acceleration 15.5
model_year 76.0
dtype: float64

Maximo y Minimo

# Máximo 
X . max () 

46.6

# Máximo en un dataframe 
data . max () 

mpg 46.6
cylinders 8
displacement 455.0
horsepower 230.0
weight 5140
acceleration 24.8
model_year 82
origin usa
name vw rabbit custom
dtype: object

# Mínimo 
X . min () 

9.0

# Mínimo en un dataframe 
data . min () 

mpg 9.0
cylinders 3
displacement 68.0
horsepower 46.0
weight 1613
acceleration 8.0
model_year 70
origin europe
name amc ambassador brougham
dtype: object

Moda

# Moda 
X . mode () 

0 13.0
Name: mpg, dtype: float64

# Moda en un dataframe 
data . mode () 

mpg cylinders displacement horsepower weight acceleration model_year origin name 

0 13.0 4.0 97.0 150.0 1985 14.5 73.0 usa ford pinto 

1 NaN NaN NaN NaN 2130 NaN NaN NaN NaN 

Cuartiles

# Valores de los cuartales 
X . quantile ([ 0 , 0.25 , 0.5 , 0.75 , 1 ]) 

0.00 9.0
0.25 17.5
0.50 23.0
0.75 29.0
1.00 46.6
Name: mpg, dtype: float64

# Valores de los cuartales en un dataframe 
data . quantile ([ 0 , 0.25 , 0.5 , 0.75 , 1 ], numeric_only = True ) 

mpg cylinders displacement horsepower weight acceleration model_year 

0.00 9.0 3.0 68.00 46.0 1613.00 8.000 70.0 

0.25 17.5 4.0 104.25 75.0 2223.75 13.825 73.0 

0.50 23.0 4.0 148.50 93.5 2803.50 15.500 76.0 

0.75 29.0 8.0 262.00 126.0 3608.00 17.175 79.0 

1.00 46.6 8.0 455.00 230.0 5140.00 24.800 82.0 

Medidas de dispersion

Varianza

# Varianza 
X . var () # unbiased Normalized by N-1 by default. 

61.089610774274405

# Varianza en un dataframe 
data . var ( numeric_only = True ) 

mpg 61.089611
cylinders 2.893415
displacement 10872.199152
horsepower 1481.569393
weight 717140.990526
acceleration 7.604848
model_year 13.672443
dtype: float64

Desviacion Estandard

# Desviación típica o desviación estándar 
X . std () 

7.815984312565782

# Desviación típica o desviación estándar en un dataframe 
data . std ( numeric_only = True ) 

mpg 7.815984
cylinders 1.701004
displacement 104.269838
horsepower 38.491160
weight 846.841774
acceleration 2.757689
model_year 3.697627
dtype: float64

Coeficiente de Variacion

# Coeficiente de Variación 
X . std ( numeric_only = True ) / X . mean ( numeric_only = True ) 

0.33238895546450203

Medidas de Asimetria

Asimetria de Fisher (skewness)

La asimetría es la medida que indica la simetría de la distribución de una variable respecto a la media aritmética, sin necesidad de hacer la representación gráfica. Los coeficientes de asimetría indican si hay el mismo número de elementos a izquierda y derecha de la media.

Existen tres tipos de curva de distribución según su asimetría:

Asimetría negativa: la cola de la distribución se alarga para valores inferiores a la media.

Simétrica: hay el mismo número de elementos a izquierda y derecha de la media. En este caso, coinciden la media, la mediana y la moda. La distribución se adapta a la forma de la campana de Gauss, o distribución normal.

Asimetría positiva: la cola de la distribución se alarga para valores superiores a la media.

# unbiased skew, Normalized by N-1 
X . skew () 

0.45706634399491913

# unbiased skew, Normalized by N-1 en un dataframe 
data . skew ( numeric_only = True ) 

mpg 0.457066
cylinders 0.526922
displacement 0.719645
horsepower 1.087326
weight 0.531063
acceleration 0.278777
model_year 0.011535
dtype: float64

Curtosis

Esta medida determina el grado de concentración que presentan los valores en la región central de la distribución. Por medio del Coeficiente de Curtosis, podemos identificar si existe una gran concentración de valores (Leptocúrtica), una concentración normal (Mesocúrtica) ó una baja concentración (Platicúrtica). 

# unbiased kurtosis over requested axis using Fisher's definition 
X . kurtosis () 

-0.5107812652123154

# unbiased kurtosis over requested axis using Fisher's definition 
# en un dataframe 
data . kurtosis ( numeric_only = True ) 

mpg -0.510781
cylinders -1.376662
displacement -0.746597
horsepower 0.696947
weight -0.785529
acceleration 0.419497
model_year -1.181232
dtype: float64

Covarianza

Entre Series

s1 = pd . Series ( np . random . randn ( 1000 )) 
s2 = pd . Series ( np . random . randn ( 1000 )) 

s1 . cov ( s2 ) 

-0.025094639027196358

# Numpy 
np . cov ( s1 , s2 ) 

array([[ 0.95048876, -0.02509464],
[-0.02509464, 0.97241405]])

Dataframe

frame = pd . DataFrame ( np . random . randn ( 1000 , 5 ), columns = [ "a" , "b" , "c" , "d" , "e" ]) 
frame . head () 

a b c d e 

0 0.499849 -0.094094 1.604184 -1.080716 1.031231 

1 0.776868 -0.056033 0.590348 -0.022956 0.031928 

2 -1.448370 0.083080 0.559249 -0.902921 -0.222358 

3 -1.042227 1.045355 -0.168918 0.361434 0.150148 

4 -1.428764 -1.904445 -2.016604 1.077732 -0.853357 

frame . cov () 

a b c d e 

a 1.009833 -0.020353 0.011463 -0.008649 -0.090720 

b -0.020353 1.015555 -0.070017 -0.000055 0.019908 

c 0.011463 -0.070017 1.022689 -0.035151 -0.023407 

d -0.008649 -0.000055 -0.035151 1.001558 0.025479 

e -0.090720 0.019908 -0.023407 0.025479 0.979957 

Correlacion

Metodos:

pearson (predeterminado)

kendall

spearman

# Creación de dataframe con datos aleatorios 
frame = pd . DataFrame ( np . random . randn ( 1000 , 5 ), columns = [ "a" , "b" , "c" , "d" , "e" ]) 
frame . head () 

a b c d e 

0 0.207381 1.140107 0.291974 -1.027103 0.806736 

1 -1.296042 -0.506816 -0.610655 0.174875 -0.023277 

2 0.097634 0.089146 2.039174 1.950184 -1.713418 

3 1.854029 -0.337418 -1.075806 0.006662 1.396997 

4 0.813020 -0.638845 -0.038826 -0.304283 0.758953 

Entre Series

frame [ "a" ] . corr ( frame [ "b" ]) # Pearson que es el predeterminado 

0.05612539367834173

frame [ "a" ] . corr ( frame [ "b" ], method = "spearman" ) # método spearman 

0.04815865215865216

frame [ "a" ] . corr ( frame [ "b" ], method = "kendall" ) # método Kendall 

0.03234834834834835

# Con Numpy se realiza el coeficiente de Pearson 
# realiza la correlación entre dos vectores 
np . corrcoef ( frame [ "a" ], frame [ "b" ]) 

array([[1. , 0.05612539],
[0.05612539, 1. ]])

Dataframe

frame . corr () 

a b c d e 

a 1.000000 0.056125 0.024210 -0.005499 -0.007650 

b 0.056125 1.000000 0.007777 -0.009033 -0.000781 

c 0.024210 0.007777 1.000000 -0.001434 -0.050740 

d -0.005499 -0.009033 -0.001434 1.000000 -0.043050 

e -0.007650 -0.000781 -0.050740 -0.043050 1.000000 

# con Numpy 
np . corrcoef ( frame ) 

array([[ 1. , -0.30647049, -0.65411155, ..., 0.29616673,
0.29013432, -0.83433691],
[-0.30647049, 1. , 0.02183588, ..., 0.71342068,
-0.59432049, -0.22950743],
[-0.65411155, 0.02183588, 1. , ..., -0.66660793,
-0.63905691, 0.61597841],
...,
[ 0.29616673, 0.71342068, -0.66660793, ..., 1. ,
-0.0088048 , -0.63793483],
[ 0.29013432, -0.59432049, -0.63905691, ..., -0.0088048 ,
1. , 0.11039718],
[-0.83433691, -0.22950743, 0.61597841, ..., -0.63793483,
0.11039718, 1. ]])

funciones Agregadas

Para aplicar una o mas funciones en cada columna de los dataframe

df . agg ([ "sum" , "min" ]) 

col1 col2 col3 

sum 10 2109 mama papa HIJO HiJa 

min 1 444 HIJO 

# Aplicar los métodos en columnas especificas 
df [[ "col1" , "col2" ]] . agg ([ "sum" , "min" ]) 

col1 col2 

sum 10 2109 

min 1 444 

Aplicando funciones a cada elemento

# definición de función 
def times2 ( x : float ) -> float : 
return x * 2 

# es mas o menos lo que hace la función map 
# aplicar la función times2 a cada elemento de la col1 de dataframe df 
df [ "col1" ] . apply ( times2 ) 

0 2
1 4
2 6
3 8
Name: col1, dtype: int64

df [ "col3" ] . apply ( len ) # longitud de cada uno de los datos de la col3 

0 7
1 6
2 9
3 4
Name: col3, dtype: int64

(Sorting) Ordenar un DataFrame:

df 

col1 col2 col3 

0 1 444 mama 

1 2 555 papa 

2 3 666 HIJO 

3 4 444 HiJa 

# ordenar el dataframe de menor a mayor basado en col2 
df . sort_values ( by = "col2" ) # inplace=False por default 

col1 col2 col3 

0 1 444 mama 

3 4 444 HiJa 

1 2 555 papa 

2 3 666 HIJO 

df . sort_values ( by = "col2" , ascending = False ) 

col1 col2 col3 

2 3 666 HIJO 

1 2 555 papa 

0 1 444 mama 

3 4 444 HiJa 

métodos de strings

Los métodos de los strings se pueden usar en pandas de forma vectorizada

https://pandas.pydata.org/docs/user_guide/basics.html#vectorized-string-methods 

Los métodos vectorizados de los strings son:

https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#text-string-methods 

Nota: Recordar que la mayoria de los métodos NO son inplace 

df 

col1 col2 col3 

0 1 444 mama 

1 2 555 papa 

2 3 666 HIJO 

3 4 444 HiJa 

Algunos ejemplos de métodos en strings en las columnas

# convertir strings en minúscula 
df [ "col3" ] . str . lower () 

0 mama
1 papa
2 hijo
3 hija
Name: col3, dtype: object

# convertir strings en Mayúscula 
df [ "col3" ] . str . upper () 

0 MAMA
1 PAPA
2 HIJO
3 HIJA
Name: col3, dtype: object

# Eliminar los espacios de los strings 
df [ "col3" ] . str . strip () 

0 mama
1 papa
2 HIJO
3 HiJa
Name: col3, dtype: object

Transformacion de Variables

Crear variables Dummy: convertir de categoría a númerica

Discretización o Binning: convertir de número a categoría

Columnas Dummy

Convertir variables categoricas a numericas

# crear datos categóricos 
raw_data = { 
"first_name" : [ "Jason" , "Molly" , "Tina" , "Jake" , "Amy" ], 
"last_name" : [ "Miller" , "Jacobson" , "Ali" , "Milner" , "Cooze" ], 
"sex" : [ "male" , "female" , "male" , "female" , "female" ], 
} 
df = pd . DataFrame ( raw_data , columns = [ "first_name" , "last_name" , "sex" ]) 
df 

first_name last_name sex 

0 Jason Miller male 

1 Molly Jacobson female 

2 Tina Ali male 

3 Jake Milner female 

4 Amy Cooze female 

# Crear un set de variables dummy para la columna sex 
df_sex = pd . get_dummies ( df [ "sex" ]) 
df_sex 

female male 

0 False True 

1 True False 

2 False True 

3 True False 

4 True False 

# unir los dos dataframes 
df_new = df . join ( df_sex ) 
df_new 

first_name last_name sex female male 

0 Jason Miller male False True 

1 Molly Jacobson female True False 

2 Tina Ali male False True 

3 Jake Milner female True False 

4 Amy Cooze female True False 

Discretización o Binning

Conversion de Numerica a Categorica

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.cut.html 

# dividir los datos en 3 rangos iguales (categorías) 

pd . cut ( np . array ([ 3.5 , 2.8 , 1 , 5 , 3 , 4 , 0 , 4.4 , 2 , 3 ]), 3 ) 

[(3.333, 5.0], (1.667, 3.333], (-0.005, 1.667], (3.333, 5.0], (1.667, 3.333], (3.333, 5.0], (-0.005, 1.667], (3.333, 5.0], (1.667, 3.333], (1.667, 3.333]]
Categories (3, interval[float64, right]): [(-0.005, 1.667] < (1.667, 3.333] < (3.333, 5.0]]

# Asignar etiquetas ordenadas 
pd . cut ( 
np . array ([ 3.5 , 2.8 , 1 , 5 , 3 , 4 , 0 , 4.4 , 2 , 3 ]), 
3 , 
labels = [ "Malo" , "Regular" , "Bien" ], 
) 

['Bien', 'Regular', 'Malo', 'Bien', 'Regular', 'Bien', 'Malo', 'Bien', 'Regular', 'Regular']
Categories (3, object): ['Malo' < 'Regular' < 'Bien']

pd . cut ( 
np . array ([ 2 , 4 , 10 , 35 , 25 , 60 , 23 , 14 ]), 
3 , 
labels = [ "Niño" , "Adolescente" , "Adulto" ], 
) 

['Niño', 'Niño', 'Niño', 'Adolescente', 'Adolescente', 'Adulto', 'Adolescente', 'Niño']
Categories (3, object): ['Niño' < 'Adolescente' < 'Adulto']

Leer y guardar Datos (Data Input and Output)

Pandas puede leer una variedad de tipos de archivos usando sus métodos pd.read_ mas informacion 

CSV

Parquet ( Formato recomendado )

Excel

Json

Html

SQL

Nota: estos se ejemplos se hacen con archivos previamente creados para la demostracion 

CSV File (comma-separated values)

Este es un formato muy común para compartir datos. Los archivos CSV son archivos de texto, sin formato, que usan comas para separar filas.
Sus desventajas son que no especifican tipos de datos, no admiten datos faltantes, entre otros.

No es un formato ideal para compartir datos.

CSV Input

# Leer archivos separados por comas, extension .csv 
df_supermarket_csv = pd . read_csv ( "supermarkets.csv" ) 
df_supermarket_csv . sample ( 5 ) 

ID Address City State Country Name Employees 

4 5 1056 Sanchez St San Francisco California USA Sanchez 12 

3 4 3995 23rd St San Francisco CA 94114 USA Ben's Shop 10 

1 2 735 Dolores St San Francisco CA 94119 USA Bready Shop 15 

0 1 3666 21st St San Francisco CA 94114 USA Madeira 8 

5 6 551 Alvarado St San Francisco CA 94114 USA Richvalley 20 

CSV Output

# Grabar el dataframe como archivo separado por comas 
df_supermarket_csv . to_csv ( "example_out.csv" , index = False ) 

Parquet

Este es un formato de archivo binario de columna que es muy bueno para compartir datos. Es muy eficiente en el espacio y el tiempo de lectura.

Es el formato recomendado para compartir datos.

pip install pyarrow 

Parquet Input

# Leer archivos separados por comas, extension .csv 
df_supermarket_parquet = pd . read_parquet ( "supermarkets.parquet" ) 
df_supermarket_parquet . sample ( 5 ) 

ID Address City State Country Name Employees 

2 3 332 Hill St San Francisco California 94114 USA Super River 25 

0 1 3666 21st St San Francisco CA 94114 USA Madeira 8 

5 6 551 Alvarado St San Francisco CA 94114 USA Richvalley 20 

3 4 3995 23rd St San Francisco CA 94114 USA Ben's Shop 10 

4 5 1056 Sanchez St San Francisco California USA Sanchez 12 

Parquet Output

# Grabar el dataframe como archivo parquet 
df_supermarket_parquet . to_parquet ( "example_out.parquet" ) 

Archivo de texto separado por otro caracter

# este archivo los valores están separados por ; 
df_supermarket = pd . read_csv ( "supermarkets-semi-colons.txt" , sep = ";" ) 
df_supermarket 

ID Address City State Country Name Employees 

0 1 3666 21st St San Francisco CA 94114 USA Madeira 8 

1 2 735 Dolores St San Francisco CA 94119 USA Bready Shop 15 

2 3 332 Hill St San Francisco California 94114 USA Super River 25 

3 4 3995 23rd St San Francisco CA 94114 USA Ben's Shop 10 

4 5 1056 Sanchez St San Francisco California USA Sanchez 12 

5 6 551 Alvarado St San Francisco CA 94114 USA Richvalley 20 

Excel

Pandas puede leer y escribir archivos de Excel, tenga en cuenta que esto solo importa datos. No fórmulas o imágenes, que tengan imágenes o macros pueden hacer que este método read_excel se bloquee.

Es necesario isntalar la libreria openpyxl 

pip install openpyxl 

Excel Input

# leer un archivo de excel 
df_supermarket_excel = pd . read_excel ( 
"supermarkets.xlsx" , 
sheet_name = 0 , # leer la primera hoja del archivo 
) 
df_supermarket_excel . sample ( 5 ) 

ID Address City State Country Supermarket Name Number of Employees 

0 1 3666 21st St San Francisco CA 94114 USA Madeira 8 

2 3 332 Hill St San Francisco California 94114 USA Super River 25 

5 6 551 Alvarado St San Francisco CA 94114 USA Richvalley 20 

4 5 1056 Sanchez St San Francisco California USA Sanchez 12 

3 4 3995 23rd St San Francisco CA 94114 USA Ben's Shop 10 

Excel Output

df_supermarket_excel . to_excel ( "Excel_Sample_out.xlsx" , sheet_name = "Hoja1" ) 

JSON

JSON (JavaScript Object Notation - Notación de Objetos de JavaScript) es un formato ligero de intercambio de datos. Leerlo y escribirlo es simple para humanos, mientras que para las máquinas es simple interpretarlo y generarlo.

Json Input

# los archivos pueden estar en un link de internet 
df_supermarket_json = pd . read_json ( "http://pythonhow.com/supermarkets.json" ) 
df_supermarket_json . sample ( 5 ) 

Address City Country Employees ID Name State 

3 3995 23rd St San Francisco USA 10 4 Ben's Shop CA 94114 

2 332 Hill St San Francisco USA 25 3 Super River California 94114 

0 3666 21st St San Francisco USA 8 1 Madeira CA 94114 

4 1056 Sanchez St San Francisco USA 12 5 Sanchez California 

5 551 Alvarado St San Francisco USA 20 6 Richvalley CA 94114 

Json output

# Para grabar 
df_supermarket_json . to_json ( "Salida.json" ) 

HTML

Pandas puede leer tablas de html

Es necesario instalar las librerias pip install lxml html5lib 

La función pandas read_html leerá las tablas de una página web y devolverá una lista de objetos DataFrame:

data_table_web = pd . read_html ( 
"https://www.runnersworld.com/races-places/a20823734/these-are-the-worlds-fastest-marathoners-and-marathon-courses/" , 
header = 0 , 
) 

data_table_web [ 0 ] 

Runner Finish Time Pace/Mile Marathon 

0 Kelvin Kiptum (Kenya) 2:00:35 4:36.0 Chicago, 2023 

1 Eliud Kipchoge (Kenya) 2:01:09 4:37.2 Berlin, 2022 

2 Kenenisa Bekele (Ethiopia) 2:01:41 4:38.5 Berlin, 2019 

3 Sisay Lemma (Ethiopia) 2:01:48 4:38.7 Valencia, 2023 

4 Benson Kipruto (Kenya) 2:02:16 4:39.8 Tokyo, 2024 

5 John Korir (Kenya) 2:02:44 4:4o.8 Chicago, 2024 

6 Birhanu Legese (Ethiopia) 2:02:48 4:41.0 Berlin, 2019 

7 Mosinet Geremew (Ethiopia) 2:02:55 4:41.3 London, 2019 

8 Timothy Kiplagat (Kenya) 2:02:55 4:41.3 Tokyo, 2024 

9 Dennis Kimetto (Kenya) 2:02:57 4:41.4 Berlin, 2014 

data_table_web [ 1 ] 

Runner Finish Time Pace/Mile Marathon 

0 Ruth Chepngetich (Kenya) 2:09:56 4:57.4 Chicago, 2024 

1 Tigist Assefa (Ethiopia) 2:11:53 5:01.8 Berlin, 2023 

2 Sifan Hassan (Netherlands) 2:13:44 5:06.0 Chicago, 2023 

3 Brigid Kosgei (Kenya) 2:14:04 5:06.8 Chicago, 2019 

4 NaN NaN NaN NaN 

5 Amane Beriso (Ethiopia) 2:14:58 5:08.9 Valencia, 2022 

6 Paula Radcliffe (Great Britain) 2:15:25 5:09.9 London, 2003 

7 Worknesh Degefa (Ethiopia) 2:15:51 5:10.9 Valencia, 2023 

8 Sutume Kebede (Ethiopia) 2:15:55 5:11.0 Tokyo, 2024 

9 Tigist Ketema (Ethiopia) 2:16:07 5:11.5 Dubai, 2024 

10 Rosemary Wanjiru (Kenya) 2:16:14 5:11.8 Tokyo, 2024 

11 NaN NaN NaN NaN 

SQL

El módulo pandas.io.sql proporciona una colección de contenedores de consultas para facilitar la recuperación de datos y reducir la dependencia de la API específica de DB. La abstracción de la base de datos es proporcionada por SQLAlchemy si está instalado. Además, necesitará una biblioteca de controladores para su base de datos. Ejemplos de tales controladores son psycopg2 para PostgreSQL o pymysql para MySQL. Para SQLite esto está incluido en la biblioteca estándar de Python por defecto. Puede encontrar una descripción general de los controladores admitidos para cada lenguaje SQL en los documentos de SQLAlchemy.

pip install sqlalchemy 

Vea también algunos ejemplos de libros para algunas estrategias avanzadas.

las funciones claves son:

read_sql_table(table_name, con[, schema, …]) 
Read SQL database table into a DataFrame.

read_sql_query(sql, con[, index_col, …]) 
Read SQL query into a DataFrame.

read_sql(sql, con[, index_col, …]) 
Read SQL query or database table into a DataFrame.

DataFrame.to_sql(name, con[, flavor, …]) 
Write records stored in a DataFrame to a SQL database.

# librerías para crear un proceso de sql sencillo 
from sqlalchemy import create_engine 

# crear un proceso en memoria 
engine = create_engine ( "sqlite:///:memory:" ) 

data_table_web [ 0 ] . to_sql ( "data" , engine ) # grabar el dataframe en formato sql 

10

sql_df = pd . read_sql ( "data" , con = engine ) # definir la conexión 

sql_df 

index Runner Finish Time Pace/Mile Marathon 

0 0 Kelvin Kiptum (Kenya) 2:00:35 4:36.0 Chicago, 2023 

1 1 Eliud Kipchoge (Kenya) 2:01:09 4:37.2 Berlin, 2022 

2 2 Kenenisa Bekele (Ethiopia) 2:01:41 4:38.5 Berlin, 2019 

3 3 Sisay Lemma (Ethiopia) 2:01:48 4:38.7 Valencia, 2023 

4 4 Benson Kipruto (Kenya) 2:02:16 4:39.8 Tokyo, 2024 

5 5 John Korir (Kenya) 2:02:44 4:4o.8 Chicago, 2024 

6 6 Birhanu Legese (Ethiopia) 2:02:48 4:41.0 Berlin, 2019 

7 7 Mosinet Geremew (Ethiopia) 2:02:55 4:41.3 London, 2019 

8 8 Timothy Kiplagat (Kenya) 2:02:55 4:41.3 Tokyo, 2024 

9 9 Dennis Kimetto (Kenya) 2:02:57 4:41.4 Berlin, 2014 

Referencias

Web Pandas 

10 Minutes to Pandas 

Tutoriales oficiales de Pandas 

Pandas Basic cheat sheet 

Pandas cheat sheet 

Phd. Jose R. Zapata 

https://joserzapata.github.io/ 

https://www.linkedin.com/in/jose-ricardo-zapata-gonzalez/ 

Feedback

Was this page helpful?

🙏

🙏

😍 Yes

😡 No 

Última actualización el nov 2, 2024

© 2018–2026 Jose Ricardo Zapata Gonzalez.

Published with Hugo Blox Builder — the free, open source website builder that empowers creators.
