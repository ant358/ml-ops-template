install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
format:
	black *.py src/*.py tests/*.py
lint:
	flake8 -v *.py src/*.py tests/*.py
tests:
	# see pytest.ini for test configuration
	pytest
build:
	# build the container
deploy:
	# deploy the code
all: install format lint test deploy