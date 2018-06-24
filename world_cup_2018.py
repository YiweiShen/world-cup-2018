import requests
# from pprint import pprint

game_now = requests.get('https://worldcup.sfg.io/matches/current').json()

# pprint(game_now)
# if you want to see all the statistics, pprint it all

home_team_country = str(game_now[0]['home_team_country'])
home_team_goal = str(game_now[0]['home_team']['goals'])

away_team_country = str(game_now[0]['away_team_country'])
away_team_goal = str(game_now[0]['away_team']['goals'])

game_time = str(game_now[0]['time'])

print('time: ' + game_time)
print(home_team_country + ' Vs. ' + away_team_country)
print(' ' * (len(home_team_country) - 1), end='')
print(home_team_goal + '  :  ' + away_team_goal)
