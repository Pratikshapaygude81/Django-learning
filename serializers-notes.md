# Django REST Framework – Serializers
## Reference:-https://www.geeksforgeeks.org/python/serializers-django-rest-framework/
## 1. Introduction to Serializers

In Django REST Framework (DRF), serializers are used to convert complex data, such as Django model instances and QuerySets, into formats like JSON or XML for API responses.

They also convert incoming JSON data into Python data types.

### Key Features

- Transform database objects into JSON or other supported formats.
- Convert incoming JSON data into Python objects.
- Validate input data before saving it to the database.
- Control what data is exposed through an API.
- Simplify communication between frontend and backend applications.

## 2. Creating a Basic Serializer

To create a serializer, import `serializers` from `rest_framework` and define the required fields.

### Example

```python
from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
```

### Explanation

- `serializers.Serializer`: Creates a basic serializer class.
- `EmailField`: Validates email address data.
- `CharField`: Handles text data.
- `DateTimeField`: Handles date and time data.

A serializer can be declared for any entity or object based on the required fields.

## 3. Using Serializer to Serialize Data

A serializer can convert a single object or a list of objects into serialized data.

First, create a Python class representing a comment.

```python
from datetime import datetime

class Comment(object):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()
```

Create an object:

```python
comment = Comment(
    email='leila@example.com',
    content='foo bar'
)
```

### Accessing Serializer Through Django Shell

Open the Django shell:

```bash
python manage.py shell
```

Import the serializer:

```python
from apis.serializers import CommentSerializer
```

Serialize the comment object:

```python
serializer = CommentSerializer(comment)
```

Access the serialized data:

```python
serializer.data
```

The `.data` property provides the serialized representation of the object.

## 4. ModelSerializer

`ModelSerializer` is a shortcut provided by Django REST Framework that automatically generates serializer fields based on a Django model.

It behaves like a regular Serializer but provides additional features.

### Key Features

- Automatically generates fields from the Django model.
- Provides model-based validators.
- Provides default implementations of `.create()` and `.update()` methods.
- Reduces the amount of code required to create serializers.

### Syntax

```python
class SerializerName(serializers.ModelSerializer):

    class Meta:
        model = ModelName
        fields = ['field1', 'field2']
```

### Example: models.py

```python
from django.db import models

class Account(models.Model):
    user_id = models.IntegerField()
    account_name = models.CharField(max_length=50)
    user = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
```

### Example: serializers.py

```python
from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['user_id', 'account_name', 'user', 'created']
```

**Explanation:**

- `ModelSerializer`: Creates a serializer based on a Django model.
- `Meta`: Defines the serializer configuration.
- `model`: Specifies the Django model.
- `fields`: Specifies which model fields should be included.

Using `fields = '__all__'` includes all model fields automatically.

## 5. HyperlinkedModelSerializer

`HyperlinkedModelSerializer` works similarly to `ModelSerializer`, but represents relationships using hyperlinks instead of primary keys.

Each object includes a URL field that represents its unique API endpoint.

### Key Features

- Represents relationships using hyperlinks.
- Includes a URL field for navigating to individual resources.
- Makes API responses more RESTful.
- Helps connect related resources through URLs.

### Syntax

```python
class SerializerName(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ModelName
        fields = ['id', 'field1', 'field2']
```

### Example

```python
class AccountSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Account
        fields = ['id', 'account_name', 'user', 'created']
```

## 6. Serializer Fields

Serializer fields work similarly to Django form fields.

Each field handles:
- Data validation.
- Default values.
- Error messages.
- Data representation.

### Commonly Used Serializer Fields

| Field | Description |
|---|---|
| `BooleanField` | Handles True or False values. |
| `CharField` | Handles text data. |
| `EmailField` | Validates email addresses. |
| `RegexField` | Validates strings against a regular expression. |
| `URLField` | Validates URL values. |
| `SlugField` | Validates strings containing letters, numbers, underscores and hyphens. |
| `IPAddressField` | Validates IPv4 or IPv6 addresses. |
| `IntegerField` | Handles integer values. |
| `FloatField` | Handles floating-point values. |
| `DecimalField` | Handles decimal values. |
| `DateTimeField` | Handles date and time values. |
| `DateField` | Handles date values. |
| `TimeField` | Handles time values. |
| `DurationField` | Handles duration values. |
| `ChoiceField` | Accepts one value from a predefined set of choices. |
| `MultipleChoiceField` | Accepts multiple values from a predefined set of choices. |
| `FileField` | Handles uploaded files. |
| `ImageField` | Handles uploaded image files. |
| `ListField` | Validates a list of objects. |
| `JSONField` | Handles JSON-compatible data. |
| `HiddenField` | Uses a default or callable value instead of user input. |
| `DictField` | Validates dictionary data. |

**Note:** `NullBooleanField` is deprecated. Use `BooleanField` with `allow_null=True` when nullable boolean values are required.

## 7. Core Arguments in Serializer Fields

Serializer fields accept different arguments to control validation, default values and data behavior.

| Argument | Description |
|---|---|
| `read_only` | Field is included in serialized output but cannot be provided as input for creating or updating an instance. |
| `write_only` | Field accepts input but is excluded from serialized output. |
| `required` | Determines whether a field must be provided during deserialization. |
| `default` | Specifies a default value when input is not supplied. |
| `allow_null` | Allows `None` as a valid value. |
| `source` | Specifies the attribute or dictionary key used to populate the field. |
| `validators` | Contains validation functions applied to incoming field data. |
| `error_messages` | Defines custom error messages for validation errors. |
| `label` | Provides a short descriptive name for the field. |
| `help_text` | Provides additional information about the field. |
| `initial` | Specifies an initial value for pre-populating HTML form fields. |

### Examples of Core Arguments

**A. read_only**

```python
id = serializers.IntegerField(read_only=True)
```

The field is included in output but cannot be changed through serializer input.

**B. write_only**

```python
password = serializers.CharField(write_only=True)
```

The password can be accepted as input but is not included in the serialized output.

**C. required**

```python
email = serializers.EmailField(required=False)
```

The email field is not compulsory during input.

**D. default**

```python
status = serializers.CharField(default='Active')
```

Uses `Active` as the default value when no value is supplied.

**E. allow_null**

```python
description = serializers.CharField(allow_null=True)
```

Allows the field to accept `None`.

## 8. Types of Serializers – Comparison

| Feature | Serializer | ModelSerializer | HyperlinkedModelSerializer |
|---|---|---|---|
| Field definition | Manual | Automatic from model | Automatic from model |
| Model integration | Not automatic | Yes | Yes |
| Default create/update | Must be implemented when needed | Provided | Provided |
| Relationships | Defined manually | Usually represented using primary keys by default | Represented using hyperlinks by default |
| Main purpose | Custom data serialization | Model-based serialization | Hyperlink-based API representation |

## 9. Important Points to Remember

1. Serializers convert complex data into JSON-compatible formats.
2. Deserialization converts incoming data into Python data types.
3. Serializers validate incoming data before saving.
4. `Serializer` requires manually defined fields.
5. `ModelSerializer` automatically generates fields from Django models.
6. `HyperlinkedModelSerializer` represents relationships using hyperlinks.
7. `.data` provides the serialized representation.
8. `read_only` prevents a field from being used as input.
9. `write_only` prevents a field from appearing in serialized output.
10. Serializer fields support validation and error handling.

## 10. Conclusion

Django REST Framework serializers provide a convenient way to convert data between Django models and API representations.

They help validate incoming data, control exposed fields and simplify communication between frontend applications and backend APIs.
