#!/usr/bin/env sh

echo "Using cron schedule $CRONTAB"

echo "$CRONTAB cd /app && /app/main.py > /var/log/speedtest.log 2>&1" | crontab -

crond -b -L /var/log/cron.log

tail -f /var/log/speedtest.log /var/log/cron.log
