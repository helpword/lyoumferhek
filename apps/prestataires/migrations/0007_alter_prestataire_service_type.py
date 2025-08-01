# Generated by Django 5.2.4 on 2025-07-22 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestataires', '0006_prestataire_service_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestataire',
            name='service_type',
            field=models.CharField(choices=[('Photographe / Vidéaste', 'Photographe / Vidéaste'), ('Traiteur (Catering)', 'Traiteur (Catering)'), ('Décorateur / Fleuriste', 'Décorateur / Fleuriste'), ('Musicien / DJ / Animateur', 'Musicien / DJ / Animateur'), ('Location de salle', 'Location de salle'), ('Maquilleuse / Coiffeuse', 'Maquilleuse / Coiffeuse'), ('Location de vêtements / Costumes', 'Location de vêtements / Costumes'), ('Location de matériel (sono, lumière, mobilier)', 'Location de matériel (sono, lumière, mobilier)'), ('Transport / Voiture de mariage', 'Transport / Voiture de mariage'), ('Planificateur d’événements (Event Planner)', 'Planificateur d’événements (Event Planner)'), ('Service de sécurité', 'Service de sécurité'), ('Service de nettoyage après fête', 'Service de nettoyage après fête')], max_length=100),
        ),
    ]
