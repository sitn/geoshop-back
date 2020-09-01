# Generated by Django 3.0.8 on 2020-08-14 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200811_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_contact',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='srid',
            field=models.IntegerField(default=2056, verbose_name='srid'),
        ),
        migrations.AlterField(
            model_name='document',
            name='link',
            field=models.URLField(default='api/default_product_thumbnail.png', help_text='Please complete the above URL', verbose_name='link'),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='image_link',
            field=models.CharField(default='api/default_metadata_image.png', max_length=250, verbose_name='image_link'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail_link',
            field=models.CharField(default='api/default_product_thumbnail.png', max_length=250, verbose_name='thumbnail_link'),
        ),
    ]