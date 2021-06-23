#!/bin/bash
set -e

# some preparations that need to be run on each start could go here...
python ./manage.py migrate --no-input

# execute the given command
exec "$@"
