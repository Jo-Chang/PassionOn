# Generated by Django 3.2.18 on 2023-05-17 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0006_auto_20230517_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommend',
            name='clothes_tags',
        ),
    ]