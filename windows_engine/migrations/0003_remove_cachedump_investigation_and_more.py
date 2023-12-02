# Generated by Django 4.2.4 on 2023-08-27 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("evidences", "0005_delete_imagesignature"),
        ("windows_engine", "0002_rename_case_id_filedump_dump_id_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cachedump",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="cmdline",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="devicetree",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="dlllist",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="drivermodule",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="envars",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="filescan",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="handles",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="hashdump",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="hivelist",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="ldrmodules",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="lsadump",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="malfind",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="netgraph",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="netscan",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="netstat",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="privs",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="psscan",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="pstree",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="sessions",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="skeletonkeycheck",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="strings",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="timelinechart",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="timeliner",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="userassist",
            name="investigation",
        ),
        migrations.RemoveField(
            model_name="vadwalk",
            name="investigation",
        ),
        migrations.AddField(
            model_name="cachedump",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_cachedump_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="cmdline",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_cmdline_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="devicetree",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_devicetree_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="dlllist",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_dllist_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="drivermodule",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_drivermodule_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="envars",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_envars_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="filescan",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_filescan_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="handles",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_handles_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="hashdump",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_hashdump_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="hivelist",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_hivelist_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ldrmodules",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_ldrmodules_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="lsadump",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_lsadump_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="malfind",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_malfind_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="netgraph",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_netgraph_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="netscan",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_netscan_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="netstat",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_netstat_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="privs",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_privs_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="psscan",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_psscan_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="pstree",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_pstree_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sessions",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_sessions_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="skeletonkeycheck",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_skc_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="strings",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_strings_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="timelinechart",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_timeline_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="timeliner",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_timeliner_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userassist",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_userassist_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="vadwalk",
            name="evidence",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_vadwalk_evidence",
                to="evidences.evidence",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="filedump",
            name="dump_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_filedump_evidence",
                to="evidences.evidence",
            ),
        ),
        migrations.AlterField(
            model_name="processdump",
            name="dump_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="windows_processdump_evidence",
                to="evidences.evidence",
            ),
        ),
    ]
