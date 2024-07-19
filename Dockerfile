FROM python:3.11-slim

WORKDIR /var/www/api

COPY requirements.txt /var/www/api

RUN pip install -r requirements.txt && \
    pip cache purge

COPY . /var/www/api

CMD ['fastapi', 'dev', 'main.py']
