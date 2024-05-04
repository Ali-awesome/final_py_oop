from abc import ABC
import uuid

class Bank:
    def __init__(self):
        self.users = {}
        self.admin = None
        self.total_balance = 1000
        self.bankrupt = False
        self.loan_feature = True
    
    def add_user(self, user):
        self.users[user.email] = user

    def delete_user(self, email):
        if email in self.users:
            del self.users[email]
            print("Account deleted successfully")
            print()
        else:
            print("User with this email does not exist")
            print()
    
    def total_balance(self):
        total_balance = self.total_balance 
        for user in self.users.values():
            total_balance += user.balance
        return total_balance
    
    def total_loan(self):
        total_loan = 0
        for user in self.users.values():
            total_loan += user.loan_amount
        return total_loan

class Account(ABC):
    def __init__(self, name, email, address, acc_type):
        self.account_number = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.address = address
        self.acc_type = acc_type
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        if self.bank.bankrupt:
            print("Bank is bankrupt! Deposit is not possible!")
        else:
            self.balance += amount
            self.transaction_history.append(("Deposit", amount))
            self.bank.total_balance += amount
            print("Deposit successful. Current balance:", self.balance)
            print()

    def withdraw(self, amount):
        if self.bank.bankrupt:
            print("Bank is bankrupt! Withdrawal is not possible!")
        elif amount > self.balance:
            print("Withdrawal amount exceeded.")
        else:
            self.balance -= amount
            self.transaction_history.append(("Withdrawal", amount))
            bank.total_balance -= amount  
            print(f"{amount} take withdrawn!. Current balance:",self.balance)
            print()

    def transfer(self, amount, recipient):
        if self.bank.bankrupt:
            print("Bank is bankrupt! Transfer is not possible!")
        elif amount > self.balance:
            print("Insufficient balance to transfer")
        else:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(("Transfer to " + recipient.name, amount))
            print(f"{amount} taka sent to {recipient.name}. Current balance:",self.balance)
            print()

    def transection_history(self):
        return self.transaction_history

class User(Account):
    def __init__(self, name, email, address, acc_type, bank):
        super().__init__(name, email, address, acc_type)
        self.loan_amount = 0
        self.loan_count = 0
        self.bank = bank
    
    def take_loan(self, amount):
        if self.bank.bankrupt:
            print("Bank is bankrupt! Loan is not possible!")
            return
        if not self.bank.loan_feature:
            print("Loan feature is currently disabled")
            return
        if self.loan_count >= 2:
            print("You have already taken the maximum number of loans")
            return
        if amount > self.bank.total_balance:
            print("You are not eligible for this much money!")
            return
        else:
            self.loan_amount += amount
            self.loan_count += 1
            self.bank.total_balance -= amount
            self.balance += amount
            self.transaction_history.append(("Loan", amount))
            print(f"{amount} taka loan taken! Current balance:", self.balance)
            print()

class Admin:
    def __init__(self, email, bank):
        self.email = email
        self.bank = bank

    def create_account(self, name, email, address, acc_type, bank):
        if email in bank.users:
            print("User with this email already exists.")
            return None
        else:
            account = User(name, email, address, acc_type, bank)
            bank.add_user(account)
            print("Account created successfully!")
            print()
            return account
        
    def toggle_loan_feature(self):
        self.bank.loan_feature = not self.bank.loan_feature
        if self.bank.loan_feature:
            print("Loan feature enabled")
        else:
            print("Loan feature disabled")

    def toggle_bankrupt_feature(self):
        self.bank.bankrupt = not self.bank.bankrupt
        if self.bank.bankrupt:
            print("Bankrupt feature enabled")
        else:
            print("Bankrupt feature disabled")

   
bank = Bank()
admin = Admin("admin@example.com", bank)

bank.users["user1@example.com"] = User("User 1", "user1@example.com", "Address 1", "Savings", bank)
bank.users["user2@example.com"] = User("User 2", "user2@example.com", "Address 2", "Current", bank)
bank.users["user3@example.com"] = User("User 3", "user3@example.com", "Address 3", "Savings", bank)

bank.admin = admin

def admin_menu(bank):
    while True:
        print("\n----- Welcome Admin! -----")
        print("1.\tCreate New Account")
        print("2.\tDelete Account")
        print("3.\tList Accounts")
        print("4.\tTotal Balance")
        print("5.\tTotal Loan Amount")
        print("6.\tToggle Loan Feature")
        print("7.\tToggle Bankrupt Feature")
        print("8.\tExit to Main Menu")
        admin_choice = input("Enter your choice: ")
        print()

        if admin_choice == "1":
            name = input("Enter user's name: ")
            email = input("Enter user's email: ")
            address = input("Enter user's address: ")
            acc_type = input("Enter user's account type (Savings/Current): ").capitalize()
            print()
            admin.create_account(name, email, address, acc_type, bank)
            

        elif admin_choice == "2":
            email = input("Enter user's email to delete account: ")
            print()
            bank.delete_user(email)

        elif admin_choice == "3":
            print("List of Accounts:")
            for user in bank.users.values():
                print("Email:", user.email)
                print("Name:", user.name)
                print("Account Number:", user.account_number)
                print("Account Type:", user.acc_type)
                print("Balance:", user.balance)
                print()

        elif admin_choice == "4":
            print("Total Balance of the Bank:", bank.total_balance)
            print()

        elif admin_choice == "5":
            print("Total Loan Amount of the Bank:", bank.total_loan())
            print()

        elif admin_choice == "6":
            admin.toggle_loan_feature()

        elif admin_choice == "7":
            admin.toggle_bankrupt_feature()

        elif admin_choice == "8":
            print("Taking Back to Main Manu...")
            print()
            break

        else:
            print("Invalid choice.")
            print()

def user_menu(bank):
    while True:
        print("\n----- Welcome Dear User! -----")
        print("1.\tDeposit")
        print("2.\tWithdraw")
        print("3.\tCheck Balance")
        print("4.\tTransection History")
        print("5.\tTake a Loan")
        print("6.\tTransfer Money")
        print("7.\tBack To Main Manu")
        choice = input("Please Enter Your Choice: ")
        print()

        if choice == '1':
            amount = int(input("Enter amount to deposit: "))
            user.deposit(amount)

        elif choice == '2':
            amount = int(input("Enter amount to withdraw: "))
            user.withdraw(amount)

        elif choice == '3':
            print("Available Balance:", user.balance)
            print()

        elif choice == '4':
            print("Transaction History:")
            for transaction in user.transection_history():
                print(transaction)
            print()

        elif choice == '5':
            amount = int(input("Enter loan amount: "))
            user.take_loan(amount)

        elif choice == '6':
            recipient = input("Enter recipient's email: ")
            if recipient not in user.bank.users:
                print("Account does not exist.")
                continue
            if recipient == user.email:
                print("You can't send money to yourself!")
                continue
            else:
                recipient = user.bank.users[recipient]
                amount = int(input("Enter amount to transfer: "))
                user.transfer(amount, recipient)

        elif choice == '7':
            print("Taking Back to Main Manu...")
            print()
            break

        else:
            print("Invalid choice.")
            print()

while True:
    print("\n----- Welcome! Please Login! -----")
    print("1.\tAdmin Login")
    print("2.\tUser Login")
    print("3.\tCreate New Account")
    print("4.\tExit")
    choice = input("Please Enter Your Choice: ")
    print()

    if choice == '1':
        email = input("Enter your email: ")
        if email == admin.email:
            admin_menu(bank)
        else:
            print("Invalid admin credentials.")

    elif choice == '2':
        email = input("Enter your email: ")
        if email in bank.users:
            user = bank.users[email]
            user_menu(user)
        else:
            print("User with this email does not exist.")
            print()

    elif choice == "3":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            account_type = input("Enter your account type (Savings/Current): ").capitalize()
            print()
            admin.create_account(name, email, address, account_type, bank)

    elif choice == '4':
        print("Exiting The Program...")
        break

    else:
        print("Invalid choice.")
        print()