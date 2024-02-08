from django.core.management.base import BaseCommand
from hw2.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='Ivan', email='ivan55877@example.com', phone=+79101857223, addres="California, street 45, home 11",
                    date_reg='')
        user.save()
        self.stdout.write(f'{user}')
