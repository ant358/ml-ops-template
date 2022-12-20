install:
	# install the dependencies
	pip install --upgrade pip &&\
	pip install -r requirements.txt
format:
	# format the code
	black *.py src/*.py tests/*.py
lint:
	# see flake8.ini for linting configuration
	flake8 -v *.py src/*.py tests/*.py
test:
	# see pytest.ini for test configuration
	python -m pytest -v --cov=src --cov=main.py tests/*.py
build:
	# build the container
	docker build -t fastapi-wiki .
deploy:
	# deploy the code
	docker run -d -p 8080:8080 fastapi-wiki
all: install format lint test deploy