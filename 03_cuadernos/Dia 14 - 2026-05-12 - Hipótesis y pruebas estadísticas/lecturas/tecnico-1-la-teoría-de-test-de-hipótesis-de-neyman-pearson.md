# La teoría de test de hipótesis de Neyman-Pearson

Fuente: [Estadística Básica Edulcorada · A. Quintela (bookdown)](https://bookdown.org/aquintela/EBE/la-teoria-de-test-de-hipotesis-de-neyman-pearson.html)  
_Copia local para lectura fuera de línea. El formato original puede verse en la URL._

---

8.4 La teoría de test de hipótesis de Neyman-Pearson | Estadística Básica Edulcorada 
























































































Estadística Básica Edulcorada 





Prólogo 


1 Introducción 

1.1 Antecedentes históricos: de la aritmética política a la estadística 


1.2 Variabilidad y correlación 

1.2.1 Curiosidad para cinéfilos 






2 Estadística descriptiva 

2.1 Los censos 


2.2 Proceso científico del análisis estadístico 


2.3 Población 


2.4 Variables y Atributos 


2.5 Variables discretas y continuas 


2.6 Distribuciones de frecuencias 

2.6.1 Gráficos para variables discretas o categóricas 




2.7 Variables continuas 

2.7.1 Histograma de Frecuencias. 


2.7.2 Estimación tipo núcleo de la función de densidad 




2.8 Medidas características de una variable 

2.8.1 Medidas de posición o de tendencia central 


2.8.2 Medidas de dispersión 


2.8.3 La Varianza y la desviación típica 


2.8.4 Recorrido 


2.8.5 Recorrido intercuartílico. 


2.8.6 Coeficiente de variación 


2.8.7 Simetría 


2.8.8 Curtosis 


2.8.9 Tipificación de una variable 


2.8.10 Tamaño del efecto 


2.8.11 Diagrama de caja (Box-Plot) 






3 Descriptiva dos-dimensional 

3.1 Distribución conjunta de caracteres 


3.2 Estructura de la información en variables bidimensionales 


3.3 Representaciones gráficas 


3.4 Dependencia e Independencia estadística. 


3.5 Dependencia estadística entre variables 

3.5.1 Diagrama de dispersión. 


3.5.2 Covarianza. Correlación lineal. 


3.5.3 Coeficiente de Correlación lineal (Pearson) 


3.5.4 Ajuste y regresión bidimensional 


3.5.5 El caso lineal 


3.5.6 El origen del término “regresión” 






4 Probabilidad 

4.1 Introducción histórica 


4.2 La geometría del azar 


4.3 El sentido estadístico-probabilista de la actualidad 


4.4 La familia Bernoulli 


4.5 Laplace 


4.6 desde Poisson hasta Kolmogorov 


4.7 Experimentos aleatorios 


4.8 Definiciones básicas 

4.8.1 Suceso elemental. 


4.8.2 Suceso. 


4.8.3 Diagramas de Venn 


4.8.4 Suceso imposible. 


4.8.5 Unión de sucesos 


4.8.6 Intersección de sucesos 


4.8.7 Sucesos incompatibles 


4.8.8 Diferencia de sucesos 


4.8.9 Complementario de un suceso 




4.9 Probabilidad 


4.10 ¿Cómo se asignan probabilidades a los sucesos? 

4.10.1 Asignación equiprobable 


4.10.2 Asignación frecuentista 




4.11 Propiedades de la probabilidad 


4.12 Probabilidad condicionada 


4.13 Independencia de sucesos 

4.13.1 Regla del producto 




4.14 Regla de Bayes 


4.15 Teorema de la probabilidad total (Laplace) 


4.16 Teorema de Bayes (Versión de Laplace) 


4.17 Notas históricas. La estadística Bayesiana 

4.17.1 Aprendiendo de la experiencia: uso recursivo de la fórmula de Bayes 


4.17.2 Ejemplos importantes de aplicación de la estadística Bayesiana 




4.18 La falacia del fiscal 


4.19 Sobre la formación correcta de jurados. 


4.20 El caso Dreyfuss 

4.20.1 Curiosidad histórica 




4.21 Problemas de paradojas 

4.21.1 Problema de Monty Hall 


4.21.2 Paradoja de los hijos 


4.21.3 Problema del prisionero (Hardin, 1968). 


4.21.4 Paradoja de la caja de Bertrand, o Gold-Silver box (Bertrand, 1988). 






5 Variables aleatorias 

5.1 Tipos de variables aleatorias 


5.2 Variables aleatorias discretas 


5.3 Variables aleatorias continuas 

5.3.1 Función de densidad 




5.4 Esperanza Matemática de una variable aleatoria 


5.5 Varianza de una variable aleatoria 

5.5.1 La falacia del jugador 




5.6 Mediana y Cuantiles (o percentiles) 


5.7 La moda 


5.8 Variables discretas notables 

5.8.1 La variable de Bernoulli 


5.8.2 Variable Binomial 


5.8.3 Variable de Poisson 


5.8.4 Variable Binomial negativa 


5.8.5 Variable Hipergeométrica 




5.9 Variables aleatorias continuas notables 

5.9.1 Variable uniforme continua 


5.9.2 Variable exponencial 


5.9.3 Las leyes de potencias (power law) 






6 La Variable Normal o Gaussiana 

6.1 Ejemplos de la distribución normal 

6.1.1 La mecánica de los gases de Maxwell 


6.1.2 Los datos antropométricos en los seres humanos 


6.1.3 La morfología del cerebro 


6.1.4 Las características psico-sociales 


6.1.5 El consumo de petroleo, gas, electricidad, de una ciudad, un pais, en un determinado periodo de tiempo 


6.1.6 Los errores de medición 


6.1.7 Duración de un embarazo 


6.1.8 Velocidad de las Galaxias 


6.1.9 La ley de Farr de las epidemias 


6.1.10 Crecimiento de las plantas 


6.1.11 Votos en las elecciones: Putin contra Gauss 


6.1.12 Los seis grados de separación 


6.1.13 La psicofísica 




6.2 El papel de Quetelet en la relevancia de la distribución normal 


6.3 Para pensar un poco: El CI 


6.4 Reproductividad de la variable normal 


6.5 El teorema central del límite 

6.5.1 Para pensar un poco: genética. 




6.6 Las leyes de los grandes números 

6.6.1 Las matemáticas 




6.7 Variables aleatorias obtenidas a partir de la variable normal 

6.7.1 Variable Chi-cuadrado (Pearson) 


6.7.2 Variable t de Student 


6.7.3 Variable F de Fisher-Snedecor 






7 Introducción a la inferencia estadística 

7.1 Muestreo aleatorio simple: 


7.2 Estimación puntual 

7.2.1 Propiedades de los estimadores 


7.2.2 Propiedades de la media muestral 


7.2.3 El error estándar de la media (muestral). 


7.2.4 Propiedades de la cuasi-varianza (muestral) 


7.2.5 Propiedades de la proporción muestral 




7.3 Ejemplos de interés. 

7.3.1 El problema de los tanques alemanes 




7.4 Intervalos de confianza 

7.4.1 Interpretación 


7.4.2 Ejemplo: Meta-análisis de eficacia de Antidepresivos 




7.5 I.C. para la media de una población normal con varianza conocida 


7.6 I.C. desconociendo la desviación típica 


7.7 I.C. para una proporción 


7.8 Intervalo de confianza para la diferencia de proporciones. 


7.9 Intervalos para la comparación de dos poblaciones normales independientes. 


7.10 Intervalo de confianza para la diferencia de medias 


7.11 Intervalo de confianza para el cociente de varianzas 




8 Contrastes de hipótesis 

8.1 Introducción: conjeturas, cisnes negros, ciencia y falsacionismo 


8.2 Hipótesis estadísticas 


8.3 Test de significación (NHST) 


8.4 La teoría de test de hipótesis de Neyman-Pearson 


8.5 Contrastes paramétricos y no paramétricos 


8.6 Contrastes de hipótesis paramétricas 

8.6.1 Tipos de contrastes: bilaterales y unilaterales 


8.6.2 Pasos a seguir al realizar un contraste de hipótesis 


8.6.3 Para la media de una variable normal 


8.6.4 Si se conoce la desviación típica 


8.6.5 La prueba \(t\) 




8.7 Contraste para una proporción 


8.8 Contrastes para comparación de poblaciones 


8.9 Para el cociente de varianzas 

8.9.1 El poder de los gráficos 




8.10 Muestras pareadas o relacionadas 


8.11 Para la diferencia de proporciones 

8.11.1 Contrastes de normalidad 


8.11.2 Contrastes de independencia entre caracteres 




8.12 Problemas del nivel de significación 

8.12.1 Evidencia y descubrimientos en física 






Bibliografía 




Publicado con bookdown 
















Estadística Básica Edulcorada 















8.4 La teoría de test de hipótesis de Neyman-Pearson


Buscando fortalecer las bases lógicas de los test de significación de Fisher, Egon Pearson (1895-1980) (hijo de Karl Pearson) y Jerzy Neyman (1894-1981) idearon varias mejoras. El eje principal de su investigación era el siguiente interrogante: ¿qué hacer si se obtiene un resultado significativo en un test estadístico? Se rechaza la hipótesis nula, pero los test de significación no arrojaban ninguna pista sobre qué hipótesis elegir a cambio.











La teoría de Neyman-Pearson utilizó el NHST de Fisher y el \(p\) -valor como parte de un proceso formal de decisión . Así, plantearon una elección real entre dos hipótesis rivales. El contraste de hipótesis quedó convertido en un método para discernir entre dos hipótesis: la hipótesis nula y la hipótesis alternativa \(H_1\) .


Todo contraste de hipótesis conduce pues, a aceptar o rechazar la hipótesis nula planteada (aceptando, en este último caso, la hipótesis alternativa). Ahora bien, pueden darse las siguientes situaciones.



Se acepta la hipótesis nula siendo verdadera. Esta es una decisión correcta.



Se rechaza la hipótesis nula siendo falsa. Esta es otra situación correcta.



Se rechaza la hipótesis nula siendo verdadera. Estamos cometiendo un error, que se llama error de tipo uno . La probabilidad de cometer este error viene dada por el nivel de significación \(\alpha\) , fijado de antemano.



Se acepta la hipótesis nula siendo falsa. También cometemos un error, que se llama error de tipo II . La probabilidad de cometer este error se representa por \(\beta\) , y la probabilidad \(1-\beta\) se llama potencia del contraste , que cuantifica la probabilidad de rechazar la hipótesis nula cuando es falsa.








Figura 8.3: Posibles opciones en un test de hipótesis.





Veamos. Si tenemos una hipótesis nula: \(H_0\) : un tratamiento nuevo no es efectivo , frente a \(H_1:\) el tratamiento sí es efectivo siempre es posible construir más de un test de hipótesis para contrastar la hipótesis nula frente a la alternativa.


Por ejemplo, tiramos una moneda al aire. Si sale cara, aceptamos \(H_0\) . Si sale cruz, rechazamos \(H_1\) .


La probabilidad de cometer un error de tipo I es \(0.5\) , igual que la probabilidad de cometer un error de tipo II.


Si en vez de tirar una moneda tiramos un dado y decidimos mediante la regla: “aceptamos la hipótesis nula si sale un 1, la rechazamos si sale cualquier otro número”, la probabilidad de error de tipo I es \(5/6\) y la de error de tipo II es \(1/6\) .


Obviamente ambos test son bastante absurdos, pero nos sirve para ver que siempre existen test con sus correspondientes errores.






Figura 8.4: Ejemplos errores tipo I y II.








Un acusado ante un tribunal:


\(H_0: inocente\) 

\(H_1: culpable\) 




El error de tipo I es rechazar que es inocente, siéndolo .


El error de tipo II es rechazar que es culpable, cuando es inocente .


Si se ponen las hipótesis al revés: \(H_0: culpable\) frente a \(H_1: inocente\) se comprueba enseguida que los errores de tipo I y tipo II se permutan.





Una alarma de incendio. Cuando suena una alarma, ante un exceso de calor, o bien que un gamberro ha acercado un mechero al sensor (se ve en las películas), la alarma puede sonar y no haber fuego.


\(H_0: fuego\) 


\(H_1: no fuego\) 





El error de tipo I es rechazar que hay fuego, cuando en realidad lo hay . El error de tipo II es aceptar que hay fuego, cuando en realidad no lo hay .


Con estos dos ejemplos, podemos ver que no es posible disminuir simultáneamente la probabilidad de error de tipo I y la probabilidad de error de tipo II: una opción para no cometer errores de tipo I en el caso de un juicio sería declarar inocente a casi todo el mundo, lo cual conlleva a cometer muchos errores de tipo II. En el caso de la alarma, puede hacerse que el aparato no tenga demasiada sensibilidad, para que no haya falsas alarmas, pero esto puede hacer peligrar el hecho de que, ante un incendio de verdad, la alarma no se active.


Neyman y Pearson demostraron que, en bastantes circunstancias, una vez fijada la probabilidad \(\alpha\) de error de tipo I -esto es, una vez acotado el porcentaje de veces que tomaremos una decisión equivocada al rechazar la hipótesis nula cuándo es verdadera- es posible construir y utilizar contrastes de máxima potencia , es decir, contrastes que minimizan la probabilidad \(\beta\) , o de error de tipo II (o sea, maximizan la llamada potencia del test: su sensibilidad o capacidad para detectar que la hipótesis nula es falsa).


Este último párrafo seguro que apesta a matemáticas. Por si alguien no se había dado cuenta, para decidir entre dos hipótesis (la nula y la alternativa) podemos, habitualmente, realizar más de un test o proceso de decisión.


Supongamos que queremos elegir entre:


\(H_0: inocente\) frente a \(H_1: culpable\) 


podemos revisar las pruebas, interrogar a los testigos, etc. y tomar una decisión. Habrá una probabilidad de error de tipo I y una probabilidad de error de tipo II (1- potencia).


Pero se podría decidir simplemente tirando una moneda al aire. La probabilidad de cometer un error de tipo I es \(0.5\) . Igual que la potencia del test (1- probabilidad de error de tipo II).


Ahora, en vez de tirar una moneda tiramos un dado. Si sale el 1, decidimos que el acusado es culpable, y si no es inocente. La probabilidad de cometer un error de tipo I es \(1/6\) . La potencia es la probabilidad de rechazar la hipótesis nula siendo falsa, es decir \(5/6\) (el que el acusado sea inocente o culpable no va a influir en el resultado del lanzamiento de la moneda; son sucesos independientes).


Vemos que reglas de decisión diferentes ocasionan probabilidades de error diferentes. En una situación “seria”, las hipótesis a elegir son de tipo estadístico. La forma de decidir será alguna función también de tipo estadístico (va a ser una variable aleatoria). A partir de ella calcularemos las probabilidades de error.


Supongamos que hay \(2\) posibles formas de decidir ( \(2\) variables aleatorias). Neymann y Pearson dijeron que la mejor manera de decir entre ambas es mantener para ambas la misma probabilidad de error de tipo I, y luego elegir la que dé mayor potencia (o menor probabilidad de error de tipo II) (Mismo valor de \(\alpha\) , máxima potencia).


En un célebre resultado publicado en \(1933\) , Neyman y Pearson probaron que en el caso de hipótesis rivales simples (que asignan valores específicos al parámetro desconocido) existe automáticamente una clase de test óptimos, de bajo tamaño y máxima potencia: los basados en la razón de verosimilitudes. Los contrastes de hipótesis que se utilizan en los casos prácticos, cuando se quiere saber, por ejemplo, si un tratamiento es efectivo, o si una proporción en una muestra aproxima una proporción real (caso de una encuesta electoral) son los propuestos mediante la teoría de Neyman y Pearson.


Quiere esto decir que son los que, desde un punto de vista matemático, son mejores para decidir entre la hipótesis nula y alternativa. Ya hemos visto antes que podemos construir muchos procedimientos de decisión (por ejemplo, tirando una moneda al aire). Aunque se puedan pensar procedimientos matemáticos más correctos, los test de Neyman y Pearson son óptimos desde el punto de vista antes comentado.
