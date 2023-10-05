from django.contrib import admin

from .models import Choice, Question

admin.site.register([Question, Choice])
