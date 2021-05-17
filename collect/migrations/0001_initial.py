# Generated by Django 2.2.17 on 2021-04-18 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('create_user', models.CharField(max_length=50, null=True, verbose_name='创建用户名称')),
                ('create_user_id', models.IntegerField(null=True, verbose_name='创建用户ID')),
                ('last_modifier_time', models.DateTimeField(auto_now=True, null=True, verbose_name='上次修改时间')),
                ('last_modifier_user', models.CharField(max_length=50, null=True, verbose_name='上次修改用户名称')),
                ('last_modifier_user_id', models.IntegerField(null=True, verbose_name='上次修改用户ID')),
                ('last_approval_time', models.DateTimeField(null=True, verbose_name='上次审阅时间')),
                ('last_approval_user', models.CharField(max_length=50, null=True, verbose_name='上次审阅用户名称')),
                ('last_approval_user_id', models.IntegerField(null=True, verbose_name='上次审阅用户ID')),
                ('delete_time', models.DateTimeField(null=True, verbose_name='删除时间')),
                ('delete_user', models.CharField(max_length=50, null=True, verbose_name='删除用户名称')),
                ('delete_user_id', models.IntegerField(null=True, verbose_name='删除用户ID')),
                ('is_deleted', models.BooleanField(null=True, verbose_name='假删')),
                ('remark', models.CharField(max_length=500, null=True, verbose_name='备注')),
                ('is_collect', models.BooleanField(default=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Services')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo')),
            ],
            options={
                'verbose_name': '收藏表',
                'verbose_name_plural': '收藏表',
                'db_table': 'collect',
            },
        ),
    ]