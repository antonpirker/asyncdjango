#!/bin/bash -x
set -e

echo "printenv"
printenv

echo "Running Migrations"
python ./manage.py migrate --no-input

echo " "
echo "*************************************************************************************************"
echo " running chamber exec"
echo " "
# execute the given command
exec chamber exec $APP_ENVIRONMENT -- newrelic-admin run-program "\$@"
