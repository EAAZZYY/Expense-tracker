# Generated by Django 4.2 on 2023-12-01 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_alter_myexpense_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myexpense',
            name='category',
            field=models.CharField(choices=[('Data', 'Data'), ('Personal', 'Personal'), ('Food', 'Food'), ('Pleasure', 'Pleasure'), ('Business', 'Business'), ('Gift', 'Gift')], max_length=100),
        ),
    ]
