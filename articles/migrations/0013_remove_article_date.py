# Generated by Django 3.2 on 2021-04-26 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20210426_0504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date',
        ),
    ]