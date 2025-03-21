from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import League
from basketball_reference_web_scraper.data import OutputType

birthday = input("Whats your birthday: ")
print(birthday + ", thats a shitty ass day to be born")
list = client.player_box_scores(day=1, month=1, year=2017)
# print(list[0]['name'])
# def getPlayerStats(String player): 
#     for i in client.player_box_scores(day=1, month=1, year=2017):
#          if i['name'] == player:
              