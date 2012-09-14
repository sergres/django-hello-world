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
    # If the form has been submitted.
    if (request.method == 'POST'
       and request.user.is_authenticated()) :  
        # Get instances of objects, they will be saved
        user = User.objects.get(pk=1)
        profile = user.get_profile()

        form_user = UserForm(request.POST, instance=user)
        form_profile = ProfileForm(request.POST, instance=profile)

        if form_user.is_valid() and form_profile.is_valid():
            from django.core.files.base import ContentFile
            form_profile.save()
            if 'image' in request.FILES:
                file_content = ContentFile(request.FILES['image'].read())
                profile.image.save(request.FILES['image'].name, file_content)
            form_user.save()
    else:
        users = User.objects.filter()
        user = users[0]
        profile = user.get_profile()
        form_user = UserForm(instance=user)
        form_profile = ProfileForm(instance=profile)
    
    if request.user.is_authenticated() :
        return {'profile': form_profile, 
                'user': form_user,
                'request': request,
                'current_image': profile.image}
    else:
        return {'profile': profile,
                'user': user,
                'request': request,
                'current_image': profile.image}
