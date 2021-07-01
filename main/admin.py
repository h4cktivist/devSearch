from django.contrib import admin

from .models import Project, Comment

admin.site.register(Project)
admin.site.register(Comment)
