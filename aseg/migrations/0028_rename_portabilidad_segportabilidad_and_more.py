# Generated by Django 4.2.7 on 2024-01-18 02:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cnf', '0011_delete_tipoafiliado'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aseg', '0027_rename_fechaatenciojn_portabilidad_fechaatencion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Portabilidad',
            new_name='SegPortabilidad',
        ),
        migrations.AlterModelOptions(
            name='segportabilidad',
            options={'verbose_name': 'Seguimiento Portabilidad'},
        ),
    ]