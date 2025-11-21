import random
from player import Player
from dealer import Dealer
from weaponClass import Weapon

class Bag:
    def __init__(self):
        self.items = []

    def randomizeBag(self):
        pool = [
            "smoke", "beer", "beer", "handcuffs", "handcuffs", "handcuffs", "handcuffs",
            "magnifier", "magnifier", "magnifier", "magnifier", "handcuffs",
            "mouseTrap", "mouseTrap", "mouseTrap", "mouseTrap", "mouseTrap", "mouseTrap", "magnifier"
        ]
        self.items = random.sample(pool, k=min(20, len(pool)))
        return self.items

    def __str__(self):
        return f"{self.items}"

    # ---------- PLAYER ----------
    def whatThingsDoToPlayer(self, item: list, player: Player, dealer: Dealer, weapon: Weapon):
        name = item

        if name == "smoke":
            if player.lives >= 3:
                return f"{player.playerName} already has maximum lives ({player.lives})."
            else:
                player.lives += 1
                return f"{player.playerName} finds smoke and gains 1 life! Lives: {player.lives}"

        elif name == "mouseTrap":
            if player.lives > 1:
                player.lives -= 1
                return f"{player.playerName} triggered a mousetrap and lost 1 life! Lives: {player.lives}"
            else:
                player.lives = 0
                return f"{player.playerName} stepped on a mousetrap... YOU ARE DEAD."

        elif name == "handcuffs":
            if weapon.magazineSize and weapon.magazineSize[0] == "liveBullet":
                dealer.lives -= 1
                weapon.magazineSize.pop(0)
                return f"{player.playerName} used handcuffs! {dealer.dealerName} loses 1 life. Dealer lives: {dealer.lives}"
            elif weapon.magazineSize:
                weapon.magazineSize.pop(0)
                return f"{player.playerName} found handcuffs, but it was a fake bullet. Nothing happened."
            else:
                return f"{player.playerName} found handcuffs, but the weapon is empty."

        elif name == "beer":
            if weapon.magazineSize:
                removed = weapon.magazineSize.pop(0)
                return f"{player.playerName} drank a beer and removed the next bullet ({removed})."
            else:
                return f"{player.playerName} drank a beer, but the weapon was already empty."

        elif name == "magnifier":
            if weapon.magazineSize:
                return f"{player.playerName} looks with magnifier: next bullet is a {weapon.magazineSize[0]}."
            else:
                return f"{player.playerName} looks with magnifier, but there are no bullets left."

        else:
            return f"{player.playerName} found {name}, but nothing happened."

    # ---------- DEALER ----------
    def whatThingsDoToDealer(self, item: list, player: Player, dealer: Dealer, weapon: Weapon):
        name = item

        if name == "smoke":
            if dealer.lives >= 3:
                return f"{dealer.dealerName} already has maximum lives ({dealer.lives})."
            else:
                dealer.lives += 1
                return f"{dealer.dealerName} finds smoke and gains 1 life! Lives: {dealer.lives}"

        elif name == "mouseTrap":
            if dealer.lives > 1:
                dealer.lives -= 1
                return f"{dealer.dealerName} triggered a mousetrap and lost 1 life! Lives: {dealer.lives}"
            else:
                dealer.lives = 0
                return f"{dealer.dealerName} stepped on a mousetrap... YOU ARE DEAD."

        elif name == "handcuffs":
            if weapon.magazineSize and weapon.magazineSize[0] == "liveBullet":
                player.lives -= 1
                weapon.magazineSize.pop(0)
                return f"{dealer.dealerName} used handcuffs! {player.playerName} loses 1 life. Player lives: {player.lives}"
            elif weapon.magazineSize:
                weapon.magazineSize.pop(0)
                return f"{dealer.dealerName} found handcuffs, but it was a fake bullet. Nothing happened."
            else:
                return f"{dealer.dealerName} found handcuffs, but the weapon is empty."

        elif name == "beer":
            if weapon.magazineSize:
                removed = weapon.magazineSize.pop(0)
                return f"{dealer.dealerName} drank a beer and removed the next bullet ({removed})."
            else:
                return f"{dealer.dealerName} drank a beer, but the weapon was already empty."

        elif name == "magnifier":
            if weapon.magazineSize:
                return f"{dealer.dealerName} looks with magnifier: next bullet is a {weapon.magazineSize[0]}."
            else:
                return f"{dealer.dealerName} looks with magnifier, but there are no bullets left."

        else:
            return f"{dealer.dealerName} found {name}, but nothing happened."
    