# Generated by Django 5.0 on 2025-04-14 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_classes', '0006_class_author_alter_class_audience_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='password',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
