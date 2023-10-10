# Django_personal_blog_site
My personal blog site
## Installation
First clone the repository and change into the directory
```bash
$ git clone https://github.com/Akash1362000/django_project_blogapp.git
```
```bash
$ cd Django_personal_blog_site
```
Create a virtual environment
```bash
$ python -m venv .venv
```
Activate the environment
```bash
$ .venv\Scripts\Activate.ps1
```
Install requirements
```bash
$ pip install -r requirements.txt
$ pre-commit install
```
Run migrations for Database
```bash
$ python manage.py migrate
```
Create superuser for Admin Login
```bash
$ python manage.py createsuperuser
```
Once superuser has been created, you can run the server to see your application up and running
```bash
$ python manage.py runserver
```
To exit the environment
```bash
$ deactivate
```
