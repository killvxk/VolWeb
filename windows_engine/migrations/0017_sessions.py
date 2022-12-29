# Generated by Django 3.2.15 on 2022-12-27 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investigations', '0001_initial'),
        ('windows_engine', '0016_filescan_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sessions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateTime', models.TextField(null=True)),
                ('Process', models.TextField(null=True)),
                ('ProcessID', models.IntegerField(null=True)),
                ('SessionID', models.IntegerField(null=True)),
                ('SessionType', models.TextField(null=True)),
                ('UserName', models.TextField(null=True)),
                ('Tag', models.CharField(choices=[('Evidence', 'Evidence'), ('Suspicious', 'Suspicious')], max_length=11, null=True)),
                ('investigation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='windows_sessions_investigation', to='investigations.uploadinvestigation')),
            ],
        ),
    ]
