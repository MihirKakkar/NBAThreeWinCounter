#Collecting all of the data required for analysis

from nba_api.stats.static import teams
team_dict = teams.get_teams()

rockets = [team for team in team_dict if team['nickname'] == 'Rockets']
# def getData():
print(rockets)
