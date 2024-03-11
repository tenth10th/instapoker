test:
	pytest

types:
	mypy .

format:
	black .

submit:
	pytest --submit

email:
	pytest --email

rules:
	pytest --rules

build: format types test
