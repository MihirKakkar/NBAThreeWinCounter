# importing libraries
import numpy
import pandas
from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamyearbyyearstats

# checking favourite team
team_dict = teams.get_teams()
rockets = [team for team in team_dict if team['nickname'] == 'Rockets']
print(rockets)

#
team_threept_stats = teamyearbyyearstats.TeamYearByYearStats(league_id='00', team_id='1610612745')
#, per_mode_simple='PerGame', season_type_all_star='regular', team_id='1610612745'
team_threept_stats_df = team_threept_stats.get_data_frames()
print(team_threept_stats_df)