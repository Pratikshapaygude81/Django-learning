# Django Authentication and Authorization
## Reference:-
- Django Official Documentation – User Authentication
- Django Official Documentation – Permissions and Authorization
- Django Official Documentation – Sessions
## 1. Introduction

Authentication and Authorization are two important security concepts in Django.

They help protect an application by identifying users and controlling what they are allowed to do.

### Authentication

Authentication is the process of verifying the identity of a user.

It answers the question:

**Who are you?**

Example:
- A patient enters their username and password.
- Django checks whether the credentials are correct.
- If valid, the user is logged in.

### Authorization

Authorization is the process of deciding what an authenticated user is allowed to access or perform.

It answers the question:

**What are you allowed to do?**

Example:
- A patient can book an appointment.
- A doctor can view their appointments.
- An admin can manage doctors, patients, and appointments.

### Difference Between Authentication and Authorization

| Authentication | Authorization |
|---|---|
| Verifies user identity | Checks user permissions |
| Happens before authorization | Happens after authentication |
| Checks username and password | Checks access rights |
| Answers "Who are you?" | Answers "What can you do?" |
| Example: User login | Example: Admin access |

---

## 2. Django Authentication System

Django provides a built-in authentication system through `django.contrib.auth`.

It handles:
- User registration
- User login
- User logout
- Password hashing
- Password validation
- User sessions
- Groups and permissions

Django provides a built-in User model to store user information.

### Important User Model Fields

| Field | Description |
|---|---|
| username | Unique username |
| password | Hashed password |
| email | User email address |
| first_name | User's first name |
| last_name | User's last name |
| is_active | Checks whether the user account is active |
| is_staff | Determines whether the user can access Django Admin |
| is_superuser | Gives all permissions |

---

## 3. Creating a User

Django provides `create_user()` to create a user securely.

```python
from django.contrib.auth.models import User

user = User.objects.create_user(
    username='pratiksha',
    email='pratiksha@example.com',
    password='mypassword123'
)
```

**Explanation:**
- `create_user()` creates a new user.
- It automatically hashes the password before storing it.
- Passwords are not stored as plain text.

---

## 4. User Login (Authentication)

Django provides the `authenticate()` and `login()` functions.

### authenticate()

Checks whether the provided username and password are valid.

### login()

Logs in the authenticated user and creates a session.

Example:

```python
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def user_login(request):

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(
        request,
        username=username,
        password=password
    )

    if user is not None:
        login(request, user)
        return redirect('home')

    return redirect('login')
```

**Explanation:**

1. Get username and password from the request.
2. `authenticate()` verifies the credentials.
3. If valid, `login()` creates an authenticated session.
4. If invalid, the login is rejected.

---

## 5. User Logout

Django provides the `logout()` function to log out a user.

```python
from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):

    logout(request)

    return redirect('login')
```

**Explanation:**

- `logout()` clears the current user's session.
- The user is logged out of the application.

---

## 6. Django Sessions

A session allows Django to remember a logged-in user across multiple requests.

HTTP is stateless, meaning each request is independent.

Sessions help maintain user login information between requests.

### How Sessions Work

1. User logs in successfully.
2. Django creates a session.
3. Django sends a session cookie to the browser.
4. The browser sends that cookie with subsequent requests.
5. Django uses the session information to identify the logged-in user.

Example:

```python
request.session['username'] = 'pratiksha'
```

To retrieve session data:

```python
username = request.session.get('username')
```

To delete session data:

```python
del request.session['username']
```

---

## 7. Django Authorization System

Django provides an authorization system using Groups and Permissions.

It helps control which users can perform specific actions.

### Permissions

Permissions define what actions a user can perform on a model.

Django automatically creates four default model permissions:

| Permission | Purpose |
|---|---|
| add | Create a new record |
| view | View records |
| change | Update records |
| delete | Delete records |

For example, for a Doctor model:
- Add doctor
- View doctor
- Change doctor
- Delete doctor

### Checking Permissions

Django provides `has_perm()` to check whether a user has a specific permission.

```python
if request.user.has_perm('hospital.view_doctor'):
    print("User can view doctors")
```

Here:
- `hospital` is the app label.
- `view_doctor` is the permission name.

---

## 8. Django Groups

Groups allow administrators to assign permissions to multiple users together.

Instead of assigning permissions individually, users can be added to groups.

Example:

Hospital application groups:

| Group | Permissions |
|---|---|
| Patient | View doctors, book appointments |
| Doctor | View appointments |
| Admin | Manage doctors, patients, and appointments |

### Creating a Group

```python
from django.contrib.auth.models import Group

patient_group = Group.objects.create(name='Patient')
```

### Adding a User to a Group

```python
from django.contrib.auth.models import User, Group

user = User.objects.get(username='pratiksha')

group = Group.objects.get(name='Patient')

user.groups.add(group)
```

### Checking Group Membership

```python
if request.user.groups.filter(name='Patient').exists():
    print("User is a patient")
```

---

## 9. Django Decorators for Authorization

Decorators help restrict access to specific views.

### login_required

Ensures that only logged-in users can access a view.

```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
```

If a user is not logged in, Django redirects them to the login page.

### permission_required

Checks whether a user has a particular permission.

```python
from django.contrib.auth.decorators import permission_required

@permission_required('hospital.view_doctor')
def doctor_list(request):
    return render(request, 'doctors.html')
```

Only users with the required permission can access this view.

### user_passes_test

Allows access based on a custom condition.

```python
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
```

Only superusers can access this view.

---

## 10. Django Admin and User Roles

Django provides three commonly used user account types:

| User Type | Description |
|---|---|
| Normal User | Regular application user |
| Staff User | Can access Django Admin if granted appropriate permissions |
| Superuser | Has all permissions |

**Important:**
- `is_staff` controls access to the Django Admin site.
- `is_superuser` grants all permissions.
- `is_active` determines whether an account is active.

---

## 11. Authentication vs Authorization in a Hospital Project

Consider a Hospital Appointment Management System.

### Authentication Flow

1. Patient registers.
2. Patient enters username and password.
3. Django verifies the credentials.
4. Patient successfully logs in.

### Authorization Flow

1. Django identifies the logged-in user.
2. Django checks the user's role and permissions.
3. Patient can book appointments.
4. Doctor can view their assigned appointments.
5. Admin can manage the hospital system.

---

## 12. Important Django Authentication Functions

| Function | Purpose |
|---|---|
| `create_user()` | Creates a new user |
| `authenticate()` | Verifies user credentials |
| `login()` | Logs in a user |
| `logout()` | Logs out a user |
| `get_user_model()` | Gets the active User model |
| `check_password()` | Checks a password |
| `set_password()` | Sets a password securely |
| `has_perm()` | Checks a user's permission |
| `has_perms()` | Checks multiple permissions |

---

## 13. Important Security Practices

1. Never store passwords in plain text.
2. Use Django's built-in password hashing.
3. Validate user input.
4. Protect private views using authentication and authorization.
5. Use CSRF protection for form submissions.
6. Assign only the permissions users need.
7. Do not expose sensitive user information through APIs.
8. Use HTTPS in production.
9. Keep Django and its dependencies updated.

---

## 14. Summary

- Authentication verifies the identity of a user.
- Authorization determines what a user is allowed to do.
- Django provides built-in authentication through `django.contrib.auth`.
- `authenticate()` verifies credentials.
- `login()` creates an authenticated session.
- `logout()` ends the session.
- Groups help manage users with similar permissions.
- Permissions control access to specific operations.
- Decorators such as `login_required` and `permission_required` protect views.

**Remember: Authentication = Who are you?**

**Authorization = What are you allowed to do?**
