# Generated by Django 4.2.4 on 2024-01-21 10:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("windows_engine", "0014_rename_graph_devicetree_artefacts_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="handles",
            name="GrantedAccess",
        ),
        migrations.RemoveField(
            model_name="handles",
            name="HandleValue",
        ),
        migrations.RemoveField(
            model_name="handles",
            name="Name",
        ),
        migrations.RemoveField(
            model_name="handles",
            name="Offset",
        ),
        migrations.RemoveField(
            model_name="handles",
            name="Process",
        ),
        migrations.RemoveField(
            model_name="handles",
            name="Tag",
        ),
        migrations.RemoveField(
            model_name="handles",
            name="Type",
        ),
        migrations.AddField(
            model_name="handles",
            name="artefacts",
            field=models.JSONField(null=True),
        ),
    ]
