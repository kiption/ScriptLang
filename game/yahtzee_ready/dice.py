import random

class Dice:
    def rollDie(self):
        self.roll = random.randint(1, 6)

    def getRoll(self):
        return self.roll
