from django.db import models
from django.forms import ModelForm, Form, DateInput 
from django.conf import settings
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
    image = models.ImageField(upload_to='photos/', blank=True)

    @property
    def filename(self):
        return self.file.name.rsplit('/', 1)[-1]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'email',)


class MyDateInput(DateInput):
    def __init__(self, attrs=None, format=None):
        super(MyDateInput, self).__init__(attrs, format)

    def render(self, name, value, attrs=None):
        media = '<link rel="stylesheet" href="' + settings.STATIC_URL +\
            'jquery/themes/base/jquery.ui.all.css">' + \
            '<script src="' + settings.STATIC_URL + \
            'jquery/jquery-1.8.0.js"></script>' + \
            '<script src="' + settings.STATIC_URL + \
            'jquery/ui/jquery.ui.core.js"></script>' + \
            '<script src="' + settings.STATIC_URL + \
            'jquery/ui/jquery.ui.widget.js"></script>' + \
            '<script src="' + settings.STATIC_URL + \
            'jquery/ui/jquery.ui.datepicker.js"></script>' + \
            """<script>
            $(function() {
                $( "#id_date_birth1" ).datepicker();
            });
            $(function() {
                $( "#id_date_birth" ).datepicker();
            });
            </script>
"""
        return media + super(MyDateInput, self).render(name, value, attrs)


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('date_birth',
                  'jabber',
                  'skype',
                  'other_contacts',
                  'image',
                  'bio',)
        widgets = {'date_birth': MyDateInput, }


class RequestsStorage(models.Model):
    REQUEST_TYPE_CHOISES = (
        ('G', 'GET'),
        ('P', 'POST'))

    time = models.DateTimeField(auto_now=True)
    body = models.CharField(max_length=8192)
    method = models.CharField(default="G", max_length=1,
                              choices=REQUEST_TYPE_CHOISES)


class SignalStorage(models.Model):
    SIGNAL_TYPE_CHOISES = (
        ('C', 'create'),
        ('D', 'delete'),
        ('E', 'edit'))

    class Meta:
        verbose_name = ('Storage of all singals')
        verbose_name_plural = ('SignalStorages')

    def __unicode__(self):
        pass

    """docstring for SignalStorage"""
    def __init__(self, action):
        super(SignalStorage, self).__init__()
        self.action = action

    action = models.CharField(max_length=1, choices=SIGNAL_TYPE_CHOISES)
    time = models.DateTimeField(auto_now=True)
    model_name = models.CharField(max_length=300)

