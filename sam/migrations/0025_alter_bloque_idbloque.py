# Generated by Django 4.2.7 on 2024-04-08 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sam', '0024_alter_bloque_options_alter_tipoacta_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloque',
            name='idbloque',
            field=models.FloatField(),
        ),
    ]
