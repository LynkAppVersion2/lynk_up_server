# Generated by Django 4.2.1 on 2023-08-16 22:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lynk_up_server', '0002_alter_event_group_alter_group_friends_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.AddField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
