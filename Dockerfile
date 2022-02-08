FROM python:3-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

COPY docker/docker-entrypoint.sh /docker-entrypoint.sh

ENV CRONTAB="0 */6 * * *"

RUN touch /var/log/speedtest.log && touch /var/log/cron.log

CMD [ "/docker-entrypoint.sh" ]
