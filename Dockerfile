#
# Dockerfile for the asyncdjango demo project
#
# Build:
# docker build --tag asyncdjango:v0 .
#
# Run:
# docker run --env-file env -p 8000:8000 asyncdjango:v0
#


FROM python:3.9-buster

RUN apt update && apt install postgresql postgresql-contrib

ADD requirements.txt /app/requirements.txt

RUN python -m venv /env
RUN /env/bin/pip install --upgrade pip
RUN /env/bin/pip install --no-cache-dir -r /app/requirements.txt
RUN cat /app/requirements.txt

ADD . /app
WORKDIR /app

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
ENV PYTHONASYNCIODEBUG 1

# db configuration
ARG ASYNC_DB_HOST
ENV ASYNC_DB_HOST=${ASYNC_DB_HOST}

COPY data/pokemon.csv .
COPY docker-entrypoint.sh docker-entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/docker-entrypoint.sh"]

# sync server:
CMD ["gunicorn", "--bind", ":8000", "--workers", "4", "asyncdjango.wsgi:application"]

# async server:
#CMD ["gunicorn", "--bind", ":8000", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "asyncdjango.asgi:application"]
