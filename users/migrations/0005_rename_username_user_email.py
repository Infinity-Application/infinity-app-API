# Generated by Django 3.2.7 on 2021-09-27 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210927_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='Email',
        ),
    ]
