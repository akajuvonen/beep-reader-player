#!/usr/bin/env python

def note_file_parser(filename):
    notes = []
    durations = []
    with open(filename,'r') as f:
        contents = f.read()
    blocks = contents.split(',')
    for item in blocks:
        note, duration = item.split(':')
        notes.append(note)
        durations.append(duration)
    return notes,durations

def main():
    filename = 'tests/notefile.txt'

if __name__=='__main__':
    main()
