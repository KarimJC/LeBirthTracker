from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import League
from basketball_reference_web_scraper.data import OutputType
from basketball_reference_web_scraper.data import Team

# year = input("year: ")
# month = input("month: ")
# day = input("day: ")

def day_points(player, month, day, year):
    list = client.player_box_scores(day=day, month=month, year=year)
    for i in list:
        if player == i['name']:
            return convert_to_points(i["made_field_goals"], 
                                     i["made_three_point_field_goals"], 
                                     i["made_free_throws"])

def convert_to_points(field_goals, threes, ft):
    return ((field_goals-threes) * 2) + (threes * 3) + ft

# returns the number of points a player (string) scored in a year (int)
def full_season_points(player, year):
    list = client.players_season_totals(season_end_year=2018)
    for i in list:
        if i['name'] == player:
            return i['points']
        
print(client.season_schedule(season_end_year=2018))
print(day_points("LeBron James", 3, 8, 2025))

# for i in list:
#     if i['name'] == "LeBron James":
#         print(i)

# print(list[0]['name'])
# def getPlayerStats(String player): 
#     for i in client.player_box_scores(day=1, month=1, year=2017):
#          if i['name'] == player:
              