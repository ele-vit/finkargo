# Imagen base con Python y Flask
FROM python:3.9-slim-buster

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY . /app

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el contenedor
EXPOSE 5000

# Establecer la variable de entorno para la aplicación Flask
ENV FLASK_APP=app.py

# Ejecutar la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0"]
