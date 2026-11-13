# Django – Create Project and Application
## Referenece:- https://www.w3schools.com/django/django_create_project.php
## 1. Create Your First Django Project

After installing Django and setting up a virtual environment, the next step is to create a Django project.

A Django project is the main container of a web application. It contains configuration files and settings required to run the entire website.

### Step 1: Navigate to the Project Location

Open Command Prompt or PowerShell and navigate to the directory where you want to create your Django project.

For example:

```powershell
cd myworld
```

Make sure your virtual environment is activated before creating the project.

### Step 2: Create a Django Project

Execute the following command:

```bash
django-admin startproject my_tennis_club
```

Here:
- `django-admin` is Django's command-line utility.
- `startproject` is the command used to create a new Django project.
- `my_tennis_club` is the name of the project.

Django creates a folder named `my_tennis_club` with the following structure:

```text
my_tennis_club/
│
├── manage.py
│
└── my_tennis_club/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

### Step 3: Understand the Project Files

| File | Purpose |
|---|---|
| `manage.py` | Command-line utility used to perform Django project management tasks, such as running the server and creating applications. |
| `__init__.py` | Marks the directory as a Python package. |
| `asgi.py` | Provides the ASGI application entry point for asynchronous web servers. |
| `settings.py` | Contains project configuration such as installed apps, database settings, middleware, templates, and other settings. |
| `urls.py` | Defines the URL patterns used to connect incoming requests to the appropriate views. |
| `wsgi.py` | Provides the WSGI application entry point for traditional synchronous web servers. |

## 2. Run the Django Project

After creating the project, we can start the Django development server to check whether the project is working.

### Step 1: Navigate to the Project Directory

Move into the directory containing the `manage.py` file:

```powershell
cd my_tennis_club
```

### Step 2: Start the Development Server

Execute:

```bash
python manage.py runserver
```

Django performs system checks and starts the development server.

Example output:

```text
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

The exact output and Django version may differ depending on your installation.

### Step 3: Open the Project in a Browser

Open your browser and enter:

```text
http://127.0.0.1:8000/
```

You should see the default Django welcome page.

This confirms that the Django development server is running successfully.

### Important: Database Migrations

When you start a new Django project, you may see a message about unapplied migrations.

Django includes built-in applications such as authentication, admin, content types, and sessions. These applications require database tables.

To apply the initial migrations, stop the server if it is running and execute:

```bash
python manage.py migrate
```

Django creates the required database tables.

After the migration completes, start the server again:

```bash
python manage.py runserver
```

To stop the development server, press `Ctrl + C` in the terminal.

---

## 3. Create a Django Application

A Django project can contain one or more applications.

A Django app is a component of a project that handles a particular functionality or feature.

For example, a hospital management project may contain different apps:

- `patients` – manages patient information.
- `doctors` – manages doctor information.
- `appointments` – manages appointment booking.
- `accounts` – manages user registration and login.

### Step 1: Navigate to the Project Directory

Make sure you are inside the directory containing `manage.py`.

### Step 2: Create an Application

Execute the following command:

```bash
python manage.py startapp patients
```

Here:
- `python manage.py` runs Django's project management utility.
- `startapp` creates a new Django application.
- `patients` is the name of the application.

### Step 3: Understand the App Structure

After creating the application, Django generates the following structure:

```text
patients/
│
├── migrations/
│   └── __init__.py
│
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

### Step 4: Understand the App Files

| File or Folder | Purpose |
|---|---|
| `migrations/` | Stores database migration files that record changes to models. |
| `__init__.py` | Marks the directory as a Python package. |
| `admin.py` | Used to register models with Django's admin interface. |
| `apps.py` | Contains the configuration class for the application. |
| `models.py` | Defines the application's data models and database structure. |
| `tests.py` | Contains test cases used to test application functionality. |
| `views.py` | Contains view functions or classes that process requests and return responses. |

## 4. Register the Application in the Project

After creating an application, it should be registered in the project's `INSTALLED_APPS` setting.

### Step 1: Open `settings.py`

Navigate to the inner project folder and open:

```text
my_tennis_club/settings.py
```

### Step 2: Find `INSTALLED_APPS`

Inside `settings.py`, locate the `INSTALLED_APPS` list.

It contains Django's default applications.

### Step 3: Add Your Application

Add the application name to the list:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'patients',
]
```

Now Django knows that the `patients` application is part of the project.

**Note:** The application must be registered before Django includes its models, templates, and other application-specific functionality in the project.

---

## 5. Difference Between Django Project and Django App

A Django project and a Django app are related, but they serve different purposes.

A project represents the complete website or system, whereas an app represents a specific functionality within that project.

| Django Project | Django App |
|---|---|
| Represents the complete web application or website. | Represents a specific feature or functionality. |
| Contains project-level configuration. | Contains feature-specific code. |
| Created using `django-admin startproject`. | Created using `python manage.py startapp`. |
| Contains files such as `settings.py`, `urls.py`, `asgi.py`, and `wsgi.py`. | Contains files such as `models.py`, `views.py`, `admin.py`, and `apps.py`. |
| A project can contain multiple apps. | An app can be included in a project. |
| Manages the overall application configuration. | Handles a particular part of the application's functionality. |

### Real-World Example: Hospital Management System

Consider a Hospital Management System.

The complete system is the Django project, and its individual modules can be created as separate Django apps.

```text
hospital_management/
│
├── manage.py
│
├── hospital_management/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── patients/
│   ├── models.py
│   ├── views.py
│   └── admin.py
│
├── doctors/
│   ├── models.py
│   ├── views.py
│   └── admin.py
│
├── appointments/
│   ├── models.py
│   ├── views.py
│   └── admin.py
│
└── accounts/
    ├── models.py
    ├── views.py
    └── admin.py
```

In this example:

- `hospital_management` is the main Django project.
- `patients` manages patient-related functionality.
- `doctors` manages doctor-related functionality.
- `appointments` handles appointment booking.
- `accounts` manages user-related functionality.

All these apps work together as part of one Django project.

---

## 6. Common Django Commands

| Purpose | Command |
|---|---|
| Create a Django project | `django-admin startproject project_name` |
| Create a Django app | `python manage.py startapp app_name` |
| Start the development server | `python manage.py runserver` |
| Apply database migrations | `python manage.py migrate` |
| Create migration files | `python manage.py makemigrations` |
| Check Django version | `python -m django --version` |
| Display available management commands | `python manage.py help` |

## 7. Important Points to Remember

- A Django project is the main structure of a website or system.
- A Django app is responsible for a specific functionality.
- One Django project can contain multiple apps.
- Use `startproject` to create a project.
- Use `startapp` to create an application.
- The `manage.py` file is used to execute Django management commands.
- Register newly created apps inside `INSTALLED_APPS`.
- Use `runserver` to start the development server.
- Use `migrate` to apply database migrations.

## Official Documentation

- [Django – Writing your first Django project](https://docs.djangoproject.com/en/6.1/intro/tutorial01/)
- [Django – Applications](https://docs.djangoproject.com/en/6.1/ref/applications/)
- [Django – django-admin and manage.py](https://docs.djangoproject.com/en/6.1/ref/django-admin/)
- [Django – Settings reference](https://docs.djangoproject.com/en/6.1/ref/settings/)
