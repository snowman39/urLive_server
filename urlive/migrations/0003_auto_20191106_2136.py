# Generated by Django 2.2.7 on 2019-11-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlive', '0002_remove_room_is_selected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(default='null', max_length=64),
        ),
    ]
