import os
from bank import Bank
from prompts import Prompts
bank = Bank()
prompt = Prompts()


while True:
    os.system('clear')
    main_option = prompt.main_menu()
    if main_option == 'Get All Owners':
        print(bank.get_all_owners())
        input()
    elif main_option == 'Get Owner Info':
        print(bank.get_owner())
        input()
    elif main_option == 'Get Account Info':
        print(bank.get_account())
        input()
    elif main_option == 'Create New Owner':
        bank.create_new_owner()
        input()
    elif main_option == 'Login To Owner':
        bank.login()
    elif main_option == 'Exit':
        bank.save()
        break  # leave application
