# Generated by Django 2.2.6 on 2019-11-02 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlive', '0004_remove_room_encrypt'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='encrypt',
            field=models.CharField(default='null', max_length=20, unique=True),
        ),
    ]
