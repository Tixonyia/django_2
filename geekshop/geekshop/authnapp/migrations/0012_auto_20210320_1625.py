# Generated by Django 2.2.17 on 2021-03-20 16:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0011_auto_20210320_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 22, 16, 25, 3, 642575, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
