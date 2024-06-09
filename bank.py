class Account:
    def __init__(self, holder_name, email, address, account_type) -> None:
        self.holder_name = holder_name
        self.email = email
        self.address = address
        self.balance = 0
        self.account_type = account_type
        self.account_number = holder_name+email
        self.transaction_history = []
        self.loan_qouta = 2

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Tk {amount} deposited to {self.account_number}")
            print(f"Tk {amount} deposited to {self.account_number}")
        else:
            print("Invalid Amount !")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded !")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Tk {amount} withdrawal from {self.account_number}")
            print(f"Tk {amount} withdrawal from {self.account_number}")


    def check_balance(self):
        print(f"Your current balance is {self.balance} tk")

    def check_transaction_history(self):
        print("---Transaction History----")
        for transaction in self.transaction_history:
            print(transaction)

    

class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.accounts = []
        self.total_balance = 100000
        self.loan_status = "on"
        self.total_loan = 0
        self.is_bankrupt = False

    def add_account(self, holder_name, email, address, account_type):
        account = Account(holder_name, email, address, account_type)
        self.accounts.append(account)
        print(f"Account created successfully")

    def view_accounts(self):
        for account in self.accounts:
            print(account.holder_name, account.email, account.address, account.account_type, account.account_number)
        

    def delete_account(self, account_number):
        account = self.get_account(account_number)
        if account:
            self.accounts.remove(account)
            print(f"Account deleted successfully")


    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
            
        print(f"Account {account_number} does not exist !")

    def transfer(self, from_account_no, to_account_no, amount):
        from_acc = self.get_account(from_account_no)
        to_acc = self.get_account(to_account_no)

        if from_acc and to_acc:
            from_acc.withdraw(amount)
            to_acc.deposit(amount)

    def take_loan(self, acc_no, amount):
        if self.total_balance < amount or self.is_bankrupt:
            print(f"Sorry, {self.name} is bankrupt !!")
            return
        
        if self.loan_status == "off":
            print(f"Sorry, loan service is currently off !!")
            return
        
        account = self.get_account(acc_no)
        if not account:
            return
        
        if account.loan_qouta == 0:
            print("Sorry, your loan qouta is finished!")
            return
        
        self.total_balance -= amount
        self.total_loan += amount
        account.deposit(amount)
        account.loan_qouta -= 1
        print("Loan successful!")


    def change_bankrupt_status(self, status):
        self.is_bankrupt = status 

    def view_total_balance(self):
        print(f"total balance {self.total_balance}")
    
    def view_total_loan(self):
        print(f"total loan: {self.total_loan}")

    def change_loan_status(self, status):
        self.loan_status = status
