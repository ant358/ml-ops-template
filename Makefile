install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
format:
	black *.py src/*.py tests/*.py
lint:
	flake8 -v *.py src/*.py tests/*.py
tests:
	pytest --cov=src tests/*.py 
build:
	# build the container
deploy:
	# deploy the code
all: install format lint test deploy