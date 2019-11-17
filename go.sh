#!/bin/bash

set -e  # fail on error
set -x  # print commands that are executed

python3 01pages.py -f
jupyter nbconvert --execute parse.ipynb

