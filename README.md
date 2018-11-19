# Beep reader player

A python program that reads notes and durations from a text file and plays them back as sine waves. Also volumes are read from the file.

Note frequencies are automatically calculated using a formula. There is no need for huge lookup tables. The program therefore supports any notes.

## Installation

Install using `pip install .` in the project directory (virtual environment recommended).

For development, install dependencies with `pip install -r requirements.txt`.

## Usage

### Command line

Run command `beep-reader-player` to play an example melody.

### Importing module

TODO.

## Notefile format

The format should include note and octave, and the duration in seconds:

`C4:1.0,D4:1.0,E4:1.0`

Note: For now, it's better not to use linebreaks, the parsing will be updated. In addition, for now you can only play notes but not rests. Only one note at a time is played.

## Running tests

TODO.
