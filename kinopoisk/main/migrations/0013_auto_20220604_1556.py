# Generated by Django 3.2.8 on 2022-06-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_kino_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kino',
            name='one',
        ),
        migrations.RemoveField(
            model_name='kino',
            name='three',
        ),
        migrations.RemoveField(
            model_name='kino',
            name='two',
        ),
        migrations.AddField(
            model_name='kino',
            name='genres',
            field=models.ManyToManyField(to='main.Zhanr'),
        ),
    ]