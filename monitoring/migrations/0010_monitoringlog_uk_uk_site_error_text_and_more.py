# Generated by Django 4.0.4 on 2022-06-27 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0009_rename_pif_lasfupdate_pif_pif_lastupdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonitoringLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('status', models.TextField()),
                ('unavailable', models.IntegerField(blank=True)),
                ('errors', models.IntegerField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='uk',
            name='uk_site_error_text',
            field=models.CharField(blank=True, max_length=2048),
        ),
        migrations.AddField(
            model_name='uk',
            name='uk_site_unavailable_code',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
