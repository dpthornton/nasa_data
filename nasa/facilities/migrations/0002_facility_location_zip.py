# Generated by Django 2.1.7 on 2019-02-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='location_zip',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
