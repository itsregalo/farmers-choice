# Generated by Django 4.0 on 2022-05-13 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issuecategory',
            options={'verbose_name_plural': 'issue Categories'},
        ),
        migrations.AddField(
            model_name='issuecategory',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
