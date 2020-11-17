from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    address = models.CharField(max_length=500, null=False, blank=False)
    phone_num = models.IntegerField(max_length=10 null=False, blank=False, default="-1")
    domain = models.CharField(max_length=20, null=False, blank=False)

class Student(models.Model):
    username = models.CharField(max_length=10, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    phone_num = models.IntegerField(max_length=10 null=False, blank=False)
    calendar_link = models.ForeignKey(URLCalendar, on_delete=models.CASCADE)

class URLCalendar(models.Model):
    calendar = models.CharField(null=False, blank=False)
