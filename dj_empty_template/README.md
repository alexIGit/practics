# installation
python -m venv env
source env/bin/activate
pip install -U pip
pip install django
pip freeze > requirements.txt

# settings
django-admin startproject <name:app> .
pytho manage.py startapp <name:first>

# settings gunicorn
pip install gunicorn
...
sudo chmod +x bin/start_gunicorn.sh
./bin/start_gunicorn.sh					# run gunicorn

check 127.0.0.1:8001