# Generated by Django 2.2.17 on 2021-01-31 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='c_goods',
            new_name='good_id',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='c_goods_num',
            new_name='good_num',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='c_is_select',
            new_name='is_select',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='c_user',
            new_name='user_id',
        ),
    ]