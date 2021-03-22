FROM python:3.9-slim

WORKDIR /app_client

COPY  app_client/ . 

RUN pip3 install --upgrade pip && \
    apt-get update && \
    apt-get install -y --no-install-recommends default-libmysqlclient-dev build-essential && \
    apt-get clean all && \
    pip install -r ./requirements/requirements_local.txt

# CMD ["sleep","infinity"]
EXPOSE 5000
