# Generated by Django 5.0.6 on 2024-12-28 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task_is_miss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_important',
            field=models.BooleanField(default=False, verbose_name='آیا این وظیفه مهم شده'),
        ),
    ]
