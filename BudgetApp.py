class BudgetApp:
    def __init__(self):
        self.transactions = {
            'income': [],
            'expense': []
        }
    
    def add_income(self, amount, category, description=''):
        if amount > 0:
            self.transactions['income'].append({'amount': amount, 'category': category, 'description': description})
            print(f"Income added: {amount} in {category}")
        else:
            print("Income amount must be positive.")
    
    def add_expense(self, amount, category, description=''):
        if amount > 0:
            self.transactions['expense'].append({'amount': amount, 'category': category, 'description': description})
            print(f"Expense added: {amount} in {category}")
        else:
            print("Expense amount must be positive.")
    
    def get_total_income(self):
        return sum(item['amount'] for item in self.transactions['income'])
    
    def get_total_expense(self):
        return sum(item['amount'] for item in self.transactions['expense'])
    
    def get_balance(self):
        return self.get_total_income() - self.get_total_expense()
    
    def get_summary_by_category(self, type_):
        summary = {}
        for item in self.transactions[type_]:
            if item['category'] not in summary:
                summary[item['category']] = 0
            summary[item['category']] += item['amount']
        return summary
    
    def display_summary(self):
        print("Income Summary by Category:")
        for category, amount in self.get_summary_by_category('income').items():
            print(f"{category}: {amount}")
        
        print("\nExpense Summary by Category:")
        for category, amount in self.get_summary_by_category('expense').items():
            print(f"{category}: {amount}")
        
        print(f"\nTotal Income: {self.get_total_income()}")
        print(f"Total Expense: {self.get_total_expense()}")
        print(f"Balance: {self.get_balance()}")

def main():
    app = BudgetApp()
    while True:
        print("\nBudget App Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = float(input("Enter income amount: "))
            category = input("Enter income category: ")
            description = input("Enter description (optional): ")
            app.add_income(amount, category, description)
        
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            description = input("Enter description (optional): ")
            app.add_expense(amount, category, description)
        
        elif choice == '3':
            app.display_summary()
        
        elif choice == '4':
            print("Exiting the app.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
