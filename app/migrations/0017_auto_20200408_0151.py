# Generated by Django 2.2.11 on 2020-04-08 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20200408_0149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddress',
            name='city',
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='state',
        ),
    ]