# importing libraries
import numpy as np
import pandas as pd
from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamyearbyyearstats

# checking favourite team
team_dict = teams.get_teams()
rockets = [team for team in team_dict if team['nickname'] == 'Rockets']
print(rockets)


# obtaining the three pointer stats
team_id_arr = ['1610612737', '1610612738', '1610612739', '1610612740', '1610612741', '1610612742', '1610612743', '1610612744', '1610612745', '1610612746', '1610612747', '1610612748', '1610612749', '1610612750', '1610612751', '1610612752', '1610612753', '1610612754', '1610612755', '1610612756', '1610612757', '1610612758', '1610612759', '1610612760', '1610612761', '1610612762', '1610612763', '1610612764', '1610612765', '1610612766']
singleteam_threept_stats = teamyearbyyearstats.TeamYearByYearStats(league_id='00', team_id='1610612765')

#team_threept_stats = []
#for i in range(len(team_id_arr)):
#    team_threept_stats.append(teamyearbyyearstats.TeamYearByYearStats(league_id='00', team_id=team_id_arr[i]))

#print(team_threept_stats)

team_threept_stats_df = singleteam_threept_stats.get_data_frames()[0]
    
percent_of_shots_from_three = team_threept_stats_df['FG3A']/team_threept_stats_df['FGA']
team_threept_stats_df.insert(34, "FG3A/FGA", percent_of_shots_from_three)
all_team_three_stats = team_threept_stats_df[['FG3A/FGA', 'FG3A', 'FGA']].copy()

# comparing to wins through plotting
correlation_with_wins = team_threept_stats_df.plot(x='FG3A/FGA', y='WIN_PCT', style='o')
