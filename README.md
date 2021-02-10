# ImageUpload
This is a web app used to upload images into a database.

## Typical commands to get you started in your local machine:

### Create python virtual environment in project directory:
python -m venv env-name
cd env-name

### To activate the virtual environment
scripts\activate 
install python and Django

### Create project
django-admin startproject imageUploadApp

### Run migrations to access database and start the django development server:
python manage.py migrate
python manage.py runserver

### Create a superuser account:
python manage.py createsuperuser

### Create a Django app
python manage.py startapp imageUpload

### Create migration file for app
python manage.py makemigrations

### Run them
python manage.py migrate

