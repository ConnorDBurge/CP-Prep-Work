import csv


class NFLTeam:

    @classmethod  # create teams from original file
    def load_all_teams(cls, file='data/nfl.csv'):
        nfl_teams = list()  # list to hold all NFLTeam objects
        with open(file) as nfl_file:  # open file
            dict_teams = csv.DictReader(nfl_file)
            for team in dict_teams:
                # creating an object for each team
                new_team = cls(**team)  # uses kwargs
                nfl_teams.append(new_team)  # append new object
        return nfl_teams  # return a list of team objects

    @classmethod
    def write_teams_to_file(cls, teams_list):
        # appending to csv files
        with open('data/nfl.csv', mode='w') as nfl_file:
            nfl_writer = csv.DictWriter(
                nfl_file, ['id', 'team', 'wins', 'losses'])
            nfl_writer.writeheader()
            for team in teams_list:
                nfl_writer.writerow(team.__dict__)

    def __init__(self, id, team, wins, losses):
        self.id = id
        self.team = team
        self.wins = wins
        self.losses = losses

    def __str__(self):
        return f'The {self.team} have {self.wins} wins and {self.losses} losses this season'
