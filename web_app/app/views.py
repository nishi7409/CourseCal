from django.http import HttpResponse, HttpRequest, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.conf import settings
from .models import *
from django import views
from django.core import mail
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django import forms
import json
from .microservices.googleCal import urlGenerator

# home page
def index(request):
    return render(request, 'index.html', {})

# sign up page
def signUp(request):
    return render(request, 'sign-up.html', {})

def save_university(request):
    if request.method == "POST":
        newUni = University(name="Rensselaer Polytechnic Institute", domain="rpi.edu", registeredStudents=0)
        newUni.save()
    else:
        pass

def save_student(request):
    if request.method == "POST":
        uniqueURL = URLCalendar(calendar=urlGenerator.createURL())
        newStud = Student(name="Nishant Srivastava", email="srivan@rpi.edu", phone_num=5186182796, calendar_link=uniqueURL)
        newStud.save()
    else:
        pass

def register(request):
    pass

def login(request):
    pass

def otp():
    pass
