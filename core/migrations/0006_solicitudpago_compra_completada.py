# Generated by Django 3.1.2 on 2024-05-20 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_solicitudpago'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudpago',
            name='compra_completada',
            field=models.BooleanField(default=False),
        ),
    ]
