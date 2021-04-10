# Django 3.2 Slow Query Building

This repository exists to highlight >3x slower SQL query building in Django 3.2 when compared to Django 3.1.8.

To test this, run `setup.sh` and `test.sh` or, run the following commands:

```sh
# Setup
pip install -r requirements.txt
python manage.py migrate

# Run test with Django 3.1.8
pip install django==3.1.8
python manage.py test

# Run test with Django 3.2
pip install django==3.2
python manage.py test
```

Example output on my machine (Python 3.9.2)
```
Installing Django 3.1.8
Collecting django==3.1.8
  Using cached Django-3.1.8-py3-none-any.whl (7.8 MB)
Requirement already satisfied: pytz in /home/phillip/miniconda3/envs/py39/lib/python3.9/site-packages (from django==3.1.8) (2021.1)
Requirement already satisfied: asgiref<4,>=3.2.10 in /home/phillip/miniconda3/envs/py39/lib/python3.9/site-packages (from django==3.1.8) (3.3.4)
Requirement already satisfied: sqlparse>=0.2.2 in /home/phillip/miniconda3/envs/py39/lib/python3.9/site-packages (from django==3.1.8) (0.4.1)
Installing collected packages: django
  Attempting uninstall: django
    Found existing installation: Django 3.2
    Uninstalling Django-3.2:
      Successfully uninstalled Django-3.2
Successfully installed django-3.1.8
Running test on 3.1.8
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
Running on Django 3.1.8
Process time taken: 0.798862333s
Real time taken: 0.7989063262939453s # <-------
.
----------------------------------------------------------------------
Ran 1 test in 0.912s

OK
Destroying test database for alias 'default'...
Installing Django 3.2
Collecting django==3.2
  Using cached Django-3.2-py3-none-any.whl (7.9 MB)
Requirement already satisfied: asgiref<4,>=3.3.2 in /home/phillip/miniconda3/envs/py39/lib/python3.9/site-packages (from django==3.2) (3.3.4)
Requirement already satisfied: pytz in /home/phillip/miniconda3/envs/py39/lib/python3.9/site-packages (from django==3.2) (2021.1)
Requirement already satisfied: sqlparse>=0.2.2 in /home/phillip/miniconda3/envs/py39/lib/python3.9/site-packages (from django==3.2) (0.4.1)
Installing collected packages: django
  Attempting uninstall: django
    Found existing installation: Django 3.1.8
    Uninstalling Django-3.1.8:
      Successfully uninstalled Django-3.1.8
Successfully installed django-3.2
Running test on 3.2
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
Running on Django 3.2
Process time taken: 2.72945918s
Real time taken: 2.7295141220092773s  # <-------
.
----------------------------------------------------------------------
Ran 1 test in 2.853s

OK
Destroying test database for alias 'default'...
```