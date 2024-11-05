# Generated by Django 4.2.3 on 2024-11-05 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0013_novedad_creado_por_alter_novedad_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novedad',
            name='creado_por',
            field=models.ForeignKey(limit_choices_to={'fecha_retiro__isnull': True, 'rol': 1}, on_delete=django.db.models.deletion.CASCADE, related_name='novedades_creadas', to='nomina.usuario'),
        ),
    ]
