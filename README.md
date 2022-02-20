# Mastering Python - Django

This is simple blog application with other small apps for learning purposes.

Deployment considerations:

1. all static files --> one folder

modify settings.py
STATIC_ROOT = BASE_ROOT / "staticfiles"

collect static files to "staticfiles"
python3 manage.py collectstatic

option 1 make DJANGO aware of staticfiles folder
modify urls.py
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
2. create virtual env
python3 -m venv blogapp
   activate virtual env (source command)
   
install packages in that virtual env
   python3 -m pip install Django Pillow

3. create requirements.txt (too many packages)
   python3 -m pip freeze > requirements.txt

4. modify ALLOWED_HOSTS in settings.py
from os import getenv 

ALLOWED_HOSTS = [getenv("APP_HOST")]
   
DEBUG = getenv("DEVENV", True)
   
do the same with SECRET_KEY

5. deploy to AWS Elastic Beanstalk
create .ebextenstion folder with
   django.config file
   option_settings:
     aws:elasticbeanstalk:container:python:
       WSGIPath: my_site.wsgi:application
   
Choose proper files for deployment (without static folder)

6. connect to db (e.g. mysql)
# settings.py
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'OPTIONS': {
'read_default_file': '/path/to/my.cnf',},}}


# my.cnf
[client]
database = NAME
user = USER
password = PASSWORD
default-character-set = utf8

7. serve static files
   create static-files.config in .ebextentions folder
   option_settings:
   aws:elasticbeanstalk:environment:proxy;staticfiles:
     /static: statisfiles
     /files: uploads
   
8. consider S3 for static files service