# Generated by Django 3.2.6 on 2021-09-01 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ConnectionApp', '0008_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familyidentity',
            name='national_doc',
        ),
    ]
