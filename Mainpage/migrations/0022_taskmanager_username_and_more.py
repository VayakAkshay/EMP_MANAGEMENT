# Generated by Django 4.1.6 on 2023-03-29 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainpage', '0021_attendacemanager_username_leavemanager_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmanager',
            name='username',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='attendacemanager',
            name='arrival_time',
            field=models.TimeField(default='10:04:58'),
        ),
    ]
