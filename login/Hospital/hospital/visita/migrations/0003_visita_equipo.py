# Generated by Django 3.0.3 on 2020-02-12 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visita', '0002_visita_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='visita',
            name='equipo',
            field=models.IntegerField(default=0),
        ),
    ]