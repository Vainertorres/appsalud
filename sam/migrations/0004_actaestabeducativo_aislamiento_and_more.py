# Generated by Django 4.0.4 on 2022-09-03 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cnf', '0002_etnia_codigo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sam', '0003_actaestabeducativo_itemactaestabeducativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='actaestabeducativo',
            name='aislamiento',
            field=models.BooleanField(default=False, verbose_name='Aislamiento o internación de personas para evitar la transmisión de enfermedades'),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='capturanimales',
            field=models.BooleanField(default=False, verbose_name='Captura y observación de animales sospechosos de enfermedades transmisibles'),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='clausuratemparcial',
            field=models.BooleanField(default=False, verbose_name='Clausura temporal parcial'),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='clausuratemptotal',
            field=models.BooleanField(default=False, verbose_name='Clausura temporal total'),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='congelacion',
            field=models.BooleanField(default=False, verbose_name='Congelación'),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='controlinsectos',
            field=models.BooleanField(default=False, verbose_name='Control de insectos u otra fauna nociva o transmisora de enfermedades'),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='decomiso',
            field=models.BooleanField(default=False, verbose_name='Decomiso'),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='desocupacion',
            field=models.BooleanField(default=False, verbose_name='Desocupación o desalojamiento de establecimientos o vivienda'),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='destruccion',
            field=models.BooleanField(default=False, verbose_name='Destrucción o desnaturalización'),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='diashabileplazo',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='fechafinplazo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='fechainiplazo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='nroactamedidasanitaria',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='nroactatomamuestras',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='nrototalmuestrastomadas',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='observacionesanitarias',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='observacionestablecimiento',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='requerimientosanitario',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='susparcialtrabajo',
            field=models.BooleanField(default=False, verbose_name='Suspensión parcial de trabajos o servicios'),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='susptotaltrabservicio',
            field=models.BooleanField(default=False, verbose_name='Suspensión total de trabajos o servicios'),
        ),
        migrations.AddField(
            model_name='actaestabeducativo',
            name='vacunacion',
            field=models.BooleanField(default=False, verbose_name='Vacunación personas o animales'),
        ),
        migrations.CreateModel(
            name='Atiende_ActaEstabEduc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('identificacion', models.CharField(max_length=20)),
                ('institucion', models.CharField(blank=True, max_length=100, null=True)),
                ('cargo', models.CharField(blank=True, max_length=80, null=True)),
                ('actaestabeducativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sam.actaestabeducativo')),
                ('tipodoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cnf.tipodoc')),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatio')),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modifica')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActaEstEduFuncionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('actaestabeducativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sam.actaestabeducativo')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cnf.funcionario')),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatio')),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modifica')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]