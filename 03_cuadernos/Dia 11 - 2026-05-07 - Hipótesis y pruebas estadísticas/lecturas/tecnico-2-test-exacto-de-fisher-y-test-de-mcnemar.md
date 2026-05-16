# Test exacto de Fisher y test de McNemar

Fuente: [Fisterra (metodología de investigación)](https://www.fisterra.com/formacion/metodologia-investigacion/asociacion-variables-cualitativas-test-exacto-fisher-test-mcnemar/)  
_Copia local para lectura fuera de línea. El formato original puede verse en la URL._

---

-->


A partir del 15 de junio de 2022, la aplicación de escritorio de Internet Explorer 11 ya no será compatible con ciertas versiones de Windows 10. Algunas características de Fisterra pueden no estar disponibles, por favor actualice su navegador a la última versión disponible 



















Identifíquese




Con su cuenta personal de Elsevier








Email/Usuario 





Contraseña 





Identificarse 




Compruebe si tine acceso institucional 

-->






¿Olvidó su contraseña? 














Email 









Enviar 








Si ha olvidado su email/usuario y/o contraseña, introduzca su dirección de correo y envíe el formulario. En breve recibirá un email con un enlace para restablecer su contraseña.
















¿No está suscrito? 







Prueba gratuita 










Suscríbase a Fisterra 




































¿Olvidó su contraseña?




Si ha olvidado su email/usuario y/o contraseña, introduzca su dirección de correo y envíe el formulario. En breve recibirá un email con un enlace para restablecer su contraseña.















Email 









Enviar 


































































Inicio 




Metodología de la Investigación 



Asociación de variables cualitativas: El test exacto de Fisher y el test de Mcnemar







Asociación de variables cualitativas: El test exacto de Fisher y el test de Mcnemar





Índice de contenidos




Inroducción 



La prueba de probabilidad exacta de Fisher 



El test de McNemar 



Anexo 



Bibliografía 



Autores 












Inroducción





Desde que Pearson introdujo el test de la en 1900, ésta se ha convertido en una herramienta de uso general para conocer si existe o no relación entre variables de tipo cualitativo. Sin embargo, su aplicación exige de ciertos requerimientos acerca del tamaño muestral que no siempre son tenidos en cuenta . La prueba es aplicable a los datos de una tabla de contingencia solamente si las frecuencias esperadas son suficientemente grandes. Del mismo modo, cuando los datos exhiben algún grado de dependencia, el test no será el método apropiado para contrastar la hipótesis nula de independencia. En este trabajo se introducirán la prueba exacta de Fisher y el test de McNemar como alternativa estadística al test cuando no se verifiquen las condiciones necesarias para su utilización . 

















La prueba de probabilidad exacta de Fisher





El test exacto de Fisher permite analizar si dos variables dicotómicas están asociadas cuando la muestra a estudiar es demasiado pequeña y no se cumplen las condiciones necesarias para que la aplicación del test sea adecuada. Estas condiciones exigen que los valores esperados de al menos el 80% de las celdas en una tabla de contingencia sean mayores de 5. Así, en una tabla 2x2 será necesario que todas las celdas verifiquen esta condición, si bien en la práctica suele permitirse que una de ellas muestre frecuencias esperadas ligeramente por debajo de este valor.

En situaciones como esta, una forma de plantear los resultados es su disposición en una tabla de contingencia de dos vías. Si las dos variables que se están considerando son dicotómicas, nos encontraremos con el caso de una tabla 2 x 2 como la que se muestra en la Tabla 1. El test exacto de Fisher se basa en evaluar la probabilidad asociada a cada una de las tablas 2 x 2 que se pueden formar manteniendo los mismos totales de filas y columnas que los de la tabla observada. Cada una de estas probabilidades se obtiene bajo la hipótesis nula de independencia de las dos variables que se están considerando.








Tabla 1. Tabla de contingencia general para la comparación de dos variables dicotómicas en el caso de grupos independientes. 











Característica A 











Característica B 



Presente 

Ausente 



Total







Presente 

a 

b 

a + b 





Ausente 

c 

d 

c + d 





Total 

a + c 

b + d 

n 









La probabilidad exacta de observar un conjunto concreto de frecuencias a, b, c y d en una tabla 2 x 2 cuando se asume independencia y los totales de filas y columnas se consideran fijos viene dada por la distribución hipergeométrica:







Esta fórmula se obtiene calculando todas las posibles formas en las que podemos disponer n sujetos en una tabla 2 x 2 de modo que los totales de filas y columnas sean siempre los mismos, (a+b), (c+d), (a+c) y (b+d).



La probabilidad anterior deberá calcularse para todas las tablas de contingencia que puedan formarse con los mismos totales marginales que la tabla observada. Posteriormente, estas probabilidades se usan para calcular valor de la p asociado al test exacto de Fisher. Este valor de p indicará la probabilidad de obtener una diferencia entre los grupos mayor o igual a la observada, bajo la hipótesis nula de independencia. Si esta probabilidad es pequeña (p<0.05) se deberá rechazar la hipótesis de partida y deberemos asumir que las dos variables no son independientes, sino que están asociadas. En caso contrario, se dirá que no existe evidencia estadística de asociación entre ambas variables.



En la literatura estadística, suelen proponerse dos métodos para el cómputo del valor de la p asociado al test exacto de Fisher. En primer lugar, podremos calcularlo sumando las probabilidades de aquellas tablas con una probabilidad asociada menor o igual a la correspondiente a los datos observados. La otra posibilidad consiste en sumar las probabilidades asociadas a resultados al menos tan favorables a la hipótesis alternativa como los datos reales. Este cálculo proporcionaría el valor de p correspondiente al test en el caso de un planteamiento unilateral. Duplicando este valor se obtendría el p-valor correspondiente a un test bilateral.



Para ilustrar la explicación anterior, supongamos que en una determinada población se desea averiguar si existen diferencias en la prevalencia de obesidad entre hombres y mujeres o si, por el contrario, el porcentaje de obesos no varía entre sexos. Tras ser observada una muestra de 14 sujetos se obtuvieron los resultados que se muestran en la Tabla 2.








Tabla 2. Tabla de contingencia para estudiar las diferencias en la prevalencia de obesidad entre sexos. Estudio de prevalencia sobre 14 sujetos. 

















Obesidad 











Sexo 



Sí 

No 



Total







Mujeres 

1 (a) 

4 (b) 

5 (a+b) 





Hombres 

7 (c) 

2 (d) 

9 (c+d) 





Total 

8 (a+c) 

6 (b+d) 

14 (n) 







En esta tabla a=1, b=4, c=7 y d=2. Los totales marginales son así a+b=5, c+d= 9, a+c=8 y b+d=6. La frecuencia esperada en tres de las cuatro celdas es menor de 5, por lo que no resulta adecuado aplicar el test , aunque sí el test exacto de Fisher. Si las variables sexo y obesidad fuesen independientes, la probabilidad asociada a los datos que han sido observados vendría dada por:














Tabla 3. Posibles combinaciones de frecuencias con los mismos totales marginales de filas y columnas que en la Tabla 2. 



























Obesidad 























Obesidad 



























Si 





No 























Si 





No 















(i) 





Mujeres 





0 





5 





5 





(iv) 





Mujeres 





3 





2 





5 















Hombres 





8 





1 





9 











Hombres 





5 





4 





9 





















8 





6 





14 

















8 





6 





14 









































































































































(ii) 





Mujeres 





1 





4 





5 





(v) 





Mujeres 





4 





1 





5 















Hombres 





7 





2 





9 











Hombres 





4 





5 





9 





















8 





6 





14 

















8 





6 





14 









































































































































(iii) 





Mujeres 





2 





3 





5 





(vi) 





Mujeres 





5 





0 





5 















Hombres 





6 





3 





9 











Hombres 





3 





6 





9 





















8 





6 





14 

















8 





6 





14 















La Tabla 3 muestra todas las posibles combinaciones de frecuencias que se podrían obtener con los mismos totales marginales que en la Tabla 2. Para cada una de estas tablas, se ha calculado la probabilidad exacta de ocurrencia bajo la hipótesis nula, según la expresión (1). Los resultados obtenidos se muestran en la Tabla 4. El valor de la p asociado al test exacto de Fisher puede entonces calcularse sumando las probabilidades de las tablas que resultan ser menores o iguales a la probabilidad de la tabla que ha sido observada:












Tabla 4. Probabilidad exacta asociada con cada una de las disposiciones de frecuencias de la Tabla 3. 





















a 





b 





c 





d 





p 









(i) 





0 





5 





8 





1 





0,0030 









(ii) 





1 





4 





7 





2 





0,0599 









(iii) 





2 





3 





6 





3 





0,2797 









(iv) 





3 





2 





5 





4 





0,4196 









(v) 





4 





1 





4 





5 





0,2098 









(vi) 





5 





0 





3 





6 





0,0280 















Otro modo de calcular el valor de p correspondiente consistiría en sumar las probabilidades asociadas a aquellas tablas que fuesen más favorables a la hipótesis alternativa que los datos observados. Es decir, aquellas situaciones en las que la diferencia en la prevalencia de obesidad entre hombres y mujeres fuese mayor que la observada en la realidad. En el ejemplo, sólo existe una tabla más extrema que la correspondiente a los datos observados (aquella en la que no se observa ninguna mujer obesa), de forma que:



(2)



Este sería el valor de la p correspondiente a un planteamiento unilateral. En este caso la hipótesis a contrastar sería que la prevalencia de obesidad es igual en hombres y mujeres, frente a la alternativa de que fuese mayor en los varones. Cuando el planteamiento se hace con una perspectiva bilateral, la hipótesis alternativa consiste en asumir que existen diferencias en la prevalencia de obesidad entre sexos, pero sin especificar de antemano en qué sentido se producen dichas diferencias. Para obtener el valor de la p correspondiente a la alternativa bilateral deberíamos multiplicar el valor obtenido en (2) por dos:







Como se puede observar, las dos formas de cálculo propuestas no tienen por qué proporcionar necesariamente los mismos resultados. El primer método siempre resultará en un valor de p menor o igual al del segundo método. Si recurrimos a un programa estadístico como el SPSS para el cómputo del test, éste utilizará la primera vía para obtener el p-valor correspondiente a la alternativa bilateral y el segundo método de cálculo para el valor de p asociado a un planteamiento unilateral. En cualquier caso, y a la vista de los resultados, no existe evidencia estadística de asociación entre el sexo y el hecho de ser obeso en la población de estudio.

















El test de McNemar





En otras ocasiones, una misma característica se mide en más de una ocasión para cada uno de los individuos que se incluyen en una investigación. En estos casos, el interés se centra en comparar si las mediciones efectuadas en dos momentos diferentes (normalmente antes y después de alguna intervención) son iguales o si, por el contrario, se produce algún cambio significativo. Por ejemplo, puede interesarnos estudiar, a distintos tiempos, el porcentaje de sujetos que se mantienen con fiebre tras la aplicación de un antitérmico o comparar la proporción de enfermos con un determinado síntoma antes y después de un tratamiento.



Para el caso de datos pareados, existen claramente cuatro tipos de pares de observaciones, según cada individuo presente o no la característica de interés en los dos momentos en los que se efectúa la evaluación (Tabla 5). Así, los resultados obtenidos pueden mostrarse igualmente en una tabla 2 x 2 como en la Tabla 1, con la salvedad de que aquí los datos son dependientes y por lo tanto no resultará adecuada la utilización del test .








Tabla 5. Frecuencia de cada una de las posibles combinaciones en un estudio de datos pareados. 









Observación 1 

Observación 2 

Número de pares 





Tipo 

Característica 

Característica 







1 

Presente 

Presente 

a 





2 

Presente 

Ausente 

b 





3 

Ausente 

Presente 

c 





4 

Ausente 

Ausente 

d 





Total 

n 







Con esta notación, las proporciones de individuos con la característica de interés en los dos momentos en los que se efectúa la medición son y , respectivamente. Estamos interesados por lo tanto en la diferencia entre estas dos proporciones:







La hipótesis nula que se quiere contrastar es que el valor esperado para esta diferencia es cero, frente a la hipótesis alternativa de que las dos proporciones y sean efectivamente diferentes. Esto se puede contrastar centrando nuestra atención en las casillas b y c que son las que muestran discordancia en los dos momentos en los que se efectuó la medición. La prueba de McNemar contrasta así si el número de individuos que han dejado de presentar la característica de interés (b) es el mismo que el número de individuos que han realizado el cambio inverso (c).



El error estándar para la diferencia entre dos proporciones viene dado por:



(3)







De modo que, bajo la hipótesis nula de que no existe diferencia entre ambas , la ecuación (3) se reduce a:







El estadístico de contraste se construye así de la forma siguiente:



(4)



que sigue una distribución normal N(0,1).



Alternativamente, se puede considerar el estadístico de contraste:







que sigue una distribución chi-cuadrado con un grado de libertad y proporciona el mismo valor de la p asociado.



A su vez, se puede aplicar una corrección de continuidad para trabajar sobre muestras pequeñas:







refiriendo el valor de dicho estadístico al de una distribución normal N(0,1) ó, equivalentemente, a una distribución chi-cuadrado con un grado de libertad si se trabaja con su valor al cuadrado:







De modo análogo, es posible obtener un intervalo de confianza para la diferencia de proporciones como:







Para ilustrar los cálculos anteriores, se dispone de información acerca de 20 pacientes a los que se les administró un determinado tratamiento para tratar el dolor tras una intervención quirúrgica. En cada individuo, se realizó una valoración del dolor inmediatamente después de la operación y al cabo de 1 hora tras la administración del analgésico. Los datos observados se muestran en la Tabla 6. En primer lugar se construye la tabla 2 x 2 con las frecuencias observadas en el estudio (Tabla 7). Según estos datos, el porcentaje de pacientes que manifiestan dolor inicialmente es de , frente al de los enfermos que dicen tener dolor una vez administrado el analgésico. El estadístico de contraste se construye según la expresión (4) como:







El valor obtenido del estadístico (z=2.49) se compara con los valores de una distribución normal estándar (Tabla 8). El valor crítico correspondiente para α =0.01 es de z=2.576 y para α =0.02 es de 2.326. Como quiera que en el cálculo del test de McNemar en el ejemplo obtuvimos un valor de 2.49, que supera al valor para α =0.02, podremos concluir que las dos variables no son independientes, sino que están asociadas (p<0.02). Aplicando la corrección de continuidad proporciona un resultado de , que sigue siendo un resultado significativo (p<0.03).



Otro modo de obtener esta misma información es mediante el cálculo de intervalos de confianza para la diferencia de proporciones en los dos momentos de observación. A mayores, el intervalo de confianza constituye una medida de la incertidumbre con la que se estima esa diferencia a partir de la muestra, permitiendo valorar tanto la significación estadística como la magnitud clínica de esa diferencia. En el caso que nos ocupa, el intervalo de confianza vendrá dado como:











Es decir, podemos asegurar (con una seguridad del 95%) de que la diferencia real en el porcentaje de pacientes que manifiestan dolor antes y después de recibir el tratamiento analgésico se mueve entre un 9.72% y un 80.28%.



En definitiva, el uso generalizado de la metodología estadística ha contribuido a dotar de un mayor rigor a la investigación clínico-epidemiológica en los últimos años. Sin embargo, también ha hecho que estas técnicas se apliquen en ocasiones de una manera un tanto superficial. Es extremadamente importante tener en cuenta las asunciones subyacentes a los distintos métodos estadísticos, como en el caso del test , para comprender cuándo es adecuado o no su uso y disponer de las técnicas estadísticas alternativas que deben utilizarse en cada ocasión.

















Anexo













Tabla 6. Datos de 20 pacientes intervenidos quirúrgicamente en los que se valoró el dolor tras la cirugía y al cabo de 1 hora tras la administración de un analgésico. 







Individuo 

Dolor tras la intervención 

Dolor 1 horas después del Tto. 





1 

No 

No 





2 

Sí 

No 





3 

No 

No 





4 

No 

No 





5 

Sí 

No 





6 

Sí 

No 





7 

No 

No 





8 

Sí 

Sí 





9 

No 

Sí 





10 

No 

No 





11 

Sí 

No 





12 

Sí 

No 





13 

Sí 

No 





14 

Sí 

No 





15 

Sí 

No 





16 

No 

Sí 





17 

No 

Sí 





18 

Sí 

No 





19 

Sí 

No 





20 

Sí 

No 

















Tabla 7. Tabla de contingencia con los datos de 20 pacientes intervenidos quirúrgicamente en los que se valoró el dolor tras la cirugía y al cabo de 1 hora tras la administración de un analgésico. 









Dolor 1 hora después del tratamiento 









Dolor tras la intervención 



Sí 

No 



Total







Sí 

1 (a) 

11 (b) 

12 (a+b) 





No 

2 (c) 

6 (d) 

8 (c+d) 





Total 

3 (a+c) 

17 (b+d) 

20 (n) 

















Tabla 8. Tabla de valores de la distribución normal. La tabla muestra los valores de z para los que la probabilidad de observar un valor mayor o igual (en valor absoluto) es igual a α. La cifra entera y el primer decimal de α se buscan en la primera columna, y la segunda cifra decimal en la cabecera de la tabla. 









































Bibliografía







Pearson K. On a criterion that a given system of deviations from the probable in the case of correlated system of variables is Duch that it can be reasonably supposed to have arisen from random sampling. Philosophical Magazine 1900, Series 5, No. 50: 157-175. 



Pearson, K. On the testo f goodness of fit. Biometrika 1922; 14: 186-191. 



Pita Fernández S, Pértega Díaz S. Asociación de variables cualitativas: Test de chi-cuadrado. Cad Aten Primaria 2004 (en prensa). [ Texto completo ]



Altman DG. Practical statistics for medical research. London: Chapman & Hall; 1991. 



Armitage P, Berry G. Estadística para la investigación biomédica. Madrid : Harcourt Brace; 1999.



Juez Martel P. Herramientas estadísticas para la investigación en Medicina y Economía de la Salud. Madrid: Ed. Centro de Estudios Ramón Areces; 2001.



Agresti A. Categoriacl Data Analisis. New York: John Wiley & Sons; 1990. 


















Autores





Sonia Pértega Díaza (1) , Salvador Pita Fernández (2) 

(1) Unidad de Epidemiología Clínica y Bioestadística. Complexo Hospitalario Universitario de A Coruña (A Coruña).

(2) Médico de Familia. Centro de Salud de Cambre (A Coruña).



























Fecha de revisión: 14/11/2004 












Imágenes

1 
















































Inicio 




Metodología de la Investigación 



Asociación de variables cualitativas: El test exacto de Fisher y el test de Mcnemar







Asociación de variables cualitativas: El test exacto de Fisher y el test de Mcnemar











Fecha de revisión: 14/11/2004 








Documento



Imágenes
1 




















Índice de contenidos 





Inroducción 



La prueba de probabilidad exacta de Fisher 



El test de McNemar 



Anexo 



Bibliografía 



Autores 









Inroducción





Desde que Pearson introdujo el test de la en 1900, ésta se ha convertido en una herramienta de uso general para conocer si existe o no relación entre variables de tipo cualitativo. Sin embargo, su aplicación exige de ciertos requerimientos acerca del tamaño muestral que no siempre son tenidos en cuenta . La prueba es aplicable a los datos de una tabla de contingencia solamente si las frecuencias esperadas son suficientemente grandes. Del mismo modo, cuando los datos exhiben algún grado de dependencia, el test no será el método apropiado para contrastar la hipótesis nula de independencia. En este trabajo se introducirán la prueba exacta de Fisher y el test de McNemar como alternativa estadística al test cuando no se verifiquen las condiciones necesarias para su utilización . 













La prueba de probabilidad exacta de Fisher





El test exacto de Fisher permite analizar si dos variables dicotómicas están asociadas cuando la muestra a estudiar es demasiado pequeña y no se cumplen las condiciones necesarias para que la aplicación del test sea adecuada. Estas condiciones exigen que los valores esperados de al menos el 80% de las celdas en una tabla de contingencia sean mayores de 5. Así, en una tabla 2x2 será necesario que todas las celdas verifiquen esta condición, si bien en la práctica suele permitirse que una de ellas muestre frecuencias esperadas ligeramente por debajo de este valor.

En situaciones como esta, una forma de plantear los resultados es su disposición en una tabla de contingencia de dos vías. Si las dos variables que se están considerando son dicotómicas, nos encontraremos con el caso de una tabla 2 x 2 como la que se muestra en la Tabla 1. El test exacto de Fisher se basa en evaluar la probabilidad asociada a cada una de las tablas 2 x 2 que se pueden formar manteniendo los mismos totales de filas y columnas que los de la tabla observada. Cada una de estas probabilidades se obtiene bajo la hipótesis nula de independencia de las dos variables que se están considerando.








Tabla 1. Tabla de contingencia general para la comparación de dos variables dicotómicas en el caso de grupos independientes. 











Característica A 











Característica B 



Presente 

Ausente 



Total







Presente 

a 

b 

a + b 





Ausente 

c 

d 

c + d 





Total 

a + c 

b + d 

n 









La probabilidad exacta de observar un conjunto concreto de frecuencias a, b, c y d en una tabla 2 x 2 cuando se asume independencia y los totales de filas y columnas se consideran fijos viene dada por la distribución hipergeométrica:







Esta fórmula se obtiene calculando todas las posibles formas en las que podemos disponer n sujetos en una tabla 2 x 2 de modo que los totales de filas y columnas sean siempre los mismos, (a+b), (c+d), (a+c) y (b+d).



La probabilidad anterior deberá calcularse para todas las tablas de contingencia que puedan formarse con los mismos totales marginales que la tabla observada. Posteriormente, estas probabilidades se usan para calcular valor de la p asociado al test exacto de Fisher. Este valor de p indicará la probabilidad de obtener una diferencia entre los grupos mayor o igual a la observada, bajo la hipótesis nula de independencia. Si esta probabilidad es pequeña (p<0.05) se deberá rechazar la hipótesis de partida y deberemos asumir que las dos variables no son independientes, sino que están asociadas. En caso contrario, se dirá que no existe evidencia estadística de asociación entre ambas variables.



En la literatura estadística, suelen proponerse dos métodos para el cómputo del valor de la p asociado al test exacto de Fisher. En primer lugar, podremos calcularlo sumando las probabilidades de aquellas tablas con una probabilidad asociada menor o igual a la correspondiente a los datos observados. La otra posibilidad consiste en sumar las probabilidades asociadas a resultados al menos tan favorables a la hipótesis alternativa como los datos reales. Este cálculo proporcionaría el valor de p correspondiente al test en el caso de un planteamiento unilateral. Duplicando este valor se obtendría el p-valor correspondiente a un test bilateral.



Para ilustrar la explicación anterior, supongamos que en una determinada población se desea averiguar si existen diferencias en la prevalencia de obesidad entre hombres y mujeres o si, por el contrario, el porcentaje de obesos no varía entre sexos. Tras ser observada una muestra de 14 sujetos se obtuvieron los resultados que se muestran en la Tabla 2.








Tabla 2. Tabla de contingencia para estudiar las diferencias en la prevalencia de obesidad entre sexos. Estudio de prevalencia sobre 14 sujetos. 

















Obesidad 











Sexo 



Sí 

No 



Total







Mujeres 

1 (a) 

4 (b) 

5 (a+b) 





Hombres 

7 (c) 

2 (d) 

9 (c+d) 





Total 

8 (a+c) 

6 (b+d) 

14 (n) 







En esta tabla a=1, b=4, c=7 y d=2. Los totales marginales son así a+b=5, c+d= 9, a+c=8 y b+d=6. La frecuencia esperada en tres de las cuatro celdas es menor de 5, por lo que no resulta adecuado aplicar el test , aunque sí el test exacto de Fisher. Si las variables sexo y obesidad fuesen independientes, la probabilidad asociada a los datos que han sido observados vendría dada por:














Tabla 3. Posibles combinaciones de frecuencias con los mismos totales marginales de filas y columnas que en la Tabla 2. 



























Obesidad 























Obesidad 



























Si 





No 























Si 





No 















(i) 





Mujeres 





0 





5 





5 





(iv) 





Mujeres 





3 





2 





5 















Hombres 





8 





1 





9 











Hombres 





5 





4 





9 





















8 





6 





14 

















8 





6 





14 









































































































































(ii) 





Mujeres 





1 





4 





5 





(v) 





Mujeres 





4 





1 





5 















Hombres 





7 





2 





9 











Hombres 





4 





5 





9 





















8 





6 





14 

















8 





6 





14 









































































































































(iii) 





Mujeres 





2 





3 





5 





(vi) 





Mujeres 





5 





0 





5 















Hombres 





6 





3 





9 











Hombres 





3 





6 





9 





















8 





6 





14 

















8 





6 





14 















La Tabla 3 muestra todas las posibles combinaciones de frecuencias que se podrían obtener con los mismos totales marginales que en la Tabla 2. Para cada una de estas tablas, se ha calculado la probabilidad exacta de ocurrencia bajo la hipótesis nula, según la expresión (1). Los resultados obtenidos se muestran en la Tabla 4. El valor de la p asociado al test exacto de Fisher puede entonces calcularse sumando las probabilidades de las tablas que resultan ser menores o iguales a la probabilidad de la tabla que ha sido observada:












Tabla 4. Probabilidad exacta asociada con cada una de las disposiciones de frecuencias de la Tabla 3. 





















a 





b 





c 





d 





p 









(i) 





0 





5 





8 





1 





0,0030 









(ii) 





1 





4 





7 





2 





0,0599 









(iii) 





2 





3 





6 





3 





0,2797 









(iv) 





3 





2 





5 





4 





0,4196 









(v) 





4 





1 





4 





5 





0,2098 









(vi) 





5 





0 





3 





6 





0,0280 















Otro modo de calcular el valor de p correspondiente consistiría en sumar las probabilidades asociadas a aquellas tablas que fuesen más favorables a la hipótesis alternativa que los datos observados. Es decir, aquellas situaciones en las que la diferencia en la prevalencia de obesidad entre hombres y mujeres fuese mayor que la observada en la realidad. En el ejemplo, sólo existe una tabla más extrema que la correspondiente a los datos observados (aquella en la que no se observa ninguna mujer obesa), de forma que:



(2)



Este sería el valor de la p correspondiente a un planteamiento unilateral. En este caso la hipótesis a contrastar sería que la prevalencia de obesidad es igual en hombres y mujeres, frente a la alternativa de que fuese mayor en los varones. Cuando el planteamiento se hace con una perspectiva bilateral, la hipótesis alternativa consiste en asumir que existen diferencias en la prevalencia de obesidad entre sexos, pero sin especificar de antemano en qué sentido se producen dichas diferencias. Para obtener el valor de la p correspondiente a la alternativa bilateral deberíamos multiplicar el valor obtenido en (2) por dos:







Como se puede observar, las dos formas de cálculo propuestas no tienen por qué proporcionar necesariamente los mismos resultados. El primer método siempre resultará en un valor de p menor o igual al del segundo método. Si recurrimos a un programa estadístico como el SPSS para el cómputo del test, éste utilizará la primera vía para obtener el p-valor correspondiente a la alternativa bilateral y el segundo método de cálculo para el valor de p asociado a un planteamiento unilateral. En cualquier caso, y a la vista de los resultados, no existe evidencia estadística de asociación entre el sexo y el hecho de ser obeso en la población de estudio.













El test de McNemar





En otras ocasiones, una misma característica se mide en más de una ocasión para cada uno de los individuos que se incluyen en una investigación. En estos casos, el interés se centra en comparar si las mediciones efectuadas en dos momentos diferentes (normalmente antes y después de alguna intervención) son iguales o si, por el contrario, se produce algún cambio significativo. Por ejemplo, puede interesarnos estudiar, a distintos tiempos, el porcentaje de sujetos que se mantienen con fiebre tras la aplicación de un antitérmico o comparar la proporción de enfermos con un determinado síntoma antes y después de un tratamiento.



Para el caso de datos pareados, existen claramente cuatro tipos de pares de observaciones, según cada individuo presente o no la característica de interés en los dos momentos en los que se efectúa la evaluación (Tabla 5). Así, los resultados obtenidos pueden mostrarse igualmente en una tabla 2 x 2 como en la Tabla 1, con la salvedad de que aquí los datos son dependientes y por lo tanto no resultará adecuada la utilización del test .








Tabla 5. Frecuencia de cada una de las posibles combinaciones en un estudio de datos pareados. 









Observación 1 

Observación 2 

Número de pares 





Tipo 

Característica 

Característica 







1 

Presente 

Presente 

a 





2 

Presente 

Ausente 

b 





3 

Ausente 

Presente 

c 





4 

Ausente 

Ausente 

d 





Total 

n 







Con esta notación, las proporciones de individuos con la característica de interés en los dos momentos en los que se efectúa la medición son y , respectivamente. Estamos interesados por lo tanto en la diferencia entre estas dos proporciones:







La hipótesis nula que se quiere contrastar es que el valor esperado para esta diferencia es cero, frente a la hipótesis alternativa de que las dos proporciones y sean efectivamente diferentes. Esto se puede contrastar centrando nuestra atención en las casillas b y c que son las que muestran discordancia en los dos momentos en los que se efectuó la medición. La prueba de McNemar contrasta así si el número de individuos que han dejado de presentar la característica de interés (b) es el mismo que el número de individuos que han realizado el cambio inverso (c).



El error estándar para la diferencia entre dos proporciones viene dado por:



(3)







De modo que, bajo la hipótesis nula de que no existe diferencia entre ambas , la ecuación (3) se reduce a:







El estadístico de contraste se construye así de la forma siguiente:



(4)



que sigue una distribución normal N(0,1).



Alternativamente, se puede considerar el estadístico de contraste:







que sigue una distribución chi-cuadrado con un grado de libertad y proporciona el mismo valor de la p asociado.



A su vez, se puede aplicar una corrección de continuidad para trabajar sobre muestras pequeñas:







refiriendo el valor de dicho estadístico al de una distribución normal N(0,1) ó, equivalentemente, a una distribución chi-cuadrado con un grado de libertad si se trabaja con su valor al cuadrado:







De modo análogo, es posible obtener un intervalo de confianza para la diferencia de proporciones como:







Para ilustrar los cálculos anteriores, se dispone de información acerca de 20 pacientes a los que se les administró un determinado tratamiento para tratar el dolor tras una intervención quirúrgica. En cada individuo, se realizó una valoración del dolor inmediatamente después de la operación y al cabo de 1 hora tras la administración del analgésico. Los datos observados se muestran en la Tabla 6. En primer lugar se construye la tabla 2 x 2 con las frecuencias observadas en el estudio (Tabla 7). Según estos datos, el porcentaje de pacientes que manifiestan dolor inicialmente es de , frente al de los enfermos que dicen tener dolor una vez administrado el analgésico. El estadístico de contraste se construye según la expresión (4) como:







El valor obtenido del estadístico (z=2.49) se compara con los valores de una distribución normal estándar (Tabla 8). El valor crítico correspondiente para α =0.01 es de z=2.576 y para α =0.02 es de 2.326. Como quiera que en el cálculo del test de McNemar en el ejemplo obtuvimos un valor de 2.49, que supera al valor para α =0.02, podremos concluir que las dos variables no son independientes, sino que están asociadas (p<0.02). Aplicando la corrección de continuidad proporciona un resultado de , que sigue siendo un resultado significativo (p<0.03).



Otro modo de obtener esta misma información es mediante el cálculo de intervalos de confianza para la diferencia de proporciones en los dos momentos de observación. A mayores, el intervalo de confianza constituye una medida de la incertidumbre con la que se estima esa diferencia a partir de la muestra, permitiendo valorar tanto la significación estadística como la magnitud clínica de esa diferencia. En el caso que nos ocupa, el intervalo de confianza vendrá dado como:











Es decir, podemos asegurar (con una seguridad del 95%) de que la diferencia real en el porcentaje de pacientes que manifiestan dolor antes y después de recibir el tratamiento analgésico se mueve entre un 9.72% y un 80.28%.



En definitiva, el uso generalizado de la metodología estadística ha contribuido a dotar de un mayor rigor a la investigación clínico-epidemiológica en los últimos años. Sin embargo, también ha hecho que estas técnicas se apliquen en ocasiones de una manera un tanto superficial. Es extremadamente importante tener en cuenta las asunciones subyacentes a los distintos métodos estadísticos, como en el caso del test , para comprender cuándo es adecuado o no su uso y disponer de las técnicas estadísticas alternativas que deben utilizarse en cada ocasión.













Anexo













Tabla 6. Datos de 20 pacientes intervenidos quirúrgicamente en los que se valoró el dolor tras la cirugía y al cabo de 1 hora tras la administración de un analgésico. 







Individuo 

Dolor tras la intervención 

Dolor 1 horas después del Tto. 





1 

No 

No 





2 

Sí 

No 





3 

No 

No 





4 

No 

No 





5 

Sí 

No 





6 

Sí 

No 





7 

No 

No 





8 

Sí 

Sí 





9 

No 

Sí 





10 

No 

No 





11 

Sí 

No 





12 

Sí 

No 





13 

Sí 

No 





14 

Sí 

No 





15 

Sí 

No 





16 

No 

Sí 





17 

No 

Sí 





18 

Sí 

No 





19 

Sí 

No 





20 

Sí 

No 

















Tabla 7. Tabla de contingencia con los datos de 20 pacientes intervenidos quirúrgicamente en los que se valoró el dolor tras la cirugía y al cabo de 1 hora tras la administración de un analgésico. 









Dolor 1 hora después del tratamiento 









Dolor tras la intervención 



Sí 

No 



Total







Sí 

1 (a) 

11 (b) 

12 (a+b) 





No 

2 (c) 

6 (d) 

8 (c+d) 





Total 

3 (a+c) 

17 (b+d) 

20 (n) 

















Tabla 8. Tabla de valores de la distribución normal. La tabla muestra los valores de z para los que la probabilidad de observar un valor mayor o igual (en valor absoluto) es igual a α. La cifra entera y el primer decimal de α se buscan en la primera columna, y la segunda cifra decimal en la cabecera de la tabla. 





































Bibliografía







Pearson K. On a criterion that a given system of deviations from the probable in the case of correlated system of variables is Duch that it can be reasonably supposed to have arisen from random sampling. Philosophical Magazine 1900, Series 5, No. 50: 157-175. 



Pearson, K. On the testo f goodness of fit. Biometrika 1922; 14: 186-191. 



Pita Fernández S, Pértega Díaz S. Asociación de variables cualitativas: Test de chi-cuadrado. Cad Aten Primaria 2004 (en prensa). [ Texto completo ]



Altman DG. Practical statistics for medical research. London: Chapman & Hall; 1991. 



Armitage P, Berry G. Estadística para la investigación biomédica. Madrid : Harcourt Brace; 1999.



Juez Martel P. Herramientas estadísticas para la investigación en Medicina y Economía de la Salud. Madrid: Ed. Centro de Estudios Ramón Areces; 2001.



Agresti A. Categoriacl Data Analisis. New York: John Wiley & Sons; 1990. 














Autores





Sonia Pértega Díaza (1) , Salvador Pita Fernández (2) 

(1) Unidad de Epidemiología Clínica y Bioestadística. Complexo Hospitalario Universitario de A Coruña (A Coruña).

(2) Médico de Familia. Centro de Salud de Cambre (A Coruña).






























































Asociación de variables cualitativas: El test exacto de Fisher y el test de Mcnemar









Fecha de revisión: 14/11/2004 








Índice de contenidos




Inroducción 



La prueba de probabilidad exacta de Fisher 



El test de McNemar 



Anexo 



Bibliografía 



Autores 













Inroducción





Desde que Pearson introdujo el test de la en 1900, ésta se ha convertido en una herramienta de uso general para conocer si existe o no relación entre variables de tipo cualitativo. Sin embargo, su aplicación exige de ciertos requerimientos acerca del tamaño muestral que no siempre son tenidos en cuenta . La prueba es aplicable a los datos de una tabla de contingencia solamente si las frecuencias esperadas son suficientemente grandes. Del mismo modo, cuando los datos exhiben algún grado de dependencia, el test no será el método apropiado para contrastar la hipótesis nula de independencia. En este trabajo se introducirán la prueba exacta de Fisher y el test de McNemar como alternativa estadística al test cuando no se verifiquen las condiciones necesarias para su utilización . 

















La prueba de probabilidad exacta de Fisher





El test exacto de Fisher permite analizar si dos variables dicotómicas están asociadas cuando la muestra a estudiar es demasiado pequeña y no se cumplen las condiciones necesarias para que la aplicación del test sea adecuada. Estas condiciones exigen que los valores esperados de al menos el 80% de las celdas en una tabla de contingencia sean mayores de 5. Así, en una tabla 2x2 será necesario que todas las celdas verifiquen esta condición, si bien en la práctica suele permitirse que una de ellas muestre frecuencias esperadas ligeramente por debajo de este valor.

En situaciones como esta, una forma de plantear los resultados es su disposición en una tabla de contingencia de dos vías. Si las dos variables que se están considerando son dicotómicas, nos encontraremos con el caso de una tabla 2 x 2 como la que se muestra en la Tabla 1. El test exacto de Fisher se basa en evaluar la probabilidad asociada a cada una de las tablas 2 x 2 que se pueden formar manteniendo los mismos totales de filas y columnas que los de la tabla observada. Cada una de estas probabilidades se obtiene bajo la hipótesis nula de independencia de las dos variables que se están considerando.








Tabla 1. Tabla de contingencia general para la comparación de dos variables dicotómicas en el caso de grupos independientes. 











Característica A 











Característica B 



Presente 

Ausente 



Total







Presente 

a 

b 

a + b 





Ausente 

c 

d 

c + d 





Total 

a + c 

b + d 

n 









La probabilidad exacta de observar un conjunto concreto de frecuencias a, b, c y d en una tabla 2 x 2 cuando se asume independencia y los totales de filas y columnas se consideran fijos viene dada por la distribución hipergeométrica:







Esta fórmula se obtiene calculando todas las posibles formas en las que podemos disponer n sujetos en una tabla 2 x 2 de modo que los totales de filas y columnas sean siempre los mismos, (a+b), (c+d), (a+c) y (b+d).



La probabilidad anterior deberá calcularse para todas las tablas de contingencia que puedan formarse con los mismos totales marginales que la tabla observada. Posteriormente, estas probabilidades se usan para calcular valor de la p asociado al test exacto de Fisher. Este valor de p indicará la probabilidad de obtener una diferencia entre los grupos mayor o igual a la observada, bajo la hipótesis nula de independencia. Si esta probabilidad es pequeña (p<0.05) se deberá rechazar la hipótesis de partida y deberemos asumir que las dos variables no son independientes, sino que están asociadas. En caso contrario, se dirá que no existe evidencia estadística de asociación entre ambas variables.



En la literatura estadística, suelen proponerse dos métodos para el cómputo del valor de la p asociado al test exacto de Fisher. En primer lugar, podremos calcularlo sumando las probabilidades de aquellas tablas con una probabilidad asociada menor o igual a la correspondiente a los datos observados. La otra posibilidad consiste en sumar las probabilidades asociadas a resultados al menos tan favorables a la hipótesis alternativa como los datos reales. Este cálculo proporcionaría el valor de p correspondiente al test en el caso de un planteamiento unilateral. Duplicando este valor se obtendría el p-valor correspondiente a un test bilateral.



Para ilustrar la explicación anterior, supongamos que en una determinada población se desea averiguar si existen diferencias en la prevalencia de obesidad entre hombres y mujeres o si, por el contrario, el porcentaje de obesos no varía entre sexos. Tras ser observada una muestra de 14 sujetos se obtuvieron los resultados que se muestran en la Tabla 2.








Tabla 2. Tabla de contingencia para estudiar las diferencias en la prevalencia de obesidad entre sexos. Estudio de prevalencia sobre 14 sujetos. 

















Obesidad 











Sexo 



Sí 

No 



Total







Mujeres 

1 (a) 

4 (b) 

5 (a+b) 





Hombres 

7 (c) 

2 (d) 

9 (c+d) 





Total 

8 (a+c) 

6 (b+d) 

14 (n) 







En esta tabla a=1, b=4, c=7 y d=2. Los totales marginales son así a+b=5, c+d= 9, a+c=8 y b+d=6. La frecuencia esperada en tres de las cuatro celdas es menor de 5, por lo que no resulta adecuado aplicar el test , aunque sí el test exacto de Fisher. Si las variables sexo y obesidad fuesen independientes, la probabilidad asociada a los datos que han sido observados vendría dada por:














Tabla 3. Posibles combinaciones de frecuencias con los mismos totales marginales de filas y columnas que en la Tabla 2. 



























Obesidad 























Obesidad 



























Si 





No 























Si 





No 















(i) 





Mujeres 





0 





5 





5 





(iv) 





Mujeres 





3 





2 





5 















Hombres 





8 





1 





9 











Hombres 





5 





4 





9 





















8 





6 





14 

















8 





6 





14 









































































































































(ii) 





Mujeres 





1 





4 





5 





(v) 





Mujeres 





4 





1 





5 















Hombres 





7 





2 





9 











Hombres 





4 





5 





9 





















8 





6 





14 

















8 





6 





14 









































































































































(iii) 





Mujeres 





2 





3 





5 





(vi) 





Mujeres 





5 





0 





5 















Hombres 





6 





3 





9 











Hombres 





3 





6 





9 





















8 





6 





14 

















8 





6 





14 















La Tabla 3 muestra todas las posibles combinaciones de frecuencias que se podrían obtener con los mismos totales marginales que en la Tabla 2. Para cada una de estas tablas, se ha calculado la probabilidad exacta de ocurrencia bajo la hipótesis nula, según la expresión (1). Los resultados obtenidos se muestran en la Tabla 4. El valor de la p asociado al test exacto de Fisher puede entonces calcularse sumando las probabilidades de las tablas que resultan ser menores o iguales a la probabilidad de la tabla que ha sido observada:












Tabla 4. Probabilidad exacta asociada con cada una de las disposiciones de frecuencias de la Tabla 3. 





















a 





b 





c 





d 





p 









(i) 





0 





5 





8 





1 





0,0030 









(ii) 





1 





4 





7 





2 





0,0599 









(iii) 





2 





3 





6 





3 





0,2797 









(iv) 





3 





2 





5 





4 





0,4196 









(v) 





4 





1 





4 





5 





0,2098 









(vi) 





5 





0 





3 





6 





0,0280 















Otro modo de calcular el valor de p correspondiente consistiría en sumar las probabilidades asociadas a aquellas tablas que fuesen más favorables a la hipótesis alternativa que los datos observados. Es decir, aquellas situaciones en las que la diferencia en la prevalencia de obesidad entre hombres y mujeres fuese mayor que la observada en la realidad. En el ejemplo, sólo existe una tabla más extrema que la correspondiente a los datos observados (aquella en la que no se observa ninguna mujer obesa), de forma que:



(2)



Este sería el valor de la p correspondiente a un planteamiento unilateral. En este caso la hipótesis a contrastar sería que la prevalencia de obesidad es igual en hombres y mujeres, frente a la alternativa de que fuese mayor en los varones. Cuando el planteamiento se hace con una perspectiva bilateral, la hipótesis alternativa consiste en asumir que existen diferencias en la prevalencia de obesidad entre sexos, pero sin especificar de antemano en qué sentido se producen dichas diferencias. Para obtener el valor de la p correspondiente a la alternativa bilateral deberíamos multiplicar el valor obtenido en (2) por dos:







Como se puede observar, las dos formas de cálculo propuestas no tienen por qué proporcionar necesariamente los mismos resultados. El primer método siempre resultará en un valor de p menor o igual al del segundo método. Si recurrimos a un programa estadístico como el SPSS para el cómputo del test, éste utilizará la primera vía para obtener el p-valor correspondiente a la alternativa bilateral y el segundo método de cálculo para el valor de p asociado a un planteamiento unilateral. En cualquier caso, y a la vista de los resultados, no existe evidencia estadística de asociación entre el sexo y el hecho de ser obeso en la población de estudio.

















El test de McNemar





En otras ocasiones, una misma característica se mide en más de una ocasión para cada uno de los individuos que se incluyen en una investigación. En estos casos, el interés se centra en comparar si las mediciones efectuadas en dos momentos diferentes (normalmente antes y después de alguna intervención) son iguales o si, por el contrario, se produce algún cambio significativo. Por ejemplo, puede interesarnos estudiar, a distintos tiempos, el porcentaje de sujetos que se mantienen con fiebre tras la aplicación de un antitérmico o comparar la proporción de enfermos con un determinado síntoma antes y después de un tratamiento.



Para el caso de datos pareados, existen claramente cuatro tipos de pares de observaciones, según cada individuo presente o no la característica de interés en los dos momentos en los que se efectúa la evaluación (Tabla 5). Así, los resultados obtenidos pueden mostrarse igualmente en una tabla 2 x 2 como en la Tabla 1, con la salvedad de que aquí los datos son dependientes y por lo tanto no resultará adecuada la utilización del test .








Tabla 5. Frecuencia de cada una de las posibles combinaciones en un estudio de datos pareados. 









Observación 1 

Observación 2 

Número de pares 





Tipo 

Característica 

Característica 







1 

Presente 

Presente 

a 





2 

Presente 

Ausente 

b 





3 

Ausente 

Presente 

c 





4 

Ausente 

Ausente 

d 





Total 

n 







Con esta notación, las proporciones de individuos con la característica de interés en los dos momentos en los que se efectúa la medición son y , respectivamente. Estamos interesados por lo tanto en la diferencia entre estas dos proporciones:







La hipótesis nula que se quiere contrastar es que el valor esperado para esta diferencia es cero, frente a la hipótesis alternativa de que las dos proporciones y sean efectivamente diferentes. Esto se puede contrastar centrando nuestra atención en las casillas b y c que son las que muestran discordancia en los dos momentos en los que se efectuó la medición. La prueba de McNemar contrasta así si el número de individuos que han dejado de presentar la característica de interés (b) es el mismo que el número de individuos que han realizado el cambio inverso (c).



El error estándar para la diferencia entre dos proporciones viene dado por:



(3)







De modo que, bajo la hipótesis nula de que no existe diferencia entre ambas , la ecuación (3) se reduce a:







El estadístico de contraste se construye así de la forma siguiente:



(4)



que sigue una distribución normal N(0,1).



Alternativamente, se puede considerar el estadístico de contraste:







que sigue una distribución chi-cuadrado con un grado de libertad y proporciona el mismo valor de la p asociado.



A su vez, se puede aplicar una corrección de continuidad para trabajar sobre muestras pequeñas:







refiriendo el valor de dicho estadístico al de una distribución normal N(0,1) ó, equivalentemente, a una distribución chi-cuadrado con un grado de libertad si se trabaja con su valor al cuadrado:







De modo análogo, es posible obtener un intervalo de confianza para la diferencia de proporciones como:







Para ilustrar los cálculos anteriores, se dispone de información acerca de 20 pacientes a los que se les administró un determinado tratamiento para tratar el dolor tras una intervención quirúrgica. En cada individuo, se realizó una valoración del dolor inmediatamente después de la operación y al cabo de 1 hora tras la administración del analgésico. Los datos observados se muestran en la Tabla 6. En primer lugar se construye la tabla 2 x 2 con las frecuencias observadas en el estudio (Tabla 7). Según estos datos, el porcentaje de pacientes que manifiestan dolor inicialmente es de , frente al de los enfermos que dicen tener dolor una vez administrado el analgésico. El estadístico de contraste se construye según la expresión (4) como:







El valor obtenido del estadístico (z=2.49) se compara con los valores de una distribución normal estándar (Tabla 8). El valor crítico correspondiente para α =0.01 es de z=2.576 y para α =0.02 es de 2.326. Como quiera que en el cálculo del test de McNemar en el ejemplo obtuvimos un valor de 2.49, que supera al valor para α =0.02, podremos concluir que las dos variables no son independientes, sino que están asociadas (p<0.02). Aplicando la corrección de continuidad proporciona un resultado de , que sigue siendo un resultado significativo (p<0.03).



Otro modo de obtener esta misma información es mediante el cálculo de intervalos de confianza para la diferencia de proporciones en los dos momentos de observación. A mayores, el intervalo de confianza constituye una medida de la incertidumbre con la que se estima esa diferencia a partir de la muestra, permitiendo valorar tanto la significación estadística como la magnitud clínica de esa diferencia. En el caso que nos ocupa, el intervalo de confianza vendrá dado como:











Es decir, podemos asegurar (con una seguridad del 95%) de que la diferencia real en el porcentaje de pacientes que manifiestan dolor antes y después de recibir el tratamiento analgésico se mueve entre un 9.72% y un 80.28%.



En definitiva, el uso generalizado de la metodología estadística ha contribuido a dotar de un mayor rigor a la investigación clínico-epidemiológica en los últimos años. Sin embargo, también ha hecho que estas técnicas se apliquen en ocasiones de una manera un tanto superficial. Es extremadamente importante tener en cuenta las asunciones subyacentes a los distintos métodos estadísticos, como en el caso del test , para comprender cuándo es adecuado o no su uso y disponer de las técnicas estadísticas alternativas que deben utilizarse en cada ocasión.

















Anexo













Tabla 6. Datos de 20 pacientes intervenidos quirúrgicamente en los que se valoró el dolor tras la cirugía y al cabo de 1 hora tras la administración de un analgésico. 







Individuo 

Dolor tras la intervención 

Dolor 1 horas después del Tto. 





1 

No 

No 





2 

Sí 

No 





3 

No 

No 





4 

No 

No 





5 

Sí 

No 





6 

Sí 

No 





7 

No 

No 





8 

Sí 

Sí 





9 

No 

Sí 





10 

No 

No 





11 

Sí 

No 





12 

Sí 

No 





13 

Sí 

No 





14 

Sí 

No 





15 

Sí 

No 





16 

No 

Sí 





17 

No 

Sí 





18 

Sí 

No 





19 

Sí 

No 





20 

Sí 

No 

















Tabla 7. Tabla de contingencia con los datos de 20 pacientes intervenidos quirúrgicamente en los que se valoró el dolor tras la cirugía y al cabo de 1 hora tras la administración de un analgésico. 









Dolor 1 hora después del tratamiento 









Dolor tras la intervención 



Sí 

No 



Total







Sí 

1 (a) 

11 (b) 

12 (a+b) 





No 

2 (c) 

6 (d) 

8 (c+d) 





Total 

3 (a+c) 

17 (b+d) 

20 (n) 

















Tabla 8. Tabla de valores de la distribución normal. La tabla muestra los valores de z para los que la probabilidad de observar un valor mayor o igual (en valor absoluto) es igual a α. La cifra entera y el primer decimal de α se buscan en la primera columna, y la segunda cifra decimal en la cabecera de la tabla. 









































Bibliografía







Pearson K. On a criterion that a given system of deviations from the probable in the case of correlated system of variables is Duch that it can be reasonably supposed to have arisen from random sampling. Philosophical Magazine 1900, Series 5, No. 50: 157-175. 



Pearson, K. On the testo f goodness of fit. Biometrika 1922; 14: 186-191. 



Pita Fernández S, Pértega Díaz S. Asociación de variables cualitativas: Test de chi-cuadrado. Cad Aten Primaria 2004 (en prensa). [ Texto completo ]



Altman DG. Practical statistics for medical research. London: Chapman & Hall; 1991. 



Armitage P, Berry G. Estadística para la investigación biomédica. Madrid : Harcourt Brace; 1999.



Juez Martel P. Herramientas estadísticas para la investigación en Medicina y Economía de la Salud. Madrid: Ed. Centro de Estudios Ramón Areces; 2001.



Agresti A. Categoriacl Data Analisis. New York: John Wiley & Sons; 1990. 


















Autores





Sonia Pértega Díaza (1) , Salvador Pita Fernández (2) 

(1) Unidad de Epidemiología Clínica y Bioestadística. Complexo Hospitalario Universitario de A Coruña (A Coruña).

(2) Médico de Familia. Centro de Salud de Cambre (A Coruña).
























© Descargado el 21/04/2026 6:01:49 Para uso personal exclusivamente. No se permiten otros usos sin autorización. Copyright © . Elsevier Inc. Todos los derechos reservados.
