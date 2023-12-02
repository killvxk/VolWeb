# Generated by Django 4.2.4 on 2023-12-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("windows_engine", "0005_alter_getsids_sid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cmdline",
            name="Tag",
            field=models.CharField(
                choices=[
                    ("Evidence", "Evidence"),
                    ("Suspicious", "Suspicious"),
                    ("Clear", "Clear"),
                ],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="dlllist",
            name="Tag",
            field=models.CharField(
                choices=[
                    ("Evidence", "Evidence"),
                    ("Suspicious", "Suspicious"),
                    ("Clear", "Clear"),
                ],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="drivermodule",
            name="Tag",
            field=models.CharField(
                choices=[
                    ("Evidence", "Evidence"),
                    ("Suspicious", "Suspicious"),
                    ("Clear", "Clear"),
                ],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="envars",
            name="Tag",
            field=models.CharField(
                choices=[
                    ("Evidence", "Evidence"),
                    ("Suspicious", "Suspicious"),
                    ("Clear", "Clear"),
                ],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="filescan",
            name="Tag",
            field=models.CharField(
                choices=[
                    ("Evidence", "Evidence"),
                    ("Suspicious", "Suspicious"),
                    ("Clear", "Clear"),
                ],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="getsids",
            name="Tag",
            field=models.CharField(
                choices=[
                    ("Evidence", "Evidence"),
                    ("Suspicious", "Suspicious"),
                    ("Clear", "Clear"),
                ],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="handles",
            name="Tag",
            field=models.CharField(
                choices=[
                    ("Evidence", "Evidence"),
                    ("Suspicious", "Suspicious"),
                    ("Clear", "Clear"),
                ],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="hashdump",
            name="Tag",
            field=models.CharField(
                choices=[
                    ("Evidence", "Evidence"),
                    ("Suspicious", "Suspicious"),
                    ("Clear", "Clear"),
                ],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="ldrmodules",
            name="Tag",
            field=models.CharField(
                choices=[
                    ("Evidence", "Evidence"),
                    ("Suspicious", "Suspicious"),
                    ("Clear", "Clear"),
                ],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="netscan",
            name="Tag",
            field=models.CharField(
                choices=[
                    ("Evidence", "Evidence"),
                    ("Suspicious", "Suspicious"),
                    ("Clear", "Clear"),
                ],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="netstat",
            name="Tag",
            field=models.CharField(
                choices=[
                    ("Evidence", "Evidence"),
                    ("Suspicious", "Suspicious"),
                    ("Clear", "Clear"),
                ],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="privs",
            name="Tag",
            field=models.CharField(
                choices=[
                    ("Evidence", "Evidence"),
                    ("Suspicious", "Suspicious"),
                    ("Clear", "Clear"),
                ],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="sessions",
            name="Tag",
            field=models.CharField(
                choices=[
                    ("Evidence", "Evidence"),
                    ("Suspicious", "Suspicious"),
                    ("Clear", "Clear"),
                ],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="skeletonkeycheck",
            name="Tag",
            field=models.CharField(
                choices=[
                    ("Evidence", "Evidence"),
                    ("Suspicious", "Suspicious"),
                    ("Clear", "Clear"),
                ],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="strings",
            name="Tag",
            field=models.CharField(
                choices=[
                    ("Evidence", "Evidence"),
                    ("Suspicious", "Suspicious"),
                    ("Clear", "Clear"),
                ],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="timeliner",
            name="Tag",
            field=models.CharField(
                choices=[
                    ("Evidence", "Evidence"),
                    ("Suspicious", "Suspicious"),
                    ("Clear", "Clear"),
                ],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="userassist",
            name="Tag",
            field=models.CharField(
                choices=[
                    ("Evidence", "Evidence"),
                    ("Suspicious", "Suspicious"),
                    ("Clear", "Clear"),
                ],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="vadwalk",
            name="Tag",
            field=models.CharField(
                choices=[
                    ("Evidence", "Evidence"),
                    ("Suspicious", "Suspicious"),
                    ("Clear", "Clear"),
                ],
                max_length=11,
                null=True,
            ),
        ),
    ]
