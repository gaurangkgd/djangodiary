# Generated by Django 5.0.6 on 2024-06-11 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='name',
            new_name='todo_name',
        ),
    ]
