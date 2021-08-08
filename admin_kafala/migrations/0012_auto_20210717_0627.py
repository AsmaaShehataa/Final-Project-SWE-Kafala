# Generated by Django 3.2.4 on 2021-07-17 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orphanage', '0009_alter_childrensmodel_orphanageid'),
        ('sponser', '0002_auto_20210619_1719'),
        ('admin_kafala', '0011_auto_20210717_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='ChildID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orphanage.childrensmodel'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='OrphanageID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orphanage.orphanagemodel'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='RequestStatusID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_kafala.requeststatus'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='UserID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sponser.usermodel'),
        ),
    ]