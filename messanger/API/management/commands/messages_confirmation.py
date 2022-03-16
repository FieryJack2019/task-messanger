from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.utils import timezone
import json


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('token', type=str)

    def handle(self, *args, **options):
        interval = IntervalSchedule.objects.filter(every=5, period=IntervalSchedule.SECONDS).first()
        if not interval:
            interval = IntervalSchedule(every=5, period=IntervalSchedule.SECONDS)
            interval.save()
        name = 'Confirmation Messages'
        PeriodicTask.objects.create(
            name=name,
            task='confirmation_messages',
            interval=interval,
            args=json.dumps([options['token']]),
            start_time=timezone.now(),
        )