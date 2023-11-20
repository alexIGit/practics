# installation
python -m venv env
source env/bin/activate
pip install -U pip
pip install django
pip freeze > requirements.txt

# settings
django-admin startproject <name:app> .
pytho manage.py startapp <name:first>