# Generated by Django 3.2.8 on 2021-12-21 11:23

from django.db import migrations
from django.db.models import F, Value
from django.db.models.functions import Concat, Coalesce

def merge_metadata_descriptions(apps, schema_editor):
    """Concats description_short and description_long with line return"""
    Metadata = apps.get_model('api', 'Metadata')
    db_alias = schema_editor.connection.alias
    Metadata.objects.using(db_alias).update(
        description_long=Concat(
            Coalesce(Concat(F('description_short'), Value('<br>\n')), Value('')),
            F('description_long'))
    )

def reverse(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_product_geom'),
    ]

    operations = [
        migrations.RunPython(merge_metadata_descriptions, reverse),
    ]