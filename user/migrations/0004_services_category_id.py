# Generated by Django 2.2.17 on 2021-01-05 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210105_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='category_id',
            field=models.IntegerField(null=True, verbose_name='分类id'),
        ),
    ]