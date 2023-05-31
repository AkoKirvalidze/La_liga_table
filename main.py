from bs4 import BeautifulSoup
import requests
from TeamSeason import Team
from TeamDatabase import TeamData

response = requests.get('https://www.laliga.com/en-GE/laliga-santander/standing')
soup = BeautifulSoup(response.text, 'html.parser')

la_liga = soup.find_all(class_="styled__StandingTabBody-e89col-0 fVocLp")

database = TeamData("la_liga_data")


def add_laliga():
    a = 0
    for i in la_liga:
        if a == 20:
            break
        name = i.find(class_="styled__ShieldContainer-lo8ov8-0 bkblFd shield-desktop").find(
            class_="styled__TextRegularStyled-sc-1raci4c-0 glrfl").string
        box = []
        for g in i:
            box.append(g.string)
        points = int(box[2])
        matches = int(box[3])
        wins = int(box[4])
        draws = int(box[5])
        loses = int(box[6])
        GD = box[9]
        team_season = Team(name, points, matches, wins, loses, draws, GD)
        database.add_team(team_season)
        a += 1


print("""           Welcome to the La Liga table
 To see what you are interested in follow instructions

 Press 1 to create database
 press 2 to see the table
 Press 3 to see who qualified to Champions League
 Press 4 to see who qualified to Europa League
 Press 5 to see who qualified to Conference League
 Press 6 to see who got relegated
 Press 7 to see certain amount of teams
 press 8 to see certain teams stats
 Press 0 to end 
""")

user = ''
while user != '0':
    print()
    user = input("Choose number - ")
    print()
    if user == '1':
        add_laliga()
    elif user == '2':
        database.table()
        print()
    elif user == '3':
        database.UCL_qualification()
        print()
    elif user == '4':
        database.EU_qualification()
        print()
    elif user == '5':
        database.CF_qualification()
        print()
    elif user == '6':
        database.relegated()
        print()
    elif user == '7':
        num = int(input("How many teams? - "))
        database.get_amount(num)
        print()
    elif user == '8':
        name = input("Team name? - ")
        database.stats(name)
        print()


