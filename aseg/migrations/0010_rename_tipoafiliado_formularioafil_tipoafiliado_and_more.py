# Generated by Django 4.2.7 on 2024-01-15 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aseg', '0009_alter_causalretiro_descripcion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formularioafil',
            old_name='TipoAfiliado',
            new_name='tipoafiliado',
        ),
        migrations.CreateModel(
            name='OpcDesaprueba',
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
                'verbose_name': 'Opción de desaprobación',
                'verbose_name_plural': 'Opciones de desaprobación',
                'ordering': ['descripcion'],
            },
        ),
        migrations.AlterField(
            model_name='formularioafil',
            name='opcdesaprueba',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aseg.opcdesaprueba'),
        ),
    ]
