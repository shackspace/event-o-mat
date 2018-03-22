from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=140, unique=True)

    def __str__(self):
        return 'Room: {name}'.format(name=self.name)


class Series(models.Model):
    name = models.CharField(max_length=140)
    start = models.TimeField(null=True)
    end = models.TimeField(null=True)
    room = models.ForeignKey(to=Room, on_delete=models.PROTECT, null=True, related_name='series')

    def __str__(self):
        return 'Series: {name}'.format(name=self.name)


class Event(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)

    start = models.DateTimeField()
    end = models.DateTimeField()

    publish = models.BooleanField(default=False)
    room = models.ForeignKey(to=Room, on_delete=models.PROTECT, related_name='events')
    series = models.ForeignKey(to=Series, on_delete=models.PROTECT, related_name='events')
    keyholder = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='keyholder_events')

    def __str__(self):
        s = 'Event: {name}'.format(name=self.name)
        if self.series:
            s += ' ({series})'.format(series=self.series.name)
        return s


class Attendance(models.Model):
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE, related_name='attendances')
    user = models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='attendances')
    state = models.CharField(
        max_length=5,
        choices=(('yes', 'yes'), ('no', 'no'), ('maybe', 'maybe')),
        default='yes',
    )

    def __str__(self):
        return 'Attentdance: {user} at {event} ({state})'.format(user=self.user.username, event=self.event.name, state=self.state)
