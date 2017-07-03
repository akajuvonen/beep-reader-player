#!/bin/bash

source .env/bin/activate
nosetests -v --with-coverage --cover-package=beep_reader_player,note_file_parser
deactivate
