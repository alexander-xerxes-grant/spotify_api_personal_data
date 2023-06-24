.PHONY: install local lint flake8 black black-fix isort isort-fix test lint-fix

.ONESHELL:
poetry-config:
	poetry config --local virtualenvs.in-project true

install: poetry-config
	poetry install

local: install
	poetry run pre-commit install

update:
	poetry update

lint: flake8 black isort

lint-fix: black-fix isort-fix

flake8:
	poetry run flake8

black:
	poetry run black --diff --check .

black-fix:
	poetry run black .

isort:
	poetry run isort --diff --check .

isort-fix:
	poetry run isort .

safety:
	poetry export -f requirements.txt | poetry run safety check --stdin

test:
	poetry run pytest \
		--cov-report term:skip-covered \
		--cov-report html:reports \
		--cov-report xml:reports/coverage.xml \
		--junitxml=reports/unit_test_report.xml \
		--cov-fail-under=10 \
		--cov=spotify_api_personal_data tests/ -ra -s

coverage:
	open reports/index.html