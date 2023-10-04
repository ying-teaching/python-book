# Django

- HTTPS Overview
- Getting Started
- Database
- Model
- View
- Form
- Generic View

## HTTPS Overview

- [Introduction Video](https://youtu.be/d_QPZPo2PLc)
- HTTPS handles authentication and encryption
- A Web page has three types of contents:
  - HTML: the structure data
  - CSS: the style
  - Javascript: the behavior

## Getting Started

First, use `python3 -m pip install django` to install the Django package.

Django comes with many tools such as `django-admin` to make development simple and quick.

To create a project, run the following command: `django-admin startproject my_site`.

### Initial Project

The command creates a `my_site` project folder with following folders and files:

- `manage.py`: it is a thin wrapper around `django-admin`. It uses the settings of the current project. You use `django-admin` to create projects and apps, then use `manage.py` to perform the rest administration tasks.
- `my_site`: it is the package folder for the project. It has the following files
  - `__init__.py`: it is an empty file to flag the parent folder as a Python package.
  - `asgi.py`: it is an entry point file for ASGI (Asynchronous Server Gateway Interface) web server. ASGI support asynchronous operations that might have better performance for certain applications at the cost of complex code and logic. Most Web applications don't use it.
  - `setting.py`: it contains settings (configurations) for this project. For example, you should change the `TIME_ZONE` if your site is not located in `UTC` time zone.
  - `urls.py`: it configures the URL paths of the project.
  - `wsgi.py`: it is an entry point file for WSGI (Web Server Gateway Interface) web server. Most Python Web applications use it.

### Dev Server

Django has a built-in WSGI web server for the development. You can run it with the initial project.

Inside `my_site` project folder (not the nested `my_site` package folder), run `python3 manage.py runserver`, you can check the initial web site at `http://127.0.0.1:8000/` or `http://locahost:8000/`.

The built-in development server monitors file changes and rebuilt the project when there is a change in the project source code files.

To quit the server, type `CONTROL-C` in the terminal.

### Creating an App

A Django project has multiple [Applications](https://docs.djangoproject.com/en/4.2/ref/applications/).

Each application is Python package that contains functions of subdomain the website.

An application consists of models, views, templates, static files, URLs, etc.

For example, Django creates a default `admin` app during the project creation. Web administrators use the admin app to manage the web site.

To create an app named `polls`, run the command: `python3 manage.py startapp polls`.

### Application Configuration

Create an `app.py` inside the application package.

Defines a subclass of `AppConfig`

Configure settings such as `name`, `verbose_name` in the configuration class.

Then add the class to the `INSTALLED_APPS` in the `setting.py` file in the project's main package.

### The App Folder

The creating app command creates a `polls` folder that has the following files:

- `__init__.py` the package flag file.
- `admin.py` the placeholder for administration page file.
- `apps.py` the configuration file for the app.
- `migrations` folder is used to store database migration files.
- `models.py` the data models used by the app.
- `tests.py` the testing file
- `views.py` the _view_ code to process HTTP requests and return HTTP responses.

### MVT

Django uses a Model-View-Template (MVT) architecture.

- Model: a model is a class the defines
  - the structure of a domain data.
  - the data operations.
- View: a view is a function or a class that handles HTTP request, performs business logic, and returns a response.
- Template: a template defines the structure or layout of the user interface. A view fills templates with data to create the final response.

Following is the [Django workflow](https://www.dothedev.com/blog/amp/what-is-django-used-for/):

![flow](../images/django_flow.jpg)

### What's a View

In Django, a view is associated with a URL pattern, i.e., Django maps URL patterns to views.

If a specific HTTP URL matches a view's URL pattern, the view usually performs the following functions:

- processes HTTP requests.
- performs business logic based on request arguments.
- uses templates to render the response content.
- returns responses in different format such as HTML, JSON, or others.

### Add the First View

As a tradition, you want to say "Hello World!" to an HTTP request. Following are codes in different files.

If you run the dev server and access `http://127.0.0.1:8000/polls/`, you should see the message "Hello World!".

```python
# polls/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")

```

```python
# polls/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

```

```python
# my_site/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]

```

### The `path()` and `include()` Function

The `path()` function maps URLs to views or defines nested URL patterns. It has two required arguments and two optional arguments.

- `route`: is a string that contains a URL pattern.
- `view`: is the view use to process the URL request.
- `kwargs`: are arbitrary keyword arguments passed to the view.
- `name`: is the name of this URL path. Then this path is used elsewhere, you can use the name to refer the path.

The code `path("", views.index, name="index")` maps the empty string to the `views.index` view. The path has a name of `index`.

The `include()` function allows nested paths. Except the built-in `admin.site.urls`, you use `include()` when you include other URL patterns.

The `path("polls/", include("polls.urls")),` puts all polls url patterns defined in `polls/urls.py` under the `polls/` path.

The `ROOT_URLCONF = "my_site.urls"` in `my_site/settings.py` specifies the URL configuration file for the root path. Django starts path matching from the this file.

## Database

Django uses relational database to store application data that is defined by models.

A model defines the table schema.

Django provides built-in CRUD operations for data.

Django supports a number of relational database engines. You can change database setup in the project `settings.py` file.

### Database Setup

By default, Django uses the SQLite relational database to manage data. [SQLite](https://www.sqlite.org/) is a small, fast, and reliable relational database engine. It is an excellent choice for learning Django. It is also a good choice for small to medium web sites in production.

The `my_site/settings.py` has two database configuration entries in the `default` item in `DATABASES`:

- `ENGINE`: default is `'django.db.backends.sqlite3'`. Other popular choices are `'django.db.backends.postgresql'` or `'django.db.backends.mysql'`.
- `NAME`: it is a database-specific setting. For SQLite, it is the database file path. For other databases, it is that database name that requires additional settings such as `USER`, `PASSWORD`, `HOST`, `PORT` and so on to build the connection string.

### Migrations

An app may have models whose data are stored in database.

Django uses `migration` to manage database schema changes. A migration consists of SQL statements to create tables and data for an app. Whenever you change data models, Django can create a new migration for the changes.

Django provides following commands to manage migrations:

- `python3 manage.py showmigrations`: shows all migrations in a project.
- `python3 manage.py makemigrations`: creates new migrations based on the changes detected to your models.
- `python3 manage.py sqlmigrate app_label migration_name`: displays the SQL commands for the named migration.
- `python3 manage.py migrate`: apply pending migrations to the database.

### Built-in Apps

Django framework comes with a number of built-in apps that provide common services for a typical web site. The `INSTALLED_APPS` item in `settings.py` has the list of activated applications:

- `django.contrib.admin`: The administration site for this project.
- `django.contrib.auth`: an app provides built-in support authentication.
- `django.contrib.contenttypes`: an app provides built-in support for content types.
- `django.contrib.sessions`: an app provides built-in support for session management.
- `django.contrib.messages`: an app provides built-in support for messaging.
- `django.contrib.staticfiles`: an app provides built-in support for managing static files.

### Initialize Database for Built-in Apps

Django has built-in migrations for built-in apps thus there is no need to run create migrations for built-in apps.

To see the built-in migrations, run `python3 manage.py showmigrations`

To initialize database for built-in apps who use models, run `python3 manage.py migrate`. The command applies migrations that create tables and initialization data for activated built-in apps.

For those who are familiar with database administration, you can use `django-admin dbshell` or `python3 manage.py dbshell` to run the command-line client for the specified database engine.

For SQLite, this runs `sqlite3` command line client, also called a _shell_.

## Model

To define a table schema and related database operations, you define a new subclass of `models.Model`.

Django derives database migrations from model definition, thus there is only a single source definition of application data.

If you change a data model, Django can create updated migrations for the changes. You can even roll back changes in some cases.

### Creating Models

In the polls app, there are two models: _Question_ and _Choice_. Adding following definitions in `polls/models.py` file.

- Each class inherits from `models.Model` class that provides many data access methods.
- Each field is defined as a class attribute.
- Each field is a descriptor defined in `models`.
  - a defined class attribute is read/set as an instance attribute
  - there are different descriptor types such as `CharField`, `DataTimeField`, and so on.
- The `models.ForeignKey` defines a foreign key that links an instance of `Choice` to an instance of `Question`.
  - It is a one-to-many relationship: one instance of `Question` is mapped to more than one instances of `Choice`.
  - The `on_delete` means that if an instance of `Question` is deleted, all its associated instances of `Choice` are deleted automatically.

```python
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

```

### Install the App

Django creates table schema and database access API based on app model definitions.

You need to add the configuration class of polls app, i.e., `"polls.apps.PollsConfig",` to top of the list in the `INSTALLED_APPS` item in the project setting file.

Then create migration from the app models using command `python3 manage.py makemigrations polls`. It creates a migration file in `polls/migrations/0001_initial.py` that has the migration code.

You can use the command `python3 manage.py sqlmigrate polls 0001` to check the SQL statements that to be applied to the database.

Finally, run `python3 manage.py migrate` to apply the migration that creates the database tables.

In your database shell (`python3 manage.py dbshell`), run `.tables` to list all created tables. The two tables for `polls` app are: `polls_question` and `polls_choice`, i.e., app name, underscore, and model class name, all in lower cases.

### Django Data API

The `models.Model` class provides database access methods for all model classes. The Django [Making queries document](https://docs.djangoproject.com/en/4.2/topics/db/queries/) has many examples.

Django provides a Python shell to interact with the project. Run `python3 manage.py shell` to execute the project Python shell.

```python
from polls.models import Choice, Question
from django.utils import timezone

# create an object, save to database, query its attributes
q = Question(question_text="How are you?", publish_date=timezone.now())
q.save()
q.id   # 1
q.question_text # "How are you?"

# update the record with new question text
q.question_text = "How old are you?"
q.save()

# get all questions in the database
Question.objects.all() # <QuerySet [<How old are you?>]>

# query by id
q = Question.objects.get(pk=1)
q.was_published_recently() # True

# the choice table can be accessed from a question
q.choice_set.all() # <QuerySet []>

# create three choices
c1 = q.choice_set.create(choice_text="28", votes=0)
c2 = q.choice_set.create(choice_text="35", votes=0)
c3 = q.choice_set.create(choice_text="15", votes=0)

# query choice attribute
c3.question # <Question: How old are you?>

# query choices from its question
q.choice_set.all() # <QuerySet [<Choice: 28>, <Choice: 35>, <Choice: 15>]>

q.choice_set.count() # 3

# delete one, it returns the number of objects deleted and a dictionary with the number of deletions per object type.
c2.delete() # (1, {'polls.Choice': 1})

# how many left
q.choice_set.count() # 2
```

### Django Admin

Django provides the ``django.contrib.admin` app to administrate the project. This is an internal site used by Web administrator.

You need to create a administrator account to use it.

Run `python manage.py createsuperuser` to create an account by filling username, email address and password.

Then you can access the internal admin site using `http://localhost:8000/admin`. By default, you can only manage users and groups after login.

### Manage Models

To let administrator to manage your app models, you need to register the models.

In `polls/admin.py`, add following lines and you can manage the registered models.

```python
# polls/admin.py

from django.contrib import admin

from .models import Question

admin.site.register(Question)

```

## View

A Django view processes requests and returns a `HttpResponse` object or raises an exception. To generate response content, it may use a template system. Django comes with a default template engine but you can use other engines.

From a developer's point of view, a view is a function or class that create Web pages.

### Create Views

There are two steps to create a view: define the view function/class and configure an URL pattern for the view.

After adding the following code, run the command `python3 manage.py runserver` to check that the URLs and views work.

```python
# polls/view.py

def detail(request, question_id):
    response = f"Detail view for {question_id}"
    return HttpResponse(response)


def results(request, question_id):
    response = f"Results view for {question_id}"
    return HttpResponse(response)


def vote(request, question_id):
    response = f"Vote view for {question_id}"
    return HttpResponse(response)

```

```python
# polls/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

```

### Django Template

A template has static content and placeholders or logic controls of dynamic data. A template uses special syntax for data display and logic controls.

By default, Django find templates in the `templates` directory of each app. It is a best practice to put a template in a folder in the `templates` directory because you may have utility templates such as layouts. For example, the path for polls app's `index.html` template file is `templates/polls/index.html`. You use the name `polls/index.html` to load the template into a view.

Django use `{}` to include data and logic. The data is also called the _context_ of the template. The `templates/polls/index.html` uses the `latest_question_list` context to create the HTML content.

```python
<!-- polls/templates/polls/index.html -->
{% if latest_question_list %}
<ul>
  {% for question in latest_question_list %}
  <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
  {% endfor %}
</ul>
{% else %}
<p>No polls are available.</p>
{% endif %}

```

### The `index` View

The `index` view fetches data from database and render the template into HTML response page.

```python
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-publish_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

```

### The `render()` Shortcut

It is a common pattern to load a template file, apply a context and return an `HttpResponse` object. Django provides a shortcut `render()` function to apply a context to a template and return an `HttpResponse` object.

The previous code could be simplified as the following:

```python
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-publish_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

```

### Rasing an Error

In the detail view, if Django couldn't find the question for the specified id, it makes sense to raise a 404 exception to let the user know that the requested object is not found.

The detail view uses a `polls/detail.html` template whose context is, not a surprise, a question.

```python
<!-- polls/templates/polls/detail.html -->
<h1>{{ question.question_text }}</h1>
<ul>
  {% for choice in question.choice_set.all %}
  <li>{{ choice.choice_text }}</li>
  {% endfor %}
</ul>

```

```python
# polls/views.py

from django.shortcuts import get_object_or_404, render

from .models import Question

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

```

### Removing Hardcoded URLs

The `polls/index.html` template has a hardcoded URL link for each question: `<a href="/polls/{{ question.id }}/">{{ question.question_text }}</a>`.

The path pattern `<int:question_id>/` is defined in `polls.urls` module. The pattern may change during the development, for example, `changed/<int:question_id>/whatever`. Then the hardcoded URL link in template will be broken.

To remove hardcoded URLs and to have a single source of path definition, you can use path name and `{% url ... %}` template tag.

The link becomes `<a href="{% url 'detail' question.id %}">{{ question.question_text }}</a>`

### URL Namespaces

The link such as `"{% url 'detail' question.id %}"` works well if you only have one `detail` view. If there are more than one `detail` view in different apps, Django cannot differentiate them.

As a best practice, it is better to give each app an URL namespace. It is done by setting `app_name` in an app's `urls.py` file.

Adding `app_name = "polls"` to the `polls/urls.py` file before the definition of URL patterns.

With the new namespace, the link in `polls/index.html` becomes `<a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a>`

## Form

A Web browser is a client that send request to a Web server and displays an HTML page returned from the server. The client can send data to the backend server using a Web _form_.

The `<form>...</form>` tag specifies a number of things to submit data:

- a URL: the target view for this data input.
- an action: an HTML action, default is `post`.
- CSRF token: a unique token generated by the server to protect server from _Cross Site Request Forgeries_ attack.
- One or more data fields and labels to let user input data.
- A submit button.

### Create a Form

The polls app creates a form in `detail` view to submit vote for a question.

It specifies the target path using the template tag `{% url 'polls:vote' question.id %}`. The view is specified with a special syntax of `'polls:vote'`.

```python
<!-- polls/template/polls/detail.html -->
<form action="{% url 'polls:vote' question.id %}" method="post">
  {% csrf_token %}
  <fieldset>
    <legend>
      <h1>{{ question.question_text }}</h1>
    </legend>

    {% if error_message %}
      <p><strong>{{ error_message }}</strong></p>
    {% endif %}

    {% for choice in question.choice_set.all %}
      <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
      <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
  </fieldset>

  <input type="submit" value="Vote">
</form>

```

### Handle Form Data

The `detail` view defines a form submitted to the `vote` view for a question.

Because the input field has a name `"choice"`, you can fetch the value using this name `request.POST["choice]`.

A user may click `Back` button in Browser after submission, it is a best practice to alway return an `HttpResponseRedirect` after successfully dealing with posted data.

The `HttpResponseRedirect` uses a redirect URL. When you need a URL from a view name, you can use `reverse()` function. The `reverse("polls:results", args=(question.id,))`

```python
# polls/views.py

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question

...

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

```

### The `results` View

The `results` shows the voted results for a question.

```python
# polls/view.py

from django.shortcuts import get_object_or_404, render

...

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

```

### The `results` Template

The `results` template defines the content of the view. Django template comes with a `pluralize` filter that you can apply to an object to transform its value. It adds a plural suffix, often `"s"` if the value is not `1`, `"1"`, or an object of length `1`

```python
<!-- polls/templates/polls/results.html -->
<h1>{{ question.question_text }}</h1>

<ul>
  {% for choice in question.choice_set.all %}
  <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
  {% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>

```

## Generic View

Django provides many utility functions/classes to simplify Web development.

Two common patterns in development are

- displaying a list of objects
- showing the details of an object

Django abstract these into so-called generic views to remove redundant code.

To use generic views, you define view classes that inherit from an appropriate generic view. Django will do the heavy lifting and let you customize the view behavior.

### View Classes

In the `polls` app, the `index` view displays a list of questions. You define a `IndexView` that inherits from `generic.ListView`.

The `detail` view and `results` view display the details of an object. You define `DetailView` and `ResultView` that inherit from `generic.DetailView`.

Both generic views will retrieve the objects from database and apply them to the corresponding templates.

You can customize the generic views by define methods in your views. For example, the `IndexView` fetches the list of objects in a specific order.

```python
# polls/views.py

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-publish_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

...

```

### Amend URLs

The generic views have many naming conventions for templates and URL paths.

For example, the default template name for a model is `<model_name>_list.html`. If you don't use the default name, you should set the `template_name` class attribute.

By convention, Django uses `pk` as the generic name as the parameter for object key. `pk` is an abbreviation of `Primary Key` that is an unique key in relational database table.

Each view class has an `as_view()` method that create an instance of the class.

```python
# polls/urls.py

from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

```
