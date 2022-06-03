# Generated by Django 4.0.4 on 2022-05-30 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_zhanrkino_zhanr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kino',
            name='zhanr',
        ),
        migrations.AddField(
            model_name='kino',
            name='one',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='one', to='main.zhanr'),
        ),
        migrations.AddField(
            model_name='kino',
            name='three',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='three', to='main.zhanr'),
        ),
        migrations.AddField(
            model_name='kino',
            name='two',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='two', to='main.zhanr'),
        ),
    ]
