from weaponClass import Weapon
from dealer import Dealer
from player import Player
import time

def round_1_result_handling():


#player és dealer egyed létrehozása, üres string mert a program majd feltölti
    player1 = Player("","","","")
    player1.firstStart()

    dealer1 = Dealer("","","","")
    dealer1.firstStart()

#első kör
    print("*                                 First Round                                  *")
        
#függvény import "betöltődik a fegyver"
    print("*                          Reloading the gun randomly                          *")
    time.sleep(3)
       
#változóba mentjük a függvény return-jét aztán vizsgáljuk
    print("*                                Gun is spinning                               *")
    time.sleep(2)

#random bullet betöltése
    whatBulletRound1 = Weapon()
    whatBulletRound1.loadRandomBulletsRound1()

#fegyverpörgetés
    spinTheGunResultRound1 = Dealer.spinTheGun(dealer1)


    playerWon = False
    dealerWon = False

    if spinTheGunResultRound1 == "Player shoot" and whatBulletRound1.magazineSize[0] == "liveBullet":
            dealer1.lives -= 1
            time.sleep(1)
            print(f"Buuuummm! {dealer1.dealerName}'s remaining lives:{dealer1.lives}")
            playerWon = True
            dealerWon = False
            player1.roundsWon += 1
            return playerWon, dealerWon, dealer1, player1, whatBulletRound1
        
    elif spinTheGunResultRound1 == "Player shoot" and whatBulletRound1.magazineSize[0] == "fakeBullet":
            time.sleep(1)
            print(f"{dealer1.dealerName} you are lucky...it's a fake bullet now...")
            playerWon = False
            dealerWon = True
            return playerWon, dealerWon, dealer1, player1, whatBulletRound1
        
    elif spinTheGunResultRound1 == "Dealer shoot"and whatBulletRound1.magazineSize[0] == "liveBullet":
            player1.lives -= 1
            time.sleep(1)
            print(f"Buuuummm! {player1.playerName}'s remaining lives':{player1.lives}")
            dealerWon = True
            playerWon = False
            dealer1.roundsWon += 1   
            return playerWon, dealerWon, dealer1, player1, whatBulletRound1     

    elif spinTheGunResultRound1 == "Dealer shoot" and whatBulletRound1.magazineSize[0] == "fakeBullet":
            time.sleep(1)
            print(f"{player1.playerName} you are lucky...it's a fake bullet now...")
            dealerWon = False
            playerWon = True
            return playerWon, dealerWon, dealer1, player1, whatBulletRound1
        
    else:
             print("result = Dealer.spinTheGun()_hiba_main.py")
    
    return playerWon, dealerWon, dealer1, player1, whatBulletRound1