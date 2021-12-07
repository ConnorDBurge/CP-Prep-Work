class Transaction:

    def __init__(self, month, category_name, name, amount):
        self.month = month
        self.category_name = category_name
        self.name = name
        self.amount = float(amount)

    def __str__(self):
        string = f'{self.name:<22}' + f'$ {self.amount:,.2f}'.rjust(10)
        return string
