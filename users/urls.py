from django.urls import path
from users import views


urlpatterns = [
    path('signup/', views.signup, name='singup'),
    path('login', views.signin, name='login'),
    path('logout/', views.logOut, name='logout'),
    path('account/', views.account, name='account'),
    path('profile/<str:id>', views.profile, name='profile'),
]
