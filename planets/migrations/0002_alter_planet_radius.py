# Generated by Django 4.2.5 on 2023-09-28 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='radius',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]