# Generated by Django 3.2.7 on 2021-12-13 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_auto_20211213_2157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='photo',
            new_name='crs',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='description',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='orcestr',
            new_name='title',
        ),
    ]
