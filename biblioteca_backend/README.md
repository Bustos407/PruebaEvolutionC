# Instrucciones para Clonar y Configurar el Proyecto

## Entorno vitual
1. `py -m venv venv`
2. Activar el Entorno con `venv\Scripts\activate`
3. Instalar dependecias `pip install -r requirements.txt`
## Iniciar el Backend
Utilizar el siguiente comando `python app.py`

## Peticiones y Swagger
Se implemento un Swagger para mayor facilidad a la hora de ver las peticiones
-Swagger = `http://localhost:5000/apidocs/`
Si queres utilizar aplicaciones como Postman estos son las URL de las peticiones
### Libros 
-POST and GET: `http://localhost:5000/libros`
-DELETE and PUT: `http://localhost:5000/libros/{id}`
### Autores
-Autores (POST and GET): `http://localhost:5000/autores`


## Acerca de la Base de datos
La base de datos esta ubicada en Clever Cloud un servicio gratiuto por lo que no es una Base de datos local. La base de datos es MySQL si desea abrirla desde otros programas como MySql WorkBench tiene la informacion y datos de la BD (HOSTNAME Y NOMBRE DE LA BD) en el archivo de Python `config.py`
