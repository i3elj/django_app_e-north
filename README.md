# Simple student registration app made in Django and PostgreSQL

### Usage:
- Change the following lines in your `django_app_e_north/settings.py`, so they match your configured database:
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

- Activate the virtual enviornment:
```bash
source env/bin/activate
```

- Run the application:
```bash
python3 manage.py runserver
```
