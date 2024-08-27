.PHONY = venv check test fix db

APP_DIR=src/catalog

export PYTHONPATH=.

venv:
	rm -rf ".venv"
	rye sync

check:
	mypy --strict --scripts-are-modules --implicit-reexport \
		$(APP_DIR) \
		tests

test:
	pytest  # configured via pyproject.toml

fix:
	isort $(APP_DIR)
	black $(APP_DIR)
	flake8 $(APP_DIR)
	pylint $(APP_DIR)/**

db:
	rm -f $(APP_DIR)/db.sqlite3
	sqlite3 $(APP_DIR)/db.sqlite3 ".read scripts/dump-all.sql"

# 	rye run python manage.py migrate
# 	DJANGO_SUPERUSER_PASSWORD=admin rye run python manage.py createsuperuser \
#		--no-input --username admin --email admin@example.com
# 	rye run python manage.py makemigrations products
# 	rye run python manage.py migrate
# 	sqlite3 $(APP_DIR)/db.sqlite3 ".read scripts/seed.sql"
