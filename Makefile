install:
	python3 -m poetry install

brain-games:
	python3 -m poetry run brain-games

build:
	python3 -m poetry build

publish:
	python3 -m poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl
