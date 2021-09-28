install:
	poetry install

test:
	poetry run pytest tests

test-coverage:
	poetry run pytest --cov=matrix_handler --cov-report xml tests

lint:
	poetry run flake8 matrix_handler tests

selfcheck:
	poetry check

check: selfcheck test-coverage lint

build:
	poetry build

publish:
	poetry publish --repository foo
	
package-install:
	pip install --user dist/*.whl

.PHONY: install test lint selfcheck check build
