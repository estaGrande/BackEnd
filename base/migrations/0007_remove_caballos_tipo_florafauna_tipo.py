# Generated by Django 4.1.6 on 2023-02-06 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_caballos_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caballos',
            name='tipo',
        ),
        migrations.AddField(
            model_name='florafauna',
            name='tipo',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
