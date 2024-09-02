#5. Write a Python program to create a class representing a bank. 
# Include methods for managing customer accounts and transactions.

class Bank:
    def __init__(self):
        self.customers = {}
        self.account_number = 1000

    def add_customer(self, name, initial_balance=0):
        # Check if the customer name already exists
        for customer in self.customers.values():
            if customer['name'] == name:
                print("Customer already exists.")
                return
        
        acc_number = self.account_number
        self.customers[acc_number] = {'name': name, 'balance': initial_balance}
        self.account_number += 1 

        print(f"Customer {name} added with account number {acc_number} and initial balance ${initial_balance}.")

    def deposit(self, acc_number, amount):
        if acc_number in self.customers:
            self.customers[acc_number]['balance'] += amount
            print(f"Deposited ${amount} to account {acc_number}. New balance: ${self.customers[acc_number]['balance']}")
        else:
            print(f"Account {acc_number} does not exist.")

    def withdraw(self, acc_number, amount):
        if acc_number in self.customers:
            if self.customers[acc_number]['balance'] >= amount:
                self.customers[acc_number]['balance'] -= amount
                print(f"Withdrew ${amount} from account {acc_number}. New balance: ${self.customers[acc_number]['balance']}")
            else:
                print(f"Insufficient balance in account {acc_number}.")
        else:
            print(f"Account {acc_number} does not exist.")

    def get_balance(self, acc_number):
        if acc_number in self.customers:
            return self.customers[acc_number]['balance']
        else:
            print(f"Account {acc_number} does not exist.")
            return None

    def transfer(self, from_account, to_account, amount):
        if from_account in self.customers and to_account in self.customers:
            if self.customers[from_account]['balance'] >= amount:
                self.customers[from_account]['balance'] -= amount
                self.customers[to_account]['balance'] += amount
                print(f"Transferred ${amount} from account {from_account} to account {to_account}.")
            else:
                print(f"Insufficient balance in account {from_account}.")
        else:
            print("One or both account numbers do not exist.")

# Example usage
bank = Bank()

while True:
    print("\n1. Add Customer")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter customer name: ")
        initial_balance = float(input("Enter initial balance: "))
        bank.add_customer(name, initial_balance)
    
    elif choice == '2':
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter amount to deposit: "))
        bank.deposit(account_number, amount)
    
    elif choice == '3':
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter amount to withdraw: "))
        bank.withdraw(account_number, amount)
    
    elif choice == '4':
        from_account = int(input("Enter from account number: "))
        to_account = int(input("Enter to account number: "))
        amount = float(input("Enter amount to transfer: "))
        bank.transfer(from_account, to_account, amount)
    
    elif choice == '5':
        account_number = int(input("Enter account number: "))
        balance = bank.get_balance(account_number)
        if balance is not None:
            print(f"Account {account_number} balance: ${balance}")
    
    elif choice == '6':
        break
    
    else:
        print("Invalid choice. Please try again.")
