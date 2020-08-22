# Generated by Django 3.0.9 on 2020-08-21 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20200817_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('diary_text', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'diaries',
            },
        ),
    ]