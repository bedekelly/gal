#!/bin/bash

set -e

# - Download/unzip gal folder

python3 -m venv .gal/venv
source .gal/venv/bin/activate
python3 -m pip install -r .gal/requirements.txt

cd .gal/frontend
yarn
yarn run build
cd ../..

python3 .gal/app.py
