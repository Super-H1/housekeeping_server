# Generated by Django 2.2.17 on 2021-03-01 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20210301_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderservice',
            name='service_price',
            field=models.FloatField(default=None, verbose_name='服务单价'),
        ),
    ]
