# Django REST Framework (DRF)
## Refernece:-https://www.django-rest-framework.org/
## 1. Introduction

Django REST Framework (DRF) is a powerful and flexible toolkit used to build Web APIs using Django.

An API (Application Programming Interface) allows two applications to communicate and exchange data.

DRF makes it easier to create APIs that allow frontend applications, mobile applications, and other services to communicate with a Django backend.

### Why use Django REST Framework?

- **Browsable API:** Provides a web interface to test APIs directly from the browser.
- **Authentication:** Supports authentication policies, including OAuth1 and OAuth2 integrations.
- **Serialization:** Converts Django model objects into JSON and converts incoming data into Python objects.
- **Flexible Views:** Supports function-based views, class-based views, generic views, and ViewSets.
- **Documentation:** Provides extensive documentation and community support.
- **Widely Used:** Used by companies such as Mozilla, Red Hat, Heroku, and Eventbrite.

---

## 2. Requirements

Django REST Framework requires:

- Django
- Python

Always check the official DRF documentation for currently supported Django and Python versions.

### Optional Packages

| Package | Purpose |
|---|---|
| PyYAML | Schema generation support |
| uritemplate | URI template support |
| Markdown | Markdown support in the browsable API |
| Pygments | Syntax highlighting |
| django-filter | Filtering API results |
| django-guardian | Object-level permissions |

---

## 3. Installation

Install Django REST Framework using pip:

```bash
pip install djangorestframework
```

Optional packages can also be installed:

```bash
pip install markdown
pip install django-filter
```

### Add DRF to INSTALLED_APPS

Open `settings.py` and add `rest_framework` to `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    # Existing Django apps
    'rest_framework',
]
```

This tells Django that the REST Framework application is being used in the project.

---

## 4. Configure API Authentication URLs

To use the browsable API's login and logout functionality, add the following to the project's root `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
]
```

This provides login and logout URLs for the browsable API.

---

## 5. REST Framework Configuration

DRF provides a configuration dictionary called `REST_FRAMEWORK`.

It is used to define global settings for APIs in `settings.py`.

Example:

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
```

### Understanding DjangoModelPermissionsOrAnonReadOnly

- Authenticated users can access data according to their Django model permissions.
- Unauthenticated users can access read-only operations.
- Unauthenticated users cannot perform write operations.

---

## 6. Creating an API Using DRF

Let's understand a simple example of creating a read-write API for Django users.

### Step 1: Import Required Modules

```python
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
```

### Step 2: Create a Serializer

Serializers convert Django model objects into API-friendly representations.

```python
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
```

**Explanation:**

- `HyperlinkedModelSerializer` represents model relationships using hyperlinks.
- `model = User` specifies the Django User model.
- `fields` specifies which fields should be included in the API response.

### Step 3: Create a ViewSet

ViewSets define the behavior of API endpoints.

```python
class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
```

**Explanation:**

- `ModelViewSet` provides common CRUD operations.
- `queryset` retrieves all user records.
- `serializer_class` specifies the serializer used to convert data.

It automatically provides operations such as:

- GET – Retrieve users.
- POST – Create a user.
- PUT – Update a user.
- PATCH – Partially update a user.
- DELETE – Delete a user.

### Step 4: Create a Router

Routers automatically generate URL patterns for ViewSets.

```python
router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
```

**Explanation:**

- `DefaultRouter()` creates automatic URL routing.
- `register()` connects the users endpoint with UserViewSet.

### Step 5: Configure URLs

Add the router URLs to the project's root `urls.py`.

```python
urlpatterns = [
    path('', include(router.urls)),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
]
```

---

## 7. Run the Server

Start the Django development server:

```bash
python manage.py runserver
```

Open the following URL in your browser:

```text
http://127.0.0.1:8000/
```

You can now access the Users API through the Django REST Framework browsable API.

The login option in the top-right corner allows authorized users to log in and perform permitted operations.

---

## 8. Important DRF Components

| Component | Purpose |
|---|---|
| Serializer | Converts Python objects into API data and validates incoming data |
| API Views | Handle API requests and responses |
| ViewSets | Group related API operations |
| Routers | Automatically generate URL patterns |
| Authentication | Identifies users |
| Permissions | Controls what users are allowed to do |

---

## 9. Important Points to Remember

1. Django REST Framework is used to build Web APIs.
2. Install DRF using `pip install djangorestframework`.
3. Add `rest_framework` to `INSTALLED_APPS`.
4. Serializers handle data conversion and validation.
5. ViewSets provide CRUD operations.
6. Routers automatically generate URLs.
7. Browsable API allows developers to test APIs through a browser.
8. Authentication identifies users, while permissions control access.

---

## 10. Official Resources

- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [Quickstart Guide](https://www.django-rest-framework.org/tutorial/quickstart/)
- [Serializers](https://www.django-rest-framework.org/api-guide/serializers/)
- [Authentication](https://www.django-rest-framework.org/api-guide/authentication/)
- [ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/)
- [Routers](https://www.django-rest-framework.org/api-guide/routers/)
