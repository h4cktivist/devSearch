from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Project
from django.contrib.auth.models import User
from django.db.models import Q


def index(request):
    if request.method == 'POST':
        search_data = request.POST.get('search')
        users = User.objects.filter(Q(first_name__contains=search_data) | Q(last_name__contains=search_data))
    else:
        users = User.objects.all()

    paginator = Paginator(users, 6)
    page = request.GET.get('page', 1)
    page_users = paginator.get_page(page)

    return render(request, 'index.html', {'users': page_users})


def projects(request):
    if request.method == 'POST':
        search_data = request.POST.get('search')
        projects = Project.objects.filter(title__contains=search_data)
    else:
        projects = Project.objects.order_by('date')

    paginator = Paginator(projects, 6)
    page = request.GET.get('page', 1)
    page_projects = paginator.get_page(page)

    return render(request, 'projects.html', {'projects': page_projects})


def singleProject(request, id):
    project = Project.objects.get(id=id)
    if request.method == 'POST':
        project.comment_set.create(
            author=request.user,
            text=request.POST.get('message')
        )
        return redirect('single-project', project.id)

    return render(request, 'single-project.html', {'project': project})
