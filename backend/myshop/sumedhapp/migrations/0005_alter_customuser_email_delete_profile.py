# Generated by Django 5.0.8 on 2024-08-15 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sumedhapp', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
