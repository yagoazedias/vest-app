test:
	coverage run -m unittest tests/all.py && make coverage

integration:
	coverage run -m unittest tests/integration.py

single-test:
	python3 -m unittest

coverage:
	coverage report --fail-under=95 --show-missing --omit=".venv/*","*/test*","lib/business/authorizer.py"

install:
	pip3 install -r requirements.txt

create-virtual-env:
	virtualenv .venv

install-virtual-env:
	source .venv/bin/activate && pip3 install -r requirements.txt

run:
	python3 authorize.py < samplefile
