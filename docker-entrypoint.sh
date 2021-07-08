#!/bin/bash
set -e

echo "printenv"
printenv

echo "Running Migrations"
python ./manage.py migrate --no-input

# execute the given command
exec "\$@"
