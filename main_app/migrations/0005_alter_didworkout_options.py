# Generated by Django 3.2.9 on 2021-12-01 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20211201_1326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='didworkout',
            options={'ordering': ['-date']},
        ),
    ]
