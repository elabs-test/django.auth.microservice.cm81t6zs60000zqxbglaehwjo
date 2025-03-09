# Imagen base
FROM python:3.10-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo
WORKDIR /code

# Instalar herramientas necesarias como psql
RUN apt-get update && apt-get install -y postgresql-client

# Instalar dependencias
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código del proyecto
COPY . /code/

# Exponer el puerto 8000
EXPOSE 8000

# Comando por defecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

