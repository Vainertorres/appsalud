# Generated by Django 4.2.7 on 2024-04-04 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sam', '0010_alter_actaestabeducativo_options_unidadsalamb_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
    ]
