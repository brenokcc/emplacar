# Generated by Django 5.1.1 on 2025-02-17 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_emplacamento_foto_boletim_ocorrencia_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cor",
            options={"verbose_name": "Cor", "verbose_name_plural": "Cores"},
        ),
    ]
