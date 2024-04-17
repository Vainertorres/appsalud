# Generated by Django 4.2.7 on 2024-03-05 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('res4505', '0005_alter_res_mamografia_codigo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='riesgo_metabolico',
            options={'verbose_name': 'Clasificación del riesgo metabólico', 'verbose_name_plural': 'Clasificación del riesgo metabólico'},
        ),
        migrations.CreateModel(
            name='Periodo_envio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('descripcion', models.CharField(max_length=80)),
                ('fechaini', models.DateField()),
                ('fechafin', models.DateField()),
                ('fechainiplazo', models.DateField()),
                ('fechafinplazo', models.DateField()),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico')),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modifica')),
            ],
            options={
                'verbose_name': 'Periodo de reporte',
                'verbose_name_plural': 'Periodos de reportes',
            },
        ),
    ]