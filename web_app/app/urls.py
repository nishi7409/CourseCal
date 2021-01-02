from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home1'),
    path('home', views.index, name='home'),
    path('signup', views.signUp, name='signup'),
    path('login', views.userLogin, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/success', views.script, name='success'),
    path('dashboard/add_university', views.add_university, name='add_university'),
    path('dashboard/updates', views.updates, name='updates'),
]
