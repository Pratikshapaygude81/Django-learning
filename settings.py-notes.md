# Django Settings (`settings.py`)

## 1. Introduction

The `settings.py` file is the main configuration file of a Django project. It is often called the **heart of a Django project** because it controls how the project works.

It contains configuration related to:
- Database connection
- Installed applications
- Middleware
- URL configuration
- Templates
- Static files
- Security settings
- Language and time zone

## 2. Import os and Path

```python
import os
from pathlib import Path
```

- `os`: Provides functions to interact with the operating system and environment variables.
- `Path`: Used to work with file and directory paths.

These imports help Django manage project paths across different operating systems.

## 3. Base Directory (`BASE_DIR`)

```python
BASE_DIR = Path(__file__).resolve().parent.parent
```

- `BASE_DIR` represents the root directory of the Django project.
- `__file__` refers to the current file (`settings.py`).
- `resolve()` returns the absolute path.
- `parent.parent` moves two directory levels up.

**Purpose:** It provides a common reference point for locating project files and directories.

## 4. Secret Key (`SECRET_KEY`)

```python
SECRET_KEY = 'your-secret-key-here'
```

- A unique and secret key used by Django for cryptographic signing.
- It helps protect important Django operations.
- It should be kept confidential.

**Important:** Never expose the secret key publicly or commit production secrets to GitHub.

Environment variables can be used to manage sensitive values.

## 5. Debug Mode (`DEBUG`)

```python
DEBUG = True
```

- Controls whether Django displays detailed error information.
- `True`: Displays detailed error pages during development.
- `False`: Hides detailed debug information in production.

**Important:** Always set `DEBUG = False` in production.

## 6. Allowed Hosts (`ALLOWED_HOSTS`)

```python
ALLOWED_HOSTS = []
```

- Defines the hostnames or domain names that can serve the Django application.
- Helps protect the application against Host header attacks.

Example:

```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```

For production, add your actual domain name.

## 7. Installed Applications (`INSTALLED_APPS`)

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

- Contains the list of applications enabled in the Django project.
- Django provides several built-in applications.
- Custom applications must also be registered here.

Example:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]
```

**Purpose:** It tells Django which applications are part of the project.

## 8. Middleware (`MIDDLEWARE`)

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

- Middleware is a framework of hooks that processes HTTP requests and responses.
- It operates between the incoming request and the outgoing response.
- It provides functionality such as security, sessions, authentication and CSRF protection.

**Purpose:** It allows Django to process requests and responses globally.

## 9. URL Configuration (`ROOT_URLCONF`)

```python
ROOT_URLCONF = 'myproject.urls'
```

- Specifies the Python module containing the project's main URL patterns.
- Usually points to the project's `urls.py` file.
- Django uses these URL patterns to determine which view should handle a request.

## 10. Templates (`TEMPLATES`)

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

This setting configures the Django template engine.

Important properties:

- `BACKEND`: Specifies the template engine.
- `DIRS`: Specifies additional directories where Django searches for templates.
- `APP_DIRS`: Allows Django to search for templates inside installed applications.
- `OPTIONS`: Contains additional template engine configuration.
- `context_processors`: Makes certain data available in templates.

Example:

```python
'DIRS': [BASE_DIR / 'templates'],
```

## 11. WSGI Application (`WSGI_APPLICATION`)

```python
WSGI_APPLICATION = 'myproject.wsgi.application'
```

- Specifies the WSGI application used by the project.
- WSGI stands for Web Server Gateway Interface.
- It provides a standard interface between Python web applications and compatible web servers.

## 12. Database Configuration (`DATABASES`)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

- Configures the database used by the Django project.
- Django uses SQLite by default.
- The `default` key represents the primary database configuration.

Important properties:

- `ENGINE`: Specifies the database backend.
- `NAME`: Specifies the database name or database file path.
- `USER`: Database username.
- `PASSWORD`: Database password.
- `HOST`: Database server address.
- `PORT`: Database server port.

Django supports databases such as SQLite, PostgreSQL and MySQL through their respective backends.

## 13. Password Validation (`AUTH_PASSWORD_VALIDATORS`)

```python
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
```

- Configures password validation rules.
- Helps ensure users create passwords that meet specified security requirements.

Built-in validators:

1. `UserAttributeSimilarityValidator`: Checks whether the password is too similar to user information.
2. `MinimumLengthValidator`: Checks the minimum password length.
3. `CommonPasswordValidator`: Prevents commonly used passwords.
4. `NumericPasswordValidator`: Prevents passwords containing only numbers.

## 14. Internationalization and Time Zone

```python
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
```

These settings control the language and time-related behavior of the application.

- `LANGUAGE_CODE`: Defines the default language.
- `TIME_ZONE`: Defines the project's default time zone.
- `USE_I18N`: Enables Django's internationalization system.
- `USE_TZ`: Enables time-zone-aware date and time handling.

## 15. Static Files (`STATIC_URL`)

```python
STATIC_URL = 'static/'
```

- Defines the URL used to access static files.
- Static files include CSS, JavaScript and images.

Additional settings:

```python
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

- `STATICFILES_DIRS`: Specifies additional directories where Django searches for static files.
- `STATIC_ROOT`: Specifies the directory where static files are collected for deployment.

## 16. Default Auto Field (`DEFAULT_AUTO_FIELD`)

```python
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

- Defines the default primary key field type for automatically created model IDs.
- `BigAutoField` is an integer field that automatically increments.
- It is commonly used for automatically generated primary keys.

## Summary

The `settings.py` file manages the overall configuration of a Django project.

| Setting | Purpose |
|---|---|
| `BASE_DIR` | Defines the project root directory |
| `SECRET_KEY` | Provides cryptographic signing |
| `DEBUG` | Controls debug mode |
| `ALLOWED_HOSTS` | Defines permitted hostnames |
| `INSTALLED_APPS` | Registers Django applications |
| `MIDDLEWARE` | Processes requests and responses |
| `ROOT_URLCONF` | Defines the main URL configuration |
| `TEMPLATES` | Configures the template engine |
| `WSGI_APPLICATION` | Defines the WSGI application |
| `DATABASES` | Configures database connections |
| `AUTH_PASSWORD_VALIDATORS` | Defines password validation rules |
| `LANGUAGE_CODE` | Sets the default language |
| `TIME_ZONE` | Sets the default time zone |
| `STATIC_URL` | Defines the static files URL |
| `DEFAULT_AUTO_FIELD` | Defines the default automatic primary key type |

**Important Points:**
- `settings.py` is responsible for project configuration.
- Custom applications must be added to `INSTALLED_APPS`.
- Database configuration is managed through `DATABASES`.
- Middleware handles request and response processing.
- Sensitive information such as `SECRET_KEY` and database credentials must be protected.
- `DEBUG` should be disabled in production.
