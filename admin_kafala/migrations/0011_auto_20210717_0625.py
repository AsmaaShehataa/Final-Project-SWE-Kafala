# Generated by Django 3.2.4 on 2021-07-17 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orphanage', '0009_alter_childrensmodel_orphanageid'),
        ('sponser', '0002_auto_20210619_1719'),
        ('admin_kafala', '0010_alter_requests_orphanageid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='ChildID',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.PROTECT, to='orphanage.childrensmodel'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='UserID',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.PROTECT, to='sponser.usermodel'),
        ),
    ]
