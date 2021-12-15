import os
from owner import Owner
from account import Account
from prompts import Prompts
prompt = Prompts()


class Bank:
    def __init__(self):
        Owner.load_owners()

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
