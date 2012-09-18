from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = ''
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        self.stdout.write('models: M1, M2, M3\n')
        from django.contrib.contenttypes.models import ContentType

        for ct in ContentType.objects.all():
            m = ct.model_class()
            print "%s.%s\t%d" % (m.__module__, m.__name__, m._default_manager.count())


