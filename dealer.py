import random
class Dealer:

    def __init__ (self, dealerName, roundsWon, lives, items):
        self.dealerName = dealerName
        self.roundsWon = roundsWon
        self.lives = lives
        self.items = items

    def firstStart(self):
        self.dealerName = "John"
        self.roundsWon = 0
        self.lives = 3
        self.items = []
        
    def spinTheGun(self):
        roll = random.randint(1, 12)

        if roll in (9, 10, 11, 12, 1, 2):
            return "Dealer shoot"
        elif roll in (3, 4, 5, 6, 7, 8, 9):
            return "Player shoot"
        else:
            return "spinTheGun_error"
