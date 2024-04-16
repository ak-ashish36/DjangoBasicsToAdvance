# Django Cheat Sheet

### Creating a virtual environment (optional)
We need to create a virtual env for our app to run in: [More Here](https://docs.python.org/3/library/venv.html)
Run this command in whatever folder you want to create your venv folder
```
python -m venv ./venv
```
#### Activate the virtualenv
```
# Mac/Linux
source ./venv/bin/activate
# Windows (CMD)
venv\Scripts\activate.bat - May need to add full path (D:\ak-ashish36\Projects\DjangoBeginnerToAdvance\venv\Scripts\activate.bat)
```
#### Escape from venv
```
deactivate
```

# Lets Start with or without virtualenv
### Check Python packages installed
```
pip freeze
```
### Install Django
```
pip install django
```
### List Django options
```
django-admin
```
### Create your project
```
django-admin startproject PROJECTNAME
```

### Run Server (http://127.0.0.1:8000) CTRL+C to stop

```
python manage.py runserver
```

### Run Server on Custom Port(http://127.0.0.1:4444) CTRL+C to stop

```
python manage.py runserver 4444
```

### Install mysql driver
```
pip install mysqlclient
```

### Create migrations (used after creating new models)
```
python manage.py makemigrations
```

### Run migration (migrates the models/tables to the database)
```
python manage.py migrate
```

### Create Superuser/admin
```
python manage.py createsuperuser
```