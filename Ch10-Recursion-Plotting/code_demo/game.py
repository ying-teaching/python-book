import random


class Game:
    def __init__(self, low, high):
        random.seed(2022)
        self.the_number = random.randint(low, high)

    def check_number(self, guess):
        if guess == self.the_number:
            return 'Bingo'
        elif guess < self.the_number:
            return 'Low'
        else:
            return 'High'
