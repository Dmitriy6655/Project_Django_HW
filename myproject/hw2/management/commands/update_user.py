from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Update user email by id."

    def add_arguments(self, parser):

        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('email', type=str, help='User email')

    def handle(self, *args, **kwargs):

        pk = kwargs.get('pk')
        email = kwargs.get('email')
        user = User.objects.filter(pk=pk).first()
        user.email = email
        user.save()
        self.stdout.write(f'{user}')
