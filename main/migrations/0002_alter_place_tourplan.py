# Generated by Django 4.0.6 on 2022-11-11 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='tourplan',
            field=models.TextField(blank=True, null=True),
        ),
    ]
