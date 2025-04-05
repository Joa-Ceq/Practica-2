from calculators import calculate_mvp, calculate_totals

def main(round_data, player_totals):
    lista = []
    max = float("-inf")
    # for item in round_data.items():
    #     print(item)
    for player in round_data:
        score = calculate_mvp(player, round_data)
        if score > max:
            max = score
            mvp = player
    lista.append(mvp)
    # print("MVP: " + mvp)
    # print()
    return calculate_totals(round_data, lista, player_totals)

def sort_players(player_totals):
    sorted_players = sorted(player_totals.items(), key=lambda item: item[1]['score'], reverse=True)

    for player, stats in sorted_players:
        print(f"{player}: {stats}")