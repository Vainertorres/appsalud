# Generated by Django 4.0.4 on 2023-08-31 01:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cnf', '0007_paciente_pais_pais_nacional'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pai', '0005_rediarioregular_namevacunador_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RediarioPaiRegCargado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('fecha', models.DateField()),
                ('file_name', models.FileField(upload_to='rediario')),
                ('uploaded', models.DateField(auto_now_add=True)),
                ('activated', models.BooleanField(default=False)),
                ('ips', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cnf.ips')),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatio')),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modifica')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
