# Generated by Django 2.1.7 on 2019-04-12 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='部门名称')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='名字')),
                ('age', models.CharField(max_length=32, verbose_name='年龄')),
                ('email', models.EmailField(max_length=32, verbose_name='邮箱')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Depart', verbose_name='部门')),
            ],
        ),
    ]
