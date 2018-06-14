from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Room(models.Model):
    name = models.CharField(max_length=140, unique=True)

    def __str__(self):
        return 'Room: {name}'.format(name=self.name)


class Series(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)

    start = models.TimeField(null=True, blank=True)
    end = models.TimeField(null=True, blank=True)
    room = models.ForeignKey(to=Room, on_delete=models.PROTECT, null=True, blank=True, related_name='series')
    rrule = models.CharField(max_length=256, null=True, blank=True)
    keyholder = models.CharField(max_length=256, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    modified_by = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Series: {name}'.format(name=self.name)


class Event(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)

    start = models.DateTimeField()
    end = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    modified_by = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    modified_date = models.DateTimeField(auto_now=True)

    publish = models.BooleanField(default=False)
    room = models.ForeignKey(to=Room, on_delete=models.PROTECT, related_name='events')
    series = models.ForeignKey(to=Series, on_delete=models.PROTECT, related_name='events', null=True, blank=True)
    keyholder = models.CharField(max_length=256, null=True, blank=True)

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


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
