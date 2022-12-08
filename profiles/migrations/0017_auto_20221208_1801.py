# Generated by Django 3.2.16 on 2022-12-08 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_auto_20221208_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Spanish', 'Spanish'), ('French', 'French'), ('Swedish', 'Swedish'), ('Dutch', 'Dutch'), ('Portuguese', 'Portuguese'), ('Mandarin', 'Mandarin'), ('Hindi', 'Hindi '), ('Chinese', 'Chinese'), ('Japanese', 'Japanese'), ('Korean', 'Korean'), ('Russian', 'Russian')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language2',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Spanish', 'Spanish'), ('French', 'French'), ('Swedish', 'Swedish'), ('Dutch', 'Dutch'), ('Portuguese', 'Portuguese'), ('Mandarin', 'Mandarin'), ('Hindi', 'Hindi '), ('Chinese', 'Chinese'), ('Japanese', 'Japanese'), ('Korean', 'Korean'), ('Russian', 'Russian')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language3',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Spanish', 'Spanish'), ('French', 'French'), ('Swedish', 'Swedish'), ('Dutch', 'Dutch'), ('Portuguese', 'Portuguese'), ('Mandarin', 'Mandarin'), ('Hindi', 'Hindi '), ('Chinese', 'Chinese'), ('Japanese', 'Japanese'), ('Korean', 'Korean'), ('Russian', 'Russian')], max_length=12, null=True),
        ),
    ]
