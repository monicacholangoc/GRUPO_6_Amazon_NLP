# La metodología CRISP-DM en ciencia de datos

Fuente: [Instituto de Ingeniería del Conocimiento (UAM)](https://www.iic.uam.es/innovacion/metodologia-crisp-dm-ciencia-de-datos/)  
_Copia local para lectura fuera de línea. El formato original puede verse en la URL._

---

La metodología CRISP-DM en ciencia de datos 

Innovación 

Facebook Twitter Whatsapp Linkedin Mail 

Se cumplen aproximadamente dos décadas de la aparición de la metodología CRISP-DM (CRoss-Industry Standard Process for Data Mining) [1] , y la prestigiosa revista IEEE Transactions on Knowledge and Data Engineering ha publicado un interesante artículo [2] donde relata el recorrido histórico de la misma, su impacto en la industria y su actual aplicabilidad en proyectos de ciencia de datos .

¿Qué es la metodología CRISP-DM?

CRISP-DM se puede considerar como la metodología de facto para proyectos dedicados a extraer valor de los datos, tal como lo reflejan las encuestas realizadas a profesionales del campo [3] . Durante estos veinte años, la metodología CRISP-DM ha sido fuente de inspiración de otros estándares como SEMMA de SAS o ASUM-DM de IBM, así como ha dado lugar a múltiples variantes que amplían o particularizan CRISP-DM a una industria o tipo de proyecto.

Y es que surgen algunas limitaciones de la metodología frente a los cambios en los proyectos de ciencia de datos durante los últimos años, que requieren que esta se adapte a nuevas formas de hacer, incluyendo nuevas fases o aplicándola solo en determinadas partes de los proyectos.

Desde el Instituto de Ingeniería del Conocimiento (IIC), por ejemplo, hemos comprobado que puede ser especialmente útil para planificar y explicar la gestión y ejecución de los proyectos a determinados clientes.

Fases de la metodología CRISP-DM

La metodología CRISP-DM se conceptualiza en 6 fases, tal como se muestra en la Figura 1. En la primera fase, el entendimiento del negocio, el equipo de trabajo debe comprender los objetivos y requisitos del proyecto definidos por el cliente, para poder convertir este conocimiento en una definición técnica del problema .

Figura 1. Esquema del ciclo CRISP-DM estándar

Esta fase es necesaria para que los miembros del equipo de desarrollo puedan entender el contexto del proyecto y resolver las dudas sobre el negocio que se pudieran tener. Es una fase que requiere una comunicación intensa entre el cliente y el equipo técnico.

Una vez está claro lo que el cliente pide, se pasa a la fase de comprensión de los datos. El equipo técnico realiza un análisis exploratorio con el objetivo de obtener una visión general de lo que se puede conseguir con los datos . Esta fase complementa el trabajo de la fase anterior, realizando un análisis guiado por el conocimiento de negocio adquirido.

Tras el resultado de esta fase se debería tener una idea clara de la viabilidad del proyecto y los resultados esperados. De ser así, se avanzaría a dos fases de trabajo técnico muy interrelacionadas, en las cuales se desarrollaría la solución al problema de negocio planteado.

La primera es la denominada preparación de los datos, que cubre todas las actividades para construir el conjunto de datos definitivo que se empleará en la siguiente fase, la de modelado de datos. Aquí el equipo técnico realizará los análisis y modelos pertinentes de los que se deriven los resultados y conclusiones del proyecto. El cliente determinará en la fase de evaluación la calidad de esos resultados y decidirá cómo pueden explotarse antes de la fase de despliegue.

Más allá de que se haya descrito la metodología como un proceso secuencial, es importante incidir en su carácter iterativo .

Tal como se puede observar en la Figura 1, las fases 1 y 2 pueden sucederse repetitivamente si tras los resultados de los análisis exploratorios (fase 2) se descubren aspectos que redefinen los objetivos de negocio (fase 1). De la misma manera, la fase de modelado (fase 4) puede motivar nuevos preprocesados de los datos (fase 3) que mejoren los análisis realizados. Finalmente, el resultado de la evaluación (fase 5) puede derivar en nuevas necesidades de negocio (fase 1).

Limitaciones de CRISP-DM en proyectos de datos

Si atendemos a su nombre, esta metodología surge en un momento en que las empresas tecnológicas que se centran en extraer conocimiento de los datos se agrupan bajo el término de minería de datos . Sin embargo, durante la última década, y especialmente a partir de 2016, este término ha sido sustituido por el de ciencia de datos [4] . Tal como acertadamente apuntan los autores, esta transmutación responde a un cambio en la manera en que se afrontan los proyectos que buscan extraer valor de los datos, algo que también requiere adaptar o modificar la metodología CRISP-DM.

En los años 90, los proyectos de datos estaban orientados a la consecución de unos objetivos concretos, bastante definidos al principio del mismo. Durante estos últimos veinte años se ha ido ampliando el alcance y la dimensión de estos proyectos, incluyendo una aproximación más exploratoria a la hora de afrontarlos.

CRISP-DM se diseñó pensando en los procesos asociados para cumplir los objetivos del proyecto, mientras que el nuevo enfoque de ciencia de datos requiere una aproximación más flexible que ponga el dato en el centro . Esta nueva perspectiva implica que los propios objetivos negocio podrían no estar disponibles al principio del proyecto, y que se tendrían que incluir en la metodología actividades de carácter exploratorio que ayuden a determinarlo a través de análisis sobre los propios datos.

Otra asunción implícita en la metodología es la disponibilidad de datos de calidad , quedando fuera todas las actividades necesarias para conseguirlos. En los años 90, las empresas que acometían proyectos basados en análisis de datos eran pocas, y técnicamente bastante avanzadas. Actualmente, el número de organizaciones que están viendo el valor que aportan estos proyectos se han multiplicado exponencialmente en estos últimos 20 años, introduciéndose en este campo con diferentes niveles de madurez tecnológica.

Esto supone que no es infrecuente que el propio proceso de catalogación, recolección y validación de los datos se convierta en un proyecto en sí mismo. Además, con la disponibilidad de grandes volúmenes de datos, estas actividades se convierten en todo un reto. Todo esto puede llevar a tener que acomodar la metodología al hecho de que los datos estén disponibles en distintos momentos del tiempo , teniendo que empezar con el proyecto una vez recibida una primera muestra. Este desafío se acentúa en el caso que los datos que se manejen sean de distinta naturaleza.

Por otro lado, los productos de datos, como aplicaciones interactivas o sistemas de toma de decisiones en tiempo real , han tomado mucha relevancia en estas dos últimas décadas. Repasando alguno de los productos que ofrece el IIC, podemos encontrar una amplia variedad que se aplican en distintos sectores: detección de fraude en tiempo real [5] , detección precoz de síntomas de sepsis [6] , optimización de la gestión forestal [7] , evaluación de competencias transversales [8] o monitorización y análisis de redes sociales [9] .

En estos casos, CRISP-DM incluye una fase de despliegue, pero que no recoge todas las actividades que requiere el mantenimiento de un producto. En especial, carece de procesos específicos para la gobernanza de los datos , tales como la recolección, el almacenamiento, versionado, la seguridad y la privacidad de los datos incluyendo el cumplimiento regulatorio y legal, que en el caso de datos personales ha cobrado una relevancia fundamental.

Tampoco se encuentran en otras fases de la metodología actividades específicas del desarrollo software del producto, como serían aspectos relacionados con la arquitectura de sistemas o la visualización e interacción con el usuario. En líneas generales, el desarrollo de un producto basado en datos requiere incorporar aspectos metodológicos relacionados con el desarrollo de software que van más allá del análisis y modelado de los datos.

El encaje de CRISP-DM en los proyectos actuales de ciencia de datos

Más allá de las limitaciones señaladas en el apartado anterior, coincidimos con los autores del artículo en que esta metodología sigue teniendo recorrido en aquellos proyectos que tienen una definición, a priori, clara y acotada del problema de negocio y de los resultados que se esperan obtener. En caso contrario, los autores proponen una metodología alternativa que permite combinar de manera más flexible las distintas etapas del proyecto, incluyendo aquellas que no están presentes en CRISP-DM y que son necesarias en proyectos más exploratorios o centrados en el desarrollo de un producto.

En nuestra experiencia, un aspecto a destacar que hemos contrastado es que la metodología CRISP-DM, o ligeras variaciones de la misma, es muy útil de cara a explicar la gestión del proyecto al cliente . Al ser una metodología orientada a procesos que siguen una trayectoria bastante secuencial, facilita el entendimiento por parte del cliente de la planificación y ejecución del proyecto . Esto es especialmente útil cuando estos tienen poca o nula experiencia en proyectos basados en datos.

Al final, cualquier metodología aporta un marco conceptual que impacta en tres aspectos claves de un proyecto. Primero, establece un vocabulario común que facilita la comunicación. Segundo, permite coordinar las actividades entre los distintos implicados al seguir todos los mismos procesos. Finalmente, ayuda en la gestión de las expectativas, ya que permite predecir tanto pasos futuros (hitos y próximas fases) como resultados esperados (entregables).

En relación a este último punto, sin llegar a ser una metodología de gestión de proyectos clásica en la que se puede estimar a priori con bastante granularidad los tiempos y costes que va a suponer el proyecto, CRISP-DM es una metodología bastante determinista en el sentido de que las fases y tipo de resultados están definidas de antemano. Esto reduce la incertidumbre del proyecto, reduce la complejidad y contribuye a que el cliente tenga una mayor comprensión y control de todo el proceso . Además, es muy probable que esta gestión le resulte familiar porque se asemeje a la que esté llevando en otros proyectos no relacionados con datos.

Por decirlo con otras palabras, podríamos ver CRISP-DM como una adaptación de la metodología tradicional de gestión de proyectos al contexto de la ciencia de datos. El punto inflexión reside en determinar si el proyecto que se va a realizar casa con esta visión tradicional o es preferible una metodología más ágil , ya que, dependiendo del tipo de cliente y de los resultados esperados, puede ser crítico utilizar una u otra.

[1] https://www.kde.cs.uni-kassel.de/lehre/ws2012-13/kdd/files/CRISPWP-0800.pdf 

[2] CRISP-DM Twenty Years Later: From Data Mining Processes to Data Science Trajectories 

[3] What main methodology are you using for your analytics, data mining, or data science projects? Poll (kdnuggets.com) 

[4] https://trends.google.es/trends/explore?hl=es&tz=-120&date=all&q=data+science,data+mining&sni=3 

[5] https://www.iic.uam.es/soluciones/banca/lynx/ 

[6] https://www.iic.uam.es/proyecto/deteccion-de-sepsis/ 

[7] https://www.iic.uam.es/proyecto/optimizacion-gestion-forestal/ 

[8] https://www.iic.uam.es/soluciones/recursos-humanos/evalue/ 

[9] https://www.iic.uam.es/soluciones/entorno-digital/lynguo/
