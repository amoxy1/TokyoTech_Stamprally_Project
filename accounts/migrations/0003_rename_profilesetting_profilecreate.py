# Generated by Django 3.2.5 on 2021-10-18 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profilesetting_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfileSetting',
            new_name='ProfileCreate',
        ),
    ]
