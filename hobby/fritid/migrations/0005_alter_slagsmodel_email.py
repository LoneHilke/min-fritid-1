# Generated by Django 4.0.4 on 2022-05-18 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fritid', '0004_kommentar_navn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slagsmodel',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
