# Generated by Django 4.2.7 on 2024-02-08 21:50

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cnf', '0012_alter_tipodoc_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividadeconomica',
            name='uc',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico'),
        ),
        migrations.AlterField(
            model_name='caractbarrio',
            name='uc',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='uc',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico'),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='uc',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico'),
        ),
        migrations.AlterField(
            model_name='ips',
            name='uc',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico'),
        ),
        migrations.AlterField(
            model_name='mes',
            name='uc',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='uc',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico'),
        ),
        migrations.AlterField(
            model_name='parentezco',
            name='uc',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico'),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='uc',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico'),
        ),
        migrations.AlterField(
            model_name='redlaboratorios',
            name='uc',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico'),
        ),
        migrations.AlterField(
            model_name='tipoconglomerado',
            name='uc',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico'),
        ),
        migrations.AlterField(
            model_name='tipocontacto',
            name='uc',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico'),
        ),
        migrations.AlterField(
            model_name='tipotrabajo',
            name='uc',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico'),
        ),
        migrations.AlterField(
            model_name='tomadordecision',
            name='uc',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico'),
        ),
        migrations.AlterField(
            model_name='varbarrio',
            name='uc',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico'),
        ),
    ]