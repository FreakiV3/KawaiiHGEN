import requests
import os
import time
from concurrent.futures import ThreadPoolExecutor
import json
from colorama import init, Fore
from pyfiglet import Figlet
import shutil

# Initialisation des couleurs avec Colorama
init(autoreset=True)
COLORS = {
    "GREEN": Fore.LIGHTGREEN_EX,
    "YELLOW": Fore.LIGHTYELLOW_EX,
    "RED": Fore.LIGHTRED_EX,
    "CYAN": Fore.LIGHTCYAN_EX,
    "MAGENTA": Fore.LIGHTMAGENTA_EX,
    "RESET": Fore.RESET,
}

# Vérifie si le dossier "Hentai" existe, sinon le crée
if not os.path.exists("Hentai"):
    os.makedirs("Hentai")

# ASCII art
ascii_art = Figlet(font="slant")
logo = ascii_art.renderText('Hentai Script')

# Animation KawaiiSquad
kawaii_animation = [
    "Script KawaiiSquad,",
    "- Scripteur FreakiV3",
]

# Fonction pour animer le texte
def animate_text(lines, delay=0.1):
    for line in lines:
        print("\r" + " " * 40, end="", flush=True)
        for char in line:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()
        time.sleep(1)
    print("\r" + " " * 40, end="", flush=True)  # Efface la dernière ligne

# Efface l'écran
os.system('cls' if os.name == 'nt' else 'clear')

# Obtient la taille de la console
columns, rows = shutil.get_terminal_size()

# Calcule la position pour centrer le texte
centered_row = int(rows) // 2 - len(kawaii_animation) // 2

# Positionne le curseur en haut de la console
print("\n" * centered_row)

# Animation des créateurs au centre
animate_text(kawaii_animation, delay=0.05)
time.sleep(1)

# Efface l'écran à nouveau
os.system('cls' if os.name == 'nt' else 'clear')

# Affiche le logo au centre de l'écran
centered_row = int(rows) // 2 - len(logo.split('\n')) // 2
print("\n" * centered_row)
print(f"{COLORS['CYAN']}{logo}{COLORS['RESET']}")
time.sleep(1)

# Définition de la variable URLS
URLS = [
    "https://nekobot.xyz/api/image?type=hentai",
    "https://api.waifu.pics/nsfw/waifu",
    "https://api.waifu.pics/nsfw/neko",
    "https://api.waifu.pics/nsfw/blowjob"
]

# Initialisation de la variable i
i = 0

# Fonction pour afficher le panneau de paramètres
def show_options():
    print("\nOptions:")
    print(f"1. {COLORS['MAGENTA']}Ajouter un nouveau webhook{COLORS['RESET']}")
    print(f"2. {COLORS['MAGENTA']}Tester le webhook actuel{COLORS['RESET']}")
    print(f"3. {COLORS['MAGENTA']}Lancer le script{COLORS['RESET']}")
    print(f"4. {COLORS['RED']}Quitter{COLORS['RESET']}")
    print(f"5. {COLORS['MAGENTA']}Envoyer un message texte sur Discord")
    print(f"6. {COLORS['MAGENTA']}Lister les fichiers dans le dossier Hentai")
    print(f"7. {COLORS['MAGENTA']}Supprimer un fichier hentai")
    print(f"8. {COLORS['MAGENTA']}Supprimer tous les fichiers hentai")
    print(f"9. {COLORS['MAGENTA']}Modifier le dossier Hentai")
    return input("Choisissez une option (1-9): ")

# Fonction pour ajouter un nouveau webhook dans le fichier JSON
def add_webhook():
    webhook_url = input(f"Entrez le nouveau webhook URL: {COLORS['MAGENTA']}")
    with open("webhooks.json", "r+") as file:
        data = json.load(file)
        data.append(webhook_url)
        file.seek(0)
        json.dump(data, file, indent=2)
        print(f"{COLORS['GREEN']}Webhook ajouté avec succès!{COLORS['RESET']}")

# Fonction pour tester le webhook actuel avec une animation
def test_webhook(webhook_url):
    print(f"{COLORS['MAGENTA']}Test du webhook en cours...{COLORS['RESET']}", end="")
    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    print()
    try:
        requests.post(webhook_url, json={"content": "Test réussi!"})
        print(f"{COLORS['GREEN']}Test réussi! Vérifiez votre serveur Discord.{COLORS['RESET']}")
    except requests.RequestException as e:
        print(f"{COLORS['RED']}Échec du test du webhook: {e}{COLORS['RESET']}")

# Fonction pour envoyer l'image sur Discord
def send_to_discord(image_path, webhook_url):
    try:
        with open(image_path, "rb") as f:
            requests.post(webhook_url, files={"file": f})
        print(f"{COLORS['GREEN']}Image envoyée à Discord{COLORS['RESET']}")
    except requests.RequestException as e:
        print(f"{COLORS['RED']}Échec de l'envoi de l'image à Discord: {e}{COLORS['RESET']}")
    except Exception as e:
        print(f"{COLORS['RED']}Erreur lors de l'envoi de l'image à Discord: {e}{COLORS['RESET']}")

def download_image(url):
    global i
    res = requests.get(url)
    res = res.json()

    if "waifu" in url:
        link = res["url"]
    else:
        link = res["message"]

    s = link.split("/")
    Name = s.pop()

    try:
        response = requests.get(link)

        with open(f"./Hentai/{Name}", "wb") as f:
            response.raise_for_status()
            for ch in response.iter_content(1024):
                f.write(ch)
        i += 1
        print(f"{COLORS['GREEN']}Téléchargé {i} hentai{COLORS['RESET']}")
        return f"./Hentai/{Name}"
    except Exception as e:
        print(f"{COLORS['RED']}Échec du téléchargement de l'image: {e}{COLORS['RESET']}")
        return None

# Fonction pour envoyer un message texte sur Discord
def send_text_to_discord(text, webhook_url):
    try:
        requests.post(webhook_url, json={"content": text})
        print(f"{COLORS['GREEN']}Message texte envoyé à Discord{COLORS['RESET']}")
    except requests.RequestException as e:
        print(f"{COLORS['RED']}Échec de l'envoi du message texte à Discord: {e}{COLORS['RESET']}")

# Fonction pour liste des fichiers dans le dossier Hentai
def list_hentai_files():
    hentai_files = os.listdir("./Hentai")
    if hentai_files:
        print(f"\n{COLORS['CYAN']}Liste des fichiers dans le dossier 'Hentai':{COLORS['RESET']}")
        for file in hentai_files:
            print(file)
    else:
        print(f"{COLORS['YELLOW']}Le dossier 'Hentai' est vide.{COLORS['RESET']}")

# Fonction pour supprimer un fichier Hentai
def delete_hentai_file():
    list_hentai_files()
    file_to_delete = input(f"Entrez le nom du fichier à supprimer: {COLORS['MAGENTA']}")
    file_path = f"./Hentai/{file_to_delete}"
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{COLORS['GREEN']}Le fichier '{file_to_delete}' a été supprimé avec succès.{COLORS['RESET']}")
    else:
        print(f"{COLORS['RED']}Le fichier spécifié n'existe pas.{COLORS['RESET']}")

# Fonction pour supprimer tous les fichiers Hentai
def delete_all_hentai_files():
    confirmation = input(
        f"{COLORS['RED']}Êtes-vous sûr de vouloir supprimer tous les fichiers hentai? (Oui/Non): {COLORS['RESET']}"
    )
    if confirmation.lower() == "oui":
        shutil.rmtree("./Hentai")
        os.makedirs("Hentai")
        print(f"{COLORS['GREEN']}Tous les fichiers hentai ont été supprimés avec succès.{COLORS['RESET']}")
    else:
        print(f"{COLORS['YELLOW']}Suppression annulée.{COLORS['RESET']}")

# Fonction pour modifier le dossier Hentai
def change_hentai_folder():
    new_folder_path = input(f"Entrez le nouveau chemin du dossier Hentai: {COLORS['MAGENTA']}")
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        print(f"{COLORS['GREEN']}Le dossier Hentai a été modifié avec succès.{COLORS['RESET']}")
    else:
        print(f"{COLORS['RED']}Le chemin spécifié existe déjà.{COLORS['RESET']}")

# Fonction principale
def main():
    if not os.path.exists("webhooks.json"):
        with open("webhooks.json", "w") as file:
            json.dump([], file)

    # Initialisation de la variable i avant d'entrer dans la boucle principale
    global i
    i = 0

    while True:
        option = show_options()

        if option == "1":
            add_webhook()
        elif option == "2":
            with open("webhooks.json", "r") as file:
                webhooks = json.load(file)
            if not webhooks:
                print(f"{COLORS['RED']}Aucun webhook enregistré. Ajoutez-en un d'abord.{COLORS['RESET']}")
            else:
                for i, webhook in enumerate(webhooks, start=1):
                    print(f"{i}. {webhook}")
                choice = input(f"Choisissez un webhook pour le tester (1-{len(webhooks)}): {COLORS['MAGENTA']}")
                try:
                    choice = int(choice)
                    if 1 <= choice <= len(webhooks):
                        test_webhook(webhooks[choice - 1])
                    else:
                        print(f"{COLORS['RED']}Choix invalide.{COLORS['RESET']}")
                except ValueError:
                    print(f"{COLORS['RED']}Veuillez entrer un nombre valide.{COLORS['RESET']}")
        elif option == "3":
            break
        elif option == "4":
            print(f"{COLORS['RED']}Au revoir!{COLORS['RESET']}")
            exit()
        elif option == "5":
            with open("webhooks.json", "r") as file:
                webhooks = json.load(file)
            if not webhooks:
                print(f"{COLORS['RED']}Aucun webhook enregistré. Ajoutez-en un d'abord.{COLORS['RESET']}")
            else:
                for i, webhook in enumerate(webhooks, start=1):
                    print(f"{i}. {webhook}")
                webhook_choice = input(f"Choisissez un webhook à utiliser (1-{len(webhooks)}): {COLORS['MAGENTA']}")
                try:
                    webhook_choice = int(webhook_choice)
                    if 1 <= webhook_choice <= len(webhooks):
                        text_message = input(f"Entrez le message à envoyer sur Discord: {COLORS['MAGENTA']}")
                        send_text_to_discord(text_message, webhooks[webhook_choice - 1])
                    else:
                        print(f"{COLORS['RED']}Choix invalide.{COLORS['RESET']}")
                except ValueError:
                    print(f"{COLORS['RED']}Veuillez entrer un nombre valide.{COLORS['RESET']}")
        elif option == "6":
            list_hentai_files()
        elif option == "7":
            delete_hentai_file()
        elif option == "8":
            delete_all_hentai_files()
        elif option == "9":
            change_hentai_folder()
        else:
            print(f"{COLORS['RED']}Option invalide. Veuillez choisir une option valide.{COLORS['RESET']}")

    # Lancement du script principal avec le webhook choisi
    with open("webhooks.json", "r") as file:
        webhooks = json.load(file)
    if not webhooks:
        print(f"{COLORS['RED']}Aucun webhook enregistré. Ajoutez-en un d'abord.{COLORS['RESET']}")
        exit()

    # Sélection du webhook à utiliser
    for i, webhook in enumerate(webhooks, start=1):
        print(f"{i}. {webhook}")
    choice = input(f"Choisissez un webhook à utiliser (1-{len(webhooks)}): {COLORS['MAGENTA']}")
    try:
        choice = int(choice)
        if 1 <= choice <= len(webhooks):
            WEBHOOK_URL = webhooks[choice - 1]
        else:
            print(f"{COLORS['RED']}Choix invalide. Utilisation du premier webhook.{COLORS['RESET']}")
            WEBHOOK_URL = webhooks[0]
    except ValueError:
        print(f"{COLORS['RED']}Veuillez entrer un nombre valide. Utilisation du premier webhook.{COLORS['RESET']}")
        WEBHOOK_URL = webhooks[0]

    # Script principal
    with ThreadPoolExecutor(10) as pool:
        while True:
            for url in URLS:
                image_path = pool.submit(download_image, url).result()
                if image_path:
                    send_to_discord(image_path, WEBHOOK_URL)
                time.sleep(1)

if __name__ == "__main__":
    main()