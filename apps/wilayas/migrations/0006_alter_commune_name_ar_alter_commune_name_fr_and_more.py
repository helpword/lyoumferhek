# Generated by Django 5.2.4 on 2025-07-08 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wilayas', '0005_alter_commune_created_at_alter_commune_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commune',
            name='name_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='commune',
            name='name_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='wilaya',
            name='name_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='wilaya',
            name='name_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
