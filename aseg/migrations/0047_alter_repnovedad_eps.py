# Generated by Django 4.2.7 on 2024-02-17 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cnf', '0015_pueblo_indigena_escolaridad'),
        ('aseg', '0046_alter_afiloficiosinsisben_uc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repnovedad',
            name='eps',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cnf.eps'),
        ),
    ]