import random
class Bank:
    def __init__(self):
        self.users = {}
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True
        
    def create_account(self, name, email, address, account_type):
        account_number = random.randint(10000, 99999)
        while account_number in self.users:
            account_number = random.randint(10000, 99999)
        self.users[account_number] = {
            'name': name,'email': email,'address': address,'account_type': account_type,'balance': 0,'transactions': []
        }
        return account_number

    def delete_account(self, account_number):
        if account_number in self.users:
            del self.users[account_number]

    def deposit(self, account_number, amount):
        if amount > 0:
            self.users[account_number]['balance'] += amount
            self.total_balance += amount
            #TODO : trsansactions er hisab korte hobe
            self.users[account_number]['transactions'].append(f"Deposited ${amount}")

    def withdraw(self, account_number, amount):
        if amount <= self.users[account_number]['balance']:
            self.users[account_number]['balance'] -= amount
            self.total_balance -= amount
            self.users[account_number]['transactions'].append(f"Withdrew ${amount}")
        else:
            print("Withdrawal money is not available ")

    def check_balance(self, account_number):
        return self.users[account_number]['balance']

    def transfer(self, from_account, to_account, amount):
        if to_account in self.users:
            if amount <= self.users[from_account]['balance']:
                self.users[from_account]['balance'] -= amount
                self.users[to_account]['balance'] += amount
                #TODO h
                self.users[from_account]['transactions'].append(f"Transferred ${amount} to account {to_account}")
                self.users[to_account]['transactions'].append(f"Received ${amount} from account {from_account}")
            else:
                print("  transfer money is not available . please diposite money ")
        else:
            print(" account number is invalid ")

    def take_loan(self, account_number, amount):
        if self.loan_feature_enabled:
            if account_number in self.users:
                if len(self.users[account_number]['transactions']) <= 2:
                    self.users[account_number]['balance'] += amount
                    self.total_loan_amount += amount
                    self.users[account_number]['transactions'].append(f"Took a loan of ${amount}")
                else:
                    print("loan can not give for 2 loans")
            else:
                print("account number is invalid")

    def show_transactions(self, account_number):
        return self.users[account_number]['transactions']

    def show_all_accounts(self):
        return self.users

    def enable_loan_feature(self):
        self.loan_feature_enabled = True

    def disable_loan_feature(self):
        self.loan_feature_enabled = False

    def show_total_balance(self):
        return self.total_balance

    def show_total_loan_amount(self):
        return self.total_loan_amount

class User:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        return self.bank.create_account(name, email, address, account_type)

    def deposit_money(self, account_number, amount):
        self.bank.deposit(account_number, amount)

    def withdraw_money(self, account_number, amount):
        self.bank.withdraw(account_number, amount)

    def check_balance(self, account_number):
        return self.bank.check_balance(account_number)

    def transfer_money(self, from_account, to_account, amount):
        self.bank.transfer(from_account, to_account, amount)

    def take_loan(self, account_number, amount):
        self.bank.take_loan(account_number, amount)

    def check_transaction_history(self, account_number):
        return self.bank.show_transactions(account_number)