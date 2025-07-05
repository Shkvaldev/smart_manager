FROM python:3.12-slim

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /app
WORKDIR /app

# Installing needed cert
# Source: https://developers.sber.ru/docs/ru/gigachat/certificates?OS=debian-ubuntu
RUN apt-get update -y && apt-get install -y curl
RUN curl -k "https://gu-st.ru/content/lending/russian_trusted_root_ca_pem.crt" -w "\n" >> $(python -m certifi)

ENTRYPOINT python main.py