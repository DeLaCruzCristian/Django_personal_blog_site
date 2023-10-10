# Django_personal_blog_site
My personal blog site.
Check out the live website [here](https://djangopersonalblogsite-production.up.railway.app/).
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

## How to Use
**Before getting started, make sure you have configured the email configurations, the Database, the DEBUG, and the SECRET_KEY which are all located in the settings file under django_project folder.**

### Adding posts
To add posts, go to the admin page
> http://127.0.0.1:8000/admin/

Then click on `+ add` next to Posts. This will prompt you to fill out a form to create a new post.

After you have created a new post, you are able to go back to the home page
> http://127.0.0.1:8000/

Where you will see your new post. Click on the post title, and it will take you to the detailed view of your post.

## Features
The notable features of my blog project are:
-  SEO-friendly URLs formated as `year/month/day/slug`
-  Canonical URLs for blog posts
-  Pagination that displays three posts per page
-  Post recommendations by email
-  Comment system (which the admin is able to moderate)
-  Tagging system to categorize posts by tags
-  Post recommendations based on similar tags
-  Sitemap for search engines
-  RSS feed that users can subscribe to
-  Full-text search engine.
