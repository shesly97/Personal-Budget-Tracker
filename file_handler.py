# Importations modules/libraires os et json 
import os
import json

# Le nom du fichier où les transactions seront enregistrées (transactions.txt)
FILE_NAME = "transactions.txt"

# Fonction permettant de charger les transactions depuis un fichier JSON 
def load_transactions():
    
    transactions = []
    
    # Vérification de l'existance du fichier 
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            # Chargement les données JSON à partir du fichier texte
            try:
                transactions = json.load(file)
            except json.JSONDecodeError:
                print("Erreur de décodage JSON.")
    return transactions

# Fonction permettant de sauvegarder les transactions 
def save_transaction(transaction):
    
    # Chargement des transactions existantes
    transactions = load_transactions()
    
    # Ajout d'une nouvelle transaction à la liste
    transactions.append(transaction)
    
    # Sauvegarde de la liste mise à jour dans le fichier transactions.txt en format JSON
    with open(FILE_NAME, "w") as file:
        # Sauvegarde les transactions en format JSON dans le fichier avec une indentation pour rendre le fichier lisible
        json.dump(transactions, file, indent=4)

