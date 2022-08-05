# Generated by Django 4.0.6 on 2022-08-01 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0004_character_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('constitution', models.IntegerField(default=0)),
                ('vigor', models.IntegerField(default=0)),
                ('strengh', models.IntegerField(default=0)),
                ('dexterity', models.IntegerField(default=0)),
                ('intelligence', models.IntegerField(default=0)),
                ('charisma', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='character',
            name='charisma',
        ),
        migrations.RemoveField(
            model_name='character',
            name='constitution',
        ),
        migrations.RemoveField(
            model_name='character',
            name='dexterity',
        ),
        migrations.RemoveField(
            model_name='character',
            name='intelligence',
        ),
        migrations.RemoveField(
            model_name='character',
            name='strengh',
        ),
        migrations.RemoveField(
            model_name='character',
            name='vigor',
        ),
        migrations.AddField(
            model_name='character',
            name='attributes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='rpg.attributes'),
        ),
    ]