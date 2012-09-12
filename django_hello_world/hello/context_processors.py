from django.conf import settings

def my_context_processor(request):
    return { 'settings': settings }
