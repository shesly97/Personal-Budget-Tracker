# Importation des fichiers income, expense et file_handler
from income import add_income
from expense import add_expense
from file_handler import load_transactions

# Fonction permettant de voir la balance
def view_balance(transactions):
   
    total_income = sum(transaction['amount'] for transaction in transactions if transaction['type'] == 'income')
    total_expenses = sum(transaction['amount'] for transaction in transactions if transaction['type'] == 'expense')
    balance = total_income - total_expenses
    
    print(f"\n-- Balance --")
    print(f"Revenu total: ${total_income:.2f}")
    print(f"Dépenses totales: ${total_expenses:.2f}")
    print(f"Balance (Revenu - Dépenses): ${balance:.2f}")
    print("-------------------")

# Fonction permettant de lister les transactions (revenus et dépenses)
def display_transactions(transactions):
    
    if not transactions:
        print("Aucune transaction enregistrée.")
    else:
        print("\n-- Transactions --")
        for transaction in transactions:
            if transaction['type'] == 'income':
                print(f"Revenu de {transaction['source']} - ${transaction['amount']:.2f} le {transaction['date']}")
            elif transaction['type'] == 'expense':
                print(f"Dépense pour {transaction['category']} - ${transaction['amount']:.2f} le {transaction['date']}")
            print("-------------------")

# Fonction permettant d'afficher le menu
def display_menu():
    
    print("\n----- Menu -----")
    print("1. Ajouter un revenu")
    print("2. Voir le total des revenus")
    print("3. Ajouter une dépense")
    print("4. Voir le total des dépenses")
    print("5. Voir toutes les transactions")
    print("6. Voir la balance")
    print("7. Quitter")

# Fonction main 
def main():
    transactions = load_transactions()  # Chargement les transactions depuis le fichier
    
    while True:
        display_menu()
        choice = input("Choisissez une option (1/2/3/4/5/6/7): ")
        
        if choice == '1':
            add_income(transactions)
        elif choice == '2':
            # Affichage du total des revenus
            total_income = sum(transaction['amount'] for transaction in transactions if transaction['type'] == 'income')
            print(f"Revenu total: ${total_income:.2f}")
        elif choice == '3':
            add_expense(transactions)
        elif choice == '4':
            # Affichage du total des dépenses
            total_expense = sum(transaction['amount'] for transaction in transactions if transaction['type'] == 'expense')
            print(f"Dépenses totales: ${total_expense:.2f}")
        elif choice == '5':
            # Affichage de toutes les transactions
            display_transactions(transactions)
        elif choice == '6':
            # Affichage de la balance
            view_balance(transactions)
        elif choice == '7':
            print("Merci d'avoir utilisé Personal Budget Tracker. À la prochaine!")
            break  # Quitter la boucle et terminer le programme
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
