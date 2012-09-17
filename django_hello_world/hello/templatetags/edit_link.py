from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def edit_link(object):
    #return value.lower(
    url = reverse('admin:%s_%s_change' %
        (object._meta.app_label, object._meta.module_name), args=[object.id])
    #url = "admin"
    #print object.__class__.__name__
    return u'<a href="%s">Edit %s</a>' % (url,  object.__class__.__name__)
