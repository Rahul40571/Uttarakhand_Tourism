# Generated by Django 4.0.6 on 2022-11-12 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_place_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='slug',
            field=models.SlugField(default='Test', max_length=100),
            preserve_default=False,
        ),
    ]
