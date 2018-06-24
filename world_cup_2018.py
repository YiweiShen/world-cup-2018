import requests
import os
# import time
# from pprint import pprint


def cal_country_and_score(game):
    home_team_country = str(game['home_team_country'])
    home_team_goal = str(game['home_team']['goals'])
    away_team_country = str(game['away_team_country'])
    away_team_goal = str(game['away_team']['goals'])
    country_vs_info = str(home_team_country + ' Vs. ' + away_team_country)
    goal_vs_info = str(home_team_goal + '  :  ' + away_team_goal)
    return country_vs_info, goal_vs_info


def main():
    game_now = requests.get('https://worldcup.sfg.io/matches/current').json()
    # pprint(game_now)
    # if you want to see all the statistics, pprint it all
    try:
        country_vs_info, goal_vs_info = cal_country_and_score(game_now[0])
        game_time = str(game_now[0]['time'])
    except Exception as _:
        print('game ends')
        os.system("""
                  osascript -e 'display notification "{}" with title "{}"'
                  """.format('Game already ends', 'Sorry'))
        # time.sleep(5)
        # in case you have a fast internet connection,
        # you will miss the first notification, that's why sleep
        games = requests.get('https://worldcup.sfg.io/matches').json()
        os.system("""
                  osascript -e 'display notification "{}" with title "{}"'
                  """.format('Let me fetch the result for you', 'Oh wait'))
        last_game_index = 0
        for i, game in enumerate(games):
            if game['status'] == 'future':
                last_game_index = i - 1
                break
        country_vs_info, goal_vs_info = cal_country_and_score(games[last_game_index])
        os.system("""
                  osascript -e 'display notification "{}" with title "{}"'
                  """.format(goal_vs_info, country_vs_info))
    else:
        print('time: ' + game_time)
        print(country_vs_info)
        # print(' ' * (len(home_team_country) - 1), end='')
        print(goal_vs_info)
    # test mac notification
        os.system("""
                  osascript -e 'display notification "{}" with title "{}"'
                  """.format(goal_vs_info, country_vs_info))


if __name__ == '__main__':
    main()
