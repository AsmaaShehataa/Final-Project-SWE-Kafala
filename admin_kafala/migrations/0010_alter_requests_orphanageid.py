# Generated by Django 3.2.4 on 2021-07-17 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orphanage', '0009_alter_childrensmodel_orphanageid'),
        ('admin_kafala', '0009_remove_requests_rootrequestid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='OrphanageID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='orphanage.orphanagemodel'),
        ),
    ]
