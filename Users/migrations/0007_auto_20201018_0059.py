# Generated by Django 3.0.8 on 2020-10-18 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_auto_20201017_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='account_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='age',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='card_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='civil_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='direction',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='nationality',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
