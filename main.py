from bag import Bag
import time
from dealer import Dealer
import greatings
import round1
from round_continues import round_continue
from who_won import who_wonPlayer
from who_won import who_wonDealer
import data_sheare
from weaponClass import Weapon
import save_round_results
import json


while True:
    
#greatings függvény meghívása (későbbi game start)
    # greatings.greatings()

#egy plusz kérdés (későbbi menü)
    start = str(input("Are you ready to test your luck? [y/n] ")).lower()

#if függvény + input vizsgálat
    if start == "y":

#if feltételek vizsgálata és a következmény kezelése
# konzolon megjelenő események
#palyer/dealer létrehozása mind a függvényben és kimentés egy közös mappába ahonnan mindenhogy elérhető
        round1_result = round1.round_1_result_handling()
        
        data_sheare.round_result = round1_result

#visszatérő érték lekezelése a folytatáshoz       
        when_playerWon = data_sheare.round_result[0]
        when_dealerWon = data_sheare.round_result[1]
        dealer1 = data_sheare.round_result[2]
        player1 = data_sheare.round_result[3]
        whatBulletRound1 = data_sheare.round_result[4]

        save_round_results.stats_save(player1, dealer1)

        print("*                                Searching the bag                             *")
        time.sleep(1)
        whatIsInTheBag = Bag()
        whatIsInTheBag.randomizeBag()
      
#ki vesz ki először a táskából?
        if when_playerWon and not when_dealerWon:
            player_alive, dealer_alive = who_wonPlayer(whatIsInTheBag, whatBulletRound1, player1, dealer1)
        elif when_dealerWon and not when_playerWon:
            player_alive, dealer_alive = who_wonDealer(whatIsInTheBag, whatBulletRound1, player1, dealer1)
        else:
            print("hiba_whoWon_main")

#random bullet betöltése
        whatBulletRoundContinue = Weapon()
        whatBulletRoundContinue.loadRandomBulletsRoundContinue()
        data_sheare.whatBulletRoundContinue = whatBulletRoundContinue      
        whatBulletRound_Continue = data_sheare.whatBulletRoundContinue
        
        while True:
            if player1.lives > 0 and dealer1.lives > 0:
                save_round_results.stats_save(player1, dealer1) 

                round_continue_result = round_continue()

                when_playerWon_continue = data_sheare.round_result[0]
                when_dealerWon_continue = data_sheare.round_result[1]
                dealer1_continue = data_sheare.round_result[2]
                player1_continue = data_sheare.round_result[3]
                whatBulletRound1_continue = data_sheare.round_result[4] 

                if when_playerWon and not when_dealerWon:
                    player_alive, dealer_alive = who_wonPlayer(whatIsInTheBag, whatBulletRound_Continue, player1, dealer1)
                elif when_dealerWon and not when_playerWon:
                    player_alive, dealer_alive = who_wonDealer(whatIsInTheBag, whatBulletRound_Continue, player1, dealer1)
            else:
                print("Game Over...")

                with open("stats.json", "r", encoding = "utf-8") as f:
                    stats = json.load(f)
                print(stats)

                break