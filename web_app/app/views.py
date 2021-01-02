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
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django import forms
from .microservices.googleCal import urlGenerator
import discord
import json
import requests
import os

# home page
def index(request):
    return render(request, 'index.html', {})

# sign up page
def signUp(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('dashboard')

    data = University.objects.all()

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
            webhookURL = os.getenv("WEBHOOK_URL")
            webhook = discord.Webhook.from_url(webhookURL, adapter=discord.RequestsWebhookAdapter())
            embed = discord.Embed(title="New User", description="A new user has registered with CourseCal!", colour=0x47ff8e)
            embed.add_field(name="Name", value=name)
            embed.add_field(name="Email", value=email)
            embed.add_field(name="Calendar ID", value=uniqueURL)
            webhook.send(embed=embed)

            html_msg = f"<p><a href='{request.build_absolute_uri('/register/confirm/')}{user.id}'>Click here to activate your account!</a></p>"
            mail.send_mail("Account Confirmation", "Please confirm your account registration.", settings.EMAIL_HOST_USER, [user.email], html_message=html_msg)
            return render(request, 'sign-up.html', {"success":"Check your email, I sent you an account confirmation link!", "universities": data})
        else:
            return render(request, 'sign-up.html', {"error": "Error: There was a form error. Retype the above information and resubmit!", "universities": data})
    return render(request, 'sign-up.html', {"universities": data})

# sign up page
def userLogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('dashboard')

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
                return HttpResponseRedirect('dashboard')
            
            # user is valid, but not active
            else:
                return HttpResponseRedirect('dashboard')

        # user doesn't exist
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})

    return render(request, 'login.html', {})

# logout user
@login_required
def logout(request):
    django_logout(request)
    return HttpResponseRedirect('home')

# dashboard page
@login_required
def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')

    data = University.objects.all()
    if request.method == "POST":
        return render(request, 'dashboard.html', {"universities": data})
    return render(request, 'dashboard.html', {"universities": data})

# updates page
@login_required
def updates(request):
    return render(request, 'updates.html', {})

# admin - save university page
@login_required
def add_university(request):
    if request.method == "POST":
        uni_name = request.POST['uni_name']
        uni_domain = request.POST['uni_domain']

        if University.objects.filter(name = uni_name).exists():
            # https://discordpy.readthedocs.io/en/latest/api.html#discord.Webhook
            webhookURL = os.getenv("WEBHOOK_URL")
            webhook = discord.Webhook.from_url(
                webhookURL, adapter=discord.RequestsWebhookAdapter())
            embed = discord.Embed(
                title="Error", description="[USER] tried to add an already existing university to the database", colour=0xff413b)
            embed.add_field(name="University name", value=uni_name)
            embed.add_field(name="University domain", value=uni_domain)
            webhook.send(embed=embed)

            return render(request, 'add_university.html', {"error": "The university already exists!"})

        if University.objects.filter(domain=uni_domain).exists():
            # https://discordpy.readthedocs.io/en/latest/api.html#discord.Webhook
            webhookURL = os.getenv("WEBHOOK_URL")
            webhook = discord.Webhook.from_url(
                webhookURL, adapter=discord.RequestsWebhookAdapter())
            embed = discord.Embed(
                title="Error", description="[USER] tried to add an already existing university to the database", colour=0xff413b)
            embed.add_field(name="University name", value=uni_name)
            embed.add_field(name="University domain", value=uni_domain)
            webhook.send(embed=embed)

            return render(request, 'add_university.html', {"error": "The university already exists!"})

        else:
            newUni = University(name=uni_name, domain=uni_domain)
            newUni.save()

            print("Saved university object")

            # https://discordpy.readthedocs.io/en/latest/api.html#discord.Webhook
            webhookURL = os.getenv("WEBHOOK_URL")
            webhook = discord.Webhook.from_url(
                webhookURL, adapter=discord.RequestsWebhookAdapter())
            embed = discord.Embed(
                title="New University", description="[USER] added a new university to the database", colour=0x47ff8e)
            embed.add_field(name="University name", value=uni_name)
            embed.add_field(name="University domain", value=uni_domain)
            webhook.send(embed=embed)

            return render(request, 'add_university.html', {"success": "Added university to the database, you should automatically be sent to the public university list in a few seconds!"})
    return render(request, 'add_university.html', {})

@login_required
def script(request):
    return render(request, 'success.html', {})
