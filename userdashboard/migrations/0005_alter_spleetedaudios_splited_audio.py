# Generated by Django 4.1.7 on 2023-04-19 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard', '0004_alter_spleetedaudios_splited_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spleetedaudios',
            name='splited_audio',
            field=models.CharField(max_length=255),
        ),
    ]
