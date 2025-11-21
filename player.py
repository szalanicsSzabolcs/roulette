class Player:

    def __init__ (self, playerName, roundsWon, lives, items):
        self.playerName = playerName
        self.roundsWon = roundsWon
        self.lives = lives
        self.items = items

    def firstStart(self):
        self.playerName = input("Your name is? : ")
        self.roundsWon = 0
        self.lives = 3
        self.items = []

