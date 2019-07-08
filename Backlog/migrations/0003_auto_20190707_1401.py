# Generated by Django 2.2 on 2019-07-07 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Backlog', '0002_backlog_projectid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backlog',
            name='ProjectID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='backlog_requests_created', to='project.Project'),
        ),
    ]
