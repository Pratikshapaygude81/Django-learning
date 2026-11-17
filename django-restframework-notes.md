# Django REST Framework – ViewSets

## References

- [Django REST Framework – ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/)
- [Django REST Framework – Routers](https://www.django-rest-framework.org/api-guide/routers/)
- [Django REST Framework – Serializers](https://www.django-rest-framework.org/api-guide/serializers/)
- [Django REST Framework – Generic Views](https://www.django-rest-framework.org/api-guide/generic-views/)

---

## 1. Introduction to ViewSets

A ViewSet is a class provided by Django REST Framework that groups related API operations into a single class.

It allows us to handle multiple HTTP methods such as GET, POST, PUT, PATCH, and DELETE without writing separate views for each operation.

### Why do we use ViewSets?

Normally, when creating APIs using function-based views, we need to write separate functions for different operations.

For example:

- Get all doctors.
- Create a new doctor.
- Update doctor details.
- Delete a doctor.

Using ViewSets, we can handle these operations in one class.

### Example

```python
from rest_framework import viewsets

class DoctorViewSet(viewsets.ViewSet):

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
```

Here, all doctor-related API operations are grouped inside `DoctorViewSet`.

---

## 2. Understanding ViewSet Actions

ViewSets provide different actions for handling API requests.

| Action | HTTP Method | Purpose |
|---|---|---|
| list() | GET | Retrieve all records |
| create() | POST | Create a new record |
| retrieve() | GET | Retrieve a single record |
| update() | PUT | Update all fields |
| partial_update() | PATCH | Update selected fields |
| destroy() | DELETE | Delete a record |

### Explanation

**1. list()**

Retrieves all records from the database.

Example:

```text
GET /api/doctors/
```

**2. create()**

Creates a new record.

Example:

```text
POST /api/doctors/
```

**3. retrieve()**

Retrieves a particular record using its ID.

Example:

```text
GET /api/doctors/1/
```

**4. update()**

Updates all fields of an existing record.

Example:

```text
PUT /api/doctors/1/
```

**5. partial_update()**

Updates only selected fields of an existing record.

Example:

```text
PATCH /api/doctors/1/
```

**6. destroy()**

Deletes a particular record.

Example:

```text
DELETE /api/doctors/1/
```

---

## 3. Types of ViewSets in Django REST Framework

DRF provides different types of ViewSets.

### 1. ViewSet

`ViewSet` provides action methods such as `list()`, `create()`, `retrieve()`, `update()`, and `destroy()`.

However, we need to write the implementation of these methods ourselves.

Example:

```python
from rest_framework import viewsets
from rest_framework.response import Response

class DoctorViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response({"message": "List of doctors"})

    def create(self, request):
        return Response({"message": "Doctor created"})
```

**Important:** ViewSet provides flexibility, but we must implement the required database operations ourselves.

### 2. ModelViewSet

`ModelViewSet` provides complete CRUD functionality automatically using a queryset and serializer.

It is commonly used when building APIs for Django models.

Example:

```python
from rest_framework import viewsets
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):

    queryset = Doctor.objects.all()

    serializer_class = DoctorSerializer
```

**Explanation:**

- `ModelViewSet` provides all standard CRUD actions.
- `queryset` defines which database records the API can access.
- `serializer_class` defines how data is converted and validated.

We do not need to write separate functions for GET, POST, PUT, PATCH, and DELETE.

### 3. ReadOnlyModelViewSet

`ReadOnlyModelViewSet` provides only read operations.

It supports:

- `list()` – Retrieve all records.
- `retrieve()` – Retrieve a single record.

Example:

```python
from rest_framework import viewsets
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Doctor.objects.all()

    serializer_class = DoctorSerializer
```

This API allows users to view doctor details but does not allow them to create, update, or delete records through this ViewSet.

---

## 4. Difference Between ViewSet, ModelViewSet and ReadOnlyModelViewSet

| Feature | ViewSet | ModelViewSet | ReadOnlyModelViewSet |
|---|---|---|---|
| List records | Yes, implement yourself | Automatic | Automatic |
| Create records | Yes, implement yourself | Automatic | No |
| Retrieve record | Yes, implement yourself | Automatic | Automatic |
| Update record | Yes, implement yourself | Automatic | No |
| Partial update | Yes, implement yourself | Automatic | No |
| Delete record | Yes, implement yourself | Automatic | No |
| Main purpose | Custom API logic | Complete CRUD API | Read-only API |

---

## 5. Creating a ViewSet Step by Step

Let's create a Doctor API for the Hospital Appointment Management System.

### Step 1: Create a Model

Inside `models.py`:

```python
from django.db import models

class Doctor(models.Model):

    name = models.CharField(max_length=100)

    specialization = models.CharField(max_length=100)

    experience = models.IntegerField()

    def __str__(self):
        return self.name
```

### Step 2: Create a Serializer

Create a file named `serializers.py` inside your app.

```python
from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'
```

**Explanation:**

- `ModelSerializer` automatically generates serializer fields from the model.
- `model = Doctor` specifies the model.
- `fields = '__all__'` includes all model fields.

### Step 3: Create a ModelViewSet

Inside `views.py`:

```python
from rest_framework import viewsets
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):

    queryset = Doctor.objects.all()

    serializer_class = DoctorSerializer
```

This creates a complete CRUD API for doctors.

### Step 4: Configure URLs Using Router

Create or open your app's `urls.py`.

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet

router = DefaultRouter()

router.register('doctors', DoctorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

**What is a Router?**

A Router automatically generates URL patterns for ViewSets.

Instead of manually defining separate URLs for every CRUD operation, we register the ViewSet with a router.

### Step 5: Include App URLs in Project URLs

Inside the main project's `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    path('api/', include('your_app_name.urls')),
]
```

Replace `your_app_name` with your actual app name.

---

## 6. API Endpoints Generated by the Router

After registering DoctorViewSet, the router automatically generates the following endpoints:

| HTTP Method | URL | Action |
|---|---|---|
| GET | `/api/doctors/` | List doctors |
| POST | `/api/doctors/` | Create doctor |
| GET | `/api/doctors/1/` | Retrieve doctor |
| PUT | `/api/doctors/1/` | Update doctor |
| PATCH | `/api/doctors/1/` | Partially update doctor |
| DELETE | `/api/doctors/1/` | Delete doctor |

The ID `1` represents a particular doctor's primary key.

---

## 7. What is a Router in DRF?

A Router automatically creates URL patterns for ViewSets.

DRF provides two commonly used routers:

### DefaultRouter

- Automatically generates URL patterns.
- Provides a browsable API root page.
- Supports registered ViewSets.

Example:

```python
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('doctors', DoctorViewSet)
```

### SimpleRouter

- Automatically generates URL patterns.
- Does not provide the API root view.

Example:

```python
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('doctors', DoctorViewSet)
```

---

## 8. Custom Actions in ViewSets

Sometimes we need additional API operations that are not part of the standard CRUD functionality.

For example, we want an API to display only active doctors.

DRF provides the `@action` decorator to create custom ViewSet actions.

Example:

```python
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

class DoctorViewSet(viewsets.ModelViewSet):

    queryset = Doctor.objects.all()

    serializer_class = DoctorSerializer

    @action(detail=False, methods=['get'])
    def active_doctors(self, request):

        doctors = Doctor.objects.filter(is_active=True)

        serializer = self.get_serializer(doctors, many=True)

        return Response(serializer.data)
```

### Explanation

- `@action` creates a custom API endpoint.
- `detail=False` means the action applies to the collection rather than one specific doctor.
- `methods=['get']` allows GET requests.
- `filter(is_active=True)` retrieves active doctors.

Generated endpoint:

```text
GET /api/doctors/active_doctors/
```

For an action related to one particular doctor, we can use `detail=True`.

---

## 9. Advantages of ViewSets

1. **Code Reusability:** Related API operations are grouped in one class.
2. **Less Code:** Reduces repetitive code.
3. **Automatic CRUD:** ModelViewSet provides standard CRUD operations.
4. **Easy Routing:** Routers automatically generate URL patterns.
5. **Maintainability:** Makes API code easier to organize and maintain.
6. **Customization:** Supports custom actions and overridden methods.
7. **Consistency:** Provides a standard structure for API development.

---

## 10. ViewSets vs APIView

| Feature | APIView | ViewSet |
|---|---|---|
| Structure | Uses HTTP method handlers | Uses action methods |
| Methods | get(), post(), put(), patch(), delete() | list(), create(), retrieve(), update(), destroy() |
| Routing | Usually define URLs manually | Can use routers |
| CRUD | Implement operations yourself | ModelViewSet provides standard CRUD |
| Flexibility | High | High |

### APIView Example

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class DoctorAPIView(APIView):

    def get(self, request):
        return Response({"message": "Get doctors"})

    def post(self, request):
        return Response({"message": "Create doctor"})
```

### ViewSet Example

```python
from rest_framework import viewsets
from rest_framework.response import Response

class DoctorViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response({"message": "Get doctors"})

    def create(self, request):
        return Response({"message": "Create doctor"})
```

The main difference is that APIView uses HTTP method handlers, while ViewSets organize functionality around resource-related actions.

---

## 11. Important Points to Remember

1. ViewSets group related API operations into one class.
2. ViewSets are provided by Django REST Framework.
3. ModelViewSet provides complete CRUD operations.
4. ReadOnlyModelViewSet provides only GET operations.
5. ViewSet requires us to implement the required actions.
6. Routers automatically generate URL patterns for ViewSets.
7. `@action` is used to create custom API endpoints.
8. `queryset` defines the records available to the ViewSet.
9. `serializer_class` defines the serializer used for data conversion and validation.

---

## 12. Conclusion

ViewSets make API development easier by grouping related operations into a single class.

ModelViewSet is especially useful when creating CRUD APIs for Django models.

Routers automatically generate URLs, reducing the need to define individual URL patterns manually.

ViewSets are commonly used in Django REST Framework projects to create clean, reusable, and maintainable APIs.
