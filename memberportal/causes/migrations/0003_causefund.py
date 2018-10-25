# Generated by Django 2.0 on 2018-10-18 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('causes', '0002_auto_20181018_0313'),
    ]

    operations = [
        migrations.CreateModel(
            name='CauseFund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Fund Name')),
                ('description', models.CharField(max_length=100, verbose_name='Description of Fund')),
                ('balance', models.FloatField(default=0, verbose_name='Amount')),
                ('cause', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='causes.Causes')),
            ],
        ),
    ]