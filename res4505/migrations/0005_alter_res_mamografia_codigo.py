# Generated by Django 4.2.7 on 2024-03-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res4505', '0004_alter_calidad_muestra_citologia_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='res_mamografia',
            name='codigo',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]