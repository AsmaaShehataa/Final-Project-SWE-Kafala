# Generated by Django 3.2.4 on 2021-07-16 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_kafala', '0005_auto_20210716_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requests',
            old_name='Date',
            new_name='RequestDate',
        ),
        migrations.RenameField(
            model_name='requests',
            old_name='FileUpload',
            new_name='RequestFileUpload',
        ),
    ]
