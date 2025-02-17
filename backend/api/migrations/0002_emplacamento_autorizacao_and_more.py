# Generated by Django 5.1.1 on 2025-02-17 08:43

import slth.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="emplacamento",
            name="autorizacao",
            field=slth.db.models.CharField(
                max_length=255, null=True, verbose_name="Autorização"
            ),
        ),
        migrations.AlterField(
            model_name="emplacamento",
            name="data_conclusao",
            field=slth.db.models.DateTimeField(
                blank=True, null=True, verbose_name="Data/Hora de Conclusão"
            ),
        ),
        migrations.AlterField(
            model_name="emplacamento",
            name="data_inicio",
            field=slth.db.models.DateTimeField(
                blank=True, null=True, verbose_name="Data/Hora de Início"
            ),
        ),
    ]
