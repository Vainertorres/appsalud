# Generated by Django 4.2.7 on 2024-01-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aseg', '0041_novlcregtipo11'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novlcregtipo10',
            name='tiporegistro',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='novlcregtipo11',
            name='tiporegistro',
            field=models.IntegerField(default=11),
        ),
        migrations.AlterField(
            model_name='novlcregtipo7',
            name='tiporegistro',
            field=models.IntegerField(default=7),
        ),
        migrations.AlterField(
            model_name='novlcregtipo8',
            name='tiporegistro',
            field=models.IntegerField(default=8),
        ),
        migrations.AlterField(
            model_name='novlcregtipo9',
            name='tiporegistro',
            field=models.IntegerField(default=9),
        ),
    ]
