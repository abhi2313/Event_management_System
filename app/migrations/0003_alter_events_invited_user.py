# Generated by Django 4.0.5 on 2022-12-07 19:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_alter_events_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='invited_user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
