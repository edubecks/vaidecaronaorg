#!/bin/bash
export CARONAS_BRASIL_DB_NAME=caronasbrasil
export CARONAS_BRASIL_DB_USER=root
export CARONAS_BRASIL_DB_PASSWORD=qwerty
export CARONAS_BRASIL_DB_HOST=127.0.0.1
export CARONAS_BRASIL_DB_PORT=8889
source /Users/edubecks/venv/venv-fbgroups/bin/activate;
cd /Users/edubecks/Dropbox/Developer/fbgroups/djangoapp;
python manage.py schemamigration caronasbrasil --auto;
python manage.py migrate caronasbrasil;