from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=140, unique=True)


class Series(models.Model):
    name = models.CharField(max_length=140)
    start = models.TimeField(null=True)
    end = models.TimeField(null=True)
    room = models.ForeignKey(to=Room, on_delete=models.PROTECT, null=True, related_name='series')


class Event(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)

    start = models.DateTimeField()
    end = models.DateTimeField()

    publish = models.BooleanField(default=False)
    room = models.ForeignKey(to=Room, on_delete=models.PROTECT, related_name='events')
    series = models.ForeignKey(to=Series, on_delete=models.PROTECT, related_name='events')
    keyholder = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='keyholder_events')


class Attendance(models.Model):
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE, related_name='attendances')
    user = models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='attendances')
    state = models.CharField(
        max_length=5,
        choices=(('yes', 'yes'), ('no', 'no'), ('maybe', 'maybe')),
        default='yes',
    )
