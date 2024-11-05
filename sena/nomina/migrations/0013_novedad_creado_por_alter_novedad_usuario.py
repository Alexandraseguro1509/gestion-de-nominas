# Generated by Django 4.2.3 on 2024-11-05 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0012_alter_novedad_dias_trabajados'),
    ]

    operations = [
        migrations.AddField(
            model_name='novedad',
            name='creado_por',
            field=models.ForeignKey(limit_choices_to={'fecha_retiro__isnull': True, 'rol': 1}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='novedades_creadas', to='nomina.usuario'),
        ),
        migrations.AlterField(
            model_name='novedad',
            name='usuario',
            field=models.ForeignKey(limit_choices_to={'fecha_retiro__isnull': True, 'rol': 2}, on_delete=django.db.models.deletion.CASCADE, related_name='novedades_usuario', to='nomina.usuario'),
        ),
    ]
