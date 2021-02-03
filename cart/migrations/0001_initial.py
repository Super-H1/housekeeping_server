# Generated by Django 2.2.17 on 2021-01-31 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_user', models.IntegerField()),
                ('c_goods', models.IntegerField()),
                ('c_goods_num', models.IntegerField(default=1)),
                ('c_is_select', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]
