# Generated by Django 3.2.4 on 2021-07-16 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_kafala', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='FileUpload',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
    ]