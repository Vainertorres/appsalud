# Generated by Django 4.2.7 on 2024-01-18 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aseg', '0026_alter_movilidad_options_portabilidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portabilidad',
            old_name='fechaatenciojn',
            new_name='fechaatencion',
        ),
    ]
