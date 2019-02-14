# Generated by Django 2.1.7 on 2019-02-13 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center', models.CharField(blank=True, max_length=64, null=True)),
                ('center_search_status', models.CharField(blank=True, max_length=64, null=True)),
                ('facility', models.CharField(blank=True, max_length=64, null=True)),
                ('facility_url', models.URLField(blank=True, null=True)),
                ('occupied', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=64, null=True)),
                ('url_link', models.URLField(blank=True, null=True)),
                ('record_date', models.DateTimeField(blank=True, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=64, null=True)),
                ('contact', models.CharField(blank=True, max_length=64, null=True)),
                ('phone', models.CharField(blank=True, max_length=64, null=True)),
                ('location_type', models.CharField(blank=True, max_length=64, null=True)),
                ('location_x', models.DecimalField(decimal_places=6, max_digits=9)),
                ('location_y', models.DecimalField(decimal_places=6, max_digits=9)),
                ('city', models.CharField(blank=True, max_length=64, null=True)),
                ('state', models.CharField(blank=True, max_length=64, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'facility',
                'managed': True,
            },
        ),
    ]
