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
    users = User.objects.filter()
    user = users[0]
    form_profile = UserProfile(user.get_profile())
    return {'form_profile': form_profile}
