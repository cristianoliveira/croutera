setup:
	pip install -r requirements.txt

install:
	python setup.py install

test:
	python -m unittest discover
