install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
format:
	black *.py src/*.py
lint:
	flake8 *.py src/*.py
test:
	python  -m pytest -vv --cov
build:
	# build the container
deploy:
	# deploy the code
all: install format lint test deploy