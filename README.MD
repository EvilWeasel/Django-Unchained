# Django-Unchained

## Table-of-Content

## About this Project

This is a little test-project, using the official getting-started guide from [Django-Docs][getting-started]

## Requirements

- Python installed on your machine (winget, windows-store, package-manager)
- PIP, which is the default package-manager for python (like npm, maven, nuGet)
- Code-Editor (VSCode)

## Writing your first Django-App

### Scaffolding the Project

First up, we have to use the `django-admin`-tool to scaffold the project with all dependencies, just like in C# but with the CLI (Command-Line-Interface).

```bash
django-admin startproject <yourNameHere>
```

After that, we just `cd` into our newly created project-root and start VSCode with:

```bash
cd <yourNameHere> && code .
```

### Generated Content

The outer `<projectName>`/ root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.

- manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.

The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

- **`mysite/**init**.py`**: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
- **`mysite/settings.py`**: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
- **`mysite/urls.py`**: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
- **`mysite/asgi.py`**: An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details.
- **`mysite/wsgi.py`**: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.

### Development-Server

Before making any changes, verify that the project runs without problems by running following command:

```bash
python3 manage.py runserver
```

You should then be able to access the website under `localhost:8000`

![default-page][default-page]

If you want to change the port for the development server, you can pass in any port-number you want as start-argument

```bash
python3 manage.py runserver <port>
```

## Understanding Apps in Django

- Project more than a few pages
- confusing at first
- example: accounts app, blogs app,...

todo:
To create a new app use the following command:

```bash
python manage.py startapp accounts
```

## URLs and routing

![Django-URLs][django-urls]

To summarize, to return content to the user depending on the url-path, you need to do **2 things**:

1. Add the path to the URL-Patterns

```python
from django.urls import path

urlpatterns = [
	path('<urlPath>', <returnViewFunction>)
]
```

2.  Create a view-function, which returns either a rendered view, or a simple `HttpResponse`

```python
from django.urls import path
from django.http import HttpResponse


def home(request):
	return HttpResponse('Home Page')

urlpatterns = [
	path('/home', home)
]
```

## Templates and Inheritance

### Returning simple views

To create a template, we first need to create a folder for them like this: `<projectRoot>/accounts/templates/accounts`

Inside this folder, we'll create a view called `dashboard.html` with following content:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Dashboard</title>
  </head>
  <body>
    <h1>Dashboard</h1>
  </body>
</html>
```

To return this page when a user requests `<hostname>/home` we add a function to `views.py`, which returns the rendered page:

```python
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')

```

Create 2 more files exactly like this and add their url-pattern to the corresponding `urls.py` and their render-method in `views.py`.

### DRY - Don't Repeat Yourself

Because it's unnecessary to repeat the same stuff that needs to be on every page, we use templates, from which our custom-views can inherit.

First, create a new file called `main.html`:

```filetree
-- templates
	-- accounts
		-- customer.html
		-- dashboard.html
		++ main.html
		-- products.html
```

Inside we declare all the recuring html-tags and something from the Django-Framework called a **block-tag**.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Dashboard</title>
  </head>
  <body>
    <h1>Navbar</h1>
    <hr />
    {% block content %} {% endblock %}
    <hr />
    <h5>Footer</h5>
  </body>
</html>
```

Now we can refactor our other templates, to _extend the 'accounts/main' template_.

**`templates/accounts/dashboard.html`**

```html
{% extends 'accounts/main.html' %} {% block content %}
<h1>Dashboard</h1>
{% endblock %}
```

### More Refactoring - Navbar template

**`navbar.html`**

```html
<h1>Navbar</h1>
<hr />
```

**`main.html`**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Dashboard</title>
  </head>
  <body>
    {% include 'accounts/navbar.html' %}
    <br />
    {% block content %} {% endblock %}
    <hr />
    <h5>Footer</h5>
  </body>
</html>
```

Note that we didn't specify `navbar.html` as a template and therefore need to use the keyword _"include"_ when using it in our pages.

## Upgrading our dashboard

**`dashboard.html`**

```html
{% extends 'accounts/main.html' %} {% block content %}
<br />
<div class="row">
  <div class="col-md-5">
    <h5>CUSTOMERS:</h5>
    <hr />
    <div class="card card-body">
      <a class="btn btn-primary btn-sm btn-block" href="">Create Customer</a>
      <table class="table table-sm">
        <tr>
          <th></th>
          <th>Customer</th>
          <th>Orders</th>
        </tr>
      </table>
    </div>
  </div>

  <div class="col-md-7">
    <h5>LAST ORDERS</h5>
    <hr />
    <div class="card card-body">
      <a class="btn btn-primary btn-sm btn-block" href="">Create Order</a>
      <table class="table table-sm">
        <tr>
          <th>Product</th>
          <th>Date Orderd</th>
          <th>Status</th>
          <th>Update</th>
          <th>Remove</th>
        </tr>
      </table>
    </div>
  </div>
</div>
{% endblock %}
```

This is basically just a little bit of UI for doing CRUD-Operations in the next part.
For the styling to work, import [Bootstrap] into `main.html`.

## Serving static files

On receiving a http-request, we return a rendered view, defined by our template html-files. But what if we need to send additional files, typically linked inside the html with a `<link>` or `<script>` tag.

To link static files in our html, we first need to set-up django for serving them.

**`settings.py`**

```python
# ...
STATIC_URL = 'static/'

MEDIA_URL = 'images/'

# Static files directories
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# ...
```

With that done, we can insert a logo for our navbar.

**`navbar.html`**

```html
{% load static %}
<nav class="navbar navbar-expand-lg bg-dark navbar-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">
      <img src="{% static 'images/tux.ico' %}" alt="" width="50" height="50" />
    </a>
<!-- ... >
```

## Database and Models

### Initital Migration

In the default configuration, Django will setup a sqlite database automatically for us.

To execute the initial migration for the auto-generated models, we use the following command:

```bash
python manage.py migrate
```

Just like in Entity-Framework in C# (Or many other ORM's), we make a migration every time our models change, to apply the changed to the schema in our DB.

When changing the models, you need to first make the migration...

```bash
python manage.py makemigrations
```

...And **then** execute it.

```bash
python manage.py migrate
```

### Creating superuser for the admin-page

Because we currently use sqlite, where we can't see our data, we create a superuser for the Django admin-page.

```bash
# Make sure
python manage.py createsuperuser
```

The next time we start our app, we can access the admin-panel on `localhost:8000/admin`.

### Models Unchained

Models in Django are essentially just python classes.

For example, a python class like this:

```python-class
Class Product:
  id = integer
  name = string
  price = float
```

Will result in a table like this:

| ID  | Name | Price |
| --- | ---- | ----- |
| 1   | Karl | 3,50  |

### Creating our Models

```python
class Customer(models.Model):
  name = models.CharField(max_length=200, null=True)
  phone = models.CharField(max_length=200, null=True)
  email = models.CharField(max_length=200, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)

  # this next bit is there to override the "toString"-Method
  def __str__(self):
    return self.name
```

Don't forget to make a new migration.

To interact with our models while using sqlite in development, we can add it to the admin-panel. This way we can easily test out our database-functionality.

## Sources

[default-page]: https://i.imgur.com/Hzf1zGR.png
[getting-started]: https://docs.djangoproject.com/en/4.0/intro/tutorial01/
[django-urls]: https://i.imgur.com/KHknp9h.png
[bootstrap]: https://getbootstrap.com/
