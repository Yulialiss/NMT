# Generated by Django 5.0 on 2025-04-11 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_visit',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
