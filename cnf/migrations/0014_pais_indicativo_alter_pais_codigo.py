# Generated by Django 4.2.7 on 2024-02-10 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnf', '0013_alter_actividadeconomica_uc_alter_caractbarrio_uc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pais',
            name='indicativo',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pais',
            name='codigo',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]