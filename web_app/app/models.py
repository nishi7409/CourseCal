from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    domain = models.CharField(max_length=20, null=False, blank=False)
    # registeredStudents = modals.IntegerField()

class Student(models.Model):
    email = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    phone_num = models.IntegerField(null=False, blank=False)
    calendar_link = models.ForeignKey("URLCalendar", on_delete=models.CASCADE)

class URLCalendar(models.Model):
    calendar = models.CharField(max_length=200, null=False, blank=False)

def saveUni(self):
    pass