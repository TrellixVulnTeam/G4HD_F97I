# Generated by Django 2.2.5 on 2019-12-02 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendar', '0007_auto_20191202_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datereserva',
            name='Status',
            field=models.IntegerField(default=1),
        ),
    ]
