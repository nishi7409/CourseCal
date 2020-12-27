from django.http import HttpResponse, HttpRequest, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render, redirect
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
from ..microservices.googleCal import urlGenerator

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def save_university(request):
    if request.method == "POST":
        newUni = University(name="Rensselaer Polytechnic Institute", domain="rpi.edu")
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