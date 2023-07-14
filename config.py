import os

# Configuración de la aplicación Flask
DEBUG = True
SECRET_KEY = "Milhouse"


POSTGRES_SERVER = os.environ.get("POSTGRES_HOST", "127.0.0.1")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "user_name")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "passwd")
POSTGRES_DB = os.environ.get("POSTGRES_DB", "finkargo")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", "5432")
SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}:{}/{}".format(
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_SERVER,
    POSTGRES_PORT,
    POSTGRES_DB
)
