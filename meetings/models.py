from django.db import models
from datetime import datetime
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=150)
    floor = models.IntegerField()
    number = models.IntegerField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.number = self.floor * 100 + self.number
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f"Room: {self.name}, {self.floor}, {self.number}"


class Meeting(models.Model):
    title = models.CharField(max_length=150)
    data = models.DateField()
    start_time = models.TimeField(default=datetime.now())
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"Meeting: {self.title}, {self.data}; {self.start_time}"

