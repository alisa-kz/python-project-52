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
	uv run manage.py collectstatic --no-input

migrate:
	manage.py migrate