# Generated by Django 2.0.3 on 2018-03-15 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='nname',
            new_name='name',
        ),
    ]