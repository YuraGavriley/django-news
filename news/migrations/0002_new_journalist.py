# Generated by Django 4.0 on 2022-03-18 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='journalist',
            field=models.CharField(default='Some Dude', max_length=100),
            preserve_default=False,
        ),
    ]
