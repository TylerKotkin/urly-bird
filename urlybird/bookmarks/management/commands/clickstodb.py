from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from random import choice
from faker import Faker
from bookmarks.models import Worm, Click


class Command(BaseCommand):

    def handle(self, *args, **options):
        fake = Faker()

        # 3. Make some fake clicks
        for _ in range(12000):
            worm = choice(Worm.objects.all())
            click = Click(
                timestamp=make_aware(fake.date_time_between(
                    start_date=worm.timestamp, end_date="now")),
                user=choice(User.objects.all()),
                worm=worm
            )
            click.save()
