# Generated by Django 3.0.8 on 2020-10-16 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='face_1',
            field=models.FileField(blank=True, default=None, null=True, upload_to='Faces'),
        ),
    ]