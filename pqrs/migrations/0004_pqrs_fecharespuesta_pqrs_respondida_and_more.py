# Generated by Django 4.2.7 on 2024-01-09 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pqrs', '0003_alter_pqrs_victima'),
    ]

    operations = [
        migrations.AddField(
            model_name='pqrs',
            name='fecharespuesta',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pqrs',
            name='respondida',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.CreateModel(
            name='TipoRespuestaPqrs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=3, unique=True)),
                ('descripcion', models.CharField(max_length=80)),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatio')),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modifica')),
            ],
            options={
                'verbose_name': 'Tipo de respuesta PQRS',
                'verbose_name_plural': 'Tipo de respuesta PQRS',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='SeguimientoPQRS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('fecha', models.DateField()),
                ('observacion', models.TextField()),
                ('pqrs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pqrs.pqrs')),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatio')),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modifica')),
            ],
            options={
                'verbose_name': 'Seguimiento Pqrs',
            },
        ),
        migrations.AddField(
            model_name='pqrs',
            name='tiporespuestapqrs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pqrs.tiporespuestapqrs'),
        ),
    ]
