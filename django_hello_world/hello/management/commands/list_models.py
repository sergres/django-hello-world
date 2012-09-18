from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = ''
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        self.stdout.write('models: M1, M2, M3\n')


