# Advanced Django

- Unit Test
- View Test
- View
- Template
- Forms

## Test

Django uses the `unittest` standard library and provides a class-based approach for unit tests.

To test a view, Python also provides a test client that simulates a Web browser to send `GET` or `POST` HTTP requests to the Web server and check the responses.

### Unit Test

Django creates a `tests.py` for each app to allow you write test classes.

A test class inherits from `TestCase` and define test methods.

For methods whose names start with `test`, `python3 manage.py test` will run those methods.

```python
# polls/tests.py

import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose publish_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(publish_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
            was_published_recently() returns False for questions whose publish_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(publish_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose publish_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(publish_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

```

### View Test

Django provides a test Client to simulate a user interacting with the code at the view level.

```python
from django.urls import reverse

def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, publish_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Questions with a publish_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a publish_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a publish_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a publish_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
```

## View

[View](https://docs.djangoproject.com/en/4.2/#the-view-layer) is the processing logic that takes user requests and returns responses. It has the following components

- URLs
- View Functions
- View Classes
- Middleware

### URLs

An elegant URL scheme is important for a high-quality web site.

Each site and each app have an `urs.py` that defines `urlpatterns` to map URL paths to views. Check [URLs document](https://docs.djangoproject.com/en/4.2/topics/http/urls/) for details.

An URL path supports typed named parts that are passed as kwargs arguments to the matching view.

An URL path supports pattern matches and customized argument converters.

### URL Examples

For the URL pattern

- `path("blogs/<int:year>/<int:month>/", my_view)`

For a request of

- `/blogs/2023/11`

`my_view` will be called as as

- `my_view(request, year=2023, month=11)`

### View Functions

A view function takes HTTP requests and return web responses.

Please check [Request and response objects document](https://docs.djangoproject.com/en/4.2/ref/request-response/) for request and response object details.

A response can be an HTML page, a plain text, a redirect, a 404 error, a JSON data, an image...

You can use view decorators to restrict allowed HTTP methods or add other features such as compression and caching.

### View Classes

A view class is a callable because it defines `__call__` special method.

A view class inherits from a provided generic base class that handles most common logics. Following are some common generic classes

- `View` handles URL linking, HTTP method dispatching.
- `RedirectView` handles an HTTP redirect
- `TemplateView` handles template rendering.

In many cases, you don't need to define a subclass, just use the provided generic views with specific arguments.

### A View Class Example

```python
# Use the generic view directly
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("about/", TemplateView.as_view(template_name="about.html")),
]

# Or create a subclass
class AboutView(TemplateView):
    template_name = "about.html"

urlpatterns = [
    path("about/", AboutView.as_view()),
]
```

### Class-based or Function-based View?

Compared to a view function, a view class is preferred because it can

- share common code in super classes.
- define specific HTTP methods (GET, POST, etc.) instead of functional-style conditional branching.

Please check [Class-based views document](https://docs.djangoproject.com/en/4.2/topics/class-based-views/) for more details.

## Template

A template contains the static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted.

Django use templates to create HTML from data. Django supports different template engines. It comes with a built-in one called **Django Template Language** (DTL) and Jinja2 engine.

DTL is used by Django’s contrib apps such as `admin` and others.

### Django Template Language (DTL)

A Django template is a text document or a Python string marked-up using the Django template language. It is rendered with a context. Rendering replaces variables with their values, which are looked up in the context, and executes tags. Everything else is output as is.

Basic constructs are:

- expression: `{{ }}`
- tag: `{% %}`
- comment: `{# #}`

### Variables

A context is a dict-like object mapping keys to values. A variable outputs a value from the context. Variables are surrounded by `{{` and `}}`. Attributes and index lookups are implemented with a dot notation.

### Tags

Tags provide logic in the rendering process. Tags are surrounded by `{%` and `%}`. For example: `{% csrf_token %}`

Please check [built-in tag reference](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#built-in-tag-reference).

Most tags accept arguments. For example: `{% cycle 'odd' 'even' %}`.

Some tags require beginning and ending tags. For example: `{% if user.is_authenticated %}Hello, {{ user.username }}.{% endif %}`.

### Common Tags

- `block` and `extends`: used in template inheritance
- `comment`: multi-line comments ignored by Django
- `debug`: for debug info
- `filter`: content transformation
- `for in` and `empty`: looping
- `if`: `in`, `not in`, `is`, `is not`, comparison and logic operations
- `include`: render another template, optionally passing keyword arguments.
- `lorem`: random text with specified length.
- `now`: current date and/or time
- `regroup as`: grouping
- `url`: create links from names

### Filters

Filters `|` transform the values of variables and tag arguments.

Django provides many filter functions such as `random`, `pluralize`, `title`, `slice`, `join` etc.

Please check [Built-in filter reference](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#built-in-filter-reference) for full list.

[`django.contrib.humanize¶`](https://docs.djangoproject.com/en/4.2/ref/contrib/humanize/) provides filters for adding a "human touch" to data.

## Forms

You can encode simple data like a page number into the URL paths.

HTML form provides an UI for rich data input including text, password, date, radio button, dropdown list and etc.

Django provides many utility functions to build form from data and process form data.

Please check [Forms document](https://docs.djangoproject.com/en/4.2/#forms) for details.

### Django Form Class

The `Form` class describes **form fields** and corresponding **UI widget**.

Form fields are classes that manage form data and perform validation in form submission.

Each form field is represented as an HTML input widget.

A form can be empty or pre-populated with default/existing data.

`ModelForm` is a subclass of `Form`. `ModelForm` make it very simple to build form from a `Model` class.

### A Form Example

The following code defines a form with a single text field that has a maximum length of `100`.

If all field values are valid, the `is_valid` is `True` and form data will be in the `cleaned_data` attribute.

```python
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
```

### Form UI

The form class only defines form fields. The form instance must be inside the HTML `<form>` element.

Let's put it into `name.html` file and link them in a `render` function.

```python
<form action="/your-name/" method="post">
  {% csrf_token %}
  {{ form }}
  <input type="submit" value="Submit">
</form>

```

```python
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "name.html", {"form": form})
```
