# Generated by Django 4.0.4 on 2022-05-24 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_staff_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
