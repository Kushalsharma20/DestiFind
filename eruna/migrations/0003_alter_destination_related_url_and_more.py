# Generated by Django 4.0.6 on 2022-07-25 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eruna', '0002_destinationimage_online_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='related_url',
            field=models.URLField(blank=True, null=True, verbose_name='Url To Related Article'),
        ),
        migrations.AlterField(
            model_name='destinationimage',
            name='online_url',
            field=models.URLField(blank=True, null=True, verbose_name='Online Image Url'),
        ),
        migrations.AlterField(
            model_name='lounge',
            name='related_url',
            field=models.URLField(blank=True, null=True, verbose_name='Url To Related Article'),
        ),
    ]
