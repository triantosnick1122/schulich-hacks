# Generated by Django 4.1.5 on 2023-04-29 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trashporter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]