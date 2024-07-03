# Generated by Django 5.0.6 on 2024-06-21 02:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentSupport', '0017_rename_user_log_user_id_alter_log_datelogged'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='log',
            name='datelogged',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 21, 12, 47, 2, 918637, tzinfo=datetime.timezone.utc), verbose_name='Date Logged'),
        ),
    ]