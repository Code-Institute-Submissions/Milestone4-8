# Generated by Django 3.0.9 on 2020-08-29 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
    ]