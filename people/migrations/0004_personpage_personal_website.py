# Generated by Django 5.2.1 on 2025-05-26 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_departmentindexpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='personpage',
            name='personal_website',
            field=models.URLField(blank=True),
        ),
    ]
