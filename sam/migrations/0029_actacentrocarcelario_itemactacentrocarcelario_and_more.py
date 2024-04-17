# Generated by Django 4.2.7 on 2024-04-11 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cnf', '0018_gestoresiduohospitalario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sam', '0028_cumplimientocondsanitaria'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActaCentroCarcelario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('fecha', models.DateTimeField()),
                ('nroacta', models.CharField(max_length=15)),
                ('inspeccionanterior', models.BooleanField(default=False)),
                ('fechaultinspeccion', models.DateTimeField(blank=True, null=True)),
                ('porcumplimientoanterior', models.FloatField(blank=True, default=0, null=True)),
                ('nroactanterior', models.CharField(blank=True, max_length=15, null=True)),
                ('requerimiento', models.TextField(blank=True, null=True)),
                ('observacionautsan', models.TextField(blank=True, null=True)),
                ('observacionestable', models.TextField(blank=True, null=True)),
                ('puntaje', models.FloatField(default=0)),
                ('nroadministativos', models.IntegerField(blank=True, default=1, null=True)),
                ('nrooperativos', models.IntegerField(blank=True, default=1, null=True)),
                ('nroafiliadosarl', models.IntegerField(blank=True, default=1, null=True)),
                ('nroafiliadosegsocial', models.IntegerField(blank=True, default=1, null=True)),
                ('concepto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carcel_concepto', to='sam.concepto')),
                ('conceptoanterior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carcel_concepto_anterior', to='sam.concepto')),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sam.establecimiento')),
                ('gestoresiduohospitalario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cnf.gestoresiduohospitalario')),
                ('motivovisita', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sam.motivovisita')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cnf.municipio')),
                ('tipoacta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sam.tipoacta')),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico')),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modifica')),
            ],
            options={
                'verbose_name_plural': 'Acta visita a centros carcelarios',
            },
        ),
        migrations.CreateModel(
            name='ItemActaCentroCarcelario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('puntaje', models.FloatField(default=0)),
                ('habilitada', models.BooleanField(default=True)),
                ('actacentrocarcelario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sam.actacentrocarcelario')),
                ('evaluacion', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='sam.evaluacion')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sam.pregunta')),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico')),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modifica')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FuncionariosActaCentroCarcelario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('actacentrocarcelario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sam.actacentrocarcelario')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cnf.funcionario')),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico')),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modifica')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AtiendeActaCentroCarcelario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('identificacion', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=150)),
                ('cargo', models.CharField(blank=True, max_length=80, null=True)),
                ('actacentrocarcelario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sam.actacentrocarcelario')),
                ('tipodoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cnf.tipodoc')),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico')),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modifica')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
