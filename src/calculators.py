def calculate_mvp(player, round):
    if round[player]["deaths"]:
        death = 1
    else:
        death = 0
    result = round[player]["kills"]*3 + round[player]["assists"] - death
    return result

def calculate_totals(round_data, lista, player_totals):
    for player, stats in round_data.items():
        if player not in player_totals:
            player_totals[player] = {"kills": 0, "assists": 0, "deaths": 0, "MVPs": 0, "score": 0}
        player_totals[player]["kills"] += stats["kills"]
        player_totals[player]["assists"] += stats["assists"]
        player_totals[player]["deaths"] += int(stats["deaths"])
        player_totals[player]["MVPs"] += lista.count(player)
        player_totals[player]["score"] = player_totals[player]["kills"] * 3 + player_totals[player]["assists"] - player_totals[player]["deaths"]
    return player_totals
