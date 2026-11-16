# Django URLs (URLConf)
## Reference:-https://www.geeksforgeeks.org/python/django-url-patterns-python/
## 1. What are Django URLs?

Django URLs connect incoming HTTP requests to the appropriate views.

- **Views** handle HTTP requests and return HTTP responses.
- **URLConf** maps URL patterns to their corresponding views.
- Django uses URL routing to decide which view should handle a request.

## 2. Understanding URLConf

URLConf is Django's URL configuration system.

Important points:

- `ROOT_URLCONF` in `settings.py` specifies the root URL configuration module.
- Usually, it points to the project's `urls.py`.
- Each URLConf module contains a `urlpatterns` list.
- Django checks URL patterns in order.
- The first matching pattern is used.
- If no URL matches, Django returns a 404 error.

## 3. Structure of URLConf

Django supports two levels of URL configuration:

1. Project-level `urls.py`
2. App-level `urls.py`

### Project-level urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
]
```

**Explanation:**

- `path()` maps a URL pattern to a view or URL configuration.
- `include()` connects an app's URL configuration to the project.
- `admin/` connects to the Django Admin interface.
- `include('books.urls')` delegates URL matching to the books app.

### App-level urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_index, name='book_index'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
]
```

The app-level URL file keeps application routes organized separately.

## 4. URL Patterns

URL patterns define which URLs Django should match.

They are written inside the `urlpatterns` list.

Example:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_index, name='book_index'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/genre/<str:genre>/', views.books_by_genre, name='books_by_genre'),
]
```

**Explanation:**

- `books/` displays the list of books.
- `books/<int:pk>/` retrieves a book using its ID.
- `books/genre/<str:genre>/` retrieves books by genre.

### URL name

The `name` argument gives a URL pattern a reusable name.

It can be used in:

- Templates with `{% url 'name' %}`
- Python code with `reverse()`

This avoids hardcoding URLs in different parts of the application.

## 5. Basic Django URL Routing with HTML Pages

### Step 1: Define views in views.py

```python
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')
```

### Step 2: Create HTML templates

Create these files inside the templates folder:

**home.html**

```html
<h1>Home Page</h1>
<p>Welcome to the home page.</p>
<a href="/about/">Go to About</a>
<a href="/contact/">Go to Contact</a>
```

**about.html**

```html
<h1>About Page</h1>
<p>This is the about page.</p>
<a href="/">Go to Home</a>
<a href="/contact/">Go to Contact</a>
```

**contact.html**

```html
<h1>Contact Page</h1>
<p>Contact us at contact@example.com.</p>
<a href="/">Go to Home</a>
<a href="/about/">Go to About</a>
```

### Step 3: Define URL patterns in urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]
```

### Output

- `/` → Home Page
- `/about/` → About Page
- `/contact/` → Contact Page

## 6. Path Converters

Path converters capture dynamic values from URLs and pass them as arguments to views.

They are written inside angle brackets `< >`.

| Converter | Description |
|---|---|
| `int` | Matches positive integers |
| `str` | Matches a non-empty string, excluding `/` |
| `slug` | Matches letters, numbers, hyphens and underscores |
| `path` | Matches a non-empty string, including `/` |
| `uuid` | Matches a valid UUID string |

### Example

```python
from django.urls import path
from . import views

urlpatterns = [
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/<str:genre>/', views.books_by_genre, name='books_by_genre'),
    path('books/<slug:slug>/', views.book_by_slug, name='book_by_slug'),
]
```

**Explanation:**

- `<int:pk>` passes an integer primary key to the view.
- `<str:genre>` passes a string representing the genre.
- `<slug:slug>` passes a slug value for a readable URL.

## 7. Important Django URL Functions

| Function | Purpose |
|---|---|
| `path()` | Defines a URL pattern |
| `include()` | Includes another URL configuration |
| `reverse()` | Generates a URL using its name |

## 8. Important Points to Remember

- URL configuration is handled by URLConf.
- `ROOT_URLCONF` identifies the root URL configuration.
- URL patterns are stored in `urlpatterns`.
- `path()` connects URLs to views.
- `include()` connects project-level URLs to app-level URLs.
- URL patterns are checked in order.
- Path converters capture dynamic URL values.
- URL names help avoid hardcoded URLs.

## 9. Practical Application in Hospital Appointment Management

In the hospital appointment project, URL routing can connect different pages to their views.

Example routes:

| URL | Purpose |
|---|---|
| `appointments/` | Display appointments |
| `appointments/<int:pk>/` | View a particular appointment |
| `providers/` | Display providers |
| `clients/` | Display clients |
| `authentication/login/` | Login page |

These routes can be connected to the appropriate app-level views using `path()` and `include()`.

---

**Official Documentation:**  
https://docs.djangoproject.com/en/6.1/topics/http/urls/
