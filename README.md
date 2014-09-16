# django-alchemy

## Quickstart

This quickstart describe the project setup on a Unix-like OS. It has been tested on OS X Mavericks.

### Install virtualenv

Install `virtualenv` if it's not already there:

```bash
$ sudo easy_install virtualenv
```

### Create a new virtualenv

Prepare and activate a new virtual environment for the project:

```bash

$ mkdir -p ~/code/virtualenvs/

$ virtualenv --no-site-packages --distribute -p `which python3` ~/code/virtualenvs/django-alchemy

$ echo 'export DJANGO_SECRET_KEY="some secret here"' >> ~/code/virtualenvs/django-alchemy/bin/activate
$ echo 'export DJANGO_SETTINGS_MODULE="alchemy.settings.local"' >> ~/code/virtualenvs/django-alchemy/bin/activate

$ source ~/code/virtualenvs/django-alchemy/bin/activate
```


### Create project directory

Create a directory to host the project files:

```bash

$ mkdir -p ~/code/projects/your-nickname/django-alchemy

$ cd ~/code/projects/your-nickname/django-alchemy

$ git clone https://github.com/zmoog/django-alchemy.git

```


### Install required packages

Install required Python packages:

```bash

$ cd ~/code/projects/your-nickname/django-alchemy

$ pip install -r requirements/local.txt

```

### Setup the database

Prepare the database and authentication:

```bash
$ python manage.py migrate --settings=alchemy.settings.local
Operations to perform:
  Apply all migrations: contenttypes, admin, auth, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying sessions.0001_initial... OK

```

### Superuser

```bash
$ python manage.py createsuperuser
Username (leave blank to use 'me'):
Email address: me@domain.com
Password:
Password (again):
Superuser created successfully.
```

### Let's go!

And finally run the server:

```bash

$ python manage.py runserver --settings=alchemy.settings.local
Performing system checks...

System check identified no issues (0 silenced).
September 16, 2014 - 22:08:21
Django version 1.7, using settings 'alchemy.settings.local'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.


# .. and when you're done exit the virtual environment with
$ deactivate

# and .. 🍺

```

## Development

If you add new feature don't forget to track the requirements list.

```bash

$ pip freeze --local > ../requirements/base.txt

```
