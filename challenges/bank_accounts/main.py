from bank import Bank
from prompts import Prompts
bank = Bank()
prompt = Prompts()


while True:
    main_option = prompt.main_menu()
    if main_option == 'Get Owner Info':
        print(bank.get_owner())
        input()
    elif main_option == 'Get Account Info':
        print(bank.get_account())
        input()
    elif main_option == 'Exit':
        break  # leave application
