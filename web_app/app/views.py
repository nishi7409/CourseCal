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
from .microservices.googleCal import urlGenerator
import discord
# from discord import Webhook, RequestsWebhookAdapter
import json
import requests

# home page
def index(request):
    return render(request, 'index.html', {})

# sign up page
def signUp(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phoneNum = request.POST['phoneNumber']
        print("HELLO!")
        form = UserForm(data = request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            print("gets here")

            user.is_active = False
            user.save()

            # uniqueURL = URLCalendar(calendar=urlGenerator.createURL(name, email))
            # uniqueURL.save()
            uniqueURL = urlGenerator.createURL(name, email)
            # print("Unique URL is " + uniqueURL)
            newStudent = Student(name=name, email=email, phone_num=phoneNum, calendar_link=uniqueURL)
            newStudent.save()

            print("Saved student object")
            
            # https://discordpy.readthedocs.io/en/latest/api.html#discord.Webhook
            webhookURL = "https://discord.com/api/webhooks/793900861436461077/y4vdzi7E9vitmOjtHAiCIVgTnvP5__rIqI_y3b4a0i-9hd-nLXygKt_gTdaa_yL4QmPJ"
            webhook = discord.Webhook.from_url(webhookURL, adapter=discord.RequestsWebhookAdapter())
            embed = discord.Embed(title="New User", description="A new user has registered with CourseCal!", colour=0x47ff8e)
            embed.add_field(name="Name", value=name)
            embed.add_field(name="Email", value=email)
            embed.add_field(name="Calendar ID", value=uniqueURL)
            webhook.send(embed=embed)

            html_msg = f"<p><a href='{request.build_absolute_uri('/register/confirm/')}{user.id}'>Click here to activate your account!</a></p>"
            mail.send_mail("Account Confirmation", "Please confirm your account registration.", settings.EMAIL_HOST_USER, [user.email], html_message=html_msg)
            return render(request, 'sign-up.html', {"success":"Check your email, I sent you an account confirmation link!"})
        else:
            return render(request, 'sign-up.html', {"error": "Error: There was a form error. Retype the above information and resubmit!"})
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
                return render(request, 'login.html', {'success': 'Success and account is activated'})
            
            # user is valid, but not active
            else:
                return render(request, 'login.html', {'success': 'Success, but account is deactivated'})

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
