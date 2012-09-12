from django.db import models
from django.forms import ModelForm

from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    date_birth = models.DateField()
    bio = models.TextField()
    jabber =  models.EmailField()
    skype = models.CharField(max_length=30)
    other_contacts = models.TextField()

class UserAndProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        

class RequestsStorage(models.Model):
    REQUEST_TYPE_CHOISES = (
    ('G','GET'),
    ('P','POST'),
    )
    time = models.DateTimeField(auto_now=True)
    body = models.CharField(max_length=8192)
    method = models.CharField(default="G", max_length=1, choices=REQUEST_TYPE_CHOISES)

