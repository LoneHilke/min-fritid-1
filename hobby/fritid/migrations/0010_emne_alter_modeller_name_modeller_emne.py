# Generated by Django 4.0.4 on 2022-05-21 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fritid', '0009_alter_modeller_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='modeller',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='modeller',
            name='emne',
            field=models.ManyToManyField(related_name='item', to='fritid.emne'),
        ),
    ]
