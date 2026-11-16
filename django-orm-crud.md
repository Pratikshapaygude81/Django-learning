# Django ORM – Inserting, Retrieving, Updating & Deleting Data
## Reference:-https://www.geeksforgeeks.org/python/django-orm-inserting-updating-deleting-data/
## 1. Introduction to Django ORM

ORM stands for **Object Relational Mapper**.

Django ORM allows developers to interact with databases using Python classes and objects instead of writing SQL queries manually.

### Key Features

- Defines database structure using Python models.
- Connects Python objects with database tables.
- Allows easy creation, retrieval, updating and deletion of records.
- Reduces the need to write raw SQL queries.

## 2. Steps to Use Django ORM

### Step 1: Define Models

Models define the structure of database tables.

Example:

```python
class Album(models.Model):
    title = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
```

**Explanation:**

- `Album`: Represents an album table.
- `Song`: Represents a song table.
- `CharField`: Stores string or text data with a specified maximum length.
- `ForeignKey`: Creates a relationship between two models.
- `on_delete=models.CASCADE`: Deletes related songs when their associated album is deleted.
- `__str__()`: Returns a readable string representation of an object.

### Step 2: Access Django ORM Using Django Shell

To interact with Django models through the ORM, open the Django shell.

Command:

```bash
python manage.py shell
```

Import the models:

```python
from music.models import Song, Album
```

The Django shell allows us to execute Python commands and interact directly with the project's database.

## 3. Django ORM Operations (CRUD)

CRUD stands for:

- **C – Create:** Insert new records.
- **R – Read:** Retrieve existing records.
- **U – Update:** Modify existing records.
- **D – Delete:** Remove records.

## 4. Inserting Records (Create)

Django ORM provides different ways to insert records into the database.

### A. Creating and Saving a Single Object

```python
a = Album(title="Divide", artist="Ed Sheeran", genre="Pop")
a.save()
```

**Explanation:**

- Creates an Album object.
- Assigns values to its fields.
- `save()` stores the object in the database.

Creating a Song associated with the Album:

```python
s = Song(name="Castle on the Hill", album=a)
s.save()
```

Here, the `album` field connects the song to the previously created album.

### B. Inserting Multiple Records

```python
a1 = Album(title="Abbey Road", artist="The Beatles", genre="Rock")
a1.save()

a2 = Album(title="Revolver", artist="The Beatles", genre="Rock")
a2.save()
```

Each `save()` operation inserts a record into the database.

### C. Using create()

Another way to insert and save a record in a single step:

```python
Album.objects.create(
    title="Divide",
    artist="Ed Sheeran",
    genre="Pop"
)
```

The `create()` method creates an object and saves it automatically.

## 5. Retrieving Records (Read)

Django ORM provides different methods to retrieve data.

### A. all()

Retrieves all records from a model.

```python
Album.objects.all()
```

Example output:

```text
<QuerySet [<Album: Divide>, <Album: Abbey Road>, <Album: Revolver>]>
```

A QuerySet is a collection of database objects returned by Django ORM.

### B. filter()

Retrieves records that match the specified condition.

```python
Album.objects.filter(artist="The Beatles")
```

This retrieves all albums created by The Beatles.

### C. exclude()

Retrieves all records except those matching the specified condition.

```python
Album.objects.exclude(genre="Rock")
```

This returns albums whose genre is not Rock.

### D. get()

Retrieves a single object matching the specified condition.

```python
Album.objects.get(pk=3)
```

Here:
- `get()` retrieves one matching object.
- `pk` represents the primary key of the record.

**Important:** `get()` raises exceptions in two situations:

1. `DoesNotExist`: When no matching record is found.
2. `MultipleObjectsReturned`: When more than one record matches.

## 6. Updating Records (Update)

Updating means modifying an existing database record.

### A. Updating a Single Object

First, retrieve the object:

```python
a = Album.objects.get(pk=3)
```

Modify its field:

```python
a.genre = "Pop"
```

Save the changes:

```python
a.save()
```

This updates the genre of the album with primary key 3.

### B. Bulk Update

The `update()` method allows us to update multiple records at once.

```python
Album.objects.filter(artist="The Beatles").update(
    genre="Classic Rock"
)
```

This updates the genre of all albums by The Beatles.

**Difference:**
- `save()`: Saves changes made to an individual model object.
- `update()`: Updates matching records directly through a QuerySet.

## 7. Deleting Records (Delete)

Deleting means removing records from the database.

### A. Deleting a Single Record

First, retrieve the object:

```python
a = Album.objects.get(pk=2)
```

Delete it:

```python
a.delete()
```

This deletes the album with primary key 2.

### B. Deleting Multiple Records

The `delete()` method can also be used with filters.

```python
Album.objects.filter(genre="Pop").delete()
```

This deletes all albums whose genre is Pop.

**Important:** Deletion operations should be performed carefully because deleted records cannot normally be recovered without a backup or other recovery mechanism.

## 8. Common Django ORM Query Methods

| Method | Purpose |
|---|---|
| `all()` | Retrieves all records |
| `filter()` | Retrieves records matching conditions |
| `exclude()` | Excludes records matching conditions |
| `get()` | Retrieves a single matching object |
| `create()` | Creates and saves a new record |
| `save()` | Saves a model object's changes |
| `update()` | Updates multiple matching records |
| `delete()` | Deletes records |

## 9. Important Concepts to Remember

1. Django ORM allows database operations using Python.
2. Models represent database tables.
3. Model objects represent individual database records.
4. QuerySets represent collections of database objects.
5. `ForeignKey` establishes a relationship between models.
6. `save()` stores a new object or saves changes to an existing object.
7. `filter()` is used to retrieve records based on conditions.
8. `get()` is used when expecting a single matching record.
9. `update()` modifies matching records.
10. `delete()` removes records from the database.

## 10. CRUD Operations Summary

| CRUD | Django ORM | Description |
|---|---|---|
| Create | `create()` / `save()` | Insert records |
| Read | `all()` / `filter()` / `get()` | Retrieve records |
| Update | `save()` / `update()` | Modify records |
| Delete | `delete()` | Remove records |

**Conclusion:**

Django ORM makes database management easier by allowing developers to perform CRUD operations using Python models and methods instead of writing SQL queries manually.
