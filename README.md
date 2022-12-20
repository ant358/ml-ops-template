[![Makefile CI process for Github](https://github.com/ant358/ml-ops-template/actions/workflows/devops-github.yml/badge.svg)](https://github.com/ant358/ml-ops-template/actions/workflows/devops-github.yml)

# ml-ops-template

## First build out the project 
Create the files and folders you need for your project.  This includes the following:
Makefile
Dockerfile
requirements.txt
main.py
src/
    __init__.py
    train.py
    predict.py
    test.py
data/
notebooks/
models/
tests/
docs/
README.md

## Create a virtual environment
python3 -m venv venv
activate the virtual environment
source venv/bin/activate or on windows venv\Scripts\activate

## Install the requirements
The first time you run the requirements it is worth removing the pinned version numbers so the best version for the python version is installed.  Once you have the project running you can pin the versions, with pip freeze > requirements.txt
pip install -r requirements.txt
or make install

## Start the CI process  
push the changes so far to github or gitlab
Then check that the requirements are installed correctly in the first stage of the CI process.
Check the first step of the CI process is successful, (add the badge to the readme file.)
Then add the formating and linting steps to the CI process.

## Add some tests and test coverage stats
Add some tests to the tests folder and run the tests with pytest
Fail some tests to check the CI process fails
