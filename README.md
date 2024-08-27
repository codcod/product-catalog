# R&D Product Catalog

Recreate database:

    $ rye run python manage.py migrate
    $ rye run python manage.py createsuperuser
    $ rye run python manage.py makemigrations products
    $ rye run python manage.py migrate
