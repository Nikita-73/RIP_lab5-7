# Generated by Django 3.2.7 on 2021-12-13 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_rename_crss_stock_crs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='crs',
            new_name='src',
        ),
    ]
