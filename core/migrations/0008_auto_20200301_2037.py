# Generated by Django 3.0.3 on 2020-03-01 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_merge_20200229_1930'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='tag',
            new_name='category',
        ),
    ]