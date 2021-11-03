#!/bin/sh

set -e

echo $(date '+%F %T.%3N %Z') "[flask] INFO: running start.sh"

env=${FLASK_ENV:-development}

if [ $env = "production" ]
then
    echo $(date '+%F %T.%3N %Z') "[flask] INFO: running production environment"
    gunicorn --bind 0.0.0.0:5000 --chdir ./ms ms:app
else
    echo $(date '+%F %T.%3N %Z') "[flask] INFO: running development environment"
    flask run --host=0.0.0.0
fi
