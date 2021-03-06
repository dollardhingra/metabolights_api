# Generated by Django 2.1.15 on 2022-02-13 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220213_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
