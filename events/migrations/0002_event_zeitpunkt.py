# Generated by Django 2.0.13 on 2019-06-17 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='zeitpunkt',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]