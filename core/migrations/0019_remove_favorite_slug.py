# Generated by Django 3.0.3 on 2020-03-04 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20200304_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='slug',
        ),
    ]