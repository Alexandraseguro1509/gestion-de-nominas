# Generated by Django 4.2.3 on 2024-08-05 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deduccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retefuente', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Devengado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.PositiveIntegerField(unique=True)),
                ('nombre', models.CharField(max_length=256)),
                ('apellido', models.CharField(max_length=256)),
                ('correo', models.EmailField(max_length=256)),
                ('contrasena', models.CharField(max_length=256)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_usuarios')),
                ('rol', models.PositiveIntegerField(choices=[(1, 'Administrador'), (2, 'Colaborador')], default=2)),
                ('cargo', models.PositiveIntegerField(blank=True, choices=[(1, 'No aplica'), (2, 'Almacenista'), (3, 'Analista de ingeniería'), (4, 'Aprendiz etapa lectiva'), (5, 'Aprendiz etapa práctica'), (6, 'Auditor'), (7, 'Auxiliar contable'), (8, 'Auxiliar de almacén'), (9, 'Auxiliar de bodega'), (10, 'Auxiliar de calidad'), (11, 'Auxiliar de diseño'), (12, 'Auxiliar de gestión humana'), (13, 'Auxiliar de ingeniería'), (14, 'Auxiliar de mecánica'), (15, 'Auxiliar de servicios generales'), (16, 'Coordinador de área'), (17, 'Despachador'), (18, 'Diseñadora'), (19, 'Domiciliario'), (20, 'Gerente'), (21, 'Jefe de calidad'), (22, 'Jefe de compras'), (23, 'Jefe de despachos'), (24, 'Jefe de Gestión Humana'), (25, 'Jefe de planta'), (26, 'Mecánico'), (27, 'Operario de corte'), (28, 'Operario de empaque'), (29, 'Operario de extendido'), (30, 'Operario de máquina'), (31, 'Operario de máquinas especiales'), (32, 'Operario de muestras'), (33, 'Operario de terminación'), (34, 'Operario manual'), (35, 'Patinador'), (36, 'Patronista'), (37, 'Recepcionista'), (38, 'Revisora'), (39, 'Secretaria'), (40, 'Supervisor'), (41, 'Vigilante')], default=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Novedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salario', models.IntegerField()),
                ('clase_salario', models.PositiveIntegerField(choices=[(1, 'Básico'), (2, 'Integral')], default=1)),
                ('dias_incapacidad', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('dias_trabajados', models.PositiveIntegerField()),
                ('horas_extras_diurnas', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('horas_extras_diurnas_dom_fes', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('horas_extras_nocturnas', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('horas_extras_nocturnas_dom_fes', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('horas_recargo_nocturno', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('horas_recargo_nocturno_dom_fes', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('horas_recargo_diurno_dom_fes', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('comisiones', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('comisiones_porcentaje', models.FloatField(blank=True, default=0, null=True)),
                ('bonificaciones', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('embargos_judiciales', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('libranzas', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('cooperativas', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('otros', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('riesgo', models.FloatField(default=0)),
                ('fecha_ingreso', models.DateField()),
                ('fecha_fin_contrato', models.DateField(blank=True, null=True)),
                ('tipo_contrato', models.PositiveIntegerField(choices=[(1, 'Término fijo inferior a 1 año'), (2, 'Término fijo superior a 1 año'), (3, 'Contrato por obra y labor'), (4, 'Contrato indefinido')])),
                ('fecha_retiro', models.DateField(blank=True, null=True)),
                ('motivo_retiro', models.CharField(blank=True, max_length=256, null=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('usuario', models.ForeignKey(limit_choices_to={'rol': 2}, on_delete=django.db.models.deletion.CASCADE, to='nomina.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Nomina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deduccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.deduccion')),
                ('devengado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.devengado')),
                ('novedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.novedad')),
            ],
        ),
        migrations.AddField(
            model_name='devengado',
            name='novedad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.novedad'),
        ),
        migrations.AddField(
            model_name='deduccion',
            name='devengado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.devengado'),
        ),
        migrations.AddField(
            model_name='deduccion',
            name='novedad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.novedad'),
        ),
    ]
