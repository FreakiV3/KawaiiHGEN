# Hentai Script

## Description

Le Hentai Script est un script Python interactif qui utilise des webhooks Discord pour télécharger et partager des images NSFW aléatoires. Le script prend en charge l'ajout de plusieurs webhooks, les tests de webhooks, et offre diverses fonctionnalités pour gérer les images téléchargées.

## Fonctionnalités

- **Téléchargement d'images NSFW :** Le script télécharge des images NSFW aléatoires à partir de différentes sources.
- **Envoi sur Discord :** Les images téléchargées sont automatiquement envoyées sur un serveur Discord via un webhook.
- **Gestion des webhooks :** Ajoutez, testez et choisissez le webhook à utiliser depuis une liste enregistrée.
- **Suppression de fichiers :** Supprimez des fichiers spécifiques du dossier Hentai.

## Prérequis

- Python 3.x
- Les bibliothèques Python nécessaires peuvent être installées via `pip install -r requirements.txt`

## Utilisation

1. Clonez le référentiel : `git clone https://github.com/FreakiV3/KawaiiHGEN.git`
2. Naviguez dans le répertoire du script : `cd hentai-script`
3. Exécutez le script : `python main.py`

## Configuration

- Le script utilise un fichier `webhooks.json` pour stocker les webhooks. Assurez-vous de le créer s'il n'existe pas.

## Options du Menu

1. **Ajouter un nouveau webhook :** Permet d'ajouter un nouveau webhook au fichier `webhooks.json`.
2. **Tester le webhook actuel :** Envoie un message de test au webhook sélectionné.
3. **Lancer le script :** Démarre le téléchargement et l'envoi d'images NSFW.
4. **Supprimer un fichier :** Permet de supprimer un fichier spécifique du dossier Hentai.
5. **Lister les fichiers :** Affiche la liste des fichiers présents dans le dossier Hentai.

## Auteur

- [FreakiV3](https://github.com/votre-utilisateur)

## Licence

Ce projet est sous licence [MIT](LICENSE).

---

**Note:** Ce script est destiné à des fins de démonstration et de divertissement. Veuillez utiliser avec responsabilité et respecter les règles et politiques de Discord.
