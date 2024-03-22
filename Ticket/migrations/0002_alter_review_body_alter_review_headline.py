# Generated by Django 5.0 on 2024-03-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(blank=True, max_length=8192, verbose_name='Commentaire'),
        ),
        migrations.AlterField(
            model_name='review',
            name='headline',
            field=models.CharField(max_length=128, verbose_name='Titre'),
        ),
    ]
