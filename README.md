# Django_personal_blog_site
A personal blog project built using the Django framework.

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
Create a **.env** file and set the following properties to your specific values
```
SECRET_KEY=mysecretkey
SENGRID_API_KEY=myapikey
DATABASE_URL=mydatabaseurl
```
> [!NOTE]
> This uses [sendgrid](https://sendgrid.com/) as the email server. If you do not want to use sendgrid, then you will need to configure the email properties in the settings.py file to your preferences.

> [!IMPORTANT]
> To generate a secret key, you will need to run this command in the terminal:
```bash
$ python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
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

### Adding posts
To add posts, go to the admin page
> http://127.0.0.1:8000/admin/

Then click on `+ add` next to Posts. This will prompt you to fill out a form to create a new post.
### Viewing all posts
After you have created a new post, you are able to go back to the home page where you will see your new post. 
> http://127.0.0.1:8000/

The root path lists all the blog posts that have been set to publish.

### Viewing individual posts
Clicking on an posts title will take you to their page where you are able to view the whole body of the post as well as comments.

You are able to share the post by filling out an email form and also make comments under posts.
