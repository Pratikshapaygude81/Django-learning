# Django Authentication System
## Reference:-https://docs.djangoproject.com/en/6.1/topics/auth/default
## 1. Introduction

Django provides a built-in authentication system that handles both:

- **Authentication:** Verifies the identity of a user.
- **Authorization:** Determines what an authenticated user is allowed to access or perform.

Django provides authentication and authorization together as an authentication system.

## 2. User Objects

User objects are the core of Django's authentication system. They represent people interacting with a website.

Django uses one User class for all users. Superusers and staff users are also User objects with special attributes.

### Default User Attributes

- `username`
- `password`
- `email`
- `first_name`
- `last_name`

User objects can be used for restricting access, managing profiles and associating content with users.

## 3. Creating Users

Django provides the `create_user()` helper method to create a new user.

```python
from django.contrib.auth.models import User

user = User.objects.create_user(
    "john",
    "john@example.com",
    "johnpassword"
)
```

The user is automatically saved to the database.

You can update other attributes and save the changes:

```python
user.last_name = "Lennon"
user.save()
```

Users can also be created through the Django Admin interface.

## 4. Creating Superusers

A superuser has administrative privileges.

Create a superuser using:

```bash
python manage.py createsuperuser
```

Django asks for the username, email and password.

A superuser can access and manage the Django Admin interface.

## 5. Changing Passwords

Django does not store raw passwords in the database. It stores password hashes.

Therefore, we should not directly modify the password attribute.

### Using the Command Line

```bash
python manage.py changepassword username
```

### Using set_password()

```python
from django.contrib.auth.models import User

user = User.objects.get(username="john")
user.set_password("newpassword")
user.save()
```

Django also provides built-in views and forms for changing passwords.

**Important:** Changing a user's password invalidates their existing sessions, unless the session is appropriately updated.

## 6. Authenticating Users

Django provides the `authenticate()` function to verify user credentials.

```python
from django.contrib.auth import authenticate

user = authenticate(
    username="john",
    password="secret"
)

if user is not None:
    print("User authenticated successfully")
else:
    print("Invalid credentials")
```

### How authenticate() works

- Takes username and password as credentials in the default configuration.
- Checks credentials against configured authentication backends.
- Returns a User object if authentication succeeds.
- Returns `None` if authentication fails.

## 7. Permissions and Authorization

Django provides a built-in permissions system to assign permissions to individual users and groups.

The Django Admin uses four default permissions:

| Permission | Purpose |
|---|---|
| Add | Create new objects |
| Change | Modify existing objects |
| Delete | Delete objects |
| View | View objects |

### Checking Permissions

```python
user.has_perm('app.add_model')
user.has_perm('app.change_model')
user.has_perm('app.delete_model')
user.has_perm('app.view_model')
```

Replace `app` and `model` with the actual application label and model name.

### User Permissions

User objects have two many-to-many fields:

- `groups`
- `user_permissions`

These allow permissions to be assigned through groups or directly to users.

## 8. Default Permissions

When `django.contrib.auth` is included in `INSTALLED_APPS`, Django automatically creates four default permissions for each model:

- Add
- Change
- Delete
- View

These permissions are created when migrations are applied using:

```bash
python manage.py migrate
```

## 9. Groups

Groups provide a way to categorize users and assign permissions to multiple users.

A user can belong to multiple groups.

For example, in a hospital appointment system, groups could include:

- Patients
- Doctors
- Administrators

Users automatically receive the permissions assigned to their groups.

## 10. Authentication in Web Requests

Django uses sessions and middleware to connect authentication with HTTP requests.

Every request provides a `request.user` attribute.

It represents:

- A User object if the user is logged in.
- An AnonymousUser object if the user is not logged in.

### Checking Authentication

```python
if request.user.is_authenticated:
    print("User is logged in")
else:
    print("User is not logged in")
```

## 11. How to Log a User In

Django provides the `login()` function to log in an authenticated user.

```python
from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(
        request,
        username=username,
        password=password
    )

    if user is not None:
        login(request, user)
    else:
        print("Invalid credentials")
```

### Purpose of login()

- Takes an HTTP request and a User object.
- Stores the user's ID in the session.
- Maintains the user's login state across requests.

## 12. How to Log a User Out

Django provides the `logout()` function.

```python
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
```

When logout is called:

- The current session data is cleared.
- The user is logged out.
- Previous session data is removed.

## 13. Limiting Access to Logged-in Users

Django provides different ways to restrict access to views.

### Using is_authenticated

```python
if request.user.is_authenticated:
    # Allow access
    pass
else:
    # Restrict access
    pass
```

### Using login_required Decorator

```python
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    pass
```

If the user is not logged in, Django redirects them to the login page.

### Using LoginRequiredMixin

For class-based views, Django provides `LoginRequiredMixin`.

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class MyView(LoginRequiredMixin, View):
    pass
```

## 14. Limiting Access Based on Conditions

Django provides `user_passes_test()` to restrict access based on a custom condition.

```python
from django.contrib.auth.decorators import user_passes_test

def email_check(user):
    return user.email.endswith("@example.com")

@user_passes_test(email_check)
def my_view(request):
    pass
```

The view is accessible only when the test function returns `True`.

## 15. Permission Required Decorator

Django provides `permission_required()` to restrict access based on specific permissions.

```python
from django.contrib.auth.decorators import permission_required

@permission_required("appointments.add_appointment")
def my_view(request):
    pass
```

The user must have the specified permission to access the view.

For class-based views, Django provides `PermissionRequiredMixin`.

## 16. Authentication Views

Django provides built-in views for:

- Login
- Logout
- Password change
- Password reset

These views use built-in authentication forms.

### Including Authentication URLs

In the project's `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
]
```

This provides URL patterns such as:

| URL | Purpose |
|---|---|
| `accounts/login/` | User login |
| `accounts/logout/` | User logout |
| `accounts/password_change/` | Change password |
| `accounts/password_reset/` | Request password reset |
| `accounts/reset/<uidb64>/<token>/` | Confirm password reset |

Django does not provide default HTML templates for these authentication views. You must create the required templates.

## 17. Built-in Authentication Forms

Django provides several forms in `django.contrib.auth.forms`.

| Form | Purpose |
|---|---|
| `AuthenticationForm` | User login |
| `UserCreationForm` | User registration |
| `PasswordChangeForm` | Change password |
| `PasswordResetForm` | Request password reset |
| `SetPasswordForm` | Set a new password |
| `UserChangeForm` | Change user information and permissions |

These forms handle common authentication-related validation tasks.

## 18. Authentication Data in Templates

Django makes the currently logged-in user available in templates through the `user` variable when the authentication context processor is enabled.

Example:

```html
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
```

### Checking Permissions in Templates

Django provides the `perms` variable to check user permissions.

```html
{% if perms.app.add_model %}
    <p>You can add objects.</p>
{% endif %}
```

## 19. Managing Users in Django Admin

When `django.contrib.admin` and `django.contrib.auth` are installed, Django Admin provides an interface to:

- Create and delete users.
- Manage groups.
- Assign permissions.
- Change user information.
- Manage passwords.

User passwords are never displayed as plain text in the Admin interface.

---

## 20. Key Takeaways

1. Django provides a built-in authentication system.
2. User objects represent people interacting with the application.
3. `create_user()` creates new user accounts.
4. `createsuperuser` creates an administrator account.
5. `authenticate()` verifies user credentials.
6. `login()` starts a user session.
7. `logout()` clears the current session.
8. `login_required` restricts access to authenticated users.
9. Groups help manage permissions for multiple users.
10. Django provides built-in authentication views and forms.

## 21. Application in Hospital Appointment Management System

The authentication system can be used to manage different users:

| User | Functionality |
|---|---|
| Patient | Register, log in and manage appointments |
| Doctor | Log in and manage appointment availability |
| Admin | Manage users, doctors and appointments |

Authentication verifies the user's identity, while authorization controls which features the user can access.
