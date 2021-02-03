# Generated by Django 2.2.17 on 2021-01-07 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_services_servicesurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='information',
            field=models.TextField(default=None, null=True, verbose_name='更多信息'),
        ),
        migrations.AlterField(
            model_name='services',
            name='training_record',
            field=models.TextField(default=None, null=True, verbose_name='培训记录'),
        ),
        migrations.AlterField(
            model_name='services',
            name='work_record',
            field=models.TextField(default=None, null=True, verbose_name='工作记录'),
        ),
    ]