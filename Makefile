help:
	@echo "    install"
	@echo "        Install project."
	@echo "    develop"
	@echo "        Install develop requirements and install project in develop mode."
	@echo "    clean-pyc"
	@echo "        Remove python artifacts."
	@echo "    clean-build"
	@echo "        Remove build artifacts."
	@echo "    clean"
	@echo "        Remove all artifacts."
	@echo "    test"
	@echo "        Run py.test"

install:
	pip install -r requirements.txt
	pip install .

develop:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	pip install -e .

clean-pyc:
	find . -name '__pycache__' -exec rm -rf {} +

clean-build:
	find . -name '.eggs' -exec rm -rf {} +
	find . -name '*.egg-info' -exec rm -rf {} +

clean: clean-build clean-pyc

test: develop
	python setup.py pytest

.PHONY: install develop clean-pyc clean-build clean test
