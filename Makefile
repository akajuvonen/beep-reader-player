all:	init

init:
	pip install -r requirements.txt

test:
	nosetests -v

run:
	python beep_reader_player.py

clean:
	rm -fv *.pyc
	rm -fv tests/*.pyc
	rm -fv config/*.pyc
