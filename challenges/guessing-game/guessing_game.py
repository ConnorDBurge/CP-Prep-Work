import random


class GuessingGame():
    last_guess = None

    def __init__(self, num):
        self.number_to_guess = random.randint(1, num)
        self.solve = False

    def guess(self, user_guess):
        if int(user_guess) < self.number_to_guess:
            return 'low'
        elif int(user_guess) > self.number_to_guess:
            return 'high'
        else:
            self.solve = True
            return 'right'

    def solved(self):
        return self.solve  # cant be same name as method
