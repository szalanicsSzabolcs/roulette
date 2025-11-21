#a táska első elemét odaadjuk player1-nek a másodikat a dealernek majd töröljük őket listából
#az választ először aki nyert
#ha nem sül el a fegyver akkor az elszenvedő nyert, ha elsül akkor az elsütő
import bag
import time

def who_wonPlayer(whatIsInBag, whatBulletRoundContinue, player1, dealer1):
    player1Alive = True
    dealer1Alive = True

    # Játékos húz egy itemet
    if not whatIsInBag.items:
        print("The bag is empty!")
        return [player1Alive, dealer1Alive]

    item = whatIsInBag.items.pop(0)
    print(f"{player1.playerName} found {item}!")

    effectPlayer = whatIsInBag.whatThingsDoToPlayer([item], player1, dealer1, whatBulletRoundContinue)
    print(effectPlayer)
    time.sleep(0.8)

    if player1.lives < 1:
        player1Alive = False
        return [player1Alive, dealer1Alive]

    # Dealer húz egy itemet, ha van még
    if not whatIsInBag.items:
        print("The bag is empty after player's turn!")
        return [player1Alive, dealer1Alive]

    item = whatIsInBag.items.pop(0)
    print(f"{dealer1.dealerName} found {item}!")

    effectDealer = whatIsInBag.whatThingsDoToDealer([item], player1, dealer1, whatBulletRoundContinue)
    print(effectDealer)
    time.sleep(0.8)

    if dealer1.lives < 1:
        dealer1Alive = False

    return [player1Alive, dealer1Alive]

def who_wonDealer(whatIsInBag, whatBulletRoundContinue, player1, dealer1):
    
    player1Alive = True
    dealer1Alive = True

    if dealer1.lives < 1:
        dealer1Alive = False
        return player1Alive, dealer1Alive

    # DEALER választ
    if whatIsInBag.items:
        dealer_choice = whatIsInBag.items.pop(0)
        dealer1.items.append(dealer_choice)

        effectDealer = whatIsInBag.whatThingsDoToDealer(
            dealer_choice, player1, dealer1, whatBulletRoundContinue
        )
        print(f"\n{effectDealer}")
        dealer1.items.pop(0)

        if dealer1.lives < 1:
            dealer1Alive = False
            return player1Alive, dealer1Alive
    else:
        print("⚠️ Bag is empty! Dealer cannot choose.")
        return player1Alive, dealer1Alive

    time.sleep(1)

    # PLAYER választ (ha még él)
    if player1.lives > 0 and whatIsInBag.items:
        player_choice = whatIsInBag.items.pop(0)
        player1.items.append(player_choice)

        effectPlayer = whatIsInBag.whatThingsDoToPlayer(
            player_choice, player1, dealer1, whatBulletRoundContinue
        )
        print(f"{effectPlayer}")
        player1.items.pop(0)

        if player1.lives < 1:
            player1Alive = False
            return player1Alive, dealer1Alive
    elif player1.lives > 0:
        print("⚠️ Bag is empty! Player cannot choose.")

    return player1Alive, dealer1Alive