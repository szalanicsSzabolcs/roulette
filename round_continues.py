import time
from dealer import Dealer
import data_sheare



def round_continue_data():

    result = data_sheare.round_result

    dealer1 = result[2]
    player1 = result[3]
    
    return dealer1, player1




def round_continue():

#első kör
    print("*                                  Next Round                                  *")

    dealer1, player1 = round_continue_data()
        
#függvény import "betöltődik a fegyver"
    print("*                          Reloading the gun randomly                          *")
    time.sleep(3)
       
#változóba mentjük a függvény return-jét aztán vizsgáljuk
    print("*                                Gun is spinning                               *")
    time.sleep(2)

#fegyverpörgetés
    spinTheGunResultRound1 = Dealer.spinTheGun(dealer1)
    whatBulletRoundContinue = data_sheare.whatBulletRoundContinue


    playerWon = False
    dealerWon = False

    if spinTheGunResultRound1 == "Player shoot" and whatBulletRoundContinue.magazineSize[0] == "liveBullet":
            dealer1.lives -= 1
            time.sleep(1)
            print(f"Buuuummm! {dealer1.dealerName}'s remaining lives:{dealer1.lives}")
            playerWon = True
            player1.roundsWon += 1
        
    elif spinTheGunResultRound1 == "Player shoot" and whatBulletRoundContinue.magazineSize[0] == "fakeBullet":
            time.sleep(1)
            print(f"{dealer1.dealerName} you are lucky...it's a fake bullet now...")
            playerWon = False
        
    elif spinTheGunResultRound1 == "Dealer shoot"and whatBulletRoundContinue.magazineSize[0] == "liveBullet":
            player1.lives -= 1
            time.sleep(1)
            print(f"Buuuummm! {player1.playerName}'s remaining lives':{player1.lives}")
            dealerWon = True
            dealer1.roundsWon += 1        

    elif spinTheGunResultRound1 == "Dealer shoot" and whatBulletRoundContinue.magazineSize[0] == "fakeBullet":
            time.sleep(1)
            print(f"{player1.playerName} you are lucky...it's a fake bullet now...")
            dealerWon = False
        
    else:
             print("result = Dealer.spinTheGun()_hiba_main.py")
    
    return playerWon, dealerWon, dealer1, player1, whatBulletRoundContinue