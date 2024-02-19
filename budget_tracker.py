import json
import os

class BudgetTracker:
    def __init__(self):
        self.transactions = []
        self.categories = set()
        self.budget = 0

    def load_transactions(self, file_name):
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                self.transactions = json.load(file)
                for transaction in self.transactions:
                    self.categories.add(transaction['category'])

    def save_transactions(self, file_name):
        with open(file_name, 'w') as file:
            json.dump(self.transactions, file, indent=4)

    def add_transaction(self, category, amount, is_income=False):
        transaction_type = 'Income' if is_income else 'Expense'
        self.transactions.append({'category': category, 'amount': amount, 'type': transaction_type})
        self.categories.add(category)

    def calculate_budget(self):
        total_income = sum(transaction['amount'] for transaction in self.transactions if transaction['type'] == 'Income')
        total_expense = sum(transaction['amount'] for transaction in self.transactions if transaction['type'] == 'Expense')
        self.budget = total_income - total_expense

    def analyze_expenses(self):
        expense_by_category = {category: 0 for category in self.categories}
        for transaction in self.transactions:
            if transaction['type'] == 'Expense':
                expense_by_category[transaction['category']] += transaction['amount']
        
        print("Expense Analysis:")
        for category, amount in expense_by_category.items():
            print(f"{category}: ${amount}")

    def display_budget(self):
        print(f"Remaining Budget: ${self.budget}")

def main():
    budget_tracker = BudgetTracker()
    budget_tracker.load_transactions('transactions.json')

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Expense Analysis")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            budget_tracker.add_transaction(category, amount, is_income=True)
        elif choice == '2':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            budget_tracker.add_transaction(category, amount)
        elif choice == '3':
            budget_tracker.calculate_budget()
            budget_tracker.display_budget()
        elif choice == '4':
            budget_tracker.analyze_expenses()
        elif choice == '5':
            budget_tracker.save_transactions('transactions.json')
            print("Exiting. Your transactions have been saved.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
