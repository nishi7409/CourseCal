from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('signup', views.signUp, name='signup'),
    path('login', views.signUp, name='login'),
]
