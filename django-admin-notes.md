# Django Admin
## Reference:-https://www.w3schools.com/django/django_admin.php
---

## 1. Introduction to Django Admin

Django Admin is a built-in administrative interface provided by Django. It allows developers to manage application data through a web-based interface without creating separate pages for every database operation.

It provides a CRUD interface for Django models.

**CRUD stands for:**
- **Create:** Add new records.
- **Read:** View existing records.
- **Update:** Modify existing records.
- **Delete:** Remove records.

Django Admin is automatically available when creating a Django project.

## 2. Getting Started with Django Admin

To access Django Admin:

1. Navigate to the project directory containing `manage.py`.
2. Start the development server.

```bash
python manage.py runserver
```

3. Open the following URL in your browser:

```text
http://127.0.0.1:8000/admin/
```

The Django Admin login page will appear.

## 3. URL Configuration

The Django Admin URL is configured in the project's main `urls.py` file.

Example:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('appointments.urls')),
    path('admin/', admin.site.urls),
]
```

**Explanation:**

- `django.contrib.admin`: Imports Django's built-in admin application.
- `admin.site.urls`: Provides the URL configuration for the admin interface.
- `path('admin/', admin.site.urls)`: Maps requests starting with `/admin/` to the Django Admin interface.

## 4. Creating a Superuser

To access the Django Admin panel, we need an administrator account.

Run:

```bash
python manage.py createsuperuser
```

Django asks for:
- Username
- Email address
- Password

After entering the required information, the superuser account is created.

A superuser has all permissions by default.

## 5. Registering Models in Django Admin

Django models must be registered to make them available in the Admin panel.

Open the `admin.py` file inside your application.

Example:

```python
from django.contrib import admin
from .models import Provider, Client, Appointment, RBAC

admin.site.register(Provider)
admin.site.register(Client)
admin.site.register(Appointment)
admin.site.register(RBAC)
```

**Explanation:**

- `admin.site.register()`: Registers a model with the Django Admin site.
- Registered models become available for management through the admin interface.

## 6. Managing Records Through Django Admin

After registering models, we can perform CRUD operations.

### Create
Add new records using the Add button.

### Read
View the list of existing records.

### Update
Open an existing record, modify its fields and save the changes.

### Delete
Select a record and delete it from the database.

## 7. ModelAdmin Class

Django provides the `ModelAdmin` class to customize how models are displayed and managed in the admin interface.

Example:

```python
@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('doctor_name', 'specialization', 'email')
    search_fields = ('doctor_name', 'specialization')
```

**Important attributes:**

- `list_display`: Specifies which fields appear in the model list.
- `search_fields`: Adds a search option for selected fields.
- `list_filter`: Adds filters to the admin list page.
- `ordering`: Defines the default ordering of records.
- `list_per_page`: Controls the number of records displayed per page.

## 8. Django Admin Features

Some important features include:

1. Automatic CRUD interface.
2. Model and database record management.
3. Search functionality.
4. Filtering records.
5. User authentication.
6. Permission management.
7. Customizable model display.
8. Pagination for large record lists.

## 9. Django Admin in Hospital Appointment Management System

In the Hospital Appointment Management project, Django Admin can be used to manage the following models:

| Model | Purpose |
|---|---|
| Provider | Manage doctor information |
| Client | Manage patient information |
| Appointment | Manage appointment records |
| RBAC | Manage role records |

The administrator can use the admin panel to add, view, update and delete records.

## 10. Advantages of Django Admin

- Reduces the need to build a separate management interface.
- Provides ready-to-use CRUD functionality.
- Supports authentication and permissions.
- Makes database management easier.
- Allows customization according to project requirements.
- Saves development time.

## 11. Important Django Admin Commands

| Command | Purpose |
|---|---|
| `python manage.py runserver` | Starts the development server |
| `python manage.py createsuperuser` | Creates an administrator account |
| `python manage.py changepassword username` | Changes a user's password |
| `python manage.py migrate` | Applies database migrations |

## 12. Conclusion

Django Admin is a built-in administrative interface that simplifies application data management. It provides CRUD operations, authentication, permissions, searching, filtering and customization features.

It is especially useful for managing application data during development and for building internal administrative tools.
