"""
Create a function to input and store:
1. Date of expense
2. Expense category (e.g., food, rent, entertainment)
3. Amount

"""
# Importation du fichier "save_transaction" pour enregistrer une transaction de "dépense"
from file_handler import save_transaction

# Fonction ajoutant une dépense comme étant une transaction
def add_expense(transactions):
    
    date = input("Entrer la date de la dépense (YYYY-MM-DD): ")
    category = input("Entrer la catégorie de la dépense (e.g., food, rent, entertainment): ")
    amount = float(input("Entrer le montant de la dépense: "))
    
    
    transaction = {'type': 'expense', 'date': date, 'category': category, 'amount': amount}
    
    transactions.append(transaction) # ajout d'une transaction à la liste des dépenses

    
    # Sauvegarder la transaction dans le fichier transactions.txt
    save_transaction(transaction)
    
    # Message de confirmation
    print("Dépense ajoutée : {} - ${:.2f} le {}".format(category, amount, date))

