#!/bin/bash
set -e

echo "printenv"
printenv

echo "Running Migrations"
python ./manage.py migrate --no-input

# execute the given command
exec chamber exec $APP_ENVIRONMENT -- newrelic-admin run-program "\$@"
