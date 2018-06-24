import requests
import os
# from pprint import pprint

game_now = requests.get('https://worldcup.sfg.io/matches/current').json()

# pprint(game_now)
# if you want to see all the statistics, pprint it all

try:
    home_team_country = str(game_now[0]['home_team_country'])
    home_team_goal = str(game_now[0]['home_team']['goals'])

    away_team_country = str(game_now[0]['away_team_country'])
    away_team_goal = str(game_now[0]['away_team']['goals'])

    game_time = str(game_now[0]['time'])
except Exception as _:
    print('game ends')
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format('game ends', 'oh'))
else:
    print('time: ' + game_time)
    country_vs_info = str(home_team_country + ' Vs. ' + away_team_country)
    print(country_vs_info)
    print(' ' * (len(home_team_country) - 1), end='')
    goal_vs_info = str(home_team_goal + '  :  ' + away_team_goal)
    print(goal_vs_info)


# test mac notification
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(goal_vs_info, country_vs_info))
