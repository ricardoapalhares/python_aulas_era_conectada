# Generated by Django 2.1.4 on 2019-01-31 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20190131_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='votes',
        ),
        migrations.AddField(
            model_name='comment',
            name='nota',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
