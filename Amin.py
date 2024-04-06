class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        return self.bank.create_account(name, email, address, account_type)

    def delete_account(self, account_number):
        self.bank.delete_account(account_number)

    def see_all_user_accounts(self):
        return self.bank.show_all_accounts()

    def check_total_available_balance(self):
        return self.bank.show_total_balance()

    def check_total_loan_amount(self):
        return self.bank.show_total_loan_amount()

    def enable_loan_feature(self):
        self.bank.enable_loan_feature()

    def disable_loan_feature(self):
        self.bank.disable_loan_feature()