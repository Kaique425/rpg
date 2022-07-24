# Generated by Django 4.0.6 on 2022-07-17 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='char_class',
        ),
        migrations.AddField(
            model_name='character',
            name='char_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='charclass', to='rpg.charclass'),
        ),
    ]
