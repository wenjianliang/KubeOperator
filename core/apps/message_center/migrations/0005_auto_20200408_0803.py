# Generated by Django 2.2.10 on 2020-04-08 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message_center', '0004_add_user_receiver'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermessage',
            options={'ordering': ('-date_created',)},
        ),
    ]
