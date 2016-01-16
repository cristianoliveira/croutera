setup:
	pip install -r requirements.txt

install:
	python setup.py install

test:
	python -m unittest discover

test3:
	python3 -m unittest discover

clean:
	rm -rf croutera.egg-info && rm -rf $(find . -name '*.pyc')
	rm -rf build && rm -rf dist

publish:
	python setup.py register -r pypi
	python setup.py sdist upload -r pypi

publish-test:
	python setup.py register -r pypitest
	python setup.py sdist upload -r pypitest
