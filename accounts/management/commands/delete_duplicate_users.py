from django.core.management.base import BaseCommand
from accounts.models import User
from django.db.models import Count

class Command(BaseCommand):
    help = 'Delete duplicate users based on phone numbers.'

    def handle(self, *args, **kwargs):
        duplicates = User.objects.values('phone_number').annotate(count=Count('id')).filter(count__gt=1)

        for duplicate in duplicates:
            phone_number = duplicate['phone_number']
            users = User.objects.filter(phone_number=phone_number).order_by('id')[1:]

            for user in users:
                user.delete()

        self.stdout.write(self.style.SUCCESS('Duplicate users deleted successfully.'))
