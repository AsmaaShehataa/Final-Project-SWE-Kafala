# Generated by Django 3.2.4 on 2021-07-16 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_kafala', '0004_alter_requests_requesttypeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='RequestStatusID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='admin_kafala.requeststatus'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='RequestTypeID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='admin_kafala.requesttype'),
        ),
    ]