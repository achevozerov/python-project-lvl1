install:
	python3 -m poetry install

brain-games:
	python3 -m poetry run brain-games

brain-even:
	python3 -m poetry run brain-even

brain-calc:
	python3 -m poetry run brain-calc

build:
	python3 -m poetry build

publish:
	python3 -m poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	python3 -m poetry run flake8 brain_games
