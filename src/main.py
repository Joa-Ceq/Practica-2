from process import main, sort_players

rounds = [
{
"Shadow": {"kills": 2, "assists": 1, "deaths": True},
"Blaze": {"kills": 1, "assists": 0, "deaths": False},
"Viper": {"kills": 1, "assists": 2, "deaths": True},
"Frost": {"kills": 0, "assists": 1, "deaths": False},
"Reaper": {"kills": 1, "assists": 1, "deaths": False}
},

{
"Shadow": {"kills": 0, "assists": 2, "deaths": False},
"Blaze": {"kills": 2, "assists": 0, "deaths": True},
"Viper": {"kills": 1, "assists": 1, "deaths": False},
"Frost": {"kills": 2, "assists": 1, "deaths": True},
"Reaper": {"kills": 0, "assists": 1, "deaths": False}
},

{
"Shadow": {"kills": 1, "assists": 0, "deaths": False},
"Blaze": {"kills": 2, "assists": 2, "deaths": True},
"Viper": {"kills": 1, "assists": 1, "deaths": True},
"Frost": {"kills": 0, "assists": 1, "deaths": False},
"Reaper": {"kills": 1, "assists": 1, "deaths": False}
},

{
"Shadow": {"kills": 2, "assists": 1, "deaths": False},
"Blaze": {"kills": 1, "assists": 0, "deaths": True},
"Viper": {"kills": 0, "assists": 2, "deaths": False},
"Frost": {"kills": 1, "assists": 1, "deaths": True},
"Reaper": {"kills": 1, "assists": 1, "deaths": False}
},

{
"Shadow": {"kills": 1, "assists": 2, "deaths": True},
"Blaze": {"kills": 0, "assists": 1, "deaths": False},
"Viper": {"kills": 2, "assists": 0, "deaths": True},
"Frost": {"kills": 1, "assists": 1, "deaths": False},
"Reaper": {"kills": 1, "assists": 1, "deaths": True}
}
]

player_totals = {}

for round_data in rounds:
    player_totals = main(round_data, player_totals)

sort_players(player_totals)