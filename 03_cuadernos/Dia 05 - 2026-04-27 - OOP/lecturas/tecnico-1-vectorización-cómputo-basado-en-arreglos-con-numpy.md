# Vectorización: cómputo basado en arreglos con NumPy

Fuente: [Computación Científica con Python · P. Huijse](https://phuijse.github.io/PythonBook/contents/hpc/vectorization.html)  
_Copia local para lectura fuera de línea. El formato original puede verse en la URL._

---

Repository 

Open issue 

.ipynb 

.pdf 

Vectorización: Cómputo basado en arreglos con NumPy

Contenido 

38.1. Reemplazar ciclo for por operaciones vectoriales 

38.2. Convertir operaciones lógicas sobre arreglos en máscaras 

38.3. Evitar copia adicional de datos 

38.4. Aprovechar el broadcasting automático de NumPy 

38.5. Utilizar el ordenamiento en memoría más adecuado en cada caso 

38. Vectorización: Cómputo basado en arreglos con NumPy # 

Consideremos el escenario en que tenemos un arreglo de datos de gran tamaño y queremos hacer una operación sobre cada elemento.

Ejemplo: Dado \(\{x\}_i\) queremos encontrar

\[
y_i = \frac{1}{1 + e^{-x_i}}, \quad i = 1,2,\ldots, N
\]

Los cómputos como el anterior son de tipo Single Instruction Multiple Data (SIMD), ya que estamos haciendo una misma operación para todos los datos.

Este problema se puede resolver ingenuamente usando un ciclo for :

y = [] 
for xi in x : 
y . append ( 1 / ( 1 + math . exp ( - xi )) 

Sin embargo, ya sabemos que esto es ineficiente en “Python puro”. Las librerías de cómputo científico vistas en este curso nos ofrecen una mejor alternativa.

Importante

NumPy nos provee de una estructura de arreglo multidimensional (ndarray) y funciones para operarla que están escritas en C y Fortran.

Utilizando NumPy podemos reemplazar un ciclo for en problemas SIMD por operaciones que trabajan sobre todo el arreglo, estas sa llaman operaciones vectoriales .

Por ejemplo, asumiendo que x es una lista, podemos vectorizar el código del ejemplo anterior como:

x = np . array ( x ) 
y = 1 / ( 1 + np . exp ( - x )) 

Nota

NumPy aplica la función exponencial a todo el arreglo x, luego aplica la aritmética (suma y división) a cada elemento del arreglo (broadcasting) y finalmente retorna un nuevo arreglo con el resultado.

El proceso de reemplazar un ciclo for por una operación vectorial se conoce como vectorización . A continuación revisaremos mediante ejemplos como implementar este y otros conceptos para mejorar el rendimiento.

38.1. Reemplazar ciclo for por operaciones vectoriales # 

Las operaciones vectoriales son funciones de NumPy de tipo element-wise aplicadas sobre un ndarray. Las funciones element-wise son aquellas que actuan sobre todos los elementos del arreglo de forma independiente:

En capítulos anteriores revisamos algunos ejemplos: exponenciación, raíces, trigonometrícas, etc

Las operaciones aritméticas entre ndarrays son por defecto element-wise 

Luego si tenemos un problema SIMD escrito con un for sobre un conjunto de datos podemos:

Convertir los datos a ndarray

Escribir la operación con funciones de NumPy element-wise 

y obtener una ganancia considerable en eficiencia de forma simple y directa.

Por ejemplo, notemos la diferencia en tiempo de cómputo al hacer aritmética simple

import numpy as np 

x_ndarray = np . random . randn ( 100000 ) 
x_list = list ( x_ndarray ) 

def operacion_simple ( data ): 
resultado = [] 
append = resultado . append 
for elemento in data : 
append ( elemento * elemento + elemento ) 
return resultado 

# Operación usando "for con mejoras" 
reference = % timeit -n3 -r7 -o operacion_simple(x_list)
# Operación usando numpy sobre un ndarray 
proposal = % timeit -n3 -r7 -o x_ndarray*x_ndarray + x_ndarray
# Comparación entre los resultados 
same_result = np . allclose ( operacion_simple ( x_list ), x_ndarray * x_ndarray + x_ndarray ) 
speed_up = reference . average / proposal . average 
same_result , speed_up 

22.1 ms ± 402 µs per loop (mean ± std. dev. of 7 runs, 3 loops each)
205 µs ± 76.2 µs per loop (mean ± std. dev. of 7 runs, 3 loops each)

(True, 108.00234301051614)

Advertencia

Las funciones de NumPy son lentas cuando operan sobre tipos que no son ndarray

Para el ejemplo de \(y_i = (1 + e^{-x_i})^{-1}, \quad i = 1,2,\ldots, N\) 

from math import exp 
# usando list comprehension (similar a un "for mejorado") 
% timeit -n3 -r7 [1./(1.+exp(xi)) for xi in x_list]
# usando numpy sobre una lista 
% timeit -n3 -r7 1./(1+np.exp(x_list))
# usando numpy sobre un ndarray 
% timeit -n3 -r7 1./(1+np.exp(x_ndarray))
# Comparación entre los resultados 
np . allclose ( 1. / ( 1 + np . exp ( x_ndarray )), [ 1. / ( 1. + exp ( xi )) for xi in x_list ]) 

17.5 ms ± 1.28 ms per loop (mean ± std. dev. of 7 runs, 3 loops each)
8.3 ms ± 254 µs per loop (mean ± std. dev. of 7 runs, 3 loops each)
364 µs ± 11.3 µs per loop (mean ± std. dev. of 7 runs, 3 loops each)

True

Las operación sobre ndarray es casi un orden de magnitud más rápida

¿Por qué ocurre esto? 

Recuerde que una lista puede tener distintos tipos y además puede estar guardada en distintos sectores de memoria. En cambio, el ndarray:

Tiene un tipo definido

Está guardado en bloques de memoria contiguos

Por ende el ndarray tiene un overhead de interpretador mucho menor que la lista. Además NumPy está escrito en C/Fortran, y hacer un loop en memoría contigua en C es muy eficiente.

Ver también

NumPy puede compilarse con librerías de alto desempeño como openblas o MKL . De esta forma se aprovechan mejor las capacidades del hardware (Cache de CPU e instrucciones vectoriales de CPU).

38.2. Convertir operaciones lógicas sobre arreglos en máscaras # 

Las operaciones lógicas en NumPy también son element-wise (Operaciones booleanas, clase NumPy, unidad 1). Si queremos recuperar los elementos de un arreglo que cumplan una cierta condición podemos:

Convertir los datos a ndarray

Escribir la operación como una máscara booleana de índices

Consideremos el ejemplo de la lección anterior donde se deseaban recuperar los elementos de una lista tal que \(\sin(x_i)>0\) 

import math 

def sin_pos ( data ): 
resultado = [] 
append = resultado . append 
sin = math . sin 
for element in data : 
if sin ( element ) > 0 : 
append ( element ) 
return resultado 

reference = % timeit -r5 -n3 -o sin_pos(x_list)
proposal = % timeit -r5 -n3 -o x_ndarray[np.sin(x_ndarray) > 0.]

same_result = np . allclose ( sin_pos ( x_list ), x_ndarray [ np . sin ( x_ndarray ) > 0 ]) 
speed_up = reference . average / proposal . average 
same_result , speed_up 

15.2 ms ± 473 µs per loop (mean ± std. dev. of 5 runs, 3 loops each)
1.54 ms ± 32.7 µs per loop (mean ± std. dev. of 5 runs, 3 loops each)

(True, 9.88342694541913)

38.3. Evitar copia adicional de datos # 

Cuando en NumPy ejecutamos

x = x * x 

Ocurre lo siguiente:

Se crea una copia interna de x*x

x es direccionado a esa nueva copia

La zona de memoria con el valor original es luego eliminada por el garbage-collector de Python

Siempre que no necesitemos el valor original podemos usar operaciones in-place y ganar rendimiento, ya que evitamos la copia y eliminación adicional

# Copia interna y cambio de referencia de x_ndarray 
reference = % timeit -r10 -n10 -o x_ndarray = np.zeros(shape=(1000000)); y = x_ndarray*x_ndarray
# Sin copia interna 
proposal = % timeit -r10 -n10 -o x_ndarray = np.zeros(shape=(1000000)); x_ndarray *= x_ndarray

x_ndarray = np . zeros ( shape = ( 1000000 )) 
y = x_ndarray * x_ndarray 
x_ndarray *= x_ndarray 

same_result = np . allclose ( x_ndarray , y ) 
speed_up = reference . average / proposal . average 
same_result , speed_up 

3.32 ms ± 71.8 µs per loop (mean ± std. dev. of 10 runs, 10 loops each)
2.25 ms ± 76.9 µs per loop (mean ± std. dev. of 10 runs, 10 loops each)

(True, 1.4759441251674865)

Sea \(x\) un ndarray, la operación

x [ 2 : 10 ] 

es una “vista de x”.

Consejo

Recordar que las “vista de arreglo” no hacen copias en memoria ya que apuntan directamente al arreglo original. Es decir que si modificamos una vista modificamos el original.

38.4. Aprovechar el broadcasting automático de NumPy # 

Se pueden hacer operaciones vectorizadas con NumPy entre arreglos con tamaños distintos. En ese caso se aplican las reglas de broadcasting que se vieron en la lección de NumPy.

Nota

El broadcasting automático no hace copias en memoria.

Ejemplo 1: Si le sumas una constante a un arreglo 1D, la constante se expande y se suma a cada elemento:

N = 1000000 
x = np . zeros ( shape = ( N , )) 
# broadcasting automático 
% timeit -n10 -r10 x + 1.
# Agrandando y luego sumando 
% timeit -n10 -r10 x + np.tile([1], len(x))
# mismo resultado 
np . allclose ( x + 1 , x + np . tile ([ 1 ], len ( x ))) 

942 µs ± 160 µs per loop (mean ± std. dev. of 10 runs, 10 loops each)
11.1 ms ± 967 µs per loop (mean ± std. dev. of 10 runs, 10 loops each)

True

Ejemplo 2: Si le sumas un arreglo 1D a un arreglo 2D, el arreglo 1D se expande en la dimensión que le falta:

N , M = 10000 , 1000 
x = np . zeros ( shape = ( N , M )) # arreglo de NxM 
y = np . zeros ( shape = ( N , )) # arreglo sin dimensión 
y_ = y [:, np . newaxis ] # arreglo de Nx1 
# broadcasting automático 
% timeit -n10 -r10 x + y_
display (( x + y_ ) . shape ) 
# Agrandando y luego sumando 
% timeit -n10 -r10 x + np.tile(y_, (1, x.shape[-1]))
# mismo resultado 
np . allclose ( x + y_ , x + np . tile ( y_ , ( 1 , x . shape [ - 1 ]))) 

30.9 ms ± 909 µs per loop (mean ± std. dev. of 10 runs, 10 loops each)

(10000, 1000)

98.4 ms ± 1.41 ms per loop (mean ± std. dev. of 10 runs, 10 loops each)

True

Ejemplo 3: Si sumas un arreglo 1D fila y un arreglo 1D columna se crea un arreglo 2D:

N , M = 10000 , 1000 
x = np . zeros ( shape = ( N , 1 )) # arreglo columna de Nx1 
y = np . zeros ( shape = ( 1 , M )) # arreglo fila de 1xM 
# broadcasting automático 
% timeit -n10 -r10 x + y
display (( x + y ) . shape ) 
# Agrandando y luego sumando 
% timeit -n10 -r10 np.tile(y, (x.shape[0], 1)) + np.tile(x, (1, y.shape[-1]))
np . allclose ( x + y , np . tile ( y , ( x . shape [ 0 ], 1 )) + np . tile ( x , ( 1 , y . shape [ - 1 ]))) 

32.6 ms ± 1.56 ms per loop (mean ± std. dev. of 10 runs, 10 loops each)

(10000, 1000)

118 ms ± 2.1 ms per loop (mean ± std. dev. of 10 runs, 10 loops each)

True

Nota

Las dimensiones de dos arreglos son compatibles con broadcast automático si son del mismo tamaño o una de ellas es igual a uno .

38.5. Utilizar el ordenamiento en memoría más adecuado en cada caso # 

Los ndarray multidimensionales pueden guardarse en memoria como row-major (filas contiguas) o column-major (columnas contiguas). Por defecto las matrices en NumPy son row-major pero podemos forzar la contigüidad usando el atributo order o trasponiendo (ojo que trasponer crea una copia).

Se puede verificar esto con el atributo flag de los ndarray:

data = np . arange ( 6 ) . reshape ( 2 , 3 ) 
display ( data ) 
# Verificamos los flags 
display ( data . flags ) 
# Así se ve row-major en memoria 
display ( data . ravel ()) 
# Verificamos los flags 
dataT = data . T 
display ( dataT . flags ) 
# Así se ve column-major en memoria 
display ( dataT . ravel ()) 

array([[0, 1, 2],
[3, 4, 5]])

C_CONTIGUOUS : True
F_CONTIGUOUS : False
OWNDATA : False
WRITEABLE : True
ALIGNED : True
WRITEBACKIFCOPY : False

array([0, 1, 2, 3, 4, 5])

C_CONTIGUOUS : False
F_CONTIGUOUS : True
OWNDATA : False
WRITEABLE : True
ALIGNED : True
WRITEBACKIFCOPY : False

array([0, 3, 1, 4, 2, 5])

Nota

La mayoría de las funciones de NumPy funcionan más rápido en formato row-major (formato C). Pero algunas funciones de scipy (heredadas de Fortran) funcionan más rápido en formato col-major (formato Fortran).

Es recomendable verificar el orden en memoria que espera la función que vas a utilizar.

data = np . random . randn ( 10000 , 10000 ) # (row-major) 
# Sumando una fila 
% timeit -n100 -r10 np.sum(data[0, :])
# Sumando todas las filas 
% timeit -n10 -r10 np.sum(data, axis=1)

11.6 µs ± 189 ns per loop (mean ± std. dev. of 10 runs, 100 loops each)
74.1 ms ± 659 µs per loop (mean ± std. dev. of 10 runs, 10 loops each)

# Sumando una columna 
% timeit -n100 -r10 np.sum(data[:, 0])
# Sumando todas las columnas 
% timeit -n10 -r10 np.sum(data, axis=0)

32.3 µs ± 8.63 µs per loop (mean ± std. dev. of 10 runs, 100 loops each)
121 ms ± 2.46 ms per loop (mean ± std. dev. of 10 runs, 10 loops each)

# Sumando todas las columnas de la matriz traspuesta (column major) 
% timeit -n10 -r10 np.sum(data.T, axis=0)

74.5 ms ± 412 µs per loop (mean ± std. dev. of 10 runs, 10 loops each)

anterior

37. Optimizando código Python

siguiente

39. Acelerando Python con Cython

Contenido

38.1. Reemplazar ciclo for por operaciones vectoriales 

38.2. Convertir operaciones lógicas sobre arreglos en máscaras 

38.3. Evitar copia adicional de datos 

38.4. Aprovechar el broadcasting automático de NumPy 

38.5. Utilizar el ordenamiento en memoría más adecuado en cada caso 

Por Pablo Huijse Heise

© Copyright 2022.
