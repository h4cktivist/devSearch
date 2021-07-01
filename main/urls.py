from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>', views.singleProject, name='single-project'),
]
