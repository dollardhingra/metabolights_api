# Generated by Django 2.1.15 on 2022-02-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220213_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyfile',
            name='size_kb',
            field=models.PositiveIntegerField(),
        ),
    ]