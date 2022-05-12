# Se toma como base una imagen de python/alpine
FROM python:3.7.4-alpine3.10

# En este archivo se encuentran los modulos de Python necesarios para el proyecto
ADD Django_app/requirements.txt /app/requirements.txt

# Instalar los modulos necesarios para la app
RUN set -ex \
    && apk add --no-cache --virtual .build-deps postgresql-dev build-base \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

# Copiar el proyecto de Django
ADD Django_app /app
WORKDIR /app

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8000

# Iniciar el servicio de Django con gunicorn
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "mysite.wsgi"]
