FROM python:3.7

RUN mkdir /app
ADD requirements.txt /app
ADD bot.py /app
RUN pip install -r /app/requirements.txt

WORKDIR /app

CMD [ "python", "/app/bot.py" ]
