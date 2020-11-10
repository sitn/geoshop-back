# Generated by Django 3.0.8 on 2020-10-09 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20201005_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='invoice_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoice_contact', to='api.Contact', verbose_name='invoice_contact'),
        ),
    ]
