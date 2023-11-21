вместо pip исп-ся poetry

# dev сервер на HTTPS
mkcert
mkcert -install
mkcert localhost
rename certificates to .key .crt

-- python packages
django_extensions
werkzeug
pyopenssl

python manage.py runserver_plus 0.0.0.0:8081 --cert-file srv/localhost.crt
