# Generated by Django 2.2.17 on 2021-03-21 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0002_auto_20210318_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активен'),
        ),
    ]
