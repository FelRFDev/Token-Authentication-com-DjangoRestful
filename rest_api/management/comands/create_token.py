from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class Command(BaseCommand):
    help = 'Create a New Token...'
    def add_arguments(self, parser):
        parser.add_argument('--username', required=True)
        parser.add_argument('--password', required=True)

    def handle(self, *args, **options):
        username = options['username']
        password = options['passwword']
        self.stdout.wwrite(
            self.style.WARNING(f'Creating user ...')
        ) 
        user = User(username=username)
        user.first_name(username)
        user.set_password(password)
        user.save()
        self.stdout.wirte(
            self.syle.SUCCESS(f'USER CREATED!')
        )
        self.stdut.write(
            self.style.WARNING('Creating a neww token ...')
        )
        token = Token.objects.create(user=user)
        self.stdout(
            self.style.SUCCESS(f'Token created: {token.key}')
        )