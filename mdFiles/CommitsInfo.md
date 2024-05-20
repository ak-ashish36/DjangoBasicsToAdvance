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

## If-Else and ForLoop
##### Used Conditional tags and For loops in HomePage

## Managing Static Files
##### Changed Home Page and added support of css,images from Static dir in index.html

## Managing Header and Footer using include keyword in Templates
##### Adde header.html and footer.html file in templates and using them in all other page using include keyword

## Extends keyword in templates
##### header and footer are included in base.html file, and base.html is included in all other pages
##### Added Contact page

## Url Templates and Highlighting links
##### Routing pages with the use of url templates
##### Highlighting the page in navbar which is opened

## HTTP Request and Page Redirecting
### Created form with GET and POST Request
### Shown example of redirecting page in post request of the page , see views.html
### Page redirecting can also be achieved by action attribute in form tag