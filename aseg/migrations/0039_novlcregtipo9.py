# Generated by Django 4.2.7 on 2024-01-19 02:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cnf', '0012_alter_tipodoc_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aseg', '0038_novlcregtipo8'),
    ]

    operations = [
        migrations.CreateModel(
            name='NovLcRegTipo9',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('tiporegistro', models.IntegerField(default=6)),
                ('identificacion', models.CharField(max_length=16)),
                ('novlcregtipo1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aseg.novlcregtipo1')),
                ('tipobelegiblesub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aseg.tipobelegiblesub')),
                ('tipodoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cnf.tipodoc')),
                ('tipopoblacionesp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aseg.tipopoblacionesp')),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatio')),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modifica')),
            ],
            options={
                'verbose_name': 'Detalle novedad listado censal registro tipo 9 Condición elegible',
            },
        ),
    ]
