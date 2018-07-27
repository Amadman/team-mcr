#!/bin/sh
source venv/bin/activate
cd app/static
npm install
cd data
./pulldata.sh
cd ../../..

flask run -h 0.0.0.0 -p 8080
