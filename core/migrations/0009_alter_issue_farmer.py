# Generated by Django 4.0.4 on 2022-05-24 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0008_alter_issue_image_alter_issue_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]