# Generated by Django 4.0.5 on 2022-06-27 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='number',
            field=models.CharField(max_length=30),
        ),
    ]
