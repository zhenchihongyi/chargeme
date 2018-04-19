from django.db import models
from django.utils import timezone

class Order(models.Model):
    id=models.CharField(primary_key=True,max_length=16)
    user_id = models.ForeignKey('auth.User')
    station_id = models.IntegerField()
    battery_id = models.IntegerField()
    start_time = models.DateTimeField(
            default=timezone.now)
    end_time = models.DateTimeField()
    price=models.PositiveIntegerField()
    memo = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.id