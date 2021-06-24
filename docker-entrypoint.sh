#!/bin/bash
set -e

echo "printenv"
printenv

echo "Test Database"
echo "postgres://antonpirker:e44ccd99e65b71bbaf13913e85e9063463fab1d3fd122d58692dc02dcede@postgres12.wdpr.run:5432/antonpirker"
psql "postgres://antonpirker:e44ccd99e65b71bbaf13913e85e9063463fab1d3fd122d58692dc02dcede@postgres12.wdpr.run:5432/antonpirker" -c "select version();"

echo "Running Migrations"
python ./manage.py migrate --no-input

# execute the given command
exec "$@"
