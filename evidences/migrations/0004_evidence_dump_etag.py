# Generated by Django 4.2.4 on 2023-08-27 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evidences', '0003_imagesignature'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidence',
            name='dump_etag',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
