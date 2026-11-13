## Reference:- https://docs.djangoproject.com/en/5.2/topics/db/models/?utm_source
# Django Models

## 1. Introduction to Models

A model is the single, definitive source of information about the data stored in an application. It contains the fields and behaviors of the data.

Generally, each Django model maps to a single database table.

### 1.1 Basics of Models

- Each model is a Python class that inherits from `django.db.models.Model`.
- Each attribute of the model represents a database field.
- Django automatically provides a database-access API for interacting with model data.

### 1.2 Creating a Model

Example:

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

In this example:
- `Person` is a Django model.
- `first_name` and `last_name` are model fields.
- Each field maps to a database column.
- Django automatically creates a primary key if one is not explicitly defined.

### 1.3 Using Models

After defining models, Django needs to know which application contains them.

Add the application name to `INSTALLED_APPS` in `settings.py`.

```python
INSTALLED_APPS = [
    # Other applications
    "myapp",
]
```

After registering the application, use Django migration commands to synchronize model changes with the database.

---

## 2. Model Fields

Fields are the most important part of a model. They define the structure of the data stored in the database.

Each field is specified as a class attribute.

### 2.1 Defining Model Fields

Example:

```python
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
```

### 2.2 Field Types

Django provides different field types to represent different kinds of data.

Examples:

| Field Type | Purpose |
|---|---|
| `CharField` | Stores short strings |
| `TextField` | Stores large text |
| `IntegerField` | Stores integer values |
| `BooleanField` | Stores True or False |
| `DateField` | Stores dates |
| `DateTimeField` | Stores date and time |
| `EmailField` | Stores email addresses |
| `FloatField` | Stores floating-point values |
| `ForeignKey` | Defines many-to-one relationships |
| `OneToOneField` | Defines one-to-one relationships |
| `ManyToManyField` | Defines many-to-many relationships |

### 2.3 Field Options

Field options specify additional properties and restrictions for model fields.

| Option | Description |
|---|---|
| `null` | Determines whether the database can store NULL |
| `blank` | Determines whether a field can be left empty during validation |
| `default` | Defines a default value |
| `db_default` | Defines a database-level default |
| `unique` | Ensures that field values are unique |
| `primary_key` | Defines the primary key |
| `choices` | Restricts values to predefined options |
| `max_length` | Specifies the maximum length of a string |
| `help_text` | Provides additional information about a field |

### 2.4 Difference Between null and blank

- `null` is related to database storage.
- `blank` is related to validation.

Example:

```python
description = models.TextField(
    null=True,
    blank=True
)
```

### 2.5 Choices in Model Fields

The `choices` option restricts a field to predefined values.

Example:

```python
from django.db import models

class Person(models.Model):
    SHIRT_SIZES = {
        "S": "Small",
        "M": "Medium",
        "L": "Large",
    }

    name = models.CharField(max_length=60)
    shirt_size = models.CharField(
        max_length=1,
        choices=SHIRT_SIZES
    )
```

The first value represents the value stored in the database, while the second value is displayed to users.

The `get_FOO_display()` method can be used to retrieve the display value.

### 2.6 Automatic Primary Key Fields

Django automatically adds an auto-incrementing primary key to a model if no primary key is explicitly defined.

Example:

```python
id = models.BigAutoField(primary_key=True)
```

A model must have exactly one primary key.

### 2.7 Verbose Field Names

Verbose names provide readable labels for model fields.

Example:

```python
first_name = models.CharField(
    "person's first name",
    max_length=30
)
```

Django automatically generates a readable name from the field attribute if a verbose name is not provided.

---

## 3. Model Relationships

Relational databases allow tables to be connected to each other.

Django supports three common types of relationships.

### 3.1 Many-to-One Relationship

A many-to-one relationship is defined using `ForeignKey`.

Example:

```python
from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

class Car(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE
    )
```

In this example:
- One manufacturer can manufacture multiple cars.
- Each car belongs to one manufacturer.

### 3.2 Many-to-Many Relationship

A many-to-many relationship is defined using `ManyToManyField`.

Example:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
```

In this example:
- One student can enroll in multiple courses.
- One course can have multiple students.

### 3.3 One-to-One Relationship

A one-to-one relationship is defined using `OneToOneField`.

Example:

```python
class Person(models.Model):
    name = models.CharField(max_length=100)

class Profile(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE
    )
```

In this example, each profile is associated with one person.

### 3.4 on_delete Option

The `on_delete` argument specifies what happens when the referenced object is deleted.

Common options include:

- `CASCADE`
- `PROTECT`
- `SET_NULL`
- `SET_DEFAULT`
- `SET()`
- `DO_NOTHING`

---

## 4. Model Meta Options

Django provides an inner `Meta` class to define additional model options.

Example:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]
        db_table = "student_details"
```

Common Meta options include:

| Option | Purpose |
|---|---|
| `ordering` | Defines default ordering |
| `db_table` | Specifies the database table name |
| `verbose_name` | Defines a readable singular name |
| `verbose_name_plural` | Defines a readable plural name |
| `abstract` | Defines an abstract model |
| `proxy` | Defines a proxy model |
| `managed` | Controls database table management |

---

## 5. Model Methods

Django models support methods that define the behavior of model instances.

### 5.1 String Representation

The `__str__()` method defines the human-readable representation of a model instance.

Example:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```

### 5.2 get_absolute_url()

The `get_absolute_url()` method defines how to calculate the URL for a particular model object.

It is commonly used by Django's admin interface and other parts of an application.

### 5.3 Overriding Predefined Model Methods

Django allows developers to override built-in model methods such as:

- `save()`
- `delete()`

Example:

```python
class Blog(models.Model):
    name = models.CharField(max_length=100)

    def save(self, **kwargs):
        # Custom logic
        super().save(**kwargs)
```

Calling `super().save(**kwargs)` ensures that Django's original save functionality is executed.

**Important:** Bulk operations do not necessarily call overridden model methods or the corresponding save signals.

---

## 6. Model Inheritance

Django supports model inheritance in a way similar to Python class inheritance.

There are three main types of model inheritance.

### 6.1 Abstract Base Classes

Abstract base classes are used to define common fields and methods that can be inherited by multiple models.

They are created using `abstract = True` inside the Meta class.

Example:

```python
from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
```

In this example:
- `CommonInfo` is an abstract base class.
- `Student` inherits its fields.
- Django creates a database table for `Student`.
- Django does not create a separate table for `CommonInfo`.

### 6.2 Multi-Table Inheritance

In multi-table inheritance, each model has its own database table.

Django automatically creates a one-to-one relationship between the parent and child models.

Example:

```python
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
```

In this example:
- `Place` has its own database table.
- `Restaurant` has its own database table.
- The child model inherits fields from the parent model.

### 6.3 Proxy Models

Proxy models are used when developers want to change the Python-level behavior of an existing model without creating another database table.

They are defined using `proxy = True`.

Example:

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class MyPerson(Person):

    class Meta:
        proxy = True

    def do_something(self):
        pass
```

Proxy models can be used to:
- Change default ordering.
- Add custom methods.
- Define custom managers.

### 6.4 Multiple Inheritance

Django supports inheriting from multiple parent models.

Normal Python name-resolution rules apply when multiple parent classes contain the same attribute names.

Multiple inheritance should be kept simple to avoid unnecessary complexity.

### 6.5 Field Name Restrictions

Django does not generally allow overriding fields inherited from non-abstract parent models.

Fields inherited from abstract base classes can be overridden or removed.

---

## 7. Organizing Models in a Package

When an application contains many models, keeping every model in a single `models.py` file may become difficult to manage.

Django allows models to be organized into separate files inside a `models` package.

### 7.1 Package Structure

Example:

```text
myapp/
│
├── models/
│   ├── __init__.py
│   ├── organic.py
│   └── synthetic.py
│
├── views.py
├── admin.py
└── apps.py
```

### 7.2 Importing Models

Models stored in separate files should be imported into the package's `__init__.py` file.

Example:

```python
from .organic import Person
from .synthetic import Robot
```

This makes the models available to Django when the application is loaded.

---

## 8. Key Learnings

- Understanding Django model structure.
- Defining model fields and field options.
- Understanding primary keys.
- Implementing relationships between models.
- Using Meta options.
- Understanding model methods.
- Learning different types of model inheritance.
- Organizing models into separate files and packages.

---

## 9. Official Documentation

The following official Django documentation was used as the learning reference:

- [Django Models](https://docs.djangoproject.com/en/5.2/topics/db/models/)
- [Model Field Reference](https://docs.djangoproject.com/en/5.2/ref/models/fields/)
- [Model Instance Reference](https://docs.djangoproject.com/en/5.2/ref/models/instances/)
- [Model Meta Options](https://docs.djangoproject.com/en/5.2/ref/models/options/)
- [Making Queries](https://docs.djangoproject.com/en/5.2/topics/db/queries/)
