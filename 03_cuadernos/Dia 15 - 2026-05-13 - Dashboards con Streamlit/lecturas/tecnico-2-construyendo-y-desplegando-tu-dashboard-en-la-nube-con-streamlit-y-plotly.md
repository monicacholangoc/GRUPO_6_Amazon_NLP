# Construyendo y desplegando tu dashboard en la nube con Streamlit y Plotly

Fuente: [Datapath · Medium](https://medium.com/datapath/construyendo-y-desplegando-tu-dashboard-en-la-nube-una-gu%C3%ADa-completa-con-streamlit-y-plotly-936cc1c8c71d)  
_Copia local para lectura fuera de línea. El formato original puede verse en la URL._

---

Construyendo y Desplegando tu Dashboard en la Nube: Una Guía Completa con Streamlit y Plotly

Macusaya Yurika 

10 min read 
· 
Feb 17, 2024 

-- 

Share

Un Dashboard es una interfaz visual que condensa información clave para facilitar la toma de decisiones informadas en análisis de datos y al iniciar nuestro viaje en el análisis de datos, surge la pregunta ¿Cómo presentar nuestros hallazgos de manera efectiva? Esta guía detalla el proceso de crear un dashboard usando herramientas de visualización como Streamlit y Plotly además de realizar el despligue de nuestra app en el entorno de Streamlit Cloud.

Plotly 

Sirve para la visualización avanzada de Datos, es una poderosa biblioteca de gráficos interactivos que se integra perfectamente con Streamlit para crear visualizaciones interactivas y dinámicas.

Imagen 1 :Ploty Logo. Fuente: Google Images 
Streamlit 

Sirve para la creación sencilla de Dashboards Interactivos, es una biblioteca esencial de Python para implementar dashboards con líneas de código simples y rápidas.

Imagen 2 : Streamlit Logo. Fuent: Google Images 
Git y GitHub 

Git es un sistema de control de versiones que permite rastrear cambios en el código, mientras que GitHub es una plataforma que utiliza Git para alojar y colaborar en proyectos de desarrollo de software en línea.

Imagen 3 : Git and github logo. Fuente: Google Images 
Streamlit Community Cloud

Streamlit Cloud es la plataforma en la nube de Streamlit para compartir y desplegar aplicaciones Streamlit de manera fácil y rápida. Permite compartir visualizaciones y análisis de datos en línea sin complicaciones.

Press enter or click to view image in full size 

Imagen 4 : Streamlit Community Cloud work. Fuente: Elaboración propia 

II. Contenido 

Descubre cómo crear y desplegar un Dashboard paso a paso utilizando Plotly y Streamlit. Utilizaremos el conjunto de datos Delivery Data , que ofrece una visión detallada de transacciones de ventas y comercio electrónico. Cada entrada en el dataset representa una transacción única, brindando información esencial sobre productos, métricas, clientes y regiones, proporcionando así una herramienta efectiva para visualizar y analizar datos comerciales clave.

1. Requisitos 

Git instalado en nuestra máquina local

cuenta en GitHub 

Python3 instalado

2. Repositorio

Creación del Repositorio Local 

Crear una carpeta que contenga todos los archivos necesarios para su dashboard.

Inicie un repositorio local ejecutando el comando ‘git init’ en la línea de comandos.

git init 

Creación del Repositorio Remoto 

Cree un repositorio remoto en GitHub para almacenar los archivos necesarios para implementar su aplicación/dashboard en Streamlit Cloud.

Visite https://github.com/ Home > seleccione ‘ Create new repository ’ > completa los campos necesarios y asegúrese de que el repositorio sea ‘Public’ > Finalmente, haga clic en ‘Create repository’ .

Press enter or click to view image in full size 

Imagen 5 :Creacion de repositorio en Github . Fuente: Elaboración propia 
3. Análisis de Datos 

Se puede visualizar los datos del dataset, como se muestra en la Imagen 6 con el archivo CSV.

Press enter or click to view image in full size 

Imagen 6 : Pandas Dataframe. Fuente: Elaboración propia 

Sobre el dataset, hemos diseñado una tabla, tabla 1 donde se encuentra información relevante sobre las variables de nuestro conjunto de datos.

Press enter or click to view image in full size 

Tabla 1: Descripción de las variables del dataset. Fuente: Elaboración propia 

Para este paso te invito a desarrollar un análisis de datos profundo para que puedas experimentar con los datos.

4. Visualizaciones y gráficas con Ploty en Notebook 

Antes de desarrollar un dashboard, es crucial realizar un Análisis exploratorio de datos y crear visualizaciones en un entorno como Google Colaboratory Notebook u otro notebook, como podrás observar en la Imagen 7.

Visualizaciones de Plotly Express utilizadas 

Gráfico de Línea (make_time_line): 

fig = px.line(data, x=’fecha_envio’, y=’Ventas’, color=’Prioridad’) 

Muestra la evolución de las ventas a lo largo del tiempo, con líneas diferenciadas por la prioridad de envío. Útil para observar patrones temporales en las ventas y cómo se distribuyen según la prioridad de envío.

Tree Map (make_tree_map): 

fig = px.treemap(input_df, path=[‘Segmento’, ‘Region’], values=’Cantidad’, color=’Ventas’, color_continuous_scale=’RdBu’, title=’Relación entre Segmento y Región’) 

Representa la relación proporcional de las cantidades de ventas en segmentos de mercado y regiones a través de un mapa de árbol. Ideal para visualizar de manera jerárquica la distribución de las ventas en diferentes segmentos y regiones.

Sunburst (make_sun): 

fig = px.sunburst(input_df, path=['Prioridad', 'Categoria'], title='', labels={'Categoria': 'Categoría'}) 

Presenta la jerarquía de prioridad de envíos con respecto a las categorías mediante un gráfico de tarta radial. Útil para entender la distribución de prioridades en las diferentes categorías de productos.

Gráfico de Tarta (make_pie): 

fig = px.pie(input_df, values='Cantidad', names='Region', title='', hover_data=['Costo_envio'], labels={'Costo_envio': 'Costo_envio'}) 

Muestra las proporciones de envíos por región a través de un gráfico de tarta. Efectivo para visualizar de manera clara y simple cómo se distribuyen los envíos y sus costos en diferentes regiones.

Press enter or click to view image in full size 

Imagen 7 : Google colaboratory Notebook . Fuente: Elaboración propia 

5. Instalaciones 

La instalación de los módulos necesarios se realiza mediante los siguientes comandos en la consola:

pip install –upgrade pip
pip install ploty
pip install streamlit
streamlit hello 

#Crear el file.py donde programaremos nuestro dashboard
touch streamlit_app.py (en linux) 

6. Dashboard con Streamlit 

Para la programación del dashboard con Streamlit, emplearemos el editor de nuestra preferencia y trasladaremos las visualizaciones creadas con Plotly en el paso anterior.

El código del archivo streamlit_app.py podría tener la siguiente estructura:

#importar modulos de ploty y streamlit
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import numpy as np
# Page configuration
st.set_page_config(
page_title="Delivery data",
page_icon="🏂",
layout="wide",
initial_sidebar_state="expanded")
# CSS styling
st.markdown("""
<style>
[data-testid="block-container"] {
padding-left: 2rem;
padding-right: 2rem;
padding-top: 1rem;
padding-bottom: 0rem;
margin-bottom: -7rem;
}
[data-testid="stVerticalBlock"] {
padding-left: 0rem;
padding-right: 0rem;
}
[data-testid="stMetric"] {
background-color: #393939;
text-align: center;
padding: 15px 0;
}
[data-testid="stMetricLabel"] {
display: flex;
justify-content: center;
align-items: center;
}
</style>
""", unsafe_allow_html=True)
# data
df = pd.read_csv('Delivery Data - datos_2017_2020.csv')
df['Ventas'] = df['Ventas'].apply(lambda x: float(x.replace('.', '').replace(',', '.')))
df['Costo_envio'] = df['Costo_envio'].apply(lambda x: float(x.replace('.', '').replace(',', '.')))
df['Descuento'] = df['Descuento'].apply(lambda x: float(x.replace('.', '').replace(',', '.')))
df['Margen'] = df['Margen'].apply(lambda x: float(x.replace('.', '').replace(',', '.')))
df['Utilidad'] = df['Utilidad'].apply(lambda x: float(x.replace('.', '').replace(',', '.')))
df['Precio_costo'] = df['Precio_costo'].apply(lambda x: float(x.replace('.', '').replace(',', '.')))
df['fecha_envio'] = pd.to_datetime(df['fecha_envio'], format='%d/%m/%Y')
df = df.sort_values('fecha_envio')
# Sidebar
with st.sidebar:
st.title('🏂 Delivery Dashboard')
years_unique = df['fecha_envio'].dt.year.unique()
year_list = list(map(str, years_unique))
selected_year = 2020
selected_year = st.selectbox('Select a year', year_list)
df_selected_year = df[df['fecha_envio'].dt.year == int(selected_year)]
# visualizaciones
#1
def make_time_line(data):
fig = px.line(data, x='fecha_envio', y='Ventas', color ='Prioridad')
fig.update_layout(
title_text="", title_x=0.5,
annotations=[dict(text="Gráfico de Línea para mostrar la cantidad de ventas por prioridad ", showarrow=False,
x=0.5, y=-0.15, xref='paper', yref='paper')])
print(selected_year)
return fig
#2
def make_tree_map(input_df):
fig = px.treemap(input_df, path=['Segmento', 'Region'], values ='Cantidad',
color = 'Ventas', color_continuous_scale='RdBu',
title='Relación entre Segmento y Región')
fig.update_layout(
title_text='', title_x=0.5,
annotations=[dict(text='Esta gráfica de Tree map muestra la relacion en proporciones de los segmentos de mercado con las cantidades de ventas por Region', showarrow=False,
x=0.5, y=-0.15, xref='paper', yref='paper')])
return fig
#3
def make_sun(input_df):
fig = px.sunburst(input_df, path=['Prioridad', 'Categoria'], title='',
labels={'Categoria': 'Categoría'})
fig.update_layout(
title_text='', title_x=0.5,
annotations=[dict(text='Gráfico de Tarta para la representación de la prioridad de envíos con respecto a su categoría', showarrow=False,
x=0.5, y=-0.15, xref='paper', yref='paper')])
return fig
#4
def make_pie(input_df):
fig = px.pie(input_df, values='Cantidad', names='Region',
title='',
hover_data=['Costo_envio'], labels={'Costo_envio':'Costo_envio'})
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(
title_text='', title_x=0.5,
annotations=[dict(text='Gráfico de Tarta que representa las proporciones de envios y costos por envíos por Región', showarrow=False,
x=0.5, y=-0.15, xref='paper', yref='paper')])
return fig
# Dashboard Main Panel
col = st.columns((1.5, 4.5, 2), gap='medium')
with col[0]:
st.metric(label='Records', value=df_selected_year.shape[0], delta=None)
with st.expander('', expanded=True):
st.write('''
- :orange[**About**]: Este conjunto de datos proporciona una visión detallada de las transacciones de ventas y comercio electrónico. Cada entrada en el dataset representa una transacción única, con información valiosa sobre productos, clientes y regiones.
''')
with col[1]:
st.markdown('#### Cantidad de Ventas por Región')
treemap = make_tree_map(df_selected_year)
st.plotly_chart(treemap, use_container_width=True)
st.markdown('#### Timeline de Ventas')
time_line = make_time_line(df_selected_year)
st.plotly_chart(time_line, use_container_width=True)
with col[2]:
st.markdown('#### Porcentaje de Envios y Costos por Region')
pie = make_pie(df_selected_year)
st.plotly_chart(pie, use_container_width=True)
st.markdown('#### Prioridad de envíos por Categoria')
sun = make_sun(df_selected_year)
st.plotly_chart(sun, use_container_width=True)
] 

En este código, se utilizan las funciones de Streamlit para crear una aplicación web interactiva que muestra visualizaciones de datos.

Aquí está la explicación de por qué y para qué se usan estas funciones específicas de Streamlit:

st.set_page_config: Se utiliza para configurar opciones de la página, como el título. Esto establece la configuración inicial de la página.

CSS Styling (marcado con st.markdown(“”” … “””, unsafe_allow_html=True)): Permite aplicar estilos CSS personalizados para mejorar el diseño visual de la aplicación.

Lectura y Preprocesamiento de Datos: 

Streamlit no está directamente involucrado aquí, pero se utiliza para cargar y preprocesar datos con bibliotecas como Pandas.

Sidebar: 

st.sidebar se utiliza para crear una barra lateral en la que se puede colocar contenido relacionado con la navegación y la configuración.

st.selectbox: Proporciona una interfaz de usuario para seleccionar un elemento de una lista desplegable.

Visualizaciones: 

La función make_graphic utiliza Plotly Express ( px ) para crear un gráfico interactivo basado en los datos proporcionados. El gráfico se devuelve como una figura de Plotly.

Dashboard Main Panel: 

Se usan columnas ( st.columns ) para dividir el panel principal en secciones con diferentes tamaños relativos (1.5, 4.5, 2).

st.metric: Muestra una métrica específica, como el valor de una función (value=data.func). Puede utilizarse para resaltar información clave.

st.expander: Permite expandir o contraer una sección de información adicional. Aquí, se utiliza para mostrar información extra cuando se hace clic en el icono de expansión.

st.markdown y st.plotly_chart: Se usan para mostrar texto en formato Markdown y visualizaciones interactivas generadas con Plotly Express, respectivamente. use_container_width=True ajusta automáticamente el ancho del gráfico al contenedor.

Para poder ver más sobre Streamlit Api references https://docs.streamlit.io/library/api-reference 

Para ver y ejecutar nuestro dashboard, simplemente escribimos el siguiente comando en la consola:

streamlit run streamlit_app.py 

Posteriormente, abrimos nuestro navegador y accedemos a la aplicación a través de la URL local generada después de ejecutar el comando anterior. La Imagen 8 muestra nuestro Dashboard en el navegador.

Local URL: http://localhost:8501 

Press enter or click to view image in full size 

Imagen 8 : Dashboard con Streamlit y Ploty. Fuente: Elaboración propia 

7. Llevar cambios del repositorio Local al Repositorio Remoto 

Necesitamos la URL del repositorio en GitHub, tal como se muestra en la Imagen 9..

Para obtenerla, vamos a GitHub

Accedemos a Repositorios

Seleccionamos el botón <>Code

Click en HTTPS

Copiamos la URL al portapapeles

Press enter or click to view image in full size 

Imagen 9 : Url Repositorio en github. Fuente: Elaboración propia 

Desde nuestra máquina nos situamos en nuestro directorio donde creamos nuestra streamlit_app.py y escribimos estas lineas en la consola.

Nota: es necesario que nuestra app esté en la rama principal Main.

#Muestra el estado actual del repositorio local.
git status
#Añade un remoto llamado "origin" con la URL del repositorio en GitHub.
git remote add origin https://github.com/YMacA/Dashboard-delivery.git [url repositorio github]#Muestra las URL de los remotos configurados.
git remote -v
#trae cambios desde la rama principal (main) del repositorio remoto.
git pull origin main
#Prepara los archivos data.csv y streamlit_app.py para ser commitidos.
git add data.csv streamlit_app.py
#Muestra el estado actual del repositorio después de la preparación.
git status
#Confirma los cambios con el mensaje "dashboard con streamlit".
git commit -m "dashboard con streamlit"
#Sube los cambios confirmados a la rama principal (main) del repositorio remoto.
git push origin HEAD:main 

En la imagen 10 podemos observar que todos los cambios y archivos se subieron correctamente a nuestro repositorio remoto.

Press enter or click to view image in full size 

Imagen 10 : Repositorio en github. Fuente: Elaboración propia 

8. Deploy de Dashboard con Streamlit Community Cloud 

1. Cuenta en Streamlit Cloud

Para realizar el deploy de nuestro dashboard con Streamlit, es necesario crear una cuenta en Streamlit Community Cloud . Haz clic en ‘Get Started’ para iniciar el proceso, tal como se muestra en la imagen 11.

En el proceso de registro, es esencial enlazar nuestra cuenta de GitHub, donde se encuentra alojado nuestro repositorio listo para el despliegue.

Press enter or click to view image in full size 

Imagen 11 : Registro Streamlit community cloud. Fuente: Elaboración propia 
También puedes consultar la guía sobre cómo crear una cuenta en Streamlit Cloud en Create your account — Streamlit Docs 

2. Deployment 

Desplegar nuestro dashboard en Streamlit Cloud desde GitHub es sencillo. Ingresa a Streamlit Cloud .

1. Ve a la sección Home y selecciona New App.

2. Completa los campos obligatorios:

3. Repository: Selecciona el repositorio de GitHub.

4. Branch principal: Main.

5. Main file path: Elige el archivo ejecutable, en nuestro caso, streamlit_app.py.

6. Haz clic en Deploy!

En la imagen 12 se puede ver la pantalla de despliegue de una nueva app en Streamlit Cloud.

Press enter or click to view image in full size 

Imagen 12 : Deploy de nueva app en Streamlit cloud. Fuente: Elaboración propia 

Automáticamente después del Deploy se abrirá una pestaña con nuestra app.

Press enter or click to view image in full size 

Imagen 13 : App en Streamlit cloud desplegada. Fuente: Elaboración propia 

Con esto, ya tienes tu dashboard desplegado en Streamlit Cloud. ¡Felicitaciones!

Todo el código utilizado en este tutorial está disponible en el repositorio de GitHub aquí . Siéntete libre de explorar, clonar y adaptar el código según tus necesidades.

Además, puedes experimentar directamente con la aplicación desplegada en Streamlit Cloud aquí .

Conclusiones 

En esta emocionante travesía, has logrado crear y desplegar tu propio dashboard con datos de Delivery. ¡Felicidades por alcanzar este hito!. Destacamos la eficacia de Plotly para visualizaciones interactivas, la simplicidad de Streamlit en la creación de dashboards y la facilidad de despliegue gracias a Streamlit Cloud. La integración sin problemas con GitHub nos ha permitido actualizar y desplegar continuamente nuestro dashboard.

Recuerda, este tutorial es solo el comienzo. ¡Hazlo tuyo, experimenta y sigue construyendo proyectos increíbles en el mundo de los datos!

Próximos pasos

Mejora de Visualizaciones : Refinar y agregar más visualizaciones para proporcionar una comprensión más profunda de los datos.

Optimización del Código: Buscar maneras de optimizar el código en streamlit_app.py para mejorar la eficiencia y rendimiento.

Incorporar Machine Learning: Si es relevante, considerar la incorporación de modelos de machine learning para análisis predictivo en el dashboard.

Interactividad Adicional: Explorar opciones para mejorar la interactividad del dashboard, como filtros adicionales o controles avanzados.

Con estos próximos pasos, podrás llevar tu dashboard a un nivel más avanzado y hacer que sea aún más valioso para los usuarios finales!.

Referencias

Plotly Python Graphing Library 

Create your account — Streamlit Docs 

Crafting a Dashboard App in Python using Streamlit 

How to Deploy Your App to Streamlit Community Cloud 

API Reference — Streamlit Docs 

Gracias por leerme,

¿Quieres seguir aprendiendo y conectarte con nuestra comunidad? Te invitamos a unirte a nuestras redes sociales. ¡Síguenos en Instagram y LinkedIn para estar al tanto de las últimas noticias, tutoriales y recursos sobre tecnología y aprendizaje automático!

Datapath 

Acelerando el talento LATAM en data, cloud, analytics e inteligencia artificial
