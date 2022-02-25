release: python src/pur_beurre/manage.py makemigrations
release: python src/pur_beurre/manage.py migrate
release: python src/pur_beurre/manage.py build_db
web: gunicorn --chdir /app/src/pur_beurre pur_beurre.wsgi:application
