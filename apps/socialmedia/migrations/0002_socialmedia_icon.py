# Generated by Django 4.1.7 on 2023-02-23 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='Icon',
            field=models.TextField(null=True),
        ),
    ]
