# Generated by Django 2.2.5 on 2020-02-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
