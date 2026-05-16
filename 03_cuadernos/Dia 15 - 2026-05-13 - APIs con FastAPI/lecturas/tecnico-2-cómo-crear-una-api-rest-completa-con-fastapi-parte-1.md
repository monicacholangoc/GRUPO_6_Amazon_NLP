# Cómo crear una API REST completa con FastAPI (Parte 1)

Fuente: [Cosas de Devs](https://cosasdedevs.com/posts/api-rest-fastapi-completa/)  
_Copia local para lectura fuera de línea. El formato original puede verse en la URL._

---

Parte 1: Cómo crear una API REST COMPLETA con FastAPI, instalación y estructura

Inicio >
Series 
> Parte 1: Cómo crear una API REST COMPLETA con FastAPI, instalación y estructura 

Alberto 

Nov 17, 2021

 Muy buenas, después de un mini descanso me he puesto manos a la obra y por fin tengo el primer tutorial de esta serie de tutoriales en el que vamos a aprender como funciona FastAPI   mientras construimos una API REST .



Que vamos a aprender en esta serie de tutoriales



En esta serie de tutoriales veremos como crear la estructura del proyecto , usar la autenticación con JWT , enrutamiento , conexiones a bases de datos y realizaremos tests para verificar el correcto funcionamiento de la aplicación.



Antes de empezar



Para este proyecto yo voy a utilizar la versión 3.9 de Python , recomiendo utilizar mínimo la 3.7 para evitar problemas de compatibilidad.



Como base de datos usaremos PostgreSQL así que podéis instalarlo en vuestro PC o emplear una imagen de Docker.



Si no tienes muy claro el funcionamiento de una API, te dejo esta guía que escribí para entender su funcionamiento al 100%.



Guía para aprender a trabajar con APIs 



De que va el proyecto



El proyecto que vamos a realizar será una herramienta en la que podremos crear un usuario y este podrá tener un listado de tareas por hacer (también conocido como to-do list ). Este podrá crearlas y después marcarlas como hechas.



Crear proyecto y entorno virtual e instalar FastAPI



Lo primero que vamos a hacer es generar la carpeta que contendrá nuestro proyecto, yo la he llamado " fastapi-todo-api ". Una vez hecho esto, vamos a nuestra terminal y nos dirigimos a la carpeta de nuestro proyecto.



El siguiente paso es crear nuestro entorno virtual, si no tenéis muy claro a que me refiero, os aconsejo que os paséis primero por este post: Qué es el entorno virtual en Python .



Lanzamos el comando para crear el entorno virtual:




python -m venv env 



Y después lo activamos:




# Windows
.\env\Scripts\activate
# Mac/linux
source env/bin/activate 



Una vez hecho, instalaremos FastAPI y uvicorn que os explicaré a continuación que es y para qué lo utilizaremos:




pip install fastapi uvicorn 



Uvicorn es un servidor ASGI de alto rendimiento que usaremos para correr nuestra aplicación, si queréis más info acerca de esta librería os dejo en enlace a su página pinchando aquí .



Hello world con FastAPI



Ahora que ya tenemos instalado FastAPI es hora de crear nuestro primer endpoint que se tratará del clásico Hello World. Para ello vamos a crear un archivo llamado main.py en la raíz de nuestro proyecto que contendrá el siguiente código:




from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
return {"message": "Hello World"} 



En este script lo primero que hacemos es importar FastAPI , posteriormente creamos la variable app que será una instancia de la clase FastAPI y nos permitirá controlar el enrutamiento, middlewares, etc.



En la siguiente parte del código crearemos nuestro primer endpoint, este consta de un decorador creado con el objeto app y el tipo de petición que vamos a realizar que en este caso será de tipo get . Como parámetro enviamos la ruta del endpoint que será el index.



Posteriormente, definimos la función que podremos nombrarla como queramos y por último retornamos la respuesta de nuestra API . Podremos retornar diccionarios, listas y unos tipos de objetos especiales que veremos más adelante y luego FastAPI se encargará de convertirlos en un string con formato JSON.



Para ver nuestra API en funcionamiento , vamos a la terminal y lanzamos el siguiente comando:




uvicorn main:app --reload 



El comando uvicorn recibe un parámetro y una flag . El parámetro indica el nombre del archivo que queremos correr, después añadimos dos puntos y le indicamos el nombre de la variable que definimos como instancia de FastAPI .



El flag --reload hará que cada vez que ejecutemos un cambio en nuestro proyecto y guardemos, se recargue el proceso de uvicorn y se reflejen nuestros cambios en la API.



Ahora solo debemos acceder a  http://127.0.0.1:8000/  y podremos ver el mensaje que definimos en la ruta principal.




{
"message": "Hello World"
} 



Estructura del proyecto



Ahora vamos a crear unos cuantos archivos y carpetas que necesitaremos para más adelante.



Como buena práctica vamos a inicializar el proyecto con git , es un paso totalmente opcional, pero yo os lo recomiendo y además así podéis aprovechar para una vez finalizado el proyecto subirlo a vuestro repositorio.




git init 



Después vamos a crear el archivo .gitignore y el archivo .env , el primero para decirle a git que archivos no queremos en nuestro repositorio y en el segundo guardaremos nuestras variables de entorno, recordad que estos ficheros empiezan por punto (.).



El contenido del archivo .gitignore será el siguiente:




*.log
*.pot
*.pyc
__pycache__/
env
.env
.pytest_cache 



Dentro del archivo .env de momento no vamos a guardar nada. Ya veremos más adelante su uso.



Una vez hecho esto, vamos a crear un directorio llamado app que contendrá a su vez una carpeta llamada v1 y que está contendrá 6 carpetas llamadas model, router, schema, scripts, service y utils :




├───app
│ └───v1
│ ├───model
│ ├───router
│ ├───schema
│ ├───scripts
│ ├───service
│ └───utils 



Y listo, ya tenemos la estructura del proyecto y hemos visto como realizar la primera petición a nuestra API . En el siguiente tutorial veremos como crear un archivo de configuración, generaremos la conexión a la base de datos y crearemos los modelos y las tablas.



También os dejo el enlace al repositorio con esta primera parte del tutorial . No os preocupéis si no veis la carpeta app , eso es porque git no sube las carpetas sin contenido.



Ya está listo el siguiente tutorial, podéis seguirlo en este enlace:  Parte 2: Conexiones a bases de datos y creación de modelos con FastAPI 

Espero que este post te ayude y como siempre, te recomiendo seguirme en  Twitter  para estar al tanto de los nuevo contenido. Ahora también puedes seguirme en  Instagram  donde estoy subiendo  tips, tutoriales en vídeo e información sobre herramientas para developers .



Por último os dejo mi  guía para aprender a trabajar con APIs  donde explico todo el funcionamiento de una API, el protocolo HTTP y veremos como construir una API con arquitectura REST.



Nos leemos 👋.

22567 vistas

Facebook 

Twitter 

#FastAPI 

#PostgreSQL 

#Python 

Sobre Alberto

Con más de 14 años trasteando con APIs y servicios de más de 5000 millones de peticiones diarias (AdTech y SaaS), he aprendido que la mejor arquitectura es la combina escalibilidad, velocidad, ahorro de costes y rentabilidad.

Saber más 

También te puede interesar

Qué es el paralelismo y cómo utilizarlo en Python 

Cómo crear un paquete con Python y subirlo a PYPI 

Métodos de clase y métodos estáticos en Python 

Cómo utilizar requests de Python con una API Rest
