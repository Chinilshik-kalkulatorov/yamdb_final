# Generated by Django 2.2.16 on 2022-11-29 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_genretitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(
                max_length=256, verbose_name='Название произведения'),
        ),
    ]
