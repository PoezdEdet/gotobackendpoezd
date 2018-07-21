from django.contrib import admin

from main.models import Choice, Question
admin.site.register(Question)
admin.site.register(Choice)