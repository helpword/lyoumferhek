# Generated by Django 5.2.4 on 2025-07-10 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wilayas', '0006_alter_commune_name_ar_alter_commune_name_fr_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commune',
            name='name_ar',
        ),
        migrations.RemoveField(
            model_name='wilaya',
            name='name_ar',
        ),
        migrations.AddField(
            model_name='commune',
            name='ar_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='wilaya',
            name='ar_name',
            field=models.CharField(default='بدون اسم عربي', max_length=100),
            preserve_default=False,
        ),
    ]
