# Generated by Django 2.1.3 on 2018-12-04 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='ovtes',
            new_name='votes',
        ),
    ]
