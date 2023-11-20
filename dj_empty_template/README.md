# installation
python -m venv env
source env/bin/activate
pip install -U pip
pip install django
pip freeze > requirements.txt

# configure
django-admin startproject <name:app> .
pytho manage.py startapp <name:first>

# configure gunicorn
pip install gunicorn
...
sudo chmod +x bin/start_gunicorn.sh
./bin/start_gunicorn.sh					# run gunicorn

check 127.0.0.1:8001	in browser

#configure nginx
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

# configure supervisor
install [supervisor] from linux package manager	

/etc/supervisord.conf
--
[program:gunicorn]
command=path/to/bin/start_gunicorn.sh
user=www
process_name=%(program_name)s
directory=/path/to/project
numproc=1
autostart=1
autorestart=1
redirect_stderr=true
--
systemctl restart supervisord.service
check <ip: ip a> 	in browser