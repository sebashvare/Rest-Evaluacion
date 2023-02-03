# Generated by Django 4.1.5 on 2023-02-03 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Backlog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", models.DateTimeField(auto_now_add=True)),
                (
                    "fuente",
                    models.CharField(max_length=50, verbose_name="Quien reporta"),
                ),
                (
                    "reporte",
                    models.CharField(max_length=250, verbose_name="Que reporta"),
                ),
                (
                    "id_punto_servicio",
                    models.CharField(max_length=15, verbose_name="ID Punto Servicio"),
                ),
                (
                    "ejecucion",
                    models.CharField(
                        max_length=200, verbose_name="Quien ejecuta la actividad"
                    ),
                ),
                (
                    "estado",
                    models.CharField(max_length=50, verbose_name="Estado Alerta"),
                ),
                (
                    "responsable",
                    models.CharField(max_length=200, verbose_name="Quien Resuelve"),
                ),
                (
                    "contrata",
                    models.CharField(max_length=200, verbose_name="Contratista"),
                ),
            ],
            options={"verbose_name": "Backlog", "verbose_name_plural": "Backlog",},
        ),
        migrations.CreateModel(
            name="Planeacion",
            fields=[
                (
                    "orden_trabajo",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("id_cuenta", models.CharField(max_length=20)),
                ("nombre_cuenta", models.CharField(max_length=150)),
                ("fuente", models.CharField(max_length=20)),
                ("contrata", models.CharField(max_length=20)),
                ("fecha_programacion", models.DateField()),
                ("estado", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Hacer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("actividad_ejecutada", models.CharField(max_length=250)),
                ("numero_formato", models.CharField(max_length=20)),
                ("multiplo", models.CharField(max_length=15)),
                ("telemedida", models.CharField(max_length=15)),
                ("actualizacion_sistema", models.CharField(max_length=30)),
                ("pagar", models.CharField(max_length=30)),
                (
                    "orden_trabajo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hacers",
                        to="planeacion.planeacion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Evaluacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("primera_factura", models.DateField()),
                ("ultima_telemedida", models.DateField()),
                ("conforme", models.CharField(max_length=150)),
                (
                    "orden_trabajo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="planeacion.planeacion",
                    ),
                ),
            ],
        ),
    ]
