# Generated by Django 2.0.13 on 2019-06-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='gamepublisher',
            field=models.CharField(default='Game:', max_length=200),
        ),
    ]
