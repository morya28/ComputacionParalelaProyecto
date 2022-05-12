# Se toma como base una imagen de mongo
FROM mongo

# Instalar librerias necesarias en caso de necesitar hacer debug
RUN apt-get update && apt-get install -y vim && apt-get install -y net-tools

# Agregar archivos con entradas de prueba en la base de datos
ADD eggs.json /eggs.json
ADD foobar.json /foobar.json
ADD spam.json /spam.json

# Archivo para poder crear la base de datos
ADD start_db.sh /start_db.sh
