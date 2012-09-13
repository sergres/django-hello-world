from annoying.decorators import render_to
from django.contrib.auth.models import User
from django_hello_world.hello.models import *


@render_to('hello/home.html')
def home(request):
    users = User.objects.filter()
    return {'users': users}


@render_to('hello/requestslog.html')
def requestslog(request):
    requests = RequestsStorage.objects.order_by("-time").filter()[:10]
    return {'requests': requests}


@render_to('hello/view_edit.html')
def view_edit(request):
    if request.method == 'POST':  # If the form has been submitted...
        user = User.objects.get(pk=1)
        profile = user.get_profile()

        form_user = UserForm(request.POST, instance=user)
        form_profile = ProfileForm(request.POST, instance=profile)
        print form_profile.errors
        if form_user.is_valid() and form_profile.is_valid():
            form_profile.save()
    else:
        users = User.objects.filter()
        user = users[0]
        profile = user.get_profile()
        form_user = UserForm(instance=user)
        form_profile = ProfileForm(instance=profile)

    return {'form_profile': form_profile, 'form_user': form_user}
