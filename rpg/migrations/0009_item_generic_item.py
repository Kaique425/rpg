# Generated by Django 4.0.6 on 2022-09-03 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0008_genericitem_alter_character_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='generic_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rpg.genericitem'),
        ),
    ]