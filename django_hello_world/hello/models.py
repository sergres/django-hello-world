from django.db import models
from django.forms import ModelForm, Form


from django.contrib.auth.models import User


class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    date_birth = models.DateField(blank=True)
    bio = models.TextField(blank=True)
    jabber = models.EmailField()
    skype = models.CharField(max_length=30, blank=True)
    other_contacts = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'email',)


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('date_birth',
                  'jabber',
                  'skype',
                  'other_contacts',
                  'image',
                  'bio',)


#class ImageForm(Form):
#        image = models.ImageField()


class RequestsStorage(models.Model):
    REQUEST_TYPE_CHOISES = (
        ('G', 'GET'),
        ('P', 'POST'))

    time = models.DateTimeField(auto_now=True)
    body = models.CharField(max_length=8192)
    method = models.CharField(default="G", max_length=1,
                              choices=REQUEST_TYPE_CHOISES)
