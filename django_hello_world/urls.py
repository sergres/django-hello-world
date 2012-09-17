from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.defaults import *



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'django_hello_world.hello.views.home', name='home'),
    url(r'^requestslog$', 'django_hello_world.hello.views.requestslog'),
    url(r'^view_edit$', 'django_hello_world.hello.views.view_edit'),
    url(r'^accounts/logout/$', 'django_hello_world.hello.views.my_logout'),
    url(r'^custom_tag$', 'django_hello_world.hello.views.custom_tag'),
    # url(r'^django_hello_world/', include('django_hello_world.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'hello/login.html'}),


)
