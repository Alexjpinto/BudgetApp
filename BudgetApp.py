import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget App")

        # Setup UI
        self.setup_ui()

        # Load transaction history
        self.load_history()

    def setup_ui(self):
        self.amount_var = tk.StringVar()
        self.category_var = tk.StringVar()
        self.description_var = tk.StringVar()
        self.type_var = tk.StringVar(value='Income')

        ttk.Label(self.root, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.amount_var).grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self.root, text="Category:").grid(row=1, column=0, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.category_var).grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self.root, text="Description:").grid(row=2, column=0, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.description_var).grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(self.root, text="Type:").grid(row=3, column=0, padx=10, pady=10)
        ttk.Combobox(self.root, textvariable=self.type_var, values=['Income', 'Expense']).grid(row=3, column=1, padx=10, pady=10)

        ttk.Button(self.root, text="Add Transaction", command=self.add_transaction).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.history_tree = ttk.Treeview(self.root, columns=('Amount', 'Category', 'Description', 'Type'), show='headings')
        self.history_tree.heading('Amount', text='Amount')
        self.history_tree.heading('Category', text='Category')
        self.history_tree.heading('Description', text='Description')
        self.history_tree.heading('Type', text='Type')
        self.history_tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def add_transaction(self):
        try:
            amount = float(self.amount_var.get())
            category = self.category_var.get()
            description = self.description_var.get()
            type_ = self.type_var.get()

            if amount <= 0:
                raise ValueError

            transaction = {
                'amount': amount,
                'category': category,
                'description': description,
                'type': type_
            }

            self.save_transaction(transaction)
            self.history_tree.insert('', 'end', values=(amount, category, description, type_))
            self.clear_form()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid amount")

    def save_transaction(self, transaction):
        if not os.path.exists('transactions.json'):
            with open('transactions.json', 'w') as file:
                json.dump([], file)

        with open('transactions.json', 'r') as file:
            transactions = json.load(file)

        transactions.append(transaction)

        with open('transactions.json', 'w') as file:
            json.dump(transactions, file)

    def load_history(self):
        if not os.path.exists('transactions.json'):
            return

        with open('transactions.json', 'r') as file:
            transactions = json.load(file)

        for transaction in transactions:
            self.history_tree.insert('', 'end', values=(transaction['amount'], transaction['category'], transaction['description'], transaction['type']))

    def clear_form(self):
        self.amount_var.set('')
        self.category_var.set('')
        self.description_var.set('')
        self.type_var.set('Income')

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()
