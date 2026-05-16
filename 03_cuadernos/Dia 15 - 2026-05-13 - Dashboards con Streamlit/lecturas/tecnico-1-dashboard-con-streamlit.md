# Dashboard con Streamlit

Fuente: [El Libro de Python](https://ellibrodepython.com/dashboard-streamlit)  
_Copia local para lectura fuera de línea. El formato original puede verse en la URL._

---

El Libro De Python 

🇪🇸 Español 🇺🇸 English 

🐍 El Libro De Python 🐍 
🕺🏻 01. Introducción 
📗 ¿Qué es Python? 
📗 Descargar e instalar Python 
📗 Hola Mundo en Python 
📗 Sintaxis Básica 
📗 Nombrando variables I 
📙 Palabras reservadas 
📙 Alcance variables 
📙 Ejecutando scripts 
📙 Tipado dinámico y duck typing 
📙 Funciones built-in 
📙 Unpacking en Python 
🏄🏻‍♀️ 02. Estructuras de control 
📗 Condicional if 
📗 Bucle for 
📗 Range 
📗 Bucle while 
📙 Switch 
📙 Match 
📙 Break 
📙 Continue 
📙 Iterar con zip 
📙 Iterar con enumerate 
📙 List comprehensions 
📕 Iteradores e Iterables 
📦 03. Tipos y estructuras 
📗 Entero o int 
📗 Booleano 
📗 Float 
📗 Números complejos 
📗 Cadenas o strings 
📗 Listas 
📙 Set 
📙 Tupla o tuple 
📙 Diccionario 
📙 Frozenset 
📙 Castings 
📙 Colecciones 
📙 Mutabilidad 
🕹 04. Funciones 
📗 Funciones en Python 
📙 Paso por valor y referencia 
📙 Uso de args y kwargs 
📙 Anotaciones en Funciones 
📙 Funciones Lambda 
📙 Recursividad 
📕 Decoradores 
📕 Generadores 
📕 Corrutinas 
📕 Caching Funciones 
📕 Programación Funcional 
➗ 05. Operadores 
📗 Operadores de asignación 
📗 Operadores Aritméticos 
📗 Operadores Relacionales 
📗 Operadores Lógicos 
📙 Operadores Bitwise 
📙 Operadores Identidad 
📙 Operadores Membresía 
📙 Operador walrus 
🏄‍♂️ 06. Programación orientada a objetos 
📗 Programación Orientada a Objetos 
📙 Tipos de métodos 
📙 Herencia 
📙 Decorador Property 
📙 Métodos dunder o mágicos 
📕 Sobreescribiendo métodos mágicos 
📕 Interfaces y Abstract Base Class 
🛠 07. Excepciones 
📗 Excepciones en Python 
📗 Uso del assert() 
📙 Definiendo Excepciones 
📕 Context Managers 
📥 08. Ficheros 
📙 Leer archivos 
📙 Escribir archivos 
🚀 09. Test y Documentación 
📙 Python PEP8 
📙 Nombrando Variables 
📙 Argparse en Python 
📙 Errores Comunes 
📙 Código Pythonico 
📙 Testing con assert y unittest 
🔬 10. Top 50 Ejemplos y Ejercicios 🆕 
📙 Firma digital con cryptography 
📙 Encriptar mensaje con cryptography 
📙 Determina si un número es primo 
📙 Factoriza un número en primos 
📙 Computación cuántica con qiskit 
📙 Fuerza bruta con itertools 
📙 Acortador de enlaces con flask 
📙 Construye una API con flask 
📙 Trabaja con ficheros con os 
📙 Bases de datos con sqlite 
📙 Pattern matching con re 
📙 Analítica de futbol con seaborn 
📙 Programar tareas 
📙 Gráficas con matplotlib 
📙 Redes neuronales con tensorflow 
📙 Logging y verbosity 
📙 Cálculo simbólico con sympy 
📙 Crear juego con pygame 
📙 Scrapping web con beautifulsoup 
📙 Unir pdfs pdf 
📙 Excels con pyexcel 
📙 Benchmark de funciones 
📙 Rotar imagen con scikit-image 
📙 Simulaciones simpy 
📙 Coordenadas y distancia con geopy 
📙 Genética y ADN con biopython 
📙 Moléculas con rdkit 
📙 Polinomios con numpy 
📙 Simular apuestas con numpy 
📙 Monte Carlo con numpy 
📙 Análisis financiero con yfinance 
📙 Programación asincrona con aiohttp 
📙 Baraja de Poker 
📙 Barajar cartas con shuffle 
📙 Ordenar con bubble sort 
📙 Convertir binario a decimal 
📙 Código C en Python 
📙 Martingala y apuestas 
📙 Temporizador con time 
📙 Calcular impuestos 
📙 Plot interactivo con bokeh 
📙 Simular hipoteca 
📙 El Quijote con wordcloud 
📙 Programas ejecutables con pyinstaller 
📙 Calcular interés compuesto 
📙 Busca el número que falta 
📙 Comprimir información 
📙 Interfaz de usuario con pyqt 
📙 Dashboard con streamlit 
📙 Problema de la mochila 

Contenido

Dashboard con streamlit 

El Libro De Python ( 24.95 € ) 📂 Comprar Ebook 

Contenido

Dashboard con streamlit 
🔬 10. Top 50 Ejemplos y Ejercicios 🆕 
📙 Dashboard con streamlit 

Dashboard con streamlit

Con streamlit podemos crear paneles de mando o dashboards con diferentes representaciones gráficas. En este ejemplo usamos datos de la esperanza de vida en diferentes países, y permitimos al usuario seleccionar diferentes países para comparar su esperanza de vida.

Como puedes ver el código es bien sencillo:

💾 Primero cargamos los datos usando pandas . Realizamos un pequeño procesado de las columnas.
📊 Usamos multiselect para permitir al usuario seleccionar diferentes países.
✅ Usamos line_chart para representar gráficamente la esperanza de vida de los países seleccionados. 

import streamlit as st 
import pandas as pd 
df = pd . read_csv ( " esperanza_vida.csv " , skiprows = 3 ) 

st . title ( " 🌎 Esperanza de Vida Mundial " ) 

df = df [[ ' Country Name ' ] + [ str ( year ) for year in range ( 1960 , 2023 )]] 
df . set_index ( ' Country Name ' , inplace = True ) 

p = st . multiselect ( " ✅ Selecciona países " , df . index ) 
st . line_chart ( df . loc [ p ]. T ) 

Y podemos ejecutar el código de esta manera.

streamlit run dashboard_streamlit . py 

Si en tu navegador introduces la siguiente dirección, podrás ver el resultado:

🔗  http://localhost:8501/ 
✏️ Ejercicios:

Representa el histograma de la esperanza de vida de todos los países y como evoluciona a lo largo de los años. 

Anterior 
📕 Corrutinas 

Siguiente 📕 Programación Funcional 

Nuestra tienda Colabora Canal de telegram 

Política de privacidad Términos y condiciones Contacta con nosotros 

Copyright © El Libro De Python. All Rights Reserved
