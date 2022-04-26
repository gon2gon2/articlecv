FROM python:3.8.12-buster
COPY . /app
WORKDIR /app
RUN pip install flask
ENTRYPOINT sh ./run.sh
