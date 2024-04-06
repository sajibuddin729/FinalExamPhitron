from UserBank import *
from Amin import *

if __name__ == "__main__":
    bank = Bank()
    user_interface = User(bank)
    admin_interface = Admin(bank)

    while True:
        print("1. User")
        print("2. Admin")
        print("0. Exit")

        user_type = int(input(" user or admin? Enter your choice: "))

        if user_type == 1:
            print("\nUser Menu:")
            print("1. Account Create")
            print("2. Deposit money ")
            print("3. Withdraw korte money")
            print("4. Balance check")
            print("5. Transfer money")
            print("6. Take Loan ")
            print("7. Transaction History")
            print("0. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                name = input(" name: ")
                email = input(" email: ")
                address = input(" address: ")
                account_type = input(" type (1.Savings/2.Current): ")

                if account_type not in ['1', '2']:
                    print("Invalid account type")
                    continue

                account_number = user_interface.create_account(name, email, address, account_type)
                print(f"Account create successfully . account number is: {account_number}")
            elif choice == 2:
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter deposit money as your wish : "))
                user_interface.deposit_money(account_number, amount)
                print("Amount deposited successfully done ")
            elif choice == 3:
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter withdraw money : "))
                user_interface.withdraw_money(account_number, amount)
            elif choice == 4:
                account_number = int(input("Enter account number: "))
                balance = user_interface.check_balance(account_number)
                print(f" balance : ${balance}")
            elif choice == 5:
                from_account = int(input("Enter account number: "))
                to_account = int(input("Enter reciver account number: "))
                amount = float(input("Enter transfer money : "))
                user_interface.transfer_money(from_account, to_account, amount)
            elif choice == 6:
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter money : "))
                user_interface.take_loan(account_number, amount)
            elif choice == 7:
                account_number = int(input("Enter account number: "))
                transactions = user_interface.check_transaction_history(account_number)
                print(" ALL transaction :")
                for transaction in transactions:
                    print(transaction)
            elif choice == 0:
                break
            else:
                print("Invalid choice")
        elif user_type == 2:
            print("\nAdmin Menu:")
            print("1.  Account Create")
            print("2. Delete Account")
            print("3. Show ALL User Accounts")
            print("4. Show available balance")
            print("5. Show loan balance ")
            print("6. enable loan")
            print("7. disable loan")
            print("0. exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                name = input("name: ")
                email = input("email: ")
                address = input("address: ")
                account_type = input("type (1.Savings/2.Current): ")

                if account_type not in ['1', '2']:
                    print("Invalid account type")
                    continue

                account_number = admin_interface.create_account(name, email, address, account_type)
                print(f"Account successfully create . user account number is {account_number}")
            elif choice == 2:
                account_number = int(input("Enter account number  : "))
                admin_interface.delete_account(account_number)
                print("Account deleted successfully ")
            elif choice == 3:
                all_accounts = admin_interface.see_all_user_accounts()
                print("Show All user :")
                for account_number, account_info in all_accounts.items():
                    print(f"Account Numbe: {account_number}")
                    print(f"Name: {account_info['name']}")
                    print(f"Email: {account_info['email']}")
                    print(f"Address: {account_info['address']}")
                    print(f"Type: {account_info['account_type']}")
                    print(f"Balanceace : ${account_info['balance']}")
                    print()
            elif choice == 4:
                total_balance = admin_interface.check_total_available_balance()
                print(f" available balance is : ${total_balance}")
            elif choice == 5:
                total_loan_amount = admin_interface.check_total_loan_amount()
                print(f"Total Loan : ${total_loan_amount}")
            elif choice == 6:
                admin_interface.enable_loan_feature()
                print("Loan feature is enable successfully ")
            elif choice == 7:
                admin_interface.disable_loan_feature()
                print("Loan feature is disable")
            elif choice == 0:
                break
            else:
                print("Invalid choice")
        elif user_type == 0:
            break
        else:
            print("Invalid choice")
