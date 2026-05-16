# Guía para principiantes: regresión lineal en Python con scikit-learn

Fuente: [DataSource.ai](https://www.datasource.ai/es/data-science-articles/una-guia-para-principiantes-sobre-la-regresion-lineal-en-python-con-scikit-learn)  
_Copia local para lectura fuera de línea. El formato original puede verse en la URL._

---

Hay dos tipos de algoritmos de aprendizaje supervisado de machine learning: Regresión y clasificación. El primero predice salidas de valores continuos mientras que el segundo predice salidas discretas. Por ejemplo, predecir el precio de una casa en dólares es un problema de regresión mientras que predecir si un tumor es maligno o benigno es un problema de clasificación.

Puedes leer más artículos de Data Science en español aquí 

En este artículo estudiaremos brevemente qué es la regresión lineal y cómo puede aplicarse tanto a dos variables como a múltiples variables utilizando Scikit-Learn , que es una de las bibliotecas de machine learning más populares para Python.

Fuente 

Teoría de la Regresión Lineal 

El término "linealidad" en álgebra se refiere a una relación lineal entre dos o más variables. Si dibujamos esta relación en un espacio bidimensional (entre dos variables), obtenemos una línea recta.

La regresión lineal realiza la tarea de predecir el valor de una variable dependiente (y) basándose en una variable independiente dada (x). Así, esta técnica de regresión encuentra una relación lineal entre x (entrada),  y (salida). Por lo tanto, el nombre es Regresión Lineal. Si trazamos la variable independiente (x) en el eje x y la variable dependiente (y) en el eje y, la regresión lineal nos da una línea recta que se ajusta mejor a los puntos de datos, como se muestra en la figura siguiente.

Sabemos que la ecuación de una línea recta es básicamente:

Y= mx + b 

“Donde b es el intercepto y m es la pendiente de la línea. Así que básicamente, el algoritmo de regresión lineal nos da el valor más óptimo para la intercepción y la pendiente (en dos dimensiones). Las variables y y x siguen siendo las mismas, ya que son las características de los datos y no pueden cambiarse. Los valores que podemos controlar son el intercepto(b) y la pendiente(m). Puede haber múltiples líneas rectas dependiendo de los valores de intercepción y pendiente. Básicamente lo que hace el algoritmo de regresión lineal es ajustar múltiples líneas en los puntos de datos y devolver la línea que da como resultado el menor error.” 

Este mismo concepto puede extenderse a los casos en que hay más de dos variables. Esto se llama regresión lineal múltiple. Por ejemplo, considera un escenario en el que tienes que predecir el precio de la casa basado en su área, número de habitaciones, el ingreso promedio de la gente en el área, la edad de la casa, y así sucesivamente. En este caso, la variable dependiente (variable objetivo) depende de varias variables independientes. Un modelo de regresión con múltiples variables puede representarse como:

y = b0 + m1b1 + m2b2 + m3b3 + ... ... mnbn 

Esta es la ecuación de un hiperplano . Recuerde, un modelo de regresión lineal en dos dimensiones es una línea recta; en tres dimensiones es un plano, y en más de tres dimensiones, un hiperplano.

En esta sección, veremos cómo la biblioteca Scikit-Learn de Python para el aprendizaje automático puede utilizarse para implementar funciones de regresión. Empezaremos con una regresión lineal simple que involucra dos variables y luego pasaremos a la regresión lineal que involucra múltiples variables.

Regresión lineal simple 

Regresión lineal simple 

Mientras exploraba el dataset de las operaciones de bombardeo aéreo de la Segunda Guerra Mundial y recordaba que los aterrizajes del Día D fueron casi pospuestos debido al mal tiempo, descargue estos informes meteorológicos del período para compararlos con el dataset de las misiones en las operaciones de bombardeo.

Puede descargar el conjunto de datos desde aquí .

El conjunto de datos contiene información sobre las condiciones meteorológicas registradas cada día en varias estaciones meteorológicas de todo el mundo. La información incluye precipitaciones, nevadas, temperaturas, velocidad del viento y si el día incluyó tormentas eléctricas u otras malas condiciones meteorológicas.

Así que nuestra tarea es predecir la temperatura máxima tomando como entrada la temperatura mínima.

Puedes leer más artículos de Data Science en español aquí 

Empecemos a escribir código:

Importar todas las bibliotecas necesarias :

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as seabornInstance 
from sklearn.model_selection 
import train_test_splitfrom sklearn.linear_model 
import LinearRegressionfrom sklearn import metrics%matplotlib inline

El siguiente comando importa el dataset en CSV usando pandas:

dataset = pd.read_csv('/Users/nageshsinghchauhan/Documents/projects/ML/ML_BLOG_LInearRegression/Weather.csv')

Vamos a explorar la información de a poco, chequeando primero el número de filas y columnas en nuestro dataset

dataset.shape

Debería recibir un output como (119040, 31), que significa que la información contiene 119040 filas y 31 columnas.

Para ver los detalles estadísticos del dataset, podemos usar: describe()

dataset.describe()

Vista estadística del dataset

Y finalmente, vamos a graficar nuestros puntos de datos en un diagrama en dos dimensiones para ilustrar nuestro dataset y ver si manualmente podemos encontrar alguna relación entre los datos usando el siguiente código:

dataset.plot(x='MinTemp', y='MaxTemp', style='o') plt.title('MinTemp vs MaxTemp') 
plt.xlabel('MinTemp') 
plt.ylabel('MaxTemp') 
plt.show()

Hemos tomado “MinTemp” y “MaxTemp” para hacer nuestro análisis. Abajo hay un gráfico en 2 dimensiones entre MinTemp y MaxTemp.

Vamos a chequear la temperatura promedio máxima y una vez la ploteamos podemos observar que la temperatura promedio máxima está entre cerca de 25 y 35

plt.figure(figsize=(15,10))
plt.tight_layout()
seabornInstance.distplot(dataset['MaxTemp'])

Temperatura promedio máxima la cual está entre 25 y 35

 

Nuestro siguiente paso es dividir nuestros datos en “atributos” y “etiquetas”.

Los atributos son las variables independientes,  mientras que las etiquetas son las variables dependientes cuyos valores se deben predecir. En nuestro conjunto de datos, sólo tenemos dos columnas. Queremos predecir el “MaxTemp” dependiendo del MinTemp registrado. Por lo tanto, nuestro conjunto de atributos consistirá en la columna "MinTemp" que se almacena en la variable X, y la etiqueta será la columna "MaxTemp" que se almacena en la variable y.

X = dataset['MinTemp'].values.reshape(-1,1)
y = dataset['MaxTemp'].values.reshape(-1,1)

A continuación, dividimos el 80% de los datos al conjunto de entrenamiento mientras que el 20% de los datos al conjunto de pruebas usando el código de abajo.

Puedes leer más artículos de Data Science en español aquí 

La variable test_size es nos permite definir  la proporción del conjunto de pruebas.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

Después de dividir los datos en conjuntos de entrenamiento y pruebas, finalmente, es el momento de entrenar nuestro algoritmo. Para ello, necesitamos importar la clase LinearRegression, instanciarla y llamar el método fit() junto con nuestros datos de entrenamiento.

regressor = LinearRegression() 
regressor.fit(X_train, y_train) #Entrena el algoritmo 

Como hemos discutido, el modelo de regresión lineal básicamente encuentra el mejor valor para la intercepción y la pendiente, lo que resulta en la línea que mejor se ajusta a los datos. Para ver el valor de la intercepción y la pendiente calculado por el algoritmo de regresión lineal para nuestro conjunto de datos, ejecute el siguiente código.

#Para obtener el intercepto:
print(regressor.intercept_)
#Para obtener la pendiente
print(regressor.coef_)

El resultado debe ser aproximadamente 10.66185201 y 0.92033997 respectivamente.

Esto significa que por cada unidad de cambio en la temperatura mínima, el cambio en la temperatura máxima es de alrededor de 0,92%.

Ahora que hemos entrenado nuestro algoritmo, es hora de hacer algunas predicciones. Para ello, utilizaremos los datos de nuestras pruebas y veremos con qué precisión nuestro algoritmo predice la puntuación porcentual. Para hacer predicciones sobre los datos de la prueba, ejecute el siguiente código:

df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
df

 

Comparación del valor real y el predecido 

También podemos visualizar el resultado de la comparación como un gráfico de barras usando el siguiente código:

Nota: Como el número de registros es enorme, para fines de representación sólo tomo 25 registros.

df1 = df.head(25)
df1.plot(kind='bar',figsize=(16,10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

Gráfico de barras mostrando la comparación de valores reales y predecidos 

Aunque nuestro modelo no es muy preciso, los porcentajes predichos se acercan a los reales.

Vamos a trazar nuestra línea recta con los datos de la prueba:

plt.scatter(X_test, y_test, color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.show()

Predicción vs datos de prueba

La línea recta del gráfico anterior muestra que nuestro algoritmo es correcto. El paso final es evaluar el desempeño del algoritmo. Este paso es especialmente importante para comparar el rendimiento de los diferentes algoritmos en un determinado dataset.  Para los algoritmos de regresión, se utilizan comúnmente tres métricas de evaluación:

1. Error absoluto medio  (MAE: Mean Absolute Error) es la media del valor absoluto de los errores. Se calcula como:

Error absoluto medio 

2.  Error cuadrático medio: (MSE: Mean Squared Error) es la media de los errores al cuadrado y se calcula como:

Error cuadrático medio

3. Raíz del error cuadrático medio: (RMSE: Root Mean Squared Error ) es la raíz cuadrada de la media del error al cuadrado

Raíz del error cuadrático medio

Por suerte, no tenemos que hacer estos cálculos manualmente. La biblioteca de Scikit-Learn viene con funciones pre construidas que pueden ser usadas para averiguar estos valores por nosotros.
Encontremos los valores de estas métricas usando nuestros datos de prueba.

print('Error Absoluto Medio:',metrics.mean_absolute_error(y_test, y_pred)) 
print('Error Cuadratico Medio:', metrics.mean_squared_error(y_test, y_pred)) 
print('Raíz del error cuadrático medio:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

Debería recibir esta salida (pero probablemente un poco diferente):
('Error Absoluto Medio:', 3.19932917837853)
('Error Cuadratico Medio:', 17.631568097568447)
('Raíz del error cuadrático medio:', 4.198996082109204)

Se puede ver que el valor Raíz del error cuadrático medio 4,19, lo cual es más del 10% del valor medio de los porcentajes de toda la temperatura, es decir, 22,41. Esto significa que nuestro algoritmo no fue muy preciso pero aún así puede hacer predicciones razonablemente buenas.

Puedes leer más artículos de Data Science en español aquí 

Regresión lineal múltiple 

Fuente 

Acabamos de realizar una regresión lineal en la sección anterior que involucra dos variables. Casi todos los problemas del mundo real con los que te vas a encontrar tendrán más de dos variables. La regresión lineal que involucra múltiples variables se llama "regresión lineal múltiple" o regresión lineal multivariable. Los pasos para realizar la regresión lineal múltiple son casi similares a los de la regresión lineal simple. La diferencia radica en la evaluación. Se puede utilizar para averiguar qué factor tiene el mayor impacto en el resultado previsto y cómo se relacionan las diferentes variables entre sí.

En esta sección, he descargado un dataset de la calidad del vino tinto. El dataset corresponde a las variantes rojas del vino portugués " Vinho Verde" . Debido a cuestiones de privacidad y logística, sólo se dispone de variables físico-químicas (los insumos) y sensoriales (el producto) (por ejemplo, no hay datos sobre los tipos de uva, la marca del vino, el precio de venta del vino, etc.).

 

Puede descargar el conjunto de datos desde aquí .

Tendremos en cuenta varios atributos de entrada como acidez fija, acidez volátil, ácido cítrico, azúcar residual, cloruros, dióxido de azufre libre, dióxido de azufre total, densidad, pH, sulfatos, alcohol. Basándonos en estos atributos predeciremos la calidad del vino.

 

Ahora, empecemos a codificar:

Importar todas las librerías requeridas:
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
%matplotlib inline

 

El siguiente comando importa el conjunto de datos del archivo que has descargado a través del enlace de arriba:

dataset = pd.read_csv('/Users/nageshsinghchauhan/Documents/projects/ML/ML_BLOG_LInearRegression/winequality.csv')

Exploremos un poco los datos comprobando el número de filas y columnas en él dataset

dataset.shape

Dará (1599, 12) como salida lo que significa que nuestro conjunto de datos tiene 1599 filas y 12 columnas.

Para ver los detalles estadísticos del conjunto de datos, podemos usar describe():

dataset.describe()

Limpiemos un poco nuestros datos, así que primero comprobemos cuáles son las columnas que contienen valores NaN (Que no son un número)

dataset.isnull().any()

Una vez que el código anterior se ejecuta, todas las columnas deben dar False, en caso de que para cualquier columna se encuentre el resultado True, entonces se eliminan todos los valores nulos de esa columna usando el código siguiente
dataset = dataset.fillna(method='ffill')

Nuestro siguiente paso es dividir los datos en "atributos" y "etiquetas". La variable X contiene todos los atributos/características y la variable Y contiene las etiquetas.

X = dataset[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates','alcohol']].values
y = dataset['quality'].values

Comprobemos el valor medio de la columna "calidad".

plt.figure(figsize=(15,10))
plt.tight_layout()
seabornInstance.distplot(dataset['quality'])

Valor promedio de la calidad del vino

 

Como podemos observar, la mayoría de las veces el valor es 5 o 6. A continuación, dividimos el 80% de los datos para el conjunto de entrenamiento y  el 20% de los datos al conjunto de pruebas usando el código de abajo.

Puedes leer más artículos de Data Science en español aquí 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

Ahora vamos a entrenar nuestro modelo

regressor = LinearRegression() 
regressor.fit(X_train, y_train)

Como se ha dicho antes, en el caso de la regresión lineal multivariable, el modelo de regresión tiene que encontrar los coeficientes más óptimos para todos los atributos. Para ver qué coeficientes ha elegido nuestro modelo de regresión, ejecute el siguiente código:

coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient']) 
coeff_df

Debe dar como resultado una salida como la siguiente:

“Esto significa que para un aumento de una unidad en la "densidad", hay una disminución de 31,51 unidades en la calidad del vino. Del mismo modo, la disminución en una unidad de los  "Cloruros" resulta en un aumento de 1,87 unidades en la calidad del vino. Podemos ver que el resto de los atributos tienen muy poco efecto en la calidad del vino.”

Ahora hagamos una predicción sobre los datos de la prueba.

y_pred = regressor.predict(X_test)

Revisemos la diferencia entre el valor real y el valor previsto.

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df1 = df.head(25)

Comparación entre el valor real y el valor predecido

Ahora vamos a graficar la comparación de los valores reales y los predecidos

df1.plot(kind='bar',figsize=(10,8))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

Gráfico de barras mostrando las diferencias entre los valores reales y los predecidos

Como podemos observar aquí, nuestro modelo ha dado muy buenos resultados de predicción.
 El paso final es evaluar el rendimiento del algoritmo. Lo haremos encontrando los valores de MAE , MSE y RMSE . Ejecute el siguiente código:

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred)) 
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred)) 
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

El resultado se ve así:
('Mean Absolute Error:', 0.46963309286611077)
('Mean Squared Error:', 0.38447119782012446)
('Root Mean Squared Error:', 0.6200574149384268)
Se puede ver que el valor de la raíz del error cuadrático medio es de 0,62, que es ligeramente superior al 10% del valor de la media que es de 5,63. Esto significa que nuestro algoritmo no fue muy preciso pero aún así puede hacer predicciones razonablemente buenas.

Hay muchos factores que pueden haber contribuido a esta inexactitud, por ejemplo:

1. Necesita más datos: Necesitamos una gran cantidad de datos para obtener la mejor predicción posible.
2. Malas suposiciones: Hicimos la suposición de que estos datos tienen una relación lineal, pero puede que no sea así. Visualizar los datos puede ayudar a determinar eso.

3. Atributos pobres: Los atributos  que usamos pueden no tener una correlación lo suficientemente alta con los valores que tratamos de predecir.

Puedes leer más artículos de Data Science en español aquí 

Conclusión

En este artículo, estudiamos los algoritmos de machine learning más fundamentales, es decir, la regresión lineal. Implementamos tanto la regresión lineal simple como la regresión lineal múltiple con la ayuda de la biblioteca de aprendizaje automático de Scikit-Learn.
Espero que hayan disfrutado de la lectura. Háganme saber sus dudas/sugerencias en la sección de comentarios.
Gracias por la lectura.

También pueden contactarme en LinkedIn .
Feliz Aprendizaje!!
Este artículo también está publicado en KDnuggets.
