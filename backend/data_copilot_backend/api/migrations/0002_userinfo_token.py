# Generated by Django 5.0.4 on 2024-05-21 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='token',
            field=models.CharField(default='', max_length=100),
        ),
    ]
