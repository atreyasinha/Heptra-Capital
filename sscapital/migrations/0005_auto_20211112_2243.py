# Generated by Django 3.2.8 on 2021-11-13 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sscapital', '0004_auto_20211112_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investors',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='investors',
            name='last_name',
        ),
    ]
