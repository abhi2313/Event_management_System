# Generated by Django 4.0.5 on 2022-12-07 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('C', 'Completed')], max_length=2),
        ),
    ]