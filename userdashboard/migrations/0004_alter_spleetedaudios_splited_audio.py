# Generated by Django 4.1.7 on 2023-04-19 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard', '0003_spleetedaudios_alter_mediafiles_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spleetedaudios',
            name='splited_audio',
            field=models.FileField(upload_to=''),
        ),
    ]