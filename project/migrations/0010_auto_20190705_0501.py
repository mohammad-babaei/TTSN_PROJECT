# Generated by Django 2.2.1 on 2019-07-05 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20190705_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectuserinvitationmodel',
            name='key',
            field=models.CharField(max_length=64),
        ),
    ]
