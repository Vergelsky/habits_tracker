# Generated by Django 5.0.4 on 2024-04-15 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooster', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crossoneself',
            name='period',
            field=models.SmallIntegerField(default=1, verbose_name='периодичность'),
        ),
    ]