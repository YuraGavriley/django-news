# Generated by Django 4.0 on 2022-04-16 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_remove_new_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='news.category'),
            preserve_default=False,
        ),
    ]
