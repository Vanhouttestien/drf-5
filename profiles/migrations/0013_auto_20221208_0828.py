# Generated by Django 3.2.16 on 2022-12-08 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20221208_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.CharField(choices=[('none', 'None'), ('english', 'English'), ('spanish', 'Spanish'), ('french', 'French'), ('swedish', 'Swedish'), ('dutch', 'Dutch'), ('portuguese', 'Portuguese'), ('mandarin', 'Mandarin'), ('hindi', 'Hindi '), ('chinese', 'Chinese'), ('japanese', 'Japanese'), ('korean', 'Korean'), ('russian', 'Russian')], default='none', max_length=12),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language2',
            field=models.CharField(choices=[('none', 'None'), ('english', 'English'), ('spanish', 'Spanish'), ('french', 'French'), ('swedish', 'Swedish'), ('dutch', 'Dutch'), ('portuguese', 'Portuguese'), ('mandarin', 'Mandarin'), ('hindi', 'Hindi '), ('chinese', 'Chinese'), ('japanese', 'Japanese'), ('korean', 'Korean'), ('russian', 'Russian')], default='none', max_length=12),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language3',
            field=models.CharField(choices=[('none', 'None'), ('english', 'English'), ('spanish', 'Spanish'), ('french', 'French'), ('swedish', 'Swedish'), ('dutch', 'Dutch'), ('portuguese', 'Portuguese'), ('mandarin', 'Mandarin'), ('hindi', 'Hindi '), ('chinese', 'Chinese'), ('japanese', 'Japanese'), ('korean', 'Korean'), ('russian', 'Russian')], default='none', max_length=12),
        ),
    ]
