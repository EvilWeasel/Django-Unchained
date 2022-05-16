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

## Sources

[default-page]: https://i.imgur.com/Hzf1zGR.png
[getting-started]: https://docs.djangoproject.com/en/4.0/intro/tutorial01/
