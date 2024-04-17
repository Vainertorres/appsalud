# Generated by Django 4.2.7 on 2024-01-15 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cnf', '0011_delete_tipoafiliado'),
        ('aseg', '0015_tipobelegiblesub_listadocensal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listadocensal',
            name='titular',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='titular', to='cnf.paciente'),
        ),
    ]
