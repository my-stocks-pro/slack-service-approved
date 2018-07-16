FROM python:3.6

COPY . /app

WORKDIR /app

RUN mkdir /app/logs_vol

VOLUME /logs_vol

RUN pip install -r requirements.txt

CMD python slack-service-approved.py
