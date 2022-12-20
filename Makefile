install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
format:
	black *.py src/*.py tests/*.py
lint:
	flake8 -vv *.py src/*.py tests/*.py
tests:
	python -m pytest -vv --cov tests/*.py
build:
	# build the container
deploy:
	# deploy the code
all: install format lint test deploy