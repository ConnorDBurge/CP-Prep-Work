from datetime import datetime
import time


class IceCream:

    def __init__(self, flavor):
        self.flavor = flavor
        self.status = 'watery'
        self.placed_in = datetime.now()

    def __str__(self):
        return f'{self.flavor}: {self.status}'

    def __repr__(self):
        return f'{self.flavor}: {self.status}'

    def freeze(self):
        start = time.time()
        print(f'In Freezer: {InFreezer.batchs.values()}')
        print(f'Out of Freezer: {OutOfFreezer.batchs.values()}')
        print(self)
        while True:
            end = time.time()
            time_elapsed = end - start
            if time_elapsed == 5:
                self.status = 'almost ready'
                print(self)
            elif time_elapsed == 10:
                self.status = 'ready'
                print(self)
                InFreezer.batchs.pop(self.flavor)
                OutOfFreezer.batchs[self.flavor] = self
                break
            elif time_elapsed == 15:
                self.status = 'freezer burned'
                print(self)
                break


class InFreezer:
    batchs = dict()

    def __str__(self):
        return f'In Freezer: {self.batchs.values()}'

    def new_batch(self, flavor):
        self.batchs[flavor] = IceCream(flavor)
        self.batchs[flavor].freeze()


class OutOfFreezer:
    batchs = dict()

    def __str__(self):
        return f'Out of Freezer: {self.batchs.values()}'

    def take_out(self, ice_cream):
        self.batchs[ice_cream.flavor] = ice_cream


freezer = InFreezer()
out_of_freezer = OutOfFreezer()
freezer.new_batch('vanilla')
print(freezer)
print(out_of_freezer)
