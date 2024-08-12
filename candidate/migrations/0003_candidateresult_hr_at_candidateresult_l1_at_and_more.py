# Generated by Django 5.0.4 on 2024-04-27 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_auto_20210523_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateresult',
            name='hr_at',
            field=models.DateTimeField(null=True, verbose_name='HR Date'),
        ),
        migrations.AddField(
            model_name='candidateresult',
            name='l1_at',
            field=models.DateTimeField(null=True, verbose_name='L1 Date'),
        ),
        migrations.AddField(
            model_name='candidateresult',
            name='l2_at',
            field=models.DateTimeField(null=True, verbose_name='L2 Date'),
        ),
    ]
