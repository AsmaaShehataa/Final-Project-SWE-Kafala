# Generated by Django 3.2.4 on 2021-07-16 22:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_kafala', '0006_auto_20210716_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='RequestDate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
