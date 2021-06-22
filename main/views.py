from django.shortcuts import render
from django.core.paginator import Paginator

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
