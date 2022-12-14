# Generated by Django 4.0.4 on 2022-05-18 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uk_npp', models.IntegerField()),
                ('uk_name', models.CharField(max_length=500)),
                ('uk_shortname', models.CharField(max_length=200)),
                ('uk_inn', models.CharField(max_length=12)),
                ('uk_ogrn', models.CharField(max_length=15)),
                ('uk_nlic', models.CharField(max_length=14)),
                ('uk_dlic', models.CharField(max_length=10)),
                ('uk_slic', models.CharField(max_length=30)),
                ('uk_addr', models.CharField(max_length=250)),
                ('uk_phones', models.TextField()),
                ('uk_site', models.CharField(max_length=500)),
                ('uk_sitetype', models.CharField(max_length=5)),
                ('uk_enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PIF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pif_npp', models.IntegerField()),
                ('pif_type', models.CharField(max_length=15)),
                ('pif_status', models.CharField(max_length=20)),
                ('pif_name', models.CharField(max_length=500)),
                ('pif_shortname', models.CharField(max_length=200)),
                ('pif_category', models.CharField(max_length=40)),
                ('pif_npdu', models.CharField(max_length=13)),
                ('pif_dpdu', models.CharField(max_length=10)),
                ('pif_spdu', models.CharField(max_length=10)),
                ('pif_prefnames', models.TextField()),
                ('pif_prefpdu', models.TextField()),
                ('pif_enabled', models.BooleanField(default=True)),
                ('pif_uk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.uk')),
            ],
        ),
    ]
