# Usa la imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia y instala las dependencias
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia los archivos del proyecto
COPY . .

# Expone el puerto de la aplicación
EXPOSE 80

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
