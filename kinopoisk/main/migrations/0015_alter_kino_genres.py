# Generated by Django 3.2.8 on 2022-06-04 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_kino_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kino',
            name='genres',
            field=models.ManyToManyField(default=None, related_name='genres', to='main.Zhanr'),
        ),
    ]
