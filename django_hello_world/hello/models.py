from django.db import models

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
