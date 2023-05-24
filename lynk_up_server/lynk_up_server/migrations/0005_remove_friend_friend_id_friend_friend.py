# Generated by Django 4.2.1 on 2023-05-24 00:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lynk_up_server', '0004_event_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='friend_id',
        ),
        migrations.AddField(
            model_name='friend',
            name='friend',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='friend_of', to='lynk_up_server.user'),
            preserve_default=False,
        ),
    ]
