# Generated by Django 2.2.1 on 2019-06-12 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0003_auto_20190607_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='TaskState',
            field=models.CharField(choices=[('IN_PROGRESS', 'in progress'), ('TO_DO', 'to do'), ('DONE', 'done')], max_length=12),
        ),
        migrations.AlterField(
            model_name='task',
            name='picker',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
