# Generated by Django 5.0.6 on 2024-06-23 23:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentSupport', '0026_rename_useraction_studenthelplog_classid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studenthelplog',
            old_name='classid',
            new_name='userAction',
        ),
        migrations.AlterField(
            model_name='log',
            name='datelogged',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 24, 9, 5, 42, 615325, tzinfo=datetime.timezone.utc), verbose_name='Date Logged'),
        ),
        migrations.AlterField(
            model_name='studenthelplog',
            name='datelogged',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 24, 9, 5, 42, 616520, tzinfo=datetime.timezone.utc), verbose_name='Date Logged'),
        ),
    ]