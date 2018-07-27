#!/bin/sh
pip install -r requirements.txt
cd app/static
npm install
cd data
./pulldata.sh
cd ../../..
