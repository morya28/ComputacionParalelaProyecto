#!/bin/bash
printf "sho dbs\nuse TelemetryHub\ndb.farm_jobs.insert({\"creation\": \"$(date)\"})\nshow dbs\ndb.farm_jobs.find()\n" | mongo && \
mongoimport --db TelemetryHub --collection farm_jobs --file /eggs.json \
    && mongoimport --db TelemetryHub --collection farm_jobs --file /foobar.json \
    && mongoimport --db TelemetryHub --collection farm_jobs --file /spam.json