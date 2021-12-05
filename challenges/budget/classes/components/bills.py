from .component import Component


class Bill(Component):

    def __init__(self):
        self.bill_dict = {}
        self.bill_total = 0

    def add_new_bill(self, name, amount):
        self.bill_dict[name] = int(amount)
        self.bill_total += int(amount)

    def reduce_bill(self, name, amount):
        self.bill_dict[name] = int(amount)
        self.bill_total -= int(amount)
