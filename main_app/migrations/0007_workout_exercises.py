# Generated by Django 3.2.9 on 2021-12-01 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_exercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='exercises',
            field=models.ManyToManyField(to='main_app.Exercise'),
        ),
    ]