from apple import Apple
import random


class AppleTree:
    def __init__(self):
        self.age = 0
        self.height = 0
        self.apples = []

    def age_tree(self):
        self.age += 1
        self.height += 1.5 if self.height < 20 else 0
        if self.age >= 4:
            for _ in range(0, random.randint(50, 200)):
                self.apples.append(Apple())

    def is_dead(self) -> bool:
        return True if self.age >= 100 else False

    def any_apples(self) -> bool:
        return True if len(self.apples) > 0 else False

    def pick_an_apple(self) -> Apple:
        if len(self.apples) == 0:
            raise Exception('No apples on your tree')
        else:
            return self.apples.pop()

    def avg_diameter(self, basket):
        sum = 0
        for apple in basket:
            sum += apple.diameter
        return sum / len(basket)
