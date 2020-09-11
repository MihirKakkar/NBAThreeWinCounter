# importing libraries
import numpy
import pandas
from nba_api.stats.static import teams
from nba_api.statss.endpoints import teamyearbyyearstats

# checking favourite team
team_dict = teams.get_teams()
rockets = [team for team in team_dict if team['nickname'] == 'Rockets']
print(rockets)

#
team_threept_stats = teamyearbyyearstats.TeamYearByYearStats()