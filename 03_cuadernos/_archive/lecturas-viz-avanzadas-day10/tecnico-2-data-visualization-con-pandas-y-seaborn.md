# Data Visualization con Pandas y Seaborn

Fuente: [Patricia Carmona · Ironhack (Medium)](https://medium.com/ironhack/data-visualization-con-pandas-y-seaborn-1044906af34f)  
_Copia local para lectura fuera de línea. El formato original puede verse en la URL._

---

Data Visualization con pandas y seaborn

Patricia Carmona 

5 min read 
· 
Apr 20, 2020 

-- 

Share

Press enter or click to view image in full size 

Photo by Michael Payne on Unsplash 
La visualización es la mejor representación de los datos y si el aspecto visual es tan importante, es recomendable hacer uso de librerías que permitan trabajar de forma adecuada el diseño del gráfico .

Esta visualización no es solo el último paso en análisis de datos, en ocasiones es el comienzo, gracias a librerías como seaborn desarrolladas para representar relaciones estadísticas entre variables.

El valor principal de la visualización está en representar los insights que se encuentran en los datos. Para ello hay que trabajar en 3 pasos:

Organizar los datos (Data Wrangling o Data Cleaning)

Desarrollar el gráfico

Estilizarlo (darle el aspecto visual que queremos)

Con matplotlib , se trabaja siguiendo este proceso y el diseño es muy customizable, pero es cierto que es muy laborioso. Por contra, hay librerías como seaborn , que facilitan tanto el trabajo con los datos como la personalización de los gráficos.

¿Por qué seaborn?

Seaborn es más que una mera librería de visualización, es una librería para representación estadística , ya que muestra fácilmente la relación que guardan los datos para detectar tendencias y patrones.

Manejo de los datos: Seaborn es capaz de “entender” directamente un DataFrame, representando fácilmente distribuciones de datos o agregaciones, sin desarrollar muchas líneas de código.

Visualizaciones disponibles : Los gráficos ayudan a entender los datos y para ello, es necesario seleccionar el gráfico más adecuado. La galería de seaborn es una de las más amplias, desarrollada para representar análisis estadísticos de forma sencilla.

Personalización: El aspecto visual de un gráfico que tan laborioso es con matplotlib, se desarrolla de forma muy sencilla con seaborn.

A tener en cuenta

Seaborn es una librería que está desarrollada sobre matplolib , por lo que algunos de los métodos de matplotlib se utilizan con seaborn.

Métodos de matplotlib que se reutilizan en seaborn 

plt.figure()
plt.title()
plt.legend()
plt.show() 

Configuración de estilos

La librería seaborn permite personalizar el estilo del gráfico, la paleta de colores que se utiliza, la fuente y el tamaño de los diferentes integrantes de la visualización, así como definir un contexto en el que se va a utilizar el gráfico para adaptar el tamaño.

sns.set_style()
sns.set_palette()
sns.set_context() 

En el repositorio del proyecto puedes encontrar todas las opciones que admite cada configuración, así como el listado completo de rcparams (que está basado en matplotlib )

Análisis de datos con seaborn

Seaborn dispone de diferentes gráficos para la representación de la relación que guardan los datos de un DataFrame. ¿Qué gráfico utilizar en cada caso? Depende.

Barplot . Muy recomendable para la visuación de datos agregados, como la media.

sns.barplot(x='Food', y='Age', hue='Gender', data=df, estimator=np.median) 

Bar plot de pedidos por edad y género 
Incluye una barra de error en la parte superior de cada barra e indican qué valores se esperan para

Histograma . Para conocer la distribución de los datos, el histograma es una herramienta básica, sin embargo, esta representación está muy influenciada por el número de bins que se seleccionen y el ancho de cada uno.

sns.distplot(df['Age']) 

Histograma de distribución de la serie ‘Age’ 
KDE plots (Kernel Density Estimation plots). Genera mejores representaciones de distribuciones de datos que un histograma al suavizar la forma de los datos, pero no aporta información estadística.

sns.kdeplot(data=df['Age'], shade=True) 

KDE plot de la serie ‘Age’ 
Box plots . Útiles para conocer los rangos de datos, si existen outliers, la media y el rango intercuartil en el que se distribuyen los datos.

sns.boxplot(data=df, x='Food', y='Age') 

Box plot 
Cada caja representa los cuartiles en los que se mueve cada grupo de usuarios según sus pedidos de comida. Los extremos representan el grueso de la distribución y por último, los puntos detectan los outliers, que son aquellos usuarios con edades tempranas o avanzadas que han realizado algún pedido y que quedan fuera del rango de edades más comunes del DataFrame.

Puede verse que según representa la caja ‘Traditional food’ el grupo de edad de usuarios que piden este tipo de comida es más amplio que el que pide ‘Western Food’, que además, son más jóvenes.

Violin plots . La conjunción de KDE + box plots, clave para comparar distribuciones. Un violin representa la distribución, su media, el rango intercuartil y el intervalo de confianza de 95% en el que se distruyen los mapas.

sns.violinplot(data=df, x='Gender', y='Age') 

Violin plot de edades por género 
Cada violín representa la distribución de usuarios por edades en función de su género. El violín tiene una función muy similar al de la caja de box plot, pero representando la densidad de la distribución.

Este gráfico representa que el volumen de hombres que piden comida es muy amplio en los early-twenties y que el rango de edad de las mujeres es más amplio, desde los mid-twenties hasta los 40.

Catplot() . Este método es muy útil cuando en el análisis se representan variables categóricas. Otra alternativa al diagrama de barras.

sns.catplot(x='Day', y='Age', hue='Gender', kind="swarm", data=df) 

Catplot de distribución de pedidos por día, edad y género 
El gráfico muestra que el día 7 fue el día con mayor número de pedidos (por la densidad de puntos), los hombres fueron más activos que las mujeres y la franja de edad estuvo entre los 20 y los 30.

Scatter plots . Ideal para la representación de correlaciones y cómo una variable afecta a la otra.

Scatter de relación edad, día y tipo de comida 
Con un DataFrame con más variables numéricas con relación, los gráficos de scatter son muy útiles para analizar la correlación entre éstas.

Conclusiones

Con estos sencillos gráficos es muy fácil visualizar la relación entre variables y representar estadísticamente el DataFrame sin necesidad de muchas líneas de código, para profundizar en el análisis de datos que necesitas de forma sencilla.

En el repositorio de este proyecto puedes encontrar todo el código de desarrollo, las configuraciones de estilos y parámetros para potenciar la visualización con seaborn. ¡Seguimos!

Más info por si quieres profundizar

Si quieres indagar más en la librería seaborn, te dejo algunas referencias:

Tutorial completo de Seaborn .

Seaborn for Data Analysis . Desarrollo de un análisis con la librería seaborn.

Python gallery . Cómo desarrollar cada gráfico de forma correcta.
