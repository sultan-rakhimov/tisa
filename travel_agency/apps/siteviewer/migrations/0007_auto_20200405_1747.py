# Generated by Django 3.0.4 on 2020-04-05 12:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('siteviewer', '0006_auto_20200405_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 5, 12, 47, 16, 868957, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='summary',
            field=models.TextField(db_index=True, max_length=500, verbose_name='summary'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Title'),
        ),
    ]
