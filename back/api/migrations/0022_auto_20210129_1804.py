# Generated by Django 3.0.8 on 2021-01-29 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20210115_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='subscribed'),
        ),
        migrations.AlterField(
            model_name='document',
            name='link',
            field=models.URLField(default='default_product_thumbnail.png', help_text='Please complete the above URL', max_length=2000, verbose_name='link'),
        ),
    ]
