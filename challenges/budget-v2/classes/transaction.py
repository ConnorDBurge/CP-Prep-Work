class Transaction:

    def __init__(self, category, name, amount):
        self.category = category
        self.name = name
        self.amount = float(amount)

    def __str__(self):
        string = f'{self.name:<22}' + f'$ {self.amount:,.2f}'.rjust(10)
        return string
