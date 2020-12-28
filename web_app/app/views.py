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
    if request.method == "POST":
        name = request.post['name']
        email = request.post['email']
        phoneNum = request.post['phoneNum']

        form = UserForm(data = request.POST)

        if form.is_valid():
            user = form.save()

            user.is_active = False
            user.save()

            uniqueURL = URLCalendar(calendar=urlGenerator.createURL())
            newStudent = Student(name=name, email=email, phone_num=phoneNum, status=False, calendar_link=uniqueURL)
            newStudent.save()

            html_msg = f"<p><a href='{request.build_absolute_uri('/register/confirm/')}{user.id}'>Click here to activate your account!</a></p>"
            mail.send_mail("Account Confirmation", "Please confirm your account registration.", settings.EMAIL_HOST_USER, [user.email], html_message=html_msg)
        else:
            pass
    else:
        form = UserCreationForm()
    return render(request, 'sign-up.html', {})

# sign up page
def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        # valid user
        if user:
            # user is valid, active, and authenticated
            if user.is_active:
                login(request, user)
                request.session['is_login'] = True
                request.session['user_name'] = username
                # user_id = User.objects.filter(username = username).values('id').first()
                # request.session['user_id'] = user_id['id']
                return render(request, 'dashboard.html', {'error': 'Success and account is activated'})
            
            # user is valid, but not active
            else:
                return render(request, 'login.html', {'error': 'Success, but account is deactivated'})

        # user doesn't exist
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})

    return render(request, 'login.html', {})

def save_university(request):
    if request.method == "POST":
        newUni = University(name="Rensselaer Polytechnic Institute", domain="rpi.edu", registeredStudents=0)
        newUni.save()
    else:
        pass


def register(request):
    pass

def otp():
    pass
