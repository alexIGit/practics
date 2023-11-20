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

check 127.0.0.1:8001	in browser

#setings nginx
vim /etc/nginx/sites-enabled/default?
ln -l ... 
or edit nginx settings: nginx.conf?
--
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	server_name _;

	location / {
            proxy_pass http://127.0.0.1:8001;
            proxy_set_header X-Forwarded-Host $server_name;
            proxy_set_header X-Real-IP $remote_addr;
            add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ANL UNI CON NAV"';
            add_header Access-Control-Allow-Origin *;
        }
}
--
./bin/start_gunicorn.sh
check <ip: ip a> 	in browser