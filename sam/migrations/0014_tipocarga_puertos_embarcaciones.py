# Generated by Django 4.2.7 on 2024-04-04 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cnf', '0017_clasifcaso_codigo_clasifinal_codigo_and_more'),
        ('sam', '0013_actageneral_atiendeactageneral_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCarga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('descripcion', models.CharField(max_length=150)),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico')),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modifica')),
            ],
            options={
                'verbose_name_plural': 'Tipo de carga',
            },
        ),
        migrations.CreateModel(
            name='Puertos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('descripcion', models.CharField(max_length=150)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cnf.pais')),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico')),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modifica')),
            ],
            options={
                'verbose_name_plural': 'Puertos',
            },
        ),
        migrations.CreateModel(
            name='Embarcaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('matricula', models.CharField(max_length=30, unique=True)),
                ('nombre', models.CharField(max_length=150)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cnf.pais')),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico')),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modifica')),
            ],
            options={
                'verbose_name_plural': 'Embarcaciones',
            },
        ),
    ]