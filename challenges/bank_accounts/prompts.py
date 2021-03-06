import inquirer


class Prompts:

    def main_menu(self):
        return inquirer.list_input("Choose an action",
                                   choices=['Get All Owners', 'Get Owner Info', 'Get Account Info', 'List All Accounts', 'Create New Owner', 'Login To Owner', 'Exit'])

    def try_again(self):
        return inquirer.confirm("Try again?")

    def owner_id_prompt(self):
        return inquirer.text(message="Enter an Owner ID")

    def password_prompt(self):
        return inquirer.text(message="Enter Password")

    def account_id_prompt(self):
        return inquirer.text(message="Enter last five of account number")

    def get_owner_info(self):
        questions = [
            inquirer.Text('last_name', message="Last Name"),
            inquirer.Text('first_name', message="First Name"),
            inquirer.Text('street', message="Street"),
            inquirer.Text('city', message="City"),
            inquirer.Text('state', message="State"),
        ]
        return inquirer.prompt(questions)

    def account_creation(self):
        return inquirer.confirm("Do you want to create a new account?")

    def get_account_info(self):
        questions = [
            inquirer.List('type', message='Checking or Savings?',
                          choices=['Checking', 'Savings']),
            inquirer.Text('balance', message="Initial Deposit"),
        ]
        return inquirer.prompt(questions)

    def owner_menu(self):
        return inquirer.list_input("Choose an action",
                                   choices=['Deposit', 'Withdraw', 'View Accounts', 'Create New Account', 'Write A Check', 'Reset Checks', 'Logout'])

    def choose_account(self, accounts):
        return inquirer.list_input("Choose an Account",
                                   choices=accounts)

    def deposit(self):
        return inquirer.text(message="Deposit Amount")

    def withdraw(self):
        return inquirer.text(message="Withdraw Amount")

    def check(self):
        return inquirer.text(message="Check Amount")
