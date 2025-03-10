# Generated by Django 5.0 on 2025-02-22 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='teacher_age',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='post',
            name='teacher_experience',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='teacher_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='teacher_phone',
            field=models.CharField(default='Not provided', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='teacher_photo',
            field=models.ImageField(default='default_teacher_photo.jpg', upload_to='teacher_photos/'),
        ),
        migrations.AddField(
            model_name='post',
            name='teacher_subjects',
            field=models.CharField(default='Not specified', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='default_post_photo.jpg', upload_to='posts/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
