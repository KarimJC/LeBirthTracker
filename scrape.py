from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import League
from basketball_reference_web_scraper.data import OutputType
from basketball_reference_web_scraper.data import Team
from datetime import datetime, timedelta, date

# year = input("year: ")
# month = input("month: ")
# day = input("day: ")



def player_points_year_to_date(player):
    null

# gets the number of points a given player has scored on a given date
def player_day_points(player, date):
    list = client.player_box_scores(day=date.day, month=date.month, year=date.year)

    # TODO: rework the loop so that the loop ends when the player's name is found
    for i in list:
        if player == i['name']:
            return convert_to_points(i["made_field_goals"], 
                                    i["made_three_point_field_goals"], 
                                    i["made_free_throws"])
    # index = list.index("LeBron James")
    # return convert_to_points(list[index]["made_field_goals"], 
    #                 list[index]["made_three_point_field_goals"], 
    #                 list[index]["made_free_throws"])

# gets the total amount of points a player hsa scored between two dates (inclusive)
# takes in a player (string), a start date and an end date
def player_points_between_dates(player, start_date, end_date):
    current_date = start_date
    total_points = 0
    while current_date <= end_date:
        day_points = player_day_points(player=player, date=current_date)
        if day_points is not None:
            total_points += day_points
        current_date += timedelta(days=1)
    
    return total_points

# converts the stats of a player in a game into points
def convert_to_points(field_goals, threes, ft):
    return ((field_goals-threes) * 2) + (threes * 3) + ft

# returns the number of points a player (string) scored in a year (int)
def full_season_points(player, year):
    list = client.players_season_totals(season_end_year=2018)
    for i in list:
        if i['name'] == player:
            return i['points']
        

#print(client.search(term="Le"))
#print(client.player_box_scores(day=22, month=4, year=2025))
print(player_points_between_dates("LeBron James", date(2025, 4, 22), date(2025, 4, 27)))

# for i in list:
#     if i['name'] == "LeBron James":
#         print(i)

# print(list[0]['name'])
# def getPlayerStats(String player): 
#     for i in client.player_box_scores(day=1, month=1, year=2017):
#          if i['name'] == player:
              