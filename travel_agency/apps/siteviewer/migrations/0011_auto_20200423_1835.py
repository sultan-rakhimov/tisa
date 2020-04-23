# Generated by Django 3.0.5 on 2020-04-23 13:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('siteviewer', '0010_auto_20200419_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 23, 13, 35, 47, 733259, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='slug',
            field=models.SlugField(max_length=150, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='summary',
            field=models.TextField(db_index=True, max_length=500, verbose_name='Summary'),
        ),
    ]
