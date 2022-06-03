# Generated by Django 4.0.4 on 2022-05-25 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20, verbose_name='логин')),
                ('password', models.CharField(max_length=30, verbose_name='пароль')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
        ),
        migrations.AlterModelOptions(
            name='kino',
            options={'verbose_name': 'фильм', 'verbose_name_plural': 'фильмы'},
        ),
    ]
