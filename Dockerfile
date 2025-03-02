FROM python:3.12-bullseye

RUN mkdir -p /home/app

COPY . home/app

WORKDIR /home/app

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn","-c","gunicorn_config.py", "app:app"]