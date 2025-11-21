import random

class Weapon:
    def __init__(self):
        self.magazineSize = []

    def loadRandomBulletsRound1(self):
        bulletsNumber = 8

        # 1 élő töltény + 7 üres
        self.magazineSize = ["liveBullet"] + ["fakeBullet"] * (bulletsNumber - 1)
            
        # Véletlenszerű sorrend
        random.shuffle(self.magazineSize)
        
        return self.magazineSize
        
    def loadRandomBulletsRoundContinue(self):

        # 4 élő töltény + 4 üres
        self.magazineSize = ["liveBullet"]*4 + ["fakeBullet"]*4

        # Véletlenszerű sorrend, ameddig a játékosok élete > 0
        random.shuffle(self.magazineSize)

        return self.magazineSize
    
   
    


