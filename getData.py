# importing libraries
import numpy
import pandas
from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamyearbyyearstats

# checking favourite team
team_dict = teams.get_teams()
rockets = [team for team in team_dict if team['nickname'] == 'Rockets']
print(rockets)

# obtaining the three stats
team_threept_stats = teamyearbyyearstats.TeamYearByYearStats(league_id='00', team_id='1610612745')
team_threept_stats_df = team_threept_stats.get_data_frames()[0]
percent_of_shots_from_three = team_threept_stats_df['FG3A']/team_threept_stats_df['FGA']
team_threept_stats_df.insert(34, "FG3A/FGA", percent_of_shots_from_three)

# comparing to wins
correlation_with_wins = team_threept_stats_df.plot(x='FG3A/FGA', y='WIN_PCT', style='o')
