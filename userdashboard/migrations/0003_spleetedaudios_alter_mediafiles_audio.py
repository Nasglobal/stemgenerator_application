# Generated by Django 4.1.7 on 2023-04-19 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard', '0002_alter_mediafiles_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpleetedAudios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('splited_audio', models.CharField(max_length=255)),
                ('originalAudioId', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='mediafiles',
            name='audio',
            field=models.FileField(upload_to=''),
        ),
    ]
