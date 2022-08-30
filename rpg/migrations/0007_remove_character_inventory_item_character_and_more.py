# Generated by Django 4.0.6 on 2022-08-29 16:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0006_remove_character_attributes_character_charisma_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='inventory',
        ),
        migrations.AddField(
            model_name='item',
            name='character',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rpg.character'),
        ),
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)]),
        ),
    ]
