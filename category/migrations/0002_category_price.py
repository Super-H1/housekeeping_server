# Generated by Django 2.2.17 on 2021-01-07 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]