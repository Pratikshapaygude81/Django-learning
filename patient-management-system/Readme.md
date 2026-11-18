# Basic Patient Management System

## 1. Project Overview

The Basic Patient Management System is a Django-based application designed to manage patient records in a hospital.

The application will perform CRUD operations (Create, Read, Update, Delete) to maintain patient information.

The main objective is to practically implement the Django concepts learned so far, including Django ORM, Models, Views, URLs, Serializers, ViewSets, Mixins, and REST API development.

## 2. Project Objectives

- Create and manage patient records.
- Implement CRUD operations using Django.
- Understand database interactions using Django ORM.
- Implement serializers for data conversion and validation.
- Use Views, ViewSets, and Mixins.
- Configure URL routing and API endpoints.
- Understand how different Django components work together.

## 3. Technology Stack

- **Programming Language:** Python
- **Framework:** Django
- **API Framework:** Django REST Framework
- **Database:** SQLite
- **Version Control:** Git and GitHub

## 4. Patient Model

Create a Patient model with the following fields:

| Field | Data Type | Description |
|---|---|---|
| id | AutoField | Unique patient ID |
| name | CharField | Patient's full name |
| age | IntegerField | Patient's age |
| gender | CharField | Patient's gender |
| phone | CharField | Contact number |
| email | EmailField | Email address |
| address | TextField | Residential address |
| created_at | DateTimeField | Record creation date |
| updated_at | DateTimeField | Last updated date |

## 5. Core Functionalities

### 5.1 Create Patient
- Accept patient details.
- Validate input data.
- Save patient information in the database.

### 5.2 Read Patient
- Retrieve all patient records.
- Retrieve an individual patient using their ID.
- Display patient information.

### 5.3 Update Patient
- Identify a patient using their ID.
- Modify existing patient information.
- Save updated details.

### 5.4 Delete Patient
- Identify a patient using their ID.
- Delete the patient record.

## 6. Django Concepts to Implement

### 6.1 Project and App Structure
- Django project creation.
- Django app creation.
- Installed apps configuration.
- Project settings.

### 6.2 Models and Database
- Patient model creation.
- Model fields and field options.
- Meta class.
- Model methods.
- Migrations.
- Django ORM operations (Create, Read, Update, Delete).

### 6.3 Django Admin
- Register Patient model.
- Customize list display.
- Add search fields.
- Add filters.
- Manage patient records through Django Admin.

### 6.4 Views
- Function-Based Views (FBV).
- Class-Based Views (CBV).
- Generic Class-Based Views.
- Understand request and response handling.

### 6.5 URL Configuration
- URL patterns.
- URLConf.
- Path converters.
- Include and app-level URL configuration.
- URL routing to views.

### 6.6 Serializers
- Serializer class.
- ModelSerializer.
- Serialization and deserialization.
- Field-level validation.
- Object-level validation.
- Create and update methods.

### 6.7 Mixins
- ListModelMixin.
- CreateModelMixin.
- RetrieveModelMixin.
- UpdateModelMixin.
- DestroyModelMixin.
- Combine multiple mixins to implement CRUD functionality.

### 6.8 ViewSets
- ViewSet.
- ModelViewSet.
- GenericViewSet.
- Action decorators.
- Router configuration.
- DefaultRouter.

### 6.9 REST API Implementation
Implement the following API operations:

| Method | Endpoint | Functionality |
|---|---|---|
| POST | /api/patients/ | Create patient |
| GET | /api/patients/ | Retrieve all patients |
| GET | /api/patients/{id}/ | Retrieve one patient |
| PUT | /api/patients/{id}/ | Update patient |
| PATCH | /api/patients/{id}/ | Partially update patient |
| DELETE | /api/patients/{id}/ | Delete patient |

## 7. Implementation Phases

### Phase 1: Project Setup
- Create virtual environment.
- Install Django and Django REST Framework.
- Create Django project.
- Create patients app.
- Configure settings.

### Phase 2: Models and ORM
- Create Patient model.
- Define model fields.
- Understand Meta class and model methods.
- Perform CRUD operations using Django ORM.
- Generate and apply migrations.

### Phase 3: Django Admin
- Register Patient model.
- Customize admin interface.
- Configure search and filtering.

### Phase 4: Views and URLs
- Implement Function-Based Views.
- Implement Class-Based Views.
- Explore Generic Class-Based Views.
- Configure URL patterns.
- Understand request and response flow.

### Phase 5: Serializers
- Create PatientSerializer.
- Implement ModelSerializer.
- Add validation.
- Understand serialization and deserialization.

### Phase 6: Mixins and ViewSets
- Implement CRUD using individual mixins.
- Combine mixins.
- Implement GenericViewSet.
- Implement ModelViewSet.
- Configure routers.

### Phase 7: Final Integration
- Connect models, serializers, views, and URLs.
- Complete all patient CRUD functionalities.
- Organize the project structure.
- Update project documentation.

## 8. Expected Outcome

At the end of the project, a functional Patient Management System will be implemented using Django and Django REST Framework.

The project will demonstrate practical implementation of the Django concepts covered during learning, with a focus on database management, CRUD operations, request-response handling, serialization, mixins, ViewSets, and API development.

## 9. Project Scope

**Included:**
- Patient CRUD operations.
- Django ORM.
- Django Admin.
- Function-Based and Class-Based Views.
- Generic Views.
- Serializers and validations.
- Mixins and ViewSets.
- REST API development.
