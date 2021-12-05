class Transaction:

    def __init__(self, category_name, name, amount):
        self.category_name = category_name
        self.name = name
        self.amount = float(amount)

    def __str__(self):
        string = f'{self.name:<22}' + f'$ {self.amount:,.2f}'.rjust(10)
        return string
