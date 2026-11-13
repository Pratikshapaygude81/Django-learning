# Django Models and Database Operations
## Reference:-https://www.w3schools.com/django/django_models.php
## 1. Introduction to Django Models

A Django model is a Python class that represents the structure of data stored in a database.

Models allow Django applications to:
- Store information in database tables.
- Retrieve records from the database.
- Insert new records.
- Update existing records.
- Delete records.

Each model generally represents one database table, and its attributes represent table fields (columns).

**Hospital Appointment System examples:**
- Patient
- Doctor
- Appointment
- Department

## 2. Creating a Model

Django models are created inside the `models.py` file of an application.

For example, in our project:

```text
appointments/
    models.py
```

A model is created by defining a Python class that inherits from `models.Model`.

General structure:

```python
from django.db import models

class ModelName(models.Model):
    field_name = models.FieldType()
```

### Common Django Model Fields

| Field | Purpose |
|---|---|
| CharField | Stores short text. |
| TextField | Stores longer text. |
| IntegerField | Stores integer values. |
| EmailField | Stores email addresses. |
| DateField | Stores dates. |
| DateTimeField | Stores date and time. |
| BooleanField | Stores True or False. |
| DecimalField | Stores decimal values. |
| ForeignKey | Creates a relationship with another model. |
| OneToOneField | Creates a one-to-one relationship. |
| ManyToManyField | Creates a many-to-many relationship. |

### Field Options

| Option | Purpose |
|---|---|
| max_length | Specifies the maximum length of text. |
| null | Allows a database field to store NULL. |
| blank | Allows a field to be empty during form validation. |
| default | Specifies a default value. |
| unique | Prevents duplicate values. |
| primary_key | Defines a field as the primary key. |

## 3. Database in Django

A database stores application data in an organized manner.

Django supports different databases, including:
- SQLite
- PostgreSQL
- MySQL
- Oracle

### SQLite Database

When a Django project is created, SQLite is configured by default in a standard project setup.

The database file is generally named:

```text
db.sqlite3
```

It is usually located in the project root directory, alongside `manage.py`.

Django uses the `DATABASES` setting in `settings.py` to configure database connections.

## 4. Migrations in Django

Migrations are used to apply changes made to Django models to the database structure.

Whenever we create or modify a model, we generally need to create and apply migrations.

There are two important commands.

### A. makemigrations

Command:

```bash
python manage.py makemigrations
```

Purpose:
- Detects changes in models.
- Creates migration files.
- Stores migration files inside the application's `migrations` folder.

Example:

```text
appointments/
    migrations/
        __init__.py
        0001_initial.py
```

### B. migrate

Command:

```bash
python manage.py migrate
```

Purpose:
- Applies pending migrations.
- Creates or updates database tables.
- Executes the database changes described by migration files.

**Important difference:**

| Command | Purpose |
|---|---|
| makemigrations | Creates migration files. |
| migrate | Applies migration files to the database. |

## 5. Primary Key and ID Field

Django automatically adds a primary key field to a model if you do not define one.

By default, this is commonly an auto-incrementing integer field, depending on the project's default primary key configuration.

Example:

| id | firstname | lastname |
|---|---|---|
| 1 | Rahul | Sharma |
| 2 | Priya | Patil |
| 3 | Amit | Joshi |

Each record gets a unique ID.

The primary key is used to identify individual database records.

## 6. Django ORM

ORM stands for Object-Relational Mapping.

Django ORM allows developers to interact with database records using Python code instead of writing SQL queries for every operation.

Using Django ORM, we can:
- Create records.
- Retrieve records.
- Update records.
- Delete records.
- Filter records.
- Sort records.
- Work with related models.

## 7. CRUD Operations in Django

CRUD represents the four basic database operations.

| Operation | Meaning | Purpose |
|---|---|---|
| Create | Insert | Add a new record. |
| Read | Retrieve | Fetch existing records. |
| Update | Modify | Change existing records. |
| Delete | Remove | Delete records. |

### A. Insert / Create

The Create operation adds a new record to a database table.

Hospital example:
- Register a new patient.
- Add a new doctor.
- Create an appointment.

Django ORM provides methods such as:
- `create()`
- `save()`

### B. Retrieve / Read

The Read operation fetches existing records from the database.

Hospital example:
- Display all doctors.
- Find a patient using their ID.
- View appointment details.

Common ORM methods:
- `all()` – Retrieves all records.
- `get()` – Retrieves a single matching record.
- `filter()` – Retrieves records matching specified conditions.
- `exclude()` – Retrieves records that do not match specified conditions.

### C. Update

The Update operation modifies existing database records.

Hospital example:
- Update patient contact details.
- Change a doctor's specialization.
- Update an appointment status.

Django ORM supports updating records through:
- Changing model object attributes and calling `save()`.
- Using the `update()` QuerySet method.

### D. Delete

The Delete operation removes existing records from the database.

Hospital example:
- Remove an incorrect appointment.
- Delete an obsolete doctor record.

Django ORM provides the `delete()` method for deleting records.

**Important:** Deletion can permanently remove data. Applications should use appropriate validation and authorization before deleting records.

## 8. QuerySet in Django

A QuerySet represents a collection of database records returned by a Django query.

QuerySets allow us to:
- Retrieve multiple records.
- Filter records.
- Exclude records.
- Sort records.
- Perform database operations.

Common QuerySet methods:

| Method | Purpose |
|---|---|
| all() | Returns all records. |
| filter() | Returns matching records. |
| exclude() | Excludes matching records. |
| order_by() | Sorts records. |
| count() | Returns the number of records. |
| exists() | Checks whether matching records exist. |
| first() | Returns the first matching record. |
| last() | Returns the last matching record. |
| update() | Updates matching records. |
| delete() | Deletes matching records. |

## 9. Updating an Existing Model

When an existing model needs changes, we can modify its fields in `models.py`.

Examples of model changes:
- Adding a new field.
- Changing a field's maximum length.
- Changing a field type.
- Adding a default value.
- Adding a relationship with another model.

After modifying the model:

**Step 1:** Create migration files.

```bash
python manage.py makemigrations
```

**Step 2:** Apply migrations.

```bash
python manage.py migrate
```

Django uses migration files to keep the database structure synchronized with the models.

## 10. Model Relationships

In a Hospital Appointment Management System, different models need to be connected.

Examples:

- One doctor can have multiple appointments.
- One patient can book multiple appointments.
- Each appointment can be associated with a patient and a doctor.

Django supports three major relationship fields:

| Relationship | Field |
|---|---|
| One-to-one | OneToOneField |
| One-to-many | ForeignKey |
| Many-to-many | ManyToManyField |

## 11. Database Administration

Django provides a built-in administration interface.

Using Django Admin, authorized administrators can:
- Add records.
- View records.
- Edit records.
- Delete records.

Models can be registered in the application's `admin.py` file to make them available in the admin interface.

## 12. Application in Hospital Appointment Management System

We will use Django models to manage the following information:

| Model | Information |
|---|---|
| Patient | Patient details. |
| Doctor | Doctor details and specialization. |
| Appointment | Appointment date, time and status. |
| Department | Hospital department information. |

CRUD operations will help us manage this information through our Django application.

## 13. Official Django Documentation

1. Models: https://docs.djangoproject.com/en/6.1/topics/db/models/
2. Model field reference: https://docs.djangoproject.com/en/6.1/ref/models/fields/
3. Migrations: https://docs.djangoproject.com/en/6.1/topics/migrations/
4. Making queries: https://docs.djangoproject.com/en/6.1/topics/db/queries/
5. QuerySet API: https://docs.djangoproject.com/en/6.1/ref/models/querysets/
6. Database configuration: https://docs.djangoproject.com/en/6.1/ref/settings/#databases
7. Django Admin: https://docs.djangoproject.com/en/6.1/ref/contrib/admin/

---

## Key Takeaways

- Models define the structure of database tables.
- Model fields define the columns.
- Django ORM allows database operations using Python.
- Migrations apply model changes to the database.
- CRUD means Create, Read, Update and Delete.
- Relationships connect different models.
- Django Admin provides an interface to manage database records.
