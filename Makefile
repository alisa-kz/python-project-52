#Makefile

install:
	uv sync

lint:
	uv run ruff check .

fix:
	uv run ruff check --fix

render-start:
	gunicorn task_manager.wsgi

build:
	./build.sh

collectstatic:
	uv run python manage.py collectstatic --no-input

migrate:
	uv run python manage.py migrate

test:
	uv run ./manage.py test

test-coverage:
	uv run coverage run --source='.' manage.py test
	uv run coverage xml

runserver:
	uv run python manage.py runserver