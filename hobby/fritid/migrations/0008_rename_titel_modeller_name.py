# Generated by Django 4.0.4 on 2022-05-20 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fritid', '0007_modeller'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modeller',
            old_name='titel',
            new_name='name',
        ),
    ]
