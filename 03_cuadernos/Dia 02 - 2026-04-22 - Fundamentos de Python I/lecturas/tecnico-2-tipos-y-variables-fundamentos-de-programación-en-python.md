# Tipos y variables — Fundamentos de Programación en Python

Fuente: [Universidad de Valladolid (EII)](https://www2.eii.uva.es/fund_inf/python/notebooks/01_Tipos_y_variables/Tipos_y_variables.html)  
_Copia local para lectura fuera de línea. El formato original puede verse en la URL._

---

Tipos y variables










Contents 






El intérprete como calculadora 


Expresiones y sentencias 

Operadores aritméticos básicos 


Reglas de precedencia 


El operador de exponenciación ** 


Operadores binarios y unarios 


El operador división 


La división entera // y el operador resto % 


Tabla de precedencias 





Tipos de datos 

Clasificación 


Tipos enteros y reales 


Expresiones con mezcla de tipos 


Números complejos 


Cadenas de caracteres 


Otras constantes literales 





Variables 

El operador de asignación = 

La asignación no es equivalente a la igualdad matemática 





Operadores de asignación compuestos 


Variables de Python en memoria 


Inmutabilidad 


La recolección de basura 





Introducción al concepto de objeto 




















Tipos y variables # 


El intérprete como calculadora 

Expresiones y sentencias 

Tipos de datos 

Variables 

Introducción al concepto de objeto 







El intérprete como calculadora # 


Antes de hacer nuestros primeros programas en Python, conviene familiarizarnos con los valores básicos que pueden ser representados y manipulados en el lenguaje. Lo haremos mediante ejemplos sencillos, utilizando el intérprete como una calculadora .


Véase, por ejemplo, la línea representada en la siguiente celda de un cuaderno Jupyter. Para seleccionar una celda nos situamos sobre ella y para ejecutarla, pulsamos el botón:
de la aplicación Jupyter Notebook o presionamos simultáneamente Shift + Enter .






2 + 3 









5









Como habrás observado, se obtiene el resultado esperado para la suma planteada de dos números enteros . Puedes modificar la suma anterior eligiendo el modo Edición de la celda y cambiando los operandos.


En programación se llaman constantes literales a aquellas cuyo valor aparece tal cual en el código fuente y cuya representación se deduce de forma evidente. En el ejemplo, 2 y 3 son dos constantes literales enteras.


La siguiente celda muestra otra operación similar, en este caso usando números reales.






2.31 - 5.63 









-3.32









Nótese que la presencia o ausencia del separador decimal , . , ha permitido a Python considerar a una constante literal como de tipo entero o real.


Algunas combinaciones producen un error sintáctico . Véase, por ejemplo, el resultado de la siguiente celda.






2 + 7 + 









Cell In [ 3 ], line 1 
2 + 7 + 
^ 
SyntaxError : invalid syntax









El intérprete nos reporta la existencia de un error debido a una construcción sintáctica inválida . Es importante que aprendas a interpretar los mensajes de error para corregir sus causas. ¡Corrige la línea para evitar que se produzca!









Expresiones y sentencias # 


Una expresión combina operandos (como los literales enteros 3 o 5 ) y operadores (como + para la suma) siguiendo unas reglas sintácticas simples, similares a las que ya conocemos de la aritmética.


Además, pueden contener palabras clave del lenguaje y signos de puntuación .


Un operador es un símbolo que determina la operación a realizar sobre los operandos (datos) a los que afecta.


Una sentencia o comando es un conjunto de expresiones que permiten ejecutar 
una determinada acción.




Operadores aritméticos básicos # 


Como es natural, además de la suma, se tienen operadores para el resto de las operaciones aritméticas
básicas:




Operador


Operación






+ 


Suma




- 


Resta




* 


Multiplicación




/ 


División






En la celda siguiente se multiplican dos enteros. ¿Te animas a intentar la resta y la división? ¿Cómo harías para multiplicar varios valores? ¿Se pueden combinar operadores diferentes?






2 * 3 









6













Reglas de precedencia # 


Considera la siguiente expresión y calcula mentalmente el resultado que debe dar. ¿Coincide con el que proporciona Python? ¿Sorprendido?






3 + 2 * 5 








Show code cell output 
Hide code cell output 




13










Cuando se combinan diferentes operadores, el valor determinado por la expresión se calcula en función de unas reglas de precedencia . Estas reglas coinciden con lo esperable a partir de nuestros conocimientos aritméticos: la multiplicación y la división son prioritarios con respecto a la suma y la resta .


La precedencia habitual se puede alterar utilizando paréntesis. Los paréntesis pueden anidarse unos dentro de otros, todo lo que se necesite.






( 3 + 2 ) * 5 









25













(( 3 + 2 ) * 5 + 1 ) * 10 









260









En presencia de operadores de igual precedencia , el cálculo del valor de una expresión se realiza típicamente de izquierda a derecha .


Por ejemplo, en la siguiente celda, la división (que aparece primero desde la izquierda) tiene preferencia sobre la multiplicación.






2 / 2 * 3 









3.0









En general, para evitar dudas y, en muchas ocasiones, para mejorar la legibilidad, ¡usa paréntesis! 






El operador de exponenciación ** # 


En Python, el operador ** eleva un valor a una potencia dada. Este operador tiene mayor preferencia que los anteriormente mencionados y, además, tiene la característica de que la prioridad se evalúa a la inversa de los anteriores, o sea, de derecha a izquierda:






2 ** 3 ** 2 









512









Usando paréntesis salimos de dudas:






2 ** ( 3 ** 2 ) 









512













Operadores binarios y unarios # 


Los operadores anteriores se denominan binarios porque afectan a dos valores, situados a su izquierda y a su derecha. Existen también operadores unarios . Por ejemplo, el - como operador unario cambia el signo al valor situado a su derecha. También existe el + unario, pero su utilidad es evidentemente menor.






- 2 *- 3 









6









Observe que la precedencia del - unario es incluso mayor que la del producto * .
Existen otros operadores unarios y binarios que veremos más adelante. Pero debemos dedicar algo de tiempo a la operación de división.






El operador división # 






2 / 3 









0.6666666666666666









A diferencia del resto de los operadores vistos, la división brinda un resultado cualitativamente diferente. El cociente contiene un punto decimal (equivalente al separador decimal coma muy utilizado en múltiples paises).
Este resultado es coherente con lo que sabemos de las matemáticas. Si nos limitamos a las operaciones de suma, resta y multiplicación entre enteros, el resultado es otro entero.
La división, sin embargo, puede dar un cociente que solo puede definirse correctamente para todos los casos si ampliamos su definición, por los menos, al campo de los números racionales.


Por otro lado, el operador división es uno de los muchos operadores que pueden ocasionar errores en tiempo de ejecución ( runtime errors ). Así, cuando el denominador es nulo, la ejecución del programa lanza una excepción llamada ZeroDivisonError .






5 / 0 









--------------------------------------------------------------------------- 
ZeroDivisionError Traceback (most recent call last)
Cell In [ 13 ], line 1 
----> 1 5 / 0 

ZeroDivisionError : division by zero













La división entera // y el operador resto % # 


Existe una forma de realizar la división sin abandonar el campo de los enteros. Se tiene para ello el operador de división entera que se representa por // .






5 // 4 









1









El resultado del operador // siempre es el entero por defecto más próximo al resultado en el campo de los reales. Así, para -5//4 obtenemos -2 , dado que -5/4=-1.25 .






- 5 // 4 









-2









También se cuenta con el operador % que devuelve el resto de la división entera tal y como se muestra en los ejemplos que siguen.






5 % 4 









1









En este caso, dado que -5//4 da como resultado -2 , el operador resto para -5%4 da como resultado 3 , dado que -2*4=-8 y -5-(-8)= 3 . Por el contrario, el operador resto para 5%-4 da como resultado -3 , dado que -2*-4=8 y -5-8= -3 .






- 5 % 4 









3













5 %- 4 









-3









Estos operadores, lejos de ser una curiosidad sin importancia, resultan muy útiles en programación.






Tabla de precedencias # 


La siguiente tabla muestra las precedencias de los operadores estudiados hasta el momento.




Operador


Evaluación


Rango






() 


Izq. a Der.


1




** 


Der. a Izq.


2




+ 


Unario


3




- 


Unario


3




* 


Izq. a Der.


4




/ 


Izq. a Der.


4




// 


Izq. a Der.


4




% 


Izq. a Der.


4




+ 


Izq. a Der.


5




- 


Izq. a Der.


5















Tipos de datos # 


Los diferentes valores que puede manejar un lenguaje se agrupan en tipos . Acabamos de trabajar con valores enteros y reales, pero pronto veremos otros, como cadenas de caracteres, tuplas, listas, etc.


Un tipo se configura a partir de:



un conjunto de valores 


Por ejemplo, un conjunto formado por enteros {…,-3,-2,-1,0,1,2,3,…}




las operaciones permitidas para esos valores


Por ejemplo, para los enteros disponemos de los operadores:



suma ( + )



resta ( - ),



división ( / )



división entera ( // )



multiplicación ( * )



resto de la división entera ( % )



exponenciación ( ** )



operadores unarios ( + y - )






una aplicación que asocia a cada valor del tipo una representación binaria interna en memoria






Clasificación # 


Los comités de estandarización de cada lenguaje o diferentes autores tienen
(y varían en el tiempo) su propia terminología acerca de conceptos tales como
tipo primitivo , tipo nativo , tipo básico , tipo fundamental ,
tipo compuesto , tipo escalar , etc. por lo que la bibliografía a veces resulta confusa
y contradictoria.


Una forma de clasificarlos que evite discusiones bizantinas podría ser:



Tipos nativos , proporcionados por el lenguaje


Por ejemplo, int , float , complex o str en Python




Tipos definidos por el programador o suministrados por una biblioteca .








Tipos enteros y reales # 


La información se representa en los computadores utilizando un conjunto de celdas de memoria que almacenan dígitos binarios (0 o 1). La cantidad y el rango de los números enteros y reales en matemáticas es un conjunto infinito. El ordenador, por contra, dispone de un número finito de celdas en las que almacenar bits. Puede profundizarse al respecto mas detalladamente en el tema de teoría de los Sistemas de Representación 


En lenguajes como C/C++, de forma nativa , el tamaño máximo de un valor entero, tipo int , está determinado por la arquitectura del ordenador concreto que se utilice, típicamente 32 celdas binarias, bits , o sea 4 bytes (8 bits son 1 byte ). Sin embargo, en Python, un lenguaje de más alto nivel, no hay un límite predeterminado para el valor absoluto del mayor entero representable. Este valor puede crecer ocupando más y más celdas hasta alcanzar los límites de la memoria disponible en el ordenador.


En la celda que sigue puedes intentar encontrar el límite de la representación de enteros.






1222333545345345 * 123432554356654 *- 12435346543443435 









-1876192258359506035892005852854952237367989050









Para los números reales se utiliza una representación muy diferente a la de los enteros, denominada de punto (o coma) flotante , definida en el estándar IEEE 754 . El tipo de dato se denomina float por ese motivo. El mayor y menor número real representable, en valor absoluto, está en el rango aproximado [1e-323,1.7e308]. Esta es la consecuencia de utilizar un total de 64 bits , 8 bytes , para esta representación.






1e-323 









1e-323









Se debe ser consciente del carácter limitado de la representación de los float . No solo no se puede expresar un número real tan grande como se quiera, sino que la precisión no es infinita y, por tanto, relativamente pocos números reales se pueden representar exactamente.






Expresiones con mezcla de tipos # 


Siempre que el resultado de la expresión sea coherente, en Python se pueden mezclar valores numéricos de diferentes tipos (ej.: int y float ). Cuando esto ocurre, la operación se convierte hacia el tipo más general, que es el float .






( 2 + 3 ) / 2.1 









2.380952380952381













100 ** 1e2 









1e+200









Aumenta el valor del exponente en la celda anterior (ej.: 1e10) ¿Qué pasa? Recuerda que a diferencia de los enteros, los reales, float , tienen un tamaño limitado. Sin embargo, observa el resultado de la celda siguiente. ¿Qué conclusión se puede sacar?






100 ** 1000 









100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000













Números complejos # 


A diferencia de muchos otros lenguajes, Python soporta de forma nativa el trabajo con los números complejos, tipo complex . Véanse los ejemplos a continuación:






1 + 2 j + 2 + 2 J 









(3+4j)













2 * ( 1 + 1 j ) 









(2+2j)









Esta posibilidad del trabajo con complejos resulta muy útil en muchos campos de aplicación de las ciencias y las ingenierías. La cobertura de este tema en este curso será sin embargo muy limitada.


El trabajo con complejos resulta además, como se sabe, una extensión natural del campo de los reales para acomodar la raíz cuadrada (o en general la raíz par) de números negativos. Se debe comentar que la integración de los complejos como dicha extensión está implementada en Python de forma natural, como lo está el paso de los enteros a racionales por efecto de la división.


Ved el siguiente ejemplo:






( - 1 ) ** 0.5 









(6.123233995736766e-17+1j)
















Cadenas de caracteres # 


Los computadores son conocidos por su capacidad para trabajar con valores numéricos. De igual forma, cualquier usuario contemporáneo de los ordenadores sabe que estos se utilizan en muchos otros tipos de aplicaciones que frecuentemente demandan otros tipos de datos.


El manejo de textos es una tarea recurrente en las aplicaciones de los ordenadores (procesadores de texto, correos electrónicos, redes sociales, etc.).
En todos estos casos, las cadenas de caracteres juegan un papel fundamental.


Una cadena de caracteres , tipo de dato str , representa precisamente eso: una ristra de caracteres alfanuméricos que puede ser tratada como una unidad.


Tanto las comillas simples , 'cadena' , como las dobles , "cadena" , identifican los caracteres alfanuméricos que delimitan un valor constante literal de tipo str .






"Esta es una cadena de caracteres" 









'Esta es una cadena de caracteres'













'Se pueden representar con comillas simples' 









'Se pueden representar con comillas simples'













"Las cadenas se pueden " + "sumar" 









'Las cadenas se pueden sumar'









El hecho de que un operador, como la suma + , se comporte de forma diferente dependiendo del tipo de los operandos sobre los que actúa, se conoce como sobrecarga .


A veces, es necesario utilizar una cadena de caracteres larga, distribuida a lo largo de varias líneas. Para ello, basta enmarcar la cadena con triples comillas.






"""Esta es una cadena 
distribuida en 
3 líneas""" 









'Esta es una cadena\ndistribuida en\n3 líneas'









El carácter de escape \n identifica la nueva línea, como veremos enseguida.


En ocasiones, y para mejorar la legibilidad del código, una cadena muy larga conviene programarla fragmentándola usando paréntesis de la siguiente forma:






( "Esta es una cadena larga " 
"que la hemos fragmentado " 
"en tres partes." ) 









'Esta es una cadena larga que la hemos fragmentado en tres partes.'













Otras constantes literales # 


Los formatos básicos para introducir las constantes literales para cada tipo de datos han sido introducidos en los ejemplos anteriores. Hay, sin embargo, otros formatos menos usuales.



Constantes literales int 



Notación decimal : dígitos decimales, opcionalmente precedidos de signo. El primer dígito no puede ser cero.


10 , -1234 




Notación binaria : dígitos binarios {0,1}, precedidos por 0B o 0b .


0b101 , 0B1110 




Notación octal : dígitos octales {0,…,7}, precedidos por 0o o 0O :


0O2357 




Notación hexadecimal : dígitos hexadecimales {0,…9,A,…,F} precedidos por 0x o 0X :


0xFE , 0X1249 







Constantes literales float 



Notación con punto : puede incluir dígitos decimales, signo y punto decimal


234.15 , -10.85 




Notación científica : donde la letra e simboliza la base 10.


-1.01e10 , 23.5e-100 , 1e6 







Constantes literales complex 



Parte real y parte imaginaria deben ser de tipo real:


1.1 + 2j , 10 - 1e2J 







Constantes literales str 



Caracteres alfanuméricos rodeados de comillas simple o dobles.




"Esta es una constante de cadena" 


'Otra cadena que incluye al final un fin de línea\n' 





Además de los caracteres convencionales que representan letras del alfabeto (mayúsculas y minúsculas), dígitos y otros signos diversos, se utiliza una codificación especial para hacer referencia a caracteres especiales .
Estos caracteres especiales comienzan con el signo \ (llamado carácter de escape en este contexto) seguido de un código que lo identifica:


Ejemplos:




Carácter de escape


Función






'\n' 


Cambio de línea




'\t' 


Tabulador




'\\' 


Para utilizar el propio carácter \ 




'\'' 


Para utilizar el propio carácter ' 




"\"" 


Para utilizar el propio carácter " 




'\dd' 


Para hacer referencia al carácter ASCII de valor decimal dd, como '\66' 




'\xhh' 


Para hacer referencia al carácter ASCII de valor hexadecimal hh, como '\x42' 















Variables # 


Sabemos que existen diferentes tipos de valores y operaciones definidas sobre dichos valores, con las que podemos formar expresiones . Y acabamos de ver que el intérprete de Python resulta una calculadora excelente. Sin embargo, a la hora de hacer cálculos más complejos, surge la necesidad de almacenar el valor de resultados intermedios para utilizarlos posteriormente. Esta posibilidad de memorizar (que ya está de presente en la inmensa mayoría de las calculadoras que conocemos) es una de las capacidades más reconocibles de los lenguajes de programación.


La solución es darles nombres o identificadores a los valores intermedios que deseamos retener. En otros lenguajes de programación (y también en Python) se reconoce esta actividad esencial como asignar valores a variables .




El operador de asignación = # 


Analizemos el siguiente ejemplo:






radio = 5 
PI = 3.14159 
area_circulo = PI * radio ** 2 













area_circulo 









78.53975









Nótese la presencia de un nuevo operador, el operador de asignación = .


El fragmento de código realiza los siguientes pasos:



Se da provisionalmente el nombre radio al valor numérico entero 5 . O dicho de otra forma, se le ha asignado el valor 5 a la variable radio .



Se ha dado el nombre PI a una aproximación de cinco valores decimales del número real \(\pi\) 



Finalmente se ha asignado a la variable area_circulo el valor que resulta de evaluar una expresión en la que aparecen:



nombres (de variables) a las que anteriormente se les ha asignado un valor, PI y radio 



los operadores * y ** 



la constante literal entera 2 .







Se tiene entonces, de una parte el nombre (o identificador) a la izquierda del operador = y a la derecha el valor que va a ser asignado a la localización de memoria que dicho nombre identifica.


Cuando se trabaja con el intérprete, la asignación no produce inmediatamente la salida por pantalla del valor almacenado. Si se desea, se puede poner dicho nombre por sí solo en una línea aparte y, entonces, el intérprete mostrará el valor al que hace referencia.


Se puede asignar el mismo valor a varios identificadores simultáneamente:






a = b = c = 1 









O diferentes valores a sendas variables utilizando la coma:






a , b , c = 1 , 2 , 5 











La asignación no es equivalente a la igualdad matemática # 


La semejanza formal entre la sintaxis de la asignación en computación y la igualdad en matemáticas no debe llevarnos a pensar que son la misma cosa.
Para convencernos de ello, baste con considerar el siguiente código de Python:


a = 3 
a = a + 1 





Sentencias similares a la segunda línea en el fragmento anterior aparecen continuamente en programación, aunque resulten absurdas desde el punto de vista matemático.
En programación, se trata simplemente de la operación mediante la cual se utiliza el valor previo asociado a la variable a (que era 3 en el ejemplo) se le adiciona la constante 1 (que aparece literalmente ) y al resultado ( 4 en el ejemplo) se le vuelve a asignar al nombre a .


En resumen, se trata de la actualización del valor asociado a a .








Operadores de asignación compuestos # 


Las sentencias de asignación como las del ejemplo anterior, en las que aparece la variable asignada también a la derecha del operador = , son muy comunes en programación. Python (al igual que en C/C++) ofrece variantes de la asignación para estos casos para las operaciones aritméticas más comunes:


a += 1 # --> a = a + 1 





También se tienen, por ejemplo:


a /= 2 # --> a = a/2 
a -= - 1 # --> a = a - (-1) 
a *= 2 # --> a = a*2 
a **= 2 # --> a = a**2 









#Prueba algunas de estas variantes de la asignación compuesta: 
a = 5 
a //= 2 
a 









2













Variables de Python en memoria # 


El tratamiento que internamente reciben las variables de Python difiere del que reciben en otros lenguajes, como es el caso del lenguaje C/C++.




En C/C++ se usa tipado estático : el tipo de cada variable se declara antes de usarlo y los nombres hacen referencia permanente a localizaciones o bloques de memoria, no cambian durante el ámbito de uso de la variable. Cada uno de estos bloques tiene la capacidad de almacenar la representación interna del tipo de dato declarado.


En el ejemplo C/C++ de la figura, x e y representan dos bloques de memoria diferentes. La primera asignación, hace que en el bloque correspondiente a x se almacene un 1 y en la segunda asignación, que el contenido de x (un 1 como se ha visto) sea copiado en las celdas de memoria que representan a y .


En el caso de Python, la interpretación es diferente. Python es un lenguaje de tipado dinámico , donde no hay que declarar el tipo de las variables antes de usarlas. De manera que, cuando se realiza la primera asignación, se almacena el valor 1 en algún bloque de memoria del ordenador, y se le asigna a ese valor el nombre o identificador x . Cuando se realiza la siguiente asignación, se le asigna un nuevo nombre, un alias , en este caso y , al mismo bloque de memoria donde estaba colocado el 1 .


En lenguajes como C/C++, cada variable identifica una localización de memoria diferente que puede modificar su contenido: de ahí el nombre de variable. Sin embargo, en Python los nombres funcionan como etiquetas . Diferentes etiquetas pueden hacer referencia al mismo valor en la misma localización de memoria. En cualquier caso, como es estándar en la bibliografía, usaremos el término variable en Python.






Inmutabilidad # 


Analicemos a continuación la siguiente figura:




Si ahora en el código de C/C++ se ejecuta la asignación x = 2 , simplemente se modifica el contenido del bloque asociado a la variable x , que ahora pasará a contener un 2 .


En el caso de Python, los enteros, int , reales, float y otros tipos se consideran inmutables . Esto significa que una vez almacenado en memoria el valor, este no se puede modificar. Ese bloque de memoria es inmutable . Por ello, cuando se hace la asignación x = 2 , en realidad se está creando, en otra localización de memoria, espacio para almacenar el nuevo valor 2 , haciendo ahora que la etiqueta x , que antes estaba ligada al bloque de memoria con valor 1 , se refiera ahora al bloque de memoria con valor 2 .


De manera que, aunque el mecanismo de funcionamiento de la memoria en Python es diferente, para el caso de los tipos inmutables el resultado neto es el mismo.






La recolección de basura # 


Analicemos el siguiente fragmento de código:


x = 1.23 
y = x 
x = 2.37 
y = 'Hola' 





¿Qué pasa con el valor del 1.23 ? En principio, no es necesario que permanezca en memoria: ¡no hay ninguna variable asociada a ese bloque de memoria! El motor de tiempo de ejecución ( runtime engine ) de Python se encargará de eliminarlo de la memoria utilizando un proceso que se conoce como recolección de basura ( garbage collection ).


Python mantiene internamente un contador que registra cuantas variables están en cada momento haciendo referencia a una localización en memoria. Tras la ejecución de y = x este contador tendrá valor 2 para el valor 1.23 . Sin embargo, las dos sentencias siguientes harán que ese contador tome el valor 0 . A partir de ahí, la memoria que ocupaba deja de ser necesaria y puede ser devuelta al Sistema Operativo para ser reutilizada posteriormente, por nuestro programa o por cualquier otro. Esta es otra de las tantas diferencias notables entre C/C++ y Python. En C/C++, siendo un lenguaje de más bajo nivel, el programador es completamente responsable de la gestión de la memoria.











Introducción al concepto de objeto # 


Tanto las variables como las funciones, que veremos más adelante, son referencias a objetos en Python.


Un objeto es una entidad conformada por atributos de dos tipos:



Un conjunto de datos que determinan el estado del objeto.



Una serie de métodos , funciones específicas que pueden ser aplicadas a los datos del objeto para obtener información acerca de este o, en ocasiones, para modificarlo.




Todo objeto en Python tiene una identidad , un tipo y un valor :



La identidad de un objeto nunca cambia una vez que ha sido creado. Ocupa una posición en memoria fija una vez creado.



El tipo , del que ya hemos hablado, determina los posibles valores y operadores que ese objeto soporta.
Al igual que la identidad, el tipo de un objeto es inalterable.



El valor de un objeto puede o no variar en función del tipo. Los objetos cuyo valor puede cambiar son objetos mutables mientras que los que no pueden ser alterados son objetos inmutables .




Ya hemos comentado que los objetos con tipos int , float o str entre otros, son inmutables. Más adelante veremos tipos como las listas y los diccionarios que son mutables.


























previous


Presentación








next


Funciones predefinidas






















Contents





El intérprete como calculadora 


Expresiones y sentencias 

Operadores aritméticos básicos 


Reglas de precedencia 


El operador de exponenciación ** 


Operadores binarios y unarios 


El operador división 


La división entera // y el operador resto % 


Tabla de precedencias 





Tipos de datos 

Clasificación 


Tipos enteros y reales 


Expresiones con mezcla de tipos 


Números complejos 


Cadenas de caracteres 


Otras constantes literales 





Variables 

El operador de asignación = 

La asignación no es equivalente a la igualdad matemática 





Operadores de asignación compuestos 


Variables de Python en memoria 


Inmutabilidad 


La recolección de basura 





Introducción al concepto de objeto 





























© Copyright Félix Miguel Trespaderne / Rogelio Mazaeda Echevarría.





















All content on this site (unless otherwise specified) is licensed under the CC BY-NC-SA 4.0 license
