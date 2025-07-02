# Backend - Projet Django

Ce dossier contient le backend du projet, développé avec Django.

## ⚙️ Installation

1. **Cloner le dépôt :**

```bash
git clone https://github.com/ton-utilisateur/ton-projet.git
cd ton-projet/backend

>>>Créer un environnement virtuel 
python -m venv venv
source venv/bin/activate  # Sous Windows : venv\Scripts\activate

>>>Installer les dépendances
pip install -r requirements.txt

>>>Appliquer la migration
python manage.py migrate

>>>Lancer le serveur
python manage.py runserver
