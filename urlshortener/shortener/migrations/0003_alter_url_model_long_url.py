# Generated by Django 4.0.1 on 2022-01-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_remove_url_model_id_alter_url_model_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url_model',
            name='long_url',
            field=models.URLField(max_length=300),
        ),
    ]
