from django.db import models
from django.utils import timezone
import datetime
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class Info(models.Model):
    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    destination=models.CharField(max_length=100)
    checkin=models.DateField()
    checkout=models.DateField()
    rooms= models.IntegerField(default=1)
    adult= models.IntegerField(default=1)
    child= models.IntegerField(default=0)
    pan = models.CharField(max_length=10, blank=True, null=True, validators=[alphanumeric], unique=True)
    first = models.CharField(max_length=100, default='null')
    last = models.CharField(max_length=100, default='null')
    email = models.CharField(max_length=150, default='null')
    phone = models.IntegerField(default=0)