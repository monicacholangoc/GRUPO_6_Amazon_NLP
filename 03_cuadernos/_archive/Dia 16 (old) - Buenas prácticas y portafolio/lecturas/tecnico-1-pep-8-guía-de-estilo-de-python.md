# PEP 8: guía de estilo de Python

Fuente: [El Pythonista](https://elpythonista.com/pep-8)  
_Copia local para lectura fuera de línea. El formato original puede verse en la URL._

---

Inicio   >   Fundamentos / Tutorial Python 

PEP 8 – Guía de estilos en Python

En la Propuesta de mejora de Python número 8 , PEP 8, se define la guía de cómo escribir Python de forma correcta, a modo de guía de estilos del lenguaje, pero ¿Qué puntos componen la guia y cómo aplicarlos?

Contenido

1 Diseño del código 
1.1 Reglas de indentación en PEP 8 

1.2 Longitud de líneas 

1.3 Posición de los operadores 

1.4 Posición de líneas en blanco 

1.5 Importaciones de código 

1.6 Variables de módulo 

2 Cadenas de caracteres 

3 Espacios en blanco 

4 Comas finales 

5 Comentarios 

6 Convenciones de nombres 

7 Anotaciones de variables 

8 ¿Como detectar errores de PEP 8 automáticamente? 

9 Libros recomendados para aprender Python 
9.1 Scripts en Python 

9.2 ¿Qué es Python? 

9.3 Usar la shell de Python (REPL Python) 

9.4 ¿Cómo instalar Python? 

Diseño del código 

Se definen las claves de cómo debería de escribirse el código Pythónico en sí, definiendo conceptos como la indentación, la longitud de las líneas, las líneas en blanco y la guía de importación de otros paquetes entre otros conceptos.

Reglas de indentación en PEP 8 

Python define la lógica de su código utilizando bloques indentados, por lo tanto se recomienda indentar usando 4 espacios , dado que los espacios ocupan el mismo tamaño en casi todos los tipos de fuente y 4 es un número aceptable para la separación visual de los bloques.

Una alternativa común a los espacios son el uso de tabulaciones pero acarrea el problema que según se defina el tamaño de las tabulaciones en cada editor, el código se verá diferente haciéndolo incluso ilegible , por lo que NO se recomienda su uso.

# Usando 4 espacios
def es_par(num):
if num % 2 == 0:
return True
return False

La indentación tambien se aplica a sentencias que ocupen más de una línea como llamadas a funciones o definiones de tipos de datos, los cuales deben de respetar una indentación visual apropiada que distinga la sentencia del código siguiente

# Mal - no se distingue los argumentos 
# y el codigo de la funcion
def mi_funcion_con_argumentos(argumento1,
argumento2,
argumento3):
print(argumento1)

# Bien
def mi_funcion_con_argumentos(argumento1,
argumento2,
argumento3):
print(argumento1)

# o con indentacion extra
def mi_funcion_con_argumentos(
argumento1, argumento2,
argumento3):
print(argumento1)

En Python 3 no está permitida la mezcla de espacios y tabuladores , y en Python 2 se podian obtener avisos usando los parámetros -t o -tt para identificar las zonas conflictivas. 

-->

Longitud de líneas 

La longitud de las líneas es un tema controvertido y permite cierta flexibilidad:

79 caracteres por línea por defecto y para la librería estandar.

72 caracteres por línea de comentarios o documentación.

99 caracteres para equipos que acuerden utilizar líneas más largas pero la limitación de comentarios y documentación sigue siendo 72.

El propósito principal de estas limitaciones es posibilitar el uso de dos ventanas de un editor , una al lado de la otra, sin que tenga que añadirse saltos de líneas por el editor, mejorando así la lectura .

Para seguir en la siguiente línea no siempre es necesario añadir ningún carácter especial, por ejemplo cuando se definen cadenas de caracteres, documentación, o se definen funciones.

Cuando se pretenda hacer un salto de línea se utiliza el carácter \, y se indentará correctamente.

def mi_funcion(primer_parametro, segundo_param= 'opcional_realmente' ,
tercer_parametro= None ):
return True

if peso > 93 and dias_hasta_verano < 100 \
and destino_vacaciones == 'Playa' :
hacer_ejercicio()

Posición de los operadores 

Cuando se tienen muchos operadores en nuevas líneas, las líneas deben de comenzar con el operador.

# Mal
patas_totales = (num_patas_gato +
num_patas_pato +
num_patas_perro)

# Bien
patas_totales = (num_patas_gato
+ num_patas_pato
+ num_patas_perro)

Posición de líneas en blanco 

Cuando se definen conceptos y lógica en Python, es relevante el uso de líneas en blanco a añadir.

2 líneas en blanco : rodeando a funciones de nivel principal y definición de clases.

1 línea en blanco : definición de métodos dentro de una clase.

1 línea extra : entre bloques lógicos de código diferentes.

1 línea en blanco al final del fichero : todos los módulos en Python deben de terminar con una línea en blanco al final de cada módulo si tienen contenido.

control-L (^L) : se utiliza para separar páginas aunque algunos editores de texto lo omiten.

CONSTANTE = 'inicio'

def mi_funcion(a):
return a + 4

class Perro:
peso = 1.7

def ladra(self):
print('guau')

def come(self):
if self.peso < 1.5:
self.peso = 1.9
else:
self.peso += 0.2

print('Guau - que rico!')

Importaciones de código 

Para las importaciones de paquetes existen algunas reglas también.

El uso de import debe de ser en líneas separadas.

El orden de importación es: librería estándar, librerías de terceros, librerías propias o locales.

Las importaciones absolutas son los recomendados.

Los importaciones relativas solo pueden ser explícitas y preferiblemente simples y cortas.

Importaciones usando * (wildcard) deben de ser evitadas.

# Mal
import json, sys

# Bien
import json
import sys

# Bien
from json import dump, load

# importacion absoluta
import pkg.funciones
from pkg import funciones
from pkg.funciones import mi_funcion

# importacion relativa
from . import funciones
from .funciones import mi_funcion

# evitar!
from pkg import * 

Variables de módulo 

Las variables de módulo definen ciertos aspectos generales:

__all__: define qué objetos se importarán al hacer uso de import *.

__author__: define el autor del módulo.

__version__: define la versión del módulo actual.

Todas estas definiciones han de hacerse al comienzo del módulo, justo debajo del bloque de importaciones.

Cadenas de caracteres 

Python soporta diferentes tipos de caracteres para crear cadenas de caracteres siendo simples o triples, comillas simples o dobles.

Comillas simples o dobles : para cadenas de caracteres de una línea o varias.

Triples comillas dobles : para cadenas de documentación y bloques de cadenas de caracteres.

Para escapar con facilidad las comillas simples o dobles se pueden utilizar un tipo u otro.

def mi_funcion():
"""Sección de documentación con triples comillas dobles"""
pass

a = "Ander's car" # escapando ' al usar "
cita = 'Iba por "la acera" con el coche' # escapando " al usar '

Espacios en blanco 

Los espacios en blanco en Python se utilizan para aclarar o remarcar partes del código, pero hay que hacer un uso contenido de los mismos definiendo las siguientes reglas:

Añadir espacios: entre elementos separados por comas, en los lados de una evaluación operacional, en una asignación o separando bloques de operaciones.

Evitar espacios : en slicings, entre los nombres de funciones y la llamada, entre las variables y el acceso interno usando [], operaciones logicamente unidas o en parentesis vacios.

# Bien
mi_funcion(param1, [1, 2])

a += 1
i = i + 1
b = a*2 - 1
c = (a+i) * (a-i)

if a == b:
print(a + 'es igual que' + b)

lst[1:2], lst[4:], lst[5:34:2]
lst[inicio + mid : mid + fin]
lst[inicio::fin]

gato = 1
perro = 2
elefante_marron = 4

# Mal
mi_funcion ( param1, [ 1, 2] )

a +=1
i=i+1
b = a * 2 - 1
c = (a + i) * (a - i)

if a==b:
print (a+'es igual que' + b)

lst[ 1:2 ], lst[ 4:], lst[5 : 34 : 2]
lst[inicio + mid:mid + fin]
lst[inicio : : fin]

gato = 1
perro = 2
elefante_marron = 4

-->

Comas finales 

El uso de comas al final de una variable debe de hacerse en una nueva línea, y hay que recordar que las comas al final de una variable crean tuplas, por tanto hacerlas explicitamente es mejor .

# Bien
variable = ('123',)
mi_funcion(param1,
param2,
)

# Mal
variable = '123', # creará una tupla de forma implicita
mi_funcion(param1, param2,) # la ultima coma sobra

Otra buena razon por la que en listas y tuplas es bueno dejar la coma al final, si el lenguaje lo soporta, es para que cuando se editen añadiendo nuevos elementos, no se modifica la línea que ya existia, dejando intacto el historial de cambios .

Comentarios 

La PEP 8 contempla muchas reglas sobre cómo tratar los comentarios que se pueden ver a continuación:

Los comentarios pueden ser contradictorios, y requiren que se actualicen con el código, por tanto si se pueden evitar haciendo código más claro, mejor.

Deben de componerse de frases completas.

Deben de comenzar en mayuscula a no ser que comiencen con el nombre de un identificador, el cual se respetará siempre su tamaño.

Los bloques de comentarios se componen de varios parrafos terminados en puntos, y terminar en dos espacios en blancos salvo la ultima frase.

Los comentarios deben de ser en Ingles a no ser “que se esté 120%” seguro de que se leeran siempre en otro idioma y serán claros.

Los bloques se aplican al código justo despues de donde se encuentran y con la misma indentación.

Los comentarios de línea comienzan con al menos 2 espacios y un # y un espacio después.

Las cadenas de documentacion (docstrings) deben de añadirse en clases, funciones y métodos que sean públicos siguiendo el PEP 257 .

# Comentario de una línea antes del código principal
def funcion(primer_parametro, segundo_parametro):
"""Docstring para describir qué hace la función

primer_parametro -- descripcion del primer parámetro
segundo_parametro -- descripcion del segundo parámetro
"""
pass

Convenciones de nombres 

Las siguientes reglas aplican para los nombres de cada tipo de objeto.

Caracteres a evitar : o, O, l y L (letra O y letra L) dado que se pueden confundir con un 0 o un 1 dependiendo del tipo de fuente usada.

Caracteres ASCII : se utilizan en la librería estándar siempre.

Nombre de modules y paquetes : se escriben en minúsculas y se desaconseja el uso de barras bajas, manteniendo los nombres lo más cortos posibles.

Nombrado de clases : se usan el FormatoCapital, donde la primera letra de cada palabra es mayúscula.

Nombres de tipos de variables : en FormatoCapital.

Excepciones : igual que el de clases pero con el sufijo “Error”.

Nombres de variables y funciones : se usan palabras en minúscula separadas por barras bajas.

Métodos en clases : el primer parámetro para métodos de instancia es self y para métodos de clase cls .

Constantes : en mayúsculas.

from vehiculos import Coche

MAXIMO_AVANZAR = 500

class LimiteDeKilometrosAlcanzadoError(Exception):
pass

class Saet(Coche):
posicion = 0

def avanza(self, num_km):
nueva_posicion += num_km

if nueva_posicion > MAXIMO_AVANZAR:
self.posicion = MAXIMO_AVANZAR
raise LimiteDeKilometrosAlcanzadoError
else:
self.posicion = nueva_posicion

-->

Anotaciones de variables 

Desde la PEP 526 se introdujeron las anotaciones para las variables y se escriben como:

Declaracion : <nombre_variable>: <tipo>

Declaracion + inicializacion : <nombre_variable>: <tipo> = <valor_por_defecto>

# Bien
num_patas: int

class Coche:
num_ruedas: int = 4

# Mal
num_patas:int

class Coche:
num_ruedas: int=4

¿Como detectar errores de PEP 8 automáticamente? 

Existen librerías que permite detectar errores/violaciones de reglas del PEP 8 denominadas linters y suelen estar incluidas en IDEs de Python (por ejemplo en PyCharm )

Algunos IDEs actuales pueden sugerir el cambio necesario automáticamente antes de realizar un commit en Git.

Se puede utilizar el programa pycodestyle (anteriormente llamado pep8), para comprobar si el código sigue las reglas de correctamente. Este programa se puede instalar usando pip y ejecutarse en consola sobre cualquier módulo python.

$ pip install pycodestyle
$ pycodestyle --first nombre_fichero.py
...
$ pycodestyle --show-source --show-pep8 nombre_fichero.py
...
$ pycodestyle --statistics -qq nombre_fichero.py
...

Libros recomendados para aprender Python 

Estos son los libros que pueden ayudarte a aprender Python, aprender a programar, tipos de datos, algoritmia y mucho más.

Disponible en: Marcombo Amazon 

Ver en Kindle Amazon 

Ver en Kindle Amazon 

Ver en Kindle Amazon 

Ver en Kindle Amazon 

Ver en Kindle Amazon 

Ver en Kindle Amazon 

Ver en Kindle Amazon 

Ver en Kindle Amazon 

-->

Scripts en Python 

Scripts en Python 

¿Qué es Python? 

¿Qué es Python? 

Usar la shell de Python (REPL Python) 

Usar la shell de Python (REPL Python) 

¿Cómo instalar Python? 

¿Cómo instalar Python? 

Categorías: Fundamentos ​ Tutorial Python 

Etiquetas: primeros pasos tutorial python 

Compartir

Compartir en Twitter 

Guardar en Hatena Bookmark 

Compartir en LINE 

Compartir en Facebook 

Guardar en Pocket 

Suscribirse en Feedly 

Entradas relacionadas

Fundamentos / Tutorial Python 

Tuplas en Python – tuple 

Fundamentos / Tutorial Python 

¿Qué es Python? 

Desarrollo de Escritorio / Desarrollo Web / Herramientas 

PyCharm – El IDE de Python para profesionales 

Fundamentos / Tutorial Python 

Listas y matrices en Python – list 

3 respuestas

Comentarios 1 

Pingbacks 2 

RAUL SANCAR dice: 

2023-01-11 a las 20:14 

Me gusta mucho el orden y entre más lejible el código mejor. Siendo sincero uitlizo sólo la regla de los 4 espacios para todos los lenguajes de programación, pero desde hoy utilizaré la identación también para comentarios y documentación.

Responder 

Pingback: ▷ ¿Qué es Python? - El Pythonista 

Pingback: ▷ Variables en Python - El Pythonista 

Deja una respuesta Cancelar la respuesta 

Tu dirección de correo electrónico no será publicada. Los campos obligatorios están marcados con * 

Comentario * 

Nombre * 

Correo electrónico * 

Web 

Guarda mi nombre, correo electrónico y web en este navegador para la próxima vez que comente. 

Publicar un comentario 

Entradas recientes

Gracias por seguir formando parte de El Pythonista 

PyQuiz 21 – upper() y count() en Python 

PyQuiz 20 – range() parámetros en Python 

PyQuiz 19 – append vs extend en Python 

PyQuiz 18 – f-strings vs format() en Python 

Categorías

Basics 

Books 

Desarrollo de Escritorio 

Desarrollo Web 

Desktop Development 

Eventos 

Fundamentos 

Herramientas 

Libros 

PyQuiz 

PyQuizzes 

Python Tutorial 

Tools 

Tutorial Python 

Uncategorized 

Web Development 

Servicios de El Pythonista 

Contacto 

Sobre El Pythonista 

Política de Cookies 

Política de Privacidad 

Aviso Legal 

Idioma 

Mentorías
