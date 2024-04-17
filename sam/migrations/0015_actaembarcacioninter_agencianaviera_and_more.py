# Generated by Django 4.2.7 on 2024-04-04 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cnf', '0017_clasifcaso_codigo_clasifinal_codigo_and_more'),
        ('sam', '0014_tipocarga_puertos_embarcaciones'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActaEmbarcacionInter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('nroacta', models.CharField(max_length=15)),
                ('nombrecapitan', models.CharField(blank=True, max_length=150, null=True)),
                ('tiempoenpuerto', models.FloatField(blank=True, default=0, null=True)),
                ('clasetiempo', models.CharField(blank=True, choices=[('H', 'Horas'), ('D', 'Días'), ('S', 'Semanas')], max_length=1, null=True)),
                ('ctrlsanidadvigente', models.BooleanField(default=True)),
                ('fechaexpcertsanidad', models.DateField(blank=True, null=True)),
                ('fechavencecertsanidad', models.DateField(blank=True, null=True)),
                ('enfermedades', models.TextField(blank=True, null=True)),
                ('nrotripulantes', models.IntegerField(default=1)),
                ('nropasajeros', models.IntegerField(default=0)),
                ('nropolisones', models.IntegerField(default=0)),
                ('vacunafiebreamarilla', models.BooleanField(default=True)),
                ('vacunafavigente', models.BooleanField(default=True)),
                ('tiempovigenciadias', models.IntegerField(default=0)),
                ('ordenvacunacionoficial', models.BooleanField(default=True)),
                ('aguapotable', models.BooleanField(default=True)),
                ('alimentos', models.BooleanField(default=True)),
                ('botiquin', models.BooleanField(default=True)),
                ('depositobasuras', models.BooleanField(default=False)),
                ('desinsectacion', models.BooleanField(default=False)),
                ('desinfeccion', models.BooleanField(default=False)),
                ('desratizacion', models.BooleanField(default=False)),
                ('cuarentena', models.BooleanField(default=False)),
                ('aislamientocasos', models.BooleanField(default=False)),
                ('aislamientoembarcacion', models.BooleanField(default=False)),
                ('otramedsan', models.BooleanField(default=False)),
                ('ningunamedsan', models.BooleanField(default=False)),
                ('mallasprotectoras', models.BooleanField(default=False)),
                ('discoatajaratas', models.BooleanField(default=False)),
                ('tapetesanitario', models.BooleanField(default=False)),
                ('cargaparapuerto', models.FloatField(default=0)),
                ('tonelajecargapeligrosa', models.FloatField(default=0)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('fechalibreplatica', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Acta embarcaciones internacionales',
            },
        ),
        migrations.CreateModel(
            name='AgenciaNaviera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('descripcion', models.CharField(max_length=150)),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico')),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modifica')),
            ],
            options={
                'verbose_name_plural': 'Tipo de carga',
            },
        ),
        migrations.CreateModel(
            name='ActaEmbarcacionInterImo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('imo', models.FloatField(default=0)),
                ('actaembarcacioninter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sam.actaembarcacioninter')),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico')),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modifica')),
            ],
            options={
                'verbose_name': 'IMO',
            },
        ),
        migrations.CreateModel(
            name='ActaEmbarcacionInterFuncionarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('actaembarcacioninter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sam.actaembarcacioninter')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cnf.funcionario')),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico')),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modifica')),
            ],
            options={
                'verbose_name': 'Funcionarios que realizaron visita',
            },
        ),
        migrations.AddField(
            model_name='actaembarcacioninter',
            name='agencianaviera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sam.agencianaviera'),
        ),
        migrations.AddField(
            model_name='actaembarcacioninter',
            name='destino',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destino_pto', to='sam.puertos'),
        ),
        migrations.AddField(
            model_name='actaembarcacioninter',
            name='embarcaciones',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sam.embarcaciones'),
        ),
        migrations.AddField(
            model_name='actaembarcacioninter',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cnf.municipio'),
        ),
        migrations.AddField(
            model_name='actaembarcacioninter',
            name='nacionalidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nacionalidad_emb', to='cnf.pais'),
        ),
        migrations.AddField(
            model_name='actaembarcacioninter',
            name='paisexpcertificado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pais_expcertificado', to='cnf.pais'),
        ),
        migrations.AddField(
            model_name='actaembarcacioninter',
            name='procedencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procedencia_pto', to='sam.puertos'),
        ),
        migrations.AddField(
            model_name='actaembarcacioninter',
            name='tipocarga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sam.tipocarga'),
        ),
        migrations.AddField(
            model_name='actaembarcacioninter',
            name='uc',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario automatico'),
        ),
        migrations.AddField(
            model_name='actaembarcacioninter',
            name='um',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modifica'),
        ),
    ]