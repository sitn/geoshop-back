# Generated by Django 3.0.8 on 2021-02-24 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20210129_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Draft'), ('PENDING', 'Pending'), ('QUOTE_DONE', 'Quote done'), ('READY', 'Ready'), ('IN_EXTRACT', 'In extract'), ('PARTIALLY_DELIVERED', 'Partially delivered'), ('PROCESSED', 'Processed'), ('ARCHIVED', 'Archived'), ('REJECTED', 'Rejected')], default='DRAFT', max_length=20, verbose_name='status'),
        ),
    ]