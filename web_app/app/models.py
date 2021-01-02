from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, validate_email
import json

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    domain = models.CharField(max_length=20, null=False, blank=False)
    registeredStudents = models.IntegerField(default=0, null=False, blank=False)

class Student(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    phone_num = models.CharField(max_length=200, null=False, blank=False)
    status = models.IntegerField(default=0, null=False, blank=False)
    admin = models.BooleanField(default=False)
    calendar_link = models.CharField(max_length=600, null=False, blank=False)

class UserForm(forms.ModelForm):
    """
        UserForm is the form for user registration
    """
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = (
            'email',
        )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # will raise a ValidationError if email is invalid
        validate_email(email)
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two passwords do not match", 'password_mismatch')
        return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.username = user.email
        if commit:
            user.save()
        return user


# class UserProfile(models.Model):
#     # links the UserProfile to a User model
#     # User model is Django's authentication model: contains username, password, etc.
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     creation_time = models.DateTimeField()
