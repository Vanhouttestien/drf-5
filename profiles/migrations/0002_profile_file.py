# Generated by Django 3.2.16 on 2022-11-28 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='file',
            field=models.FileField(default=True, upload_to='uploads/'),
        ),
    ]