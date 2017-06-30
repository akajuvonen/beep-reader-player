#!/bin/bash

source .env/bin/activate
nosetests -v --with-coverage
deactivate
