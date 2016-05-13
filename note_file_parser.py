#!/usr/bin/env python

def note_file_parser(filename):
    # Init notes and durations lists
    notes = []
    durations = []
    # Open file and read contents to string
    with open(filename,'r') as f:
        contents = f.read()
    # Divide string to blocks which contain 'note:duration'
    blocks = contents.split(',')
    # Split the block into note name and duration
    for item in blocks:
        note, duration = item.split(':')
        notes.append(note)
        # Here we must convert to float, it also automatically
        # gets rid of line breaks at the end of lines in the file
        durations.append(float(duration))
    return notes,durations

def main():
    filename = 'tests/notefile.txt'
    notes,durations = note_file_parser(filename)
    print(notes)
    print(durations)

if __name__=='__main__':
    main()
