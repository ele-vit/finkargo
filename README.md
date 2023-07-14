# Finkargo

### Instrucciones Entorno Local con Docker-Compose

1. Clonar el repositorio:

    `git clone`

2. Pasar a directorio de trabajo:

    `cd finkargo`

3. en el archivo Makefile tendrá los comandos necesarios para desplegar el api:

    `make deploy-api`    
    `make down-api`     
    `make log-api`  
    `make restart-api`

## Pre-requisitos 📋
* Python 3

### Recomendación para el uso del API
1. usar postman u otra herramienta que le permita realizar peticiones http
2. el archivo `postman_collection.json` le ayudara a crear todos los endpoint en postman con tan solo importarlos
3. el api tiene un sistema de autenticación con un middleware que se inyecto como dependencia en algunos endpoint y por ende cada que haga login, deberá cambiar el token en las variables del postman.

## este es un ejemplo de despliegue y funcioamiento a nivel general
* [https://youtu.be/-lE6kISirR8](https://youtu.be/-lE6kISirR8)

### Construido con 🛠️

* [Flask](https://flask.palletsprojects.com/en/2.3.x/)