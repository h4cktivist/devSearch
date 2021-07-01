from django.urls import path
from users import views


urlpatterns = [
    path('signup/', views.signup, name='singup'),
    path('login', views.signin, name='login'),
    path('logout/', views.logOut, name='logout'),
    path('account/', views.account, name='account'),
    path('profile/<str:username>', views.profile, name='profile'),

    path('account/edit-account', views.editAccount, name='edit-account'),

    path('account/add-skill', views.addSkill, name='add-skill'),
    path('account/edit-skill/<int:id>', views.editSkill, name='edit-skill'),
    path('account/delete-skill/<int:id>', views.deleteSkill, name='delete-skill'),

    path('account/add-project', views.addProject, name='add-project'),
    path('account/edit-project/<int:id>', views.editProject, name='edit-project'),
    path('account/delete-project/<int:id>', views.deleteProject, name='delete-project'),

]
