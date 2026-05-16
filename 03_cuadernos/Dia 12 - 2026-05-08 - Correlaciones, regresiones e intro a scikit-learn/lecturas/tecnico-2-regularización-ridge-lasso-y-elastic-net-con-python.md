# Regularización Ridge, Lasso y Elastic Net con Python

Fuente: [Joaquín Amat · cienciadedatos.net](https://cienciadedatos.net/documentos/py14-ridge-lasso-elastic-net-python)  
_Copia local para lectura fuera de línea. El formato original puede verse en la URL._

---

Regularización Ridge, Lasso y Elastic Net con Python 

Regularización Ridge, Lasso y Elastic Net con Python

Joaquín Amat Rodrigo

Noviembre, 2020 (última actualización Enero 2026)

Más sobre ciencia de datos en: cienciadedatos.net 

Regresión lineal con Python 

Regresión lineal múltiple con Python 

Regresión logística con Python 

Regularización Ridge, Lasso y Elastic Net con Python 

Machine learning con Python y Scikitlearn 

Árboles de decisión con Python: regresión y clasificación 

Random Forest con Python y Scikit-learn 

Gradient Boosting con Python y Scikit-learn 

Gradient Boosting probabilístico con Python 

Máquinas de Vector Soporte (SVM) 

Redes neuronales con Python 

Análisis de componentes principales PCA 

Clustering 

Detección de anomalías con PCA 

Detección de anomalías con autoencoders 

Detección de anomalías con Gaussian Mixture Models 

Detección de anomalías con Isolation Forest 

Análisis de texto (text mining) con Python 

Reglas de asociación 

Análisis Tweets con Python 

Introducción ¶ 

La regresión lineal es un método estadístico que trata de modelar la relación entre una variable continua y una o más variables independientes mediante el ajuste de una ecuación lineal. Tres de las limitaciones que aparecen en la práctica al tratar de emplear este tipo de modelos (ajustados por mínimos cuadrados ordinarios) son:

Se ven perjudicados por la incorporación de predictores correlacionados.

No realizan selección de predictores, todos los predictores se incorporan en el modelo aunque no aporten información relevante. Esto suele complicar la interpretación del modelo y reducir su capacidad predictiva.

No pueden ajustarse cuando el número de predictores es superior al número de observaciones.

Una forma de atenuar el impacto de estos problemas es utilizar estrategias de regularización como ridge , Lasso o Elastic Net , que fuerzan a que los coeficientes del modelo tiendan a cero, minimizando así el riesgo de overfitting , reduciendo varianza, atenuando el efecto de la correlación entre predictores y reduciendo la influencia en el modelo de los predictores menos relevantes.

A lo largo de este documento, se describen de forma progresiva los fundamentos teóricos de la regresión lineal con regularización ridge , Lasso y Elastic Net , los principales aspectos prácticos a tener en cuenta y ejemplos de cómo crear este tipo de modelos en Python y Scikitlearn .

Regresión lineal ¶ 

El modelo de regresión lineal (Legendre, Gauss, Galton y Pearson) considera que, dado un conjunto de observaciones $\{y_i, x_{i1},...,x_{np}\}^{n}_{i=1}$, la media $\mu$ de la variable respuesta $y$ se relaciona de forma lineal con la o las variables regresoras $x_1$ ... $x_p$ acorde a la ecuación:

$$\mu_y = \beta_0 + \beta_1 x_{1} + \beta_2 x_{2} + ... + \beta_p x_{p}$$
El resultado de esta ecuación se conoce como la línea de regresión poblacional, y recoge la relación entre los predictores y la media de la variable respuesta.

Otra definición que se encuentra con frecuencia en los libros de estadística es:

$$y_i= \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + ... + \beta_p x_{ip} +\epsilon_i$$
En este caso, se está haciendo referencia al valor de $y$ para una observación $i$ concreta. El valor de una observación puntual nunca va a ser exactamente igual al promedio, de ahí que se añada el término de error $\epsilon$.

En ambos casos, la interpretación de los elementos del modelo es la misma:

$\beta_{0}$: es la ordenada en el origen, se corresponde con el valor promedio de la variable respuesta $y$ cuando todos los predictores son cero.

$\beta_{j}$: es el efecto promedio que tiene sobre la variable respuesta el incremento en una unidad de la variable predictora $x_{j}$, manteniéndose constantes el resto de variables. Se conocen como coeficientes parciales de regresión.

$e$: es el residuo o error, la diferencia entre el valor observado y el estimado por el modelo. Recoge el efecto de todas aquellas variables que influyen en $y$ pero que no se incluyen en el modelo como predictores.

En la gran mayoría de casos, los valores $\beta_0$ y $\beta_j$ poblacionales se desconocen, por lo que, a partir de una muestra, se obtienen sus estimaciones $\hat{\beta}_0$ y $\hat{\beta}_j$. Ajustar el modelo consiste en estimar, a partir de los datos disponibles, los valores de los coeficientes de regresión que maximizan la verosimilitud ( likelihood ), es decir, los que dan lugar al modelo que con mayor probabilidad puede haber generado los datos observados. El método empleado con más frecuencia es el ajuste por mínimos cuadrados ordinarios ( OLS ), que identifica como mejor modelo la recta (o plano si es regresión múltiple) que minimiza la suma de las desviaciones verticales entre cada dato de entrenamiento y la recta, elevadas al cuadrado.

Los coeficientes de regresión del modelo son por lo tanto los que controlan la influencia de cada predictor en el modelo. Sin embargo, la magnitud de cada coeficiente depende de las unidades en las que se midan los predictores, por lo que su magnitud no está asociada con la importancia de cada predictor. Para poder considerar que, cuanto más próximo a cero es el coeficiente un predictor, menor su influencia sobre la variable respuesta en comparación al resto, es necesario estandarizar todos los predictores antes de ajustar el modelo.

Regularización ¶ 

Las estrategias de regularización incorporan penalizaciones en el ajuste por mínimos cuadrados ordinarios ( OLS ) con el objetivo de evitar overfitting , reducir varianza, atenuar el efecto de la correlación entre predictores y minimizar la influencia en el modelo de los predictores menos relevantes. Por lo general, aplicando regularización se consigue modelos con mayor poder predictivo (generalización).

⚠️ 
Warning 

Dado que estos métodos de regularización actúan sobre la magnitud de los coeficientes del modelo, todos deben de estár en la misma escala, por esta razón es necesario estandarizar o normalizar los predictores antes de entrenar el modelo .

Ridge ¶ 

La regularización Ridge penaliza la suma de los coeficientes elevados al cuadrado $(||\beta||^2_2 = \sum_{j=1} ^p \beta^2_j)$. A esta penalización se le conoce como l2 y tiene el efecto de reducir el valor de todos los coeficientes del modelo pero sin que estos lleguen a cero . El grado de penalización está controlado por el hiperparámetro $\lambda$. Cuando $\lambda = 0$, la penalización es nula y el resultado es equivalente al de un modelo lineal por mínimos cuadrados ordinarios ( OLS ). A medida que $\lambda$ aumenta, mayor es la penalización y menor el valor de los coeficientes.

$$\sum^n_{i=1}(y_i - \beta_0 - \sum^p_{j=1} \beta_j x_{ij})^2 + \lambda \sum^p_{j=1} \beta_j^2 = \text{suma residuos cuadrados} + \lambda \sum^p_{j=1} \beta_j^2$$
La principal ventaja de aplicar ridge frente al ajuste por mínimos cuadrados ordinarios ( OLS ) es la reducción de varianza. Por lo general, en situaciones en las que la relación entre la variable respuesta y los predictores es aproximadamente lineal, las estimaciones por mínimos cuadrados tienen poco bias pero aún pueden sufrir alta varianza (pequeños cambios en los datos de entrenamiento tienen mucho impacto en el modelo resultante). Este problema se acentúa conforme el número de predictores introducido en el modelo se aproxima al número de observaciones de entrenamiento, llegando al punto en que, si $p>n$, no es posible ajustar el modelo por mínimos cuadrados ordinarios. Empleando un valor adecuado de $\lambda$, el método de ridge es capaz de reducir varianza sin apenas aumentar el bias , consiguiendo así un menor error total.

La desventaja del método ridge es que, el modelo final, incluye todos los predictores. Esto es así porque, si bien la penalización fuerza a que los coeficientes tiendan a cero, nunca llegan a ser exactamente cero (solo si $\lambda=\infty$). Este método consigue minimizar la influencia sobre el modelo de los predictores menos relacionados con la variable respuesta pero, en el modelo final, van a seguir apareciendo. Aunque esto no supone un problema para la precisión del modelo, sí lo es para su interpretación.

Lasso ¶ 

La regularización Lasso penaliza la suma del valor absolutos de los coeficientes de regresión $(||\beta||_1 = \sum_{j=1} ^p |\beta_j|)$. A esta penalización se le conoce como l1 y tiene el efecto de forzar a que los coeficientes de los predictores tiendan a cero . Dado que un predictor con coeficiente de regresión cero no influye en el modelo, lasso consigue excluir los predictores menos relevantes. Al igual que en ridge , el grado de penalización está controlado por el hiperparámetro $\lambda$. Cuando $\lambda = 0$, el resultado es equivalente al de un modelo lineal por mínimos cuadrados ordinarios. A medida que $\lambda$ aumenta, mayor es la penalización y más predictores quedan excluidos.

$$\sum^n_{i=1}(y_i - \beta_0 - \sum^p_{j=1} \beta_j x_{ij})^2 + \lambda \sum^p_{j=1} |\beta_j| = \text{suma residuos cuadrados} + \lambda \sum^p_{j=1} |\beta_j|$$

Comparación Ridge y Lasso ¶ 

La principal diferencia práctica entre lasso y ridge es que el primero consigue que algunos coeficientes sean exactamente cero, por lo que realiza selección de predictores, mientras que el segundo no llega a excluir ninguno. Esto supone una ventaja notable de lasso en escenarios donde no todos los predictores son importantes para el modelo y se desea que los menos influyentes queden excluidos.

Por otro lado, cuando existen predictores altamente correlacionados (linealmente), ridge reduce la influencia de todos ellos a la vez y de forma proporcional, mientras que lasso tiende a seleccionar uno de ellos, dándole todo el peso y excluyendo al resto. En presencia de correlaciones, esta selección varía mucho con pequeñas perturbaciones (cambios en los datos de entrenamiento), por lo que, las soluciones de lasso , son muy inestables si los predictores están altamente correlacionados.

Para conseguir un equilibrio óptimo entre estas dos propiedades, se puede emplear lo que se conoce como penalización elastic net , que combina ambas estrategias.

Elastic net ¶ 

Elastic net incluye una regularización que combina la penalización l1 y l2 $(\alpha \lambda ||\beta||_1 + \frac{1}{2}(1- \alpha)||\beta||^2_2)$. El grado en que influye cada una de las penalizaciones está controlado por el hiperparámetro $\alpha$. Su valor está comprendido en el intervalo [0,1]. Cuando $\alpha = 0$, se aplica ridge y cuando $\alpha = 1$ se aplica lasso . La combinación de ambas penalizaciones suele dar lugar a buenos resultados. Una estrategia frecuentemente utilizada es asignarle casi todo el peso a la penalización l1 ($\alpha$ muy próximo a 1) para conseguir seleccionar predictores y un poco a la l2 para dar cierta estabilidad en el caso de que algunos predictores estén correlacionados.

$$\frac{\sum^n_{i=1}(y_i - \beta_0 - \sum^p_{j=1} \beta_j x_{ij})^2}{2n} + \lambda (\alpha \sum^p_{j=1} |\beta_j| + \frac{1-\alpha}{2} + \sum^p_{j=1} \beta_j^2$$

Lambda Search ¶ 

Encontrar el mejor modelo implica identificar el valor óptimo del hiperparámetro de regularización lambda ($\lambda$). Al tratarse de un hiperparámetro, no hay forma de saber de antemano qué valor es el adecuado. Una forma de lograrlo es emplear validación cruzada o generalized cross validation , esta última es una adaptación eficiente de leave-one-out cross validation disponible para la regulación Ridge . Con scikit learn esto puede conseguirse fácilmente de dos formas:

Combinar GridSearchCV y un modelo de tipo Ridge , Lasso o ElasticNet .

Emplear RidgeCV , LassoCV o ElasticNetCV . Son adaptaciones que incorporan validación cruzada. Si no se indica nada en el argumento cv , en RidgeCV , se aplica Generalized Cross-Validation (GCV) . Si se le indica un valor entero, se aplica validación cruzada con GridSearchCV . Por ejemplo cv=10 equivale a 10-fold cross-validation , en lugar de Generalized Cross-Validation .

Por lo general, las versiones que incorporan la validación cruzada son más directas y cómodas de utilizar, sin embargo, hay situaciones para las que no son adecuadas. Por ejemplo, si los datos tienen un orden temporal (series temporales), la validación cruzada debe hacer un reparto ordenado de las observaciones, lo que se consigue combinando sklearn.model_selection.TimeSeriesSplit con GridSearchCV . Para más información sobre cómo utilizar GridSearchCV consultar machine learning con scikit learn .

Se emplee un método u otro siempre hay que estandarizar o normalizar los predictores .

Aunque el valor óptimo de $\lambda$ es aquel con el que se minimiza el error de validación cruzada, una práctica extendida es utilizar, en lugar de este, el mayor valor de $\lambda$ que se aleja menos de una desviación típica del óptimo. De este modo, se consigue un modelo más sencillo (excluye más predictores) pero cuya capacidad predictiva es similar a la conseguida con el modelo más complejo.

✏️ 
Note 

scikitlearn utiliza el argumento alpha para hacer referencia al parámetro de regularización lambda ($\lambda$) y el argumento l1_ratio para referirse al parámetro de mezcla alpha ($\alpha$) en Elastic Net.

Ejemplo regresión ¶ 

El departamento de calidad de una empresa de alimentación se encarga de medir el contenido en grasa de la carne que comercializa. Este estudio se realiza mediante técnicas de analítica química, un proceso relativamente costoso en tiempo y recursos. Una alternativa que permitiría reducir costes y optimizar tiempo es emplear un espectrofotómetro (instrumento capaz de detectar la absorbancia que tiene un material a diferentes tipos de luz en función de sus características) e inferir el contenido en grasa a partir de sus medidas.

Antes de dar por válida esta nueva técnica, la empresa necesita comprobar qué margen de error tiene respecto al análisis químico. Para ello, se mide el espectro de absorbancia a 100 longitudes de onda en 215 muestras de carne, cuyo contenido en grasa se obtiene también por análisis químico, y se entrena un modelo con el objetivo de predecir el contenido en grasa a partir de los valores dados por el espectrofotómetro.

Los datos meatspec.csv empleados en este ejemplo se han obtenido del magnífico libro Linear Models with R, Second Edition .

Librerías ¶ 

Las librerías utilizadas en este ejemplo son:

# Tratamiento de datos 
# ============================================================================== 
import pandas as pd 
import numpy as np 

# Gráficos 
# ============================================================================== 
import matplotlib.pyplot as plt 
plt . style . use ( 'fivethirtyeight' ) 
plt . rcParams [ 'lines.linewidth' ] = 1.5 
plt . rcParams [ 'font.size' ] = 8 
import seaborn as sns 

# Preprocesado y modelado 
# ============================================================================== 
from scipy.stats import pearsonr 
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import root_mean_squared_error 
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import Ridge 
from sklearn.linear_model import Lasso 
from sklearn.linear_model import ElasticNet 
from sklearn.linear_model import RidgeCV 
from sklearn.linear_model import LassoCV 
from sklearn.linear_model import ElasticNetCV 

# Configuración warnings 
# ============================================================================== 
import warnings 
warnings . filterwarnings ( 'once' ) 

Datos ¶ 

El set de datos contiene 101 columnas. Las 100 primeras, nombradas como $V1$, ..., $V100$ recogen el valor de absorbancia para cada una de las 100 longitudes de onda analizadas (predictores), y la columna fat el contenido en grasa medido por técnicas químicas (variable respuesta).

# Datos 
# ============================================================================== 
datos = pd . read_csv ( 'meatspec.csv' ) 
datos = datos . drop ( columns = datos . columns [ 0 ]) 
datos . info () 
datos . head ( 3 ) 

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 215 entries, 0 to 214
Columns: 101 entries, V1 to fat
dtypes: float64(101)
memory usage: 169.8 KB

V1 
V2 
V3 
V4 
V5 
V6 
V7 
V8 
V9 
V10 
... 
V92 
V93 
V94 
V95 
V96 
V97 
V98 
V99 
V100 
fat 

0 
2.61776 
2.61814 
2.61859 
2.61912 
2.61981 
2.62071 
2.62186 
2.62334 
2.62511 
2.62722 
... 
2.98145 
2.96072 
2.94013 
2.91978 
2.89966 
2.87964 
2.85960 
2.83940 
2.81920 
22.5 

1 
2.83454 
2.83871 
2.84283 
2.84705 
2.85138 
2.85587 
2.86060 
2.86566 
2.87093 
2.87661 
... 
3.29186 
3.27921 
3.26655 
3.25369 
3.24045 
3.22659 
3.21181 
3.19600 
3.17942 
40.1 

2 
2.58284 
2.58458 
2.58629 
2.58808 
2.58996 
2.59192 
2.59401 
2.59627 
2.59873 
2.60131 
... 
2.68951 
2.67009 
2.65112 
2.63262 
2.61461 
2.59718 
2.58034 
2.56404 
2.54816 
8.4 

3 rows × 101 columns

Relación entre variables ¶ 

El primer paso a la hora de establecer un modelo lineal múltiple es estudiar la relación que existe entre variables. Esta información es crítica a la hora de identificar cuáles pueden ser los mejores predictores para el modelo, y para detectar colinealidad entre predictores. A modo complementario, es recomendable representar la distribución de cada variable mediante histogramas.

# Correlación entre columnas numéricas 
# ============================================================================== 

def tidy_corr_matrix ( corr_mat ): 
''' 
Función para convertir una matriz de correlación de pandas en formato tidy 
''' 
corr_mat = corr_mat . stack () . reset_index () 
corr_mat . columns = [ 'variable_1' , 'variable_2' , 'r' ] 
corr_mat = corr_mat . loc [ corr_mat [ 'variable_1' ] != corr_mat [ 'variable_2' ], :] 
corr_mat [ 'abs_r' ] = np . abs ( corr_mat [ 'r' ]) 
corr_mat = corr_mat . sort_values ( 'abs_r' , ascending = False ) 

return ( corr_mat ) 

corr_matrix = datos . select_dtypes ( include = [ 'float64' , 'int' ]) \
. corr ( method = 'pearson' ) 
display ( tidy_corr_matrix ( corr_matrix ) . head ( 5 )) 

variable_1 
variable_2 
r 
abs_r 

1019 
V11 
V10 
0.999996 
0.999996 

919 
V10 
V11 
0.999996 
0.999996 

1121 
V12 
V11 
0.999996 
0.999996 

1021 
V11 
V12 
0.999996 
0.999996 

917 
V10 
V9 
0.999996 
0.999996 

# Heatmap matriz de correlaciones 
# ============================================================================== 
fig , ax = plt . subplots ( nrows = 1 , ncols = 1 , figsize = ( 5 , 5 )) 
sns . heatmap ( 
data = corr_matrix , 
square = True , 
ax = ax 
) 
ax . tick_params ( labelsize = 8 ) 

Muchas de las variables están altamente correlacionadas (correlación absoluta > 0.8), lo que supone un problema a la hora de emplear modelos de regresión lineal.

Partición de datos ¶ 

En los siguientes apartados se ajustan varios modelos lineales con y sin regularización, con el objetivo de identificar cuál de ellos es capaz de predecir mejor el contenido en grasa de la carne en función de las señales registradas por el espectrofotómetro.

Para poder evaluar la capacidad predictiva de cada modelo, se dividen las observaciones disponibles en dos grupos: uno de entrenamiento (70%) y otro de test (30%).

# División de los datos en train y test 
# ============================================================================== 
X = datos . drop ( columns = 'fat' ) 
y = datos [ 'fat' ] 
X_train , X_test , y_train , y_test = train_test_split ( 
X , 
y , 
train_size = 0.7 , 
random_state = 1234 , 
shuffle = True 
) 

Escalado ¶ 

Los modelos de regresión lineal con regularización Ridge , Lasso y Elastic Net penalizan la magnitud de los coeficientes del modelo, por lo que es necesario que todos los predictores estén en la misma escala. Para ello, se puede emplear estandarización o normalización. En este ejemplo se utiliza estandarización.

# Escalado 
# ============================================================================== 
scaler = StandardScaler () . set_output ( transform = "pandas" ) 
X_train = scaler . fit_transform ( X_train ) 
X_test = scaler . transform ( X_test ) 

Mínimos cuadrados (OLS) ¶ 

# Creación y entrenamiento del modelo 
# ============================================================================== 
modelo = LinearRegression () 
modelo . fit ( X = X_train , y = y_train ) 

LinearRegression()
In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. 
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org. 

LinearRegression

? Documentation for LinearRegression i Fitted 

Parameters 

fit_intercept  
True 

copy_X  
True 

tol  
1e-06 

n_jobs  
None 

positive  
False 

# Coeficientes del modelo 
# ============================================================================== 
df_coeficientes = pd . DataFrame ( 
{ 'predictor' : X_train . columns , 
'coef' : modelo . coef_ . flatten ()} 
) 

fig , ax = plt . subplots ( figsize = ( 8 , 3 )) 
ax . stem ( df_coeficientes . predictor , df_coeficientes . coef , markerfmt = ' ' ) 
plt . xticks ( rotation = 90 , ha = 'right' , size = 6 ) 
ax . set_xlabel ( 'variable' ) 
ax . set_ylabel ( 'coeficientes' ) 
ax . set_title ( 'Coeficientes del modelo' ); 

# Predicciones test 
# ============================================================================== 
predicciones = modelo . predict ( X = X_test ) 
predicciones = predicciones . flatten () 
predicciones [: 10 ] 

array([36.88226752, 62.47992661, 61.04825535, 9.95161352, 18.11993067,
6.56158193, 28.42860453, 9.18085599, 15.56800749, 16.50461443])

# Error de test del modelo 
# ============================================================================== 
rmse_ols = root_mean_squared_error ( 
y_true = y_test , 
y_pred = predicciones , 
) 
print ( f "El error (rmse) de test es: { rmse_ols } " ) 

El error (rmse) de test es: 3.839667585638014

Las predicciones del modelo final se alejan en promedio 3.84 unidades del valor real.

Ridge ¶ 

# Creación y entrenamiento del modelo (con búsqueda por CV del valor óptimo alpha) 
# ============================================================================== 
# Por defecto RidgeCV utiliza el neg mean squared error 
modelo = RidgeCV ( 
alphas = np . logspace ( - 20 , 2 , 200 ), 
scoring = 'neg_root_mean_squared_error' , 
fit_intercept = True , 
store_cv_results = True 
) 

_ = modelo . fit ( X = X_train , y = y_train ) 

Cuando se utiliza regularización, es útil evaluar cómo se aproximan a cero los coeficientes a medida que se
incrementa el valor de alpha así como la evolución del error de validación cruzada en función del alpha empleado.

# Evolución de los coeficientes en función de alpha 
# ============================================================================== 
alphas = modelo . alphas 
coefs = [] 

for alpha in alphas : 
modelo_temp = Ridge ( alpha = alpha , fit_intercept = True ) 
modelo_temp . fit ( X_train , y_train ) 
coefs . append ( modelo_temp . coef_ . flatten ()) 

fig , ax = plt . subplots ( figsize = ( 7 , 3.84 )) 
ax . plot ( alphas , coefs ) 
ax . set_xscale ( 'log' ) 
ax . set_xlabel ( 'alpha' ) 
ax . set_ylabel ( 'coeficientes' ) 
ax . set_title ( 'Coeficientes del modelo en función de la regularización' ); 
plt . axis ( 'tight' ) 
plt . show () 

Puede ver se como, a medida que aumenta el valor de alpha, la regularización es mayor y el valor de los coeficientes se reduce.

# Evolución del error en función de alpha 
# ============================================================================== 
# modelo.cv_results_ almacena el resultado de cv para cada valor de alpha. 
# Tiene dimensiones (n_samples, n_alphas) o (n_samples, n_targets, n_alphas) 
cv_results = modelo . cv_results_ 
# Se multiplica por -1 para obtener el RMSE positivo 
rmse_cv = - 1 * cv_results . mean ( axis = 0 ) 
rmse_sd = cv_results . std ( axis = 0 ) 

# Se identifica el óptimo y el óptimo + 1std 
min_rmse = np . min ( rmse_cv ) 
sd_min_rmse = rmse_sd [ np . argmin ( rmse_cv )] 
min_rmse_1sd = np . max ( rmse_cv [ rmse_cv <= min_rmse + sd_min_rmse ]) 
optimo = modelo . alphas [ np . argmin ( rmse_cv )] . item () 
optimo_1sd = modelo . alphas [ rmse_cv == min_rmse_1sd ] . item () 

# Gráfico del error +- 1 desviación estándar 
fig , ax = plt . subplots ( figsize = ( 7 , 3.84 )) 
ax . plot ( modelo . alphas , rmse_cv ) 
ax . fill_between ( 
modelo . alphas , 
rmse_cv + rmse_sd , 
rmse_cv - rmse_sd , 
alpha = 0.2 
) 
ax . axvline ( 
x = optimo , 
c = "gray" , 
linestyle = '--' , 
label = 'óptimo' 
) 
ax . axvline ( 
x = optimo_1sd , 
c = "blue" , 
linestyle = '--' , 
label = 'óptimo_1sd' 
) 
ax . set_xscale ( 'log' ) 
ax . set_ylim ([ 0 , None ]) 
ax . set_title ( 'Evolución del error CV en función de la regularización' ) 
ax . set_xlabel ( 'alpha' ) 
ax . set_ylabel ( 'RMSE' ) 
plt . legend (); 

# Mejor valor alpha encontrado 
# ============================================================================== 
print ( f "Mejor valor de alpha encontrado: { modelo . alpha_ } " ) 

Mejor valor de alpha encontrado: 5.0526310653357e-06

# Coeficientes del modelo 
# ============================================================================== 
df_coeficientes = pd . DataFrame ( 
{ 'predictor' : X_train . columns , 
'coef' : modelo . coef_ . flatten ()} 
) 

fig , ax = plt . subplots ( figsize = ( 8 , 3 )) 
ax . stem ( df_coeficientes . predictor , df_coeficientes . coef , markerfmt = ' ' ) 
plt . xticks ( rotation = 90 , ha = 'right' , size = 6 ) 
ax . set_xlabel ( 'variable' ) 
ax . set_ylabel ( 'coeficientes' ) 
ax . set_title ( 'Coeficientes del modelo' ); 

En comparación al modelo por mínimos cuadrados ordinarios, con ridge, el orden de magnitud de los coeficientes es mucho menor.

# Predicciones test 
# ============================================================================== 
predicciones = modelo . predict ( X = X_test ) 
predicciones = predicciones . flatten () 
predicciones [: 10 ] 

array([43.18344257, 40.77188055, 51.13840121, 9.98568293, 17.87646644,
7.66526713, 28.10025771, 8.19516254, 14.75080466, 14.43545959])

# Error de test del modelo 
# ============================================================================== 
rmse_ridge = root_mean_squared_error ( 
y_true = y_test , 
y_pred = predicciones , 
) 
print ( f "El error (rmse) de test es: { rmse_ridge } " ) 

El error (rmse) de test es: 2.3915892373049306

Las predicciones del modelo final se alejan en promedio 2.45 unidades del valor real.

Lasso ¶ 

# Creación y entrenamiento del modelo (con búsqueda por CV del valor óptimo alpha) 
# ============================================================================== 
# Por defecto LassoCV utiliza el mean squared error 
modelo = LassoCV ( 
alphas = np . logspace ( - 5 , 3 , 200 ), 
cv = 5 , 
) 
_ = modelo . fit ( X = X_train , y = y_train ) 

Cuando se utiliza regularización, es útil evaluar cómo se aproximan a cero los coeficientes a medida que se
incrementa el valor de alpha así como la evolución del error de validación cruzada en función del alpha empleado.

# Evolución de los coeficientes en función de alpha 
# ============================================================================== 
alphas = modelo . alphas_ 
coefs = [] 

for alpha in alphas : 
modelo_temp = Lasso ( alpha = alpha , fit_intercept = True ) 
modelo_temp . fit ( X_train , y_train ) 
coefs . append ( modelo_temp . coef_ . flatten ()) 

fig , ax = plt . subplots ( figsize = ( 7 , 3.84 )) 
ax . plot ( alphas , coefs ) 
ax . set_xscale ( 'log' ) 
ax . set_xlabel ( 'alpha' ) 
ax . set_ylabel ( 'coeficientes' ) 
ax . set_title ( 'Coeficientes del modelo en función de la regularización' ); 

Puede ver se como, a medida que aumenta el valor de alpha, la regularización es mayor y más predictores quedan excluidos (su coeficiente es 0).

# Número de predictores incluidos (coeficiente !=0) en función de alpha 
# ============================================================================== 
alphas = modelo . alphas_ 
n_predictores = [] 

for alpha in alphas : 
modelo_temp = Lasso ( alpha = alpha , fit_intercept = True ) 
modelo_temp . fit ( X_train , y_train ) 
coef_no_cero = np . sum ( modelo_temp . coef_ . flatten () != 0 ) 
n_predictores . append ( coef_no_cero ) 

fig , ax = plt . subplots ( figsize = ( 7 , 3 )) 
ax . plot ( alphas , n_predictores ) 
ax . set_xscale ( 'log' ) 
ax . set_ylim ([ - 15 , None ]) 
ax . set_xlabel ( 'alpha' ) 
ax . set_ylabel ( 'nº predictores' ) 
ax . set_title ( 'Predictores incluidos en función de la regularización' ); 

# Evolución del error en función de alpha 
# ============================================================================== 
# modelo.mse_path_ almacena el mse de cv para cada valor de alpha. Tiene 
# dimensiones (n_alphas, n_folds) 
mse_cv = modelo . mse_path_ . mean ( axis = 1 ) 
mse_sd = modelo . mse_path_ . std ( axis = 1 ) 

# Se aplica la raíz cuadrada para pasar de mse a rmse 
rmse_cv = np . sqrt ( mse_cv ) 
rmse_sd = np . sqrt ( mse_sd ) 

# Se identifica el óptimo y el óptimo + 1std 
min_rmse = np . min ( rmse_cv ) 
sd_min_rmse = rmse_sd [ np . argmin ( rmse_cv )] 
min_rmse_1sd = np . max ( rmse_cv [ rmse_cv <= min_rmse + sd_min_rmse ]) 
optimo = modelo . alphas_ [ np . argmin ( rmse_cv )] 
optimo_1sd = modelo . alphas_ [ rmse_cv == min_rmse_1sd ] 

# Gráfico del error +- 1 desviación estándar 
fig , ax = plt . subplots ( figsize = ( 7 , 3.84 )) 
ax . plot ( modelo . alphas_ , rmse_cv ) 
ax . fill_between ( 
modelo . alphas_ , 
rmse_cv + rmse_sd , 
rmse_cv - rmse_sd , 
alpha = 0.2 
) 
ax . axvline ( 
x = optimo , 
c = "gray" , 
linestyle = '--' , 
label = 'óptimo' 
) 
ax . axvline ( 
x = optimo_1sd , 
c = "blue" , 
linestyle = '--' , 
label = 'óptimo_1sd' 
) 

ax . set_xscale ( 'log' ) 
ax . set_ylim ([ 0 , None ]) 
ax . set_title ( 'Evolución del error CV en función de la regularización' ) 
ax . set_xlabel ( 'alpha' ) 
ax . set_ylabel ( 'RMSE' ) 
plt . legend (); 

# Mejor valor alpha encontrado 
# ============================================================================== 
print ( f "Mejor valor de alpha encontrado: { modelo . alpha_ } " ) 

Mejor valor de alpha encontrado: 1e-05

# Mejor valor alpha encontrado + 1sd 
# ============================================================================== 
min_rmse = np . min ( rmse_cv ) 
sd_min_rmse = rmse_sd [ np . argmin ( rmse_cv )] 
min_rmse_1sd = np . max ( rmse_cv [ rmse_cv <= min_rmse + sd_min_rmse ]) 
optimo = modelo . alphas_ [ np . argmin ( rmse_cv )] 
optimo_1sd = modelo . alphas_ [ rmse_cv == min_rmse_1sd ] . item () 

print ( f "Mejor valor de alpha encontrado + 1 desviación estándar: { optimo_1sd } " ) 

Mejor valor de alpha encontrado + 1 desviación estándar: 0.08703591361485166

Se entrena de nuevo el modelo, esta vez empleando el mayor valor de alpha cuyo error está a menos de una desviación típica del mínimo encontrado en la validación cruzada.

# Mejor modelo alpha óptimo + 1sd 
# ============================================================================== 
modelo = Lasso ( alpha = optimo_1sd ) 
modelo . fit ( X_train , y_train ) 

Lasso(alpha=0.08703591361485166)
In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. 
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org. 

Lasso

? Documentation for Lasso i Fitted 

Parameters 

alpha  
0.08703591361485166 

fit_intercept  
True 

precompute  
False 

copy_X  
True 

max_iter  
1000 

tol  
0.0001 

warm_start  
False 

positive  
False 

random_state  
None 

selection  
'cyclic' 

# Coeficientes del modelo 
# ============================================================================== 
df_coeficientes = pd . DataFrame ( 
{ 'predictor' : X_train . columns , 
'coef' : modelo . coef_ . flatten ()} 
) 

# Predictores incluidos en el modelo (coeficiente != 0) 
df_coeficientes [ df_coeficientes . coef != 0 ] . reset_index ( drop = True ) 

predictor 
coef 

0 
V8 
-2.809618 

1 
V9 
-7.678029 

2 
V10 
-6.773139 

3 
V11 
-6.028624 

4 
V12 
-5.284843 

5 
V13 
-4.547397 

6 
V14 
-3.780134 

7 
V15 
-3.064607 

8 
V16 
-2.425411 

9 
V17 
-1.873268 

10 
V18 
-1.218858 

11 
V19 
-0.605048 

12 
V20 
-0.076677 

13 
V36 
5.480320 

14 
V37 
16.903281 

15 
V38 
16.934001 

16 
V39 
15.131325 

17 
V40 
10.970831 

18 
V41 
4.323470 

19 
V49 
-2.789976 

20 
V50 
-9.042049 

21 
V51 
-4.566902 

22 
V52 
-2.128191 

23 
V53 
-0.259053 

De los 100 predictores disponibles, el modelo final solo incluye 24.

fig , ax = plt . subplots ( figsize = ( 8 , 3 )) 
ax . stem ( df_coeficientes . predictor , df_coeficientes . coef , markerfmt = ' ' ) 
plt . xticks ( rotation = 90 , ha = 'right' , size = 6 ) 
ax . set_xlabel ( 'variable' ) 
ax . set_ylabel ( 'coeficientes' ) 
ax . set_title ( 'Coeficientes del modelo' ); 

# Predicciones test 
# ============================================================================== 
predicciones = modelo . predict ( X = X_test ) 
predicciones = predicciones . flatten () 
predicciones [: 10 ] 

array([34.35041421, 53.75222685, 36.17366435, 11.74672533, 15.1183471 ,
6.35327526, 24.5488085 , 7.48191556, 13.46044097, 18.71293633])

# Error de test del modelo 
# ============================================================================== 
rmse_lasso = root_mean_squared_error ( 
y_true = y_test , 
y_pred = predicciones , 
) 
print ( "" ) 
print ( f "El error (rmse) de test es: { rmse_lasso } " ) 

El error (rmse) de test es: 3.747834638323956

Las predicciones del modelo final se alejan en promedio 3.95 unidades del valor real, utilizando solo 24 de los 100 predictores disponibles.

Elastic net ¶ 

# Creación y entrenamiento del modelo (con búsqueda por CV del valor óptimo alpha) 
# ============================================================================== 
# Por defecto ElasticNetCV utiliza el mean squared error 
modelo = ElasticNetCV ( 
l1_ratio = [ 0 , 0.1 , 0.5 , 0.7 , 0.9 , 0.95 , 0.99 ], 
alphas = np . logspace ( - 10 , 3 , 200 ), 
cv = 5 
) 
_ = modelo . fit ( X = X_train , y = y_train ) 

# Evolución del error en función de alpha y l1_ratio 
# ============================================================================== 
# modelo.mse_path_ almacena el mse de cv para cada valor de alpha y l1_ratio. 
# Tiene dimensiones (n_l1_ratio, n_alpha, n_folds) 

# Error medio de las 10 particiones por cada valor de alpha y l1_ratio 
mean_error_cv = modelo . mse_path_ . mean ( axis = 2 ) 

# El resultado es un array de dimensiones (n_l1_ratio, n_alpha) 
# Se convierte en un dataframe 
df_resultados_cv = pd . DataFrame ( 
data = mean_error_cv . flatten (), 
index = pd . MultiIndex . from_product ( 
iterables = [ modelo . l1_ratio , modelo . alphas_ ], 
names = [ 'l1_ratio' , 'modelo.alphas_' ] 
), 
columns = [ "mse_cv" ] 
) 

df_resultados_cv [ 'rmse_cv' ] = np . sqrt ( df_resultados_cv [ 'mse_cv' ]) 
df_resultados_cv = df_resultados_cv . reset_index () . sort_values ( 'mse_cv' , ascending = True ) 
df_resultados_cv 

l1_ratio 
modelo.alphas_ 
mse_cv 
rmse_cv 

1351 
0.99 
1.366716e-07 
7.313915 
2.704425 

1352 
0.99 
1.175850e-07 
7.313916 
2.704425 

1350 
0.99 
1.588565e-07 
7.313945 
2.704431 

1353 
0.99 
1.011638e-07 
7.313964 
2.704434 

1349 
0.99 
1.846425e-07 
7.313992 
2.704439 

... 
... 
... 
... 
... 

628 
0.70 
1.482021e+01 
153.374640 
12.384452 

627 
0.70 
1.722586e+01 
153.374640 
12.384452 

629 
0.70 
1.275051e+01 
153.374640 
12.384452 

630 
0.70 
1.096986e+01 
153.374640 
12.384452 

631 
0.70 
9.437878e+00 
153.374640 
12.384452 

1400 rows × 4 columns

# Mejor valor encontrado para cada l1_ratio 
# ============================================================================== 
fig , ax = plt . subplots ( figsize = ( 7 , 3 )) 
df_resultados_cv . groupby ( 'l1_ratio' )[ 'rmse_cv' ] . min () . plot ( ax = ax ) 
ax . set_title ( 'Evolución del error CV en función de la l1_ratio' ) 
ax . set_xlabel ( 'l1_ratio' ) 
ax . set_ylabel ( 'rmse_cv' ); 

# Mejor valor alpha y l1_ratio_ encontrado 
# ============================================================================== 
print ( f "Mejor valor de alpha encontrado: { modelo . alpha_ } " ) 
print ( f "Mejor valor de l1_ratio encontrado: { modelo . l1_ratio_ } " ) 

Mejor valor de alpha encontrado: 1.3667163564620074e-07
Mejor valor de l1_ratio encontrado: 0.99

# Coeficientes del modelo 
# ============================================================================== 
df_coeficientes = pd . DataFrame ( 
{ 'predictor' : X_train . columns , 
'coef' : modelo . coef_ . flatten ()} 
) 

fig , ax = plt . subplots ( figsize = ( 8 , 3 )) 
ax . stem ( df_coeficientes . predictor , df_coeficientes . coef , markerfmt = ' ' ) 
plt . xticks ( rotation = 90 , ha = 'right' , size = 6 ) 
ax . set_xlabel ( 'variable' ) 
ax . set_ylabel ( 'coeficientes' ) 
ax . set_title ( 'Coeficientes del modelo' ); 

# Predicciones test 
# ============================================================================== 
predicciones = modelo . predict ( X = X_test ) 
predicciones = predicciones . flatten () 

# Error de test del modelo 
# ============================================================================== 
rmse_elastic = root_mean_squared_error ( 
y_true = y_test , 
y_pred = predicciones , 
) 
print ( "" ) 
print ( f "El error (rmse) de test es: { rmse_elastic } " ) 

El error (rmse) de test es: 5.232998798175906

Las predicciones del modelo final se alejan en promedio 5.23 unidades del valor real, utilizando solo 22 de los 100 predictores disponibles. Aunque el error es mayor que con Ridge o Lasso, el modelo es más simple (menos predictores).

Comparación ¶ 

Se compara el error de test ( rmse ) de los 4 modelos

df_comparacion = pd . DataFrame ({ 
'modelo' : [ 'OLS' , 'Ridge' , 'Lasso' , 'Elastic-net' ], 
'test rmse' : [ rmse_ols , rmse_ridge , rmse_lasso , rmse_elastic ] 
}) 

fig , ax = plt . subplots ( figsize = ( 7 , 3.84 )) 
df_comparacion . set_index ( 'modelo' ) . plot ( kind = 'barh' , ax = ax ) 
ax . set_xlabel ( 'rmse' ) 
ax . set_ylabel ( 'modelo' ) 
ax . set_title ( 'Comparación de modelos' ); 

En este caso el mejor modelo en términos de error predictivo se obtiene aplicando regularización Ridge . El modelo con regularización Lasso tiene un error ligeramente superior al modelo OLS pero emplea solo 24 predictores en lugar de 100, ofreciendo un buen balance entre precisión e interpretabilidad. La regularización Elastic-net ofrece el modelo más simple (22 predictores) pero con mayor error.

Información de sesión ¶ 

import session_info 
session_info . show ( html = False ) 

-----
matplotlib 3.10.8
numpy 2.2.6
pandas 2.3.3
scipy 1.15.3
seaborn 0.13.2
session_info v1.0.1
sklearn 1.7.2
-----
IPython 9.8.0
jupyter_client 8.7.0
jupyter_core 5.9.1
-----
Python 3.13.11 | packaged by Anaconda, Inc. | (main, Dec 10 2025, 21:28:48) [GCC 14.3.0]
Linux-6.14.0-37-generic-x86_64-with-glibc2.39
-----
Session information updated at 2026-01-12 09:04

Bibliografía ¶ 

Linear Models with R by Julian J.Faraway

An Introduction to Statistical Learning: with Applications in R (Springer Texts in Statistics)

Applied Predictive Modeling by Max Kuhn and Kjell Johnson

The Elements of Statistical Learning by T.Hastie, R.Tibshirani, J.Friedman

Introduction to Machine Learning with Python: A Guide for Data Scientists

Python Data Science Handbook by Jake VanderPlas

Lever, J., Krzywinski, M. & Altman, N. Regularization. Nat Methods 13, 803–804 (2016)

Instrucciones para citar ¶ 

¿Cómo citar este documento? 

Si utilizas este documento o alguna parte de él, te agradecemos que lo cites. ¡Muchas gracias!

Regularización Ridge, Lasso y Elastic Net con Python por Joaquín Amat Rodrigo, disponible con una licencia Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0 DEED) en https://cienciadedatos.net/documentos/py14-ridge-lasso-elastic-net-python.html

¿Te ha gustado el artículo? Tu ayuda es importante 

Tu contribución me ayudará a seguir generando contenido divulgativo gratuito. ¡Muchísimas gracias! 😊

Este documento creado por Joaquín Amat Rodrigo tiene licencia Attribution-NonCommercial-ShareAlike 4.0 International .

Se permite: 

Compartir: copiar y redistribuir el material en cualquier medio o formato. 

Adaptar: remezclar, transformar y crear a partir del material. 

Bajo los siguientes términos: 

Atribución: Debes otorgar el crédito adecuado , proporcionar un enlace a la licencia e indicar si se realizaron cambios . Puedes hacerlo de cualquier manera razonable, pero no de una forma que sugiera que el licenciante te respalda o respalda tu uso. 

No-Comercial: No puedes utilizar el material para fines comerciales . 

Compartir-Igual: Si remezclas, transformas o creas a partir del material, debes distribuir tus contribuciones bajo la misma licencia que el original. 

Content licensed under 

CC BY-NC-SA 4.0

Cienciadedatos.net 

Dark Mode 
Back to Top
