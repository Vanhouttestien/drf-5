# Generated by Django 3.2.16 on 2022-12-08 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_auto_20221208_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.CharField(blank=True, choices=[('', ''), ('english', 'English'), ('spanish', 'Spanish'), ('french', 'French'), ('swedish', 'Swedish'), ('dutch', 'Dutch'), ('portuguese', 'Portuguese'), ('mandarin', 'Mandarin'), ('hindi', 'Hindi '), ('chinese', 'Chinese'), ('japanese', 'Japanese'), ('korean', 'Korean'), ('russian', 'Russian')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language2',
            field=models.CharField(blank=True, choices=[('', ''), ('english', 'English'), ('spanish', 'Spanish'), ('french', 'French'), ('swedish', 'Swedish'), ('dutch', 'Dutch'), ('portuguese', 'Portuguese'), ('mandarin', 'Mandarin'), ('hindi', 'Hindi '), ('chinese', 'Chinese'), ('japanese', 'Japanese'), ('korean', 'Korean'), ('russian', 'Russian')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language3',
            field=models.CharField(blank=True, choices=[('', ''), ('english', 'English'), ('spanish', 'Spanish'), ('french', 'French'), ('swedish', 'Swedish'), ('dutch', 'Dutch'), ('portuguese', 'Portuguese'), ('mandarin', 'Mandarin'), ('hindi', 'Hindi '), ('chinese', 'Chinese'), ('japanese', 'Japanese'), ('korean', 'Korean'), ('russian', 'Russian')], max_length=12, null=True),
        ),
    ]
