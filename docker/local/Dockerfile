FROM python:3.9-slim

COPY app_client/ app_client/

RUN pip install --upgrade pip && \
    apt-get update && \
    apt-get install -y --no-install-recommends default-libmysqlclient-dev build-essential && \
    apt-get clean all && \
    pip install -r ./app_client/requirements/requirements_local.txt

CMD python -m debugpy --listen 0.0.0.0:5678 --wait-for-client -m flask run --host 0.0.0.0 --port 5000
# CMD ["sleep","infinity"]
EXPOSE 5000
