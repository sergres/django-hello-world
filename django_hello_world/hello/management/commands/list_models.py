from django.core.management.base import BaseCommand 
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    args = ''
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        for ct in ContentType.objects.all():
            m = ct.model_class()
            print "%s.%s\t%d" % (m.__module__, m.__name__, m._default_manager.count())


