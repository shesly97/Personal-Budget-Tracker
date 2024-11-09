"""
Create a function to input and store:
1. Date of income
2. Income source (e.g., salary, gift)
3. Amount

"""

# Importation du fichier "save_transaction" pour enregistrer une transaction de "revenu"
from file_handler import save_transaction

# Fonction ajoutant un revenu comme étant une transaction
def add_income(transactions):
   
    date = input("Entrer la date (YYYY-MM-DD): ")
    source = input("Entrer la source de revenu (e.g., salary, gift): ")
    amount = float(input("Entrer le montant du revenu: "))
    
    transaction = {'type': 'income', 'date': date, 'source': source, 'amount': amount}
    transactions.append(transaction) # ajout d'une transaction à la liste des transactions
    
    # Sauvegarde la transaction dans le fichier transactions.txt
    save_transaction(transaction)
    
    # Message de confirmation
    print("Revenu ajouté : {} - ${:.2f} le {}".format(source, amount, date))
