import os
from owner import Owner
from account import Account
from prompts import Prompts
prompt = Prompts()


class Bank:
    def __init__(self):
        self.owners = Owner.load_owners()

    def save(self):
        Owner.save()
        Account.save()

    def get_all_owners(self):
        return self.owners

    def get_owner(self):
        while True:
            os.system('clear')
            try:
                id = prompt.owner_id_prompt()  # 5656435622
                print()
                return Owner.owners[id]
            except KeyError:
                f'Owner not found'
                if not prompt.try_again():
                    break

    def get_account(self):
        while True:
            os.system('clear')
            try:
                id = prompt.owner_id_prompt()  # 5656435622
                print()
                owner = Owner.owners[id]
                break
            except KeyError:
                f'Owner not found'
                if not prompt.try_again():
                    return ''
        while True:
            try:
                id = prompt.account_id_prompt()  # 87934
                print()
                return owner.accounts[id]
            except KeyError:
                f'Account not found'
                if not prompt.try_again():
                    return ''

    def list_all_accounts(self):
        os.system('clear')
        while True:
            password = prompt.password_prompt()
            if password == '12345':
                break
        print()
        for account in Account.accounts.values():
            print(f'{str(account)}\n')

    def create_new_owner(self):
        os.system('clear')
        owner_info = prompt.get_owner_info()
        owner = Owner(**owner_info)
        print(f'\n{owner}\n')
        if prompt.account_creation():
            self.create_new_account(owner)

    def create_new_account(self, owner):
        account_info = prompt.get_account_info()
        account = owner.new_account(account_info)
        print(f'\n{account}\n')

    def login(self):
        count = 0
        logged_in = False
        while True:
            while not logged_in:
                os.system('clear')
                try:
                    id = prompt.owner_id_prompt()  # 5656435622
                    print()
                    owner = Owner.owners[id]
                    logged_in = True
                    break
                except KeyError:
                    f'Owner not found'
                    if not prompt.try_again():
                        return ''
            os.system('clear')
            if count == 0:
                print(f'\nWelcome back {owner.first_name}.\n')
            else:
                print()
            count += 1
            option = prompt.owner_menu()
            accounts = [
                f'{account.last_five} {account.type}: ${account.get_balance():,.2f}' for account in owner.accounts.values()]
            if option == 'Deposit':
                choice = str(prompt.choose_account(accounts))[0:5]
                acc = owner.accounts[choice]
                print(f'\nBalance: ${acc.get_balance():,.2f}\n')
                amount = int(prompt.deposit())
                acc.deposit(amount)
                input()
            elif option == 'Withdraw':
                choice = str(prompt.choose_account(accounts))[0:5]
                acc = owner.accounts[choice]
                print(f'\nBalance: ${acc.get_balance():,.2f}\n')
                amount = int(prompt.withdraw())
                acc.withdraw(amount)
                input()
            elif option == 'View Accounts':
                choice = str(prompt.choose_account(accounts))[0:5]
                acc = owner.accounts[choice]
                os.system('clear')
                print(acc)
                input()
            elif option == 'Create New Account':
                account_info = prompt.get_account_info()
                owner.new_account(account_info)
            elif option == 'Write A Check':
                accounts = [
                    f'{account.last_five} {account.type}: ${account.get_balance():,.2f}' for account in owner.accounts.values() if account.type == 'Checking']
                choice = str(prompt.choose_account(accounts))[0:5]
                acc = owner.accounts[choice]
                acc.withdraw_using_check()
                input()
            elif option == 'Reset Checks':
                accounts = [
                    f'{account.last_five} {account.type}: ${account.get_balance():,.2f}' for account in owner.accounts.values() if account.type == 'Checking']
                choice = str(prompt.choose_account(accounts))[0:5]
                acc = owner.accounts[choice]
                acc.reset_checks()
            elif option == 'Logout':
                break
