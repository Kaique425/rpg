# Generated by Django 4.0.6 on 2022-09-03 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0007_remove_character_inventory_item_character_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='character',
            options={'ordering': ['id']},
        ),
    ]
