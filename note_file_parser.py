#!/usr/bin/env python

def note_file_parser(filename):
    with open(filename,'r') as f:
        contents = f.read()
    # Dummy return for now
    notes = ['C4','D4','E4']
    durations = [1.0,1.0,1.0]
    return notes,durations

def main():
    filename = 'tests/notefile.txt'

if __name__=='__main__':
    main()
