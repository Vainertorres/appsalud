# Generated by Django 4.2.7 on 2024-04-03 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aseg', '0048_alter_repnovedad_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoafiliacion',
            name='codigo',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]