from classes.transaction import Transaction
from termcolor import colored


class Category:

    def __init__(self, name):
        self.category_name = name
        self.total = 0
        self.transactions = []

    def transaction(self, month, category_name, name, amount):
        new_transaction = Transaction(month, category_name, name, amount)
        for transaction in self.transactions:
            if transaction.name == name:
                self.transactions.remove(transaction)
                self.transactions.append(new_transaction)
                break
        else:
            self.transactions.append(new_transaction)

        self.sum()
        return new_transaction

    def sum(self):
        sum = 0
        for transaction in self.transactions:
            sum += transaction.amount
        self.total = sum
        return self.total

    def change_transaction_name(self, name, new_name):
        for transaction in self.transactions:
            if transaction.name == name:
                transaction.name = new_name
                return transaction

    def str(self, percent):
        line = '\n--------------------------------\n'
        percent = f' - {percent:.0%}'
        name = colored(
            f'{self.category_name.upper() + f"{percent}":<22}', 'magenta')
        total = colored(f'$ {self.total:,.2f}'.rjust(10), 'magenta')

        string = line + name + total
        for transaction in self.transactions:
            string += f'\n{transaction.name:<22}' + \
                f'$ {transaction.amount:,.2f}'.rjust(10)
        return string
