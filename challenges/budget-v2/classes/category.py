from classes.transaction import Transaction


class Category:

    def __init__(self, name):
        self.name = name
        self.total = 0
        self.transactions = list()

    def transaction(self, name, amount):
        new_transaction = Transaction(self.name, name, amount)
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

    def str(self, percent):
        string = f'\n--------------------------------\n{self.name.upper() + f" - {percent:.0%}":<22}' + \
            f'$ {self.total:,.2f}'.rjust(10)
        for transaction in self.transactions:
            string += f'\n{transaction.name:<22}' + \
                f'$ {transaction.amount:,.2f}'.rjust(10)
        return string
