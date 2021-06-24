#!/bin/bash
set -e

echo "printenv"
printenv

echo "Test Database"
#echo "postgres://antonpirker:e44ccd99e65b71bbaf13913e85e9063463fab1d3fd122d58692dc02dcede@postgres12.wdpr.run:5432/antonpirker"
#psql "postgres://antonpirker:e44ccd99e65b71bbaf13913e85e9063463fab1d3fd122d58692dc02dcede@postgres12.wdpr.run:5432/antonpirker" -c "select version();"

psql "postgres://wdprcustomeradm:%25AqsI]IBvS[you[zK8z^=mOb-+gQ1$p<s}9=k%25u}@customers-postgres-12.c0ivpkyb3o26.eu-central-1.rds.amazonaws.com:5432/postgres" -c "select * from information_schema.schemata;"

echo "Running Migrations"
python ./manage.py migrate --no-input

# execute the given command
exec "$@"
