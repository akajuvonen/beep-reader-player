# Beep reader player

A python program that reads notes and durations from a text file and plays them back as sine waves. TODO: Also volumes should be read from the file.

Note frequencies are automatically calculated. There is no need for huge lookup tables.

Uses pygame (mainly sndarray) to play waveforms. Requires python 2.x (unless you have a suitably new version of pygame, in which game 3.x is also ok.)

# Notefile format

The format should include note and octave, and the duration in seconds:

`C4:1.0,D4:1.0,E4:1.0`

# Tests

The easiest way to run tests is `nosetests -v` .
