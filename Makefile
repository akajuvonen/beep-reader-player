init:
	pip install -r

test:
	nosetests -v

clean:
	rm -fv *.pyc
	rm -fv tests/*.pyc
	rm -fv config/*.pyc
