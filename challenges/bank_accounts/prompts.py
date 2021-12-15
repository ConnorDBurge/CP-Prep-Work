import inquirer


class Prompts:

    def main_menu(self):
        return inquirer.list_input("Choose an action",
                                   choices=['Get Owner Info', 'Get Account Info', 'Exit'])

    def try_again(self):
        return inquirer.confirm("Try again?", default=False)

    def owner_id_prompt(self):
        return inquirer.text(message="Enter an Owner ID")

    def account_id_prompt(self):
        return inquirer.text(message="Enter last five of account number")
