# Django_Codes
Learning Django of University.

Here’s a concise and comprehensive set of **Django notes** for beginners to intermediate learners. This can help you in quick revisions, project development, or interviews.

---

# 🐍 Django Notes

## 📘 Introduction to Django

* **Django**: A high-level Python web framework that enables rapid development of secure and maintainable websites.
* **Features**:

  * Fast development
  * Secure (handles user authentication, CSRF, etc.)
  * Scalable
  * Batteries-included (ORM, admin panel, forms, etc.)

---

## 🏗️ Django Project Structure

When you run `django-admin startproject mysite`, it creates:

```
mysite/
├── manage.py
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
```

* `manage.py`: Command-line utility for administrative tasks.
* `settings.py`: Configuration file (database, apps, middleware, etc.).
* `urls.py`: URL declarations for this project.
* `wsgi.py/asgi.py`: Entry points for web servers.

---

## ⚙️ Starting an App

```bash
python manage.py startapp appname
```

App structure:

```
appname/
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
├── urls.py (manually create)
└── migrations/
```

Add app to `INSTALLED_APPS` in `settings.py`.

---

## 🌐 URL Routing

### Project level `urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
```

### App level `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

---

## 🎨 Views

### Function-based view

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world!")
```

### Render templates

```python
from django.shortcuts import render

def home(request):
    return render(request, 'appname/home.html')
```

---

## 📄 Templates

* Create `templates/` folder inside your app or at project level.
* Use Django Template Language:

```html
<h1>Hello, {{ user.username }}!</h1>
{% if user.is_authenticated %}
  <p>Welcome back!</p>
{% endif %}
```

---

## 🧠 Models

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🔐 Admin Panel

Enable admin:

```python
from .models import Post
admin.site.register(Post)
```

Create superuser:

```bash
python manage.py createsuperuser
```

Login: `/admin`

---

## 📥 Forms

### Basic Form

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
```

### ModelForm

```python
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
```

---

## 📤 Handling Forms in Views

```python
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'create.html', {'form': form})
```

---

## 📂 Static and Media Files

### settings.py

```python
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Template usage

```html
{% load static %}
<img src="{% static 'images/logo.png' %}">
```

---

## 🔒 User Authentication

### Login View

```python
from django.contrib.auth import authenticate, login

user = authenticate(username='john', password='pass')
if user is not None:
    login(request, user)
```

### Built-in Views

* `LoginView`, `LogoutView`, `PasswordChangeView`
* URLconf example:

```python
path('accounts/', include('django.contrib.auth.urls'))
```

---

## 🔁 Middleware

* Functions/classes that process requests/responses globally.
* Set in `MIDDLEWARE` in `settings.py`.

---

## 🧪 Testing

```python
from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def test_str(self):
        post = Post(title='Test Title')
        self.assertEqual(str(post), 'Test Title')
```

---

## 🔌 Useful Commands

```bash
python manage.py runserver       # Start dev server
python manage.py makemigrations  # Generate migrations
python manage.py migrate         # Apply DB changes
python manage.py shell           # Python shell with Django context
python manage.py createsuperuser # Create admin user
```

---

## 📚 Recommended Folder Structure for Larger Projects

```
project/
├── manage.py
├── project/
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   └── urls.py
├── app1/
├── app2/
├── templates/
├── static/
└── media/
```

---

If you want this in a **PDF or printable format**, just ask and I can generate it for you. Want advanced Django topics (like signals, custom middleware, REST APIs with DRF)? Let me know!
