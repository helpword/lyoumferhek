# Generated by Django 5.2.4 on 2025-07-05 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wilaya',
            options={'ordering': ['id'], 'verbose_name': 'Wilaya', 'verbose_name_plural': 'Wilayas'},
        ),
    ]
