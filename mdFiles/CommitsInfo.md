# Commits Information step by step

## Initial Commit
##### created new django Project named 'newProject' and initialized the repo.
##### created media,static and templates folder inside the BASE_DIR

## Configured Database and Created Superuser
##### Installed 'mysqlclient' and Changed the database to MySql
##### Migrated the default models/tables to the database 'python manage.py migrate'
##### Created the super user by 'python manage.py createsuperuser'


## Added Views.py
##### Created views.py file and added some urls
##### Created dynamic urls, there are 3 types of dynamic urls (int,string,slug), for example 'url/<string:courseName>'.
##### Leave the data type blank to pass any type of value in dynamic url, for example 'url/<yourValue>'

## Render Html Page
##### Created HTML page rendering from templates.
##### Passing dynamic values in the html page.