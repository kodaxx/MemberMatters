# Generated by Django 2.0.6 on 2018-06-23 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20180623_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='state', to='portal.MemberState'),
        ),
    ]