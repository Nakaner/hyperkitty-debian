# Generated by Django 2.1a1 on 2018-05-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hyperkitty', '0016_auto_20180309_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='content',
            field=models.BinaryField(null=True),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='size',
            field=models.IntegerField(null=True),
        ),
    ]
