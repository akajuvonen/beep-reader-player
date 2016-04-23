# Beep reader player

A python program that reads notes and durations from a text file (in the future, TODO...) and plays them back as sine waves.

Note frequencies are automatically calculated. There is no need for huge lookup tables.

Uses pygame (mainly sndarray) to play waveforms. Requires python 2.x (unless you have a suitably new version of pygame, in which game 3.x is also ok.)

# Tests

The easiest way to run tests is `nosetests -v` .
