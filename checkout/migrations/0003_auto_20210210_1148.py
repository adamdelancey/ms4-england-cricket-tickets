# Generated by Django 3.1.5 on 2021-02-10 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20210210_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='match',
        ),
        migrations.RemoveField(
            model_name='orderlineitem',
            name='tour',
        ),
    ]
