FROM python:2.7-alpine

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD python2 inlinebot.py
