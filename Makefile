# variables
VENV = venv
PYTHON = ${VENV}/bin/python
PIP = ${venv}/bin/pip

setup-venv:
	python -m venv ${VENV}

install-packages:
	pip install -r requirements.txt

run-server:
	${PYTHON} manage.py runserver
