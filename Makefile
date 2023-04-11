install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=calCLI --cov=devopslib test_*.py

format:
	black *.py devopslib/*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py  devopslib/*.py

container_lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	# echo "deploy not implemented"

all: install lint test format
