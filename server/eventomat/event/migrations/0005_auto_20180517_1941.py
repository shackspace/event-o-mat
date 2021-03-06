# Generated by Django 2.0.3 on 2018-05-17 17:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0004_event_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='keyholder',
            new_name='modified_by'
        ),
        migrations.AddField(
            model_name='event',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
