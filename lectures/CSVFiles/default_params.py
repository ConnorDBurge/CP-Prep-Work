def nfl_team(name, location, wins=0, losses=0):
    print(f'The {name} have {wins} wins and {losses} losses this seasone')


nfl_team('Falcons', 'Atlanta')  # defaults to 0W and 0L
nfl_team('Falcons', 'Atlanta', losses=16)  # defaults to 0W


class NFLTeam:

    def __init__(self, name, location, wins=0, losses=0):
        self.name = name
        self.location = location
        self.wins = wins
        self.losses = losses

    def __str__(self):
        return f'The {self.name} have {self.wins} wins and {self.losses} losses this seasone'


# defaults to 0W and 0L# defaults to 0W
team = NFLTeam('Falcons', 'Atlanta', losses=4)
print(team)
