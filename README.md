# Beep reader player

A python program that reads notes and durations from a text file and plays them back as sine waves. Also volumes are read from the file.

Note frequencies are automatically calculated using a formula. There is no need for huge lookup tables. The program therefore supports any notes.

## Dependencies

Initially you need python and virtualenv to be installed. You can install needed dependencies using `make init`. The virtual environment and dependency installation are automatically done, system python packages are not affected. The packages are also listed in `requirements.txt`.

## Running

After installing the required dependencies, use `make run` to run the example program in found in main function. It should play back a short melody.

## Options

Configuration can be changed from `config/config.py`.

## Notefile format

The format should include note and octave, and the duration in seconds:

`C4:1.0,D4:1.0,E4:1.0`

Note: For now, it's better not to use linebreaks, the parsing will be updated. In addition, for now you can only play notes but not rests. Only one note at a time is played.

## Unit tests

Just run `make test` to run the test suite.

## Make clean

Running `make clean` will remove the virtual environment folder, pyc-files and other temporary files, restoring the folder to it's original state.
