# Generated by Django 4.2.7 on 2023-11-29 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_alter_booking_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='username',
        ),
    ]