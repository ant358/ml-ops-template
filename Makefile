install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
format:
	black *.py src/*.py
lint:
	# lint the code
test:
	# test the code
deploy:
	# deploy the code
all: install format lint test deploy