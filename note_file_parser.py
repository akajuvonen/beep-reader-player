#!/usr/bin/env python

def note_file_parser(filename):
    with open(filename,'r') as f:
        contents = f.read()
