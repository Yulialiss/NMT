# Generated by Django 5.0 on 2025-02-16 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_phoneverification'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PhoneVerification',
        ),
    ]
