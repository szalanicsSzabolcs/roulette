import json
import data_sheare

def stats_save(player1, dealer1):
    player_stats = {"player_name": player1.playerName, "player_rounds_won": player1.roundsWon }
    dealer_stats = {"dealer_name": dealer1.dealerName, "dealer_rounds_won": dealer1.roundsWon }

    with open("stats.json", "w", encoding="utf-8") as f:
        json.dump({"player": player_stats, "dealer": dealer_stats}, f, ensure_ascii=False, indent=4)

    return "Stats saved!"