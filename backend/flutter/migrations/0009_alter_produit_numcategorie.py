# Generated by Django 5.0.1 on 2025-07-03 09:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flutter', '0008_alter_utilisateur_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='numCategorie',
            field=models.ForeignKey(db_column='numCategorie', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produits', to='flutter.categorie'),
        ),
    ]
