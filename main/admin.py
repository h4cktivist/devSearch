from django.contrib import admin

from .models import Project, Comment, Message

admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Message)
