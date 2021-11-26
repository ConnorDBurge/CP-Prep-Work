# reading lines without csv with a for loop
from nfl_team import NFLTeam  # used on line 31
import csv

# nfl_file = open('data/nfl.csv')  # open file
# for line in nfl_file.readlines():
#     line_data = line.split(',')  # split line into list
#     print(line_data)
# nfl_file.close()  # always close

# # reading lines with csv module
# nfl_file = open('data/nfl.csv')  # open file
# reader = csv.reader(nfl_file)  # create a reader object
# for line in reader:
#     print(line)  # auto splits into list
# nfl_file.close()  # always close

# # preferred method to read csv files, no manual close
# with open('data/nfl.csv') as nfl_file:  # deault is to read the file
#     reader = csv.reader(nfl_file)  # create a reader object
#     for line in reader:
#         print(line)  # auto splits into list

# # creates a dict containing headers as keys and values as values
# with open('data/nfl.csv') as nfl_file:
#     # create a reader object# create a reader object
#     dict_reader = csv.DictReader(nfl_file)
#     for line in dict_reader:
#         print(line)  # auto splits into list

# used class method to create nfl_teams for abstraction
team_data = NFLTeam.load_all_teams()  # reads file
team_data.append(NFLTeam(4, 'Giants', 6, 10))
team_data.append(NFLTeam(5, 'Lions', 8, 8))
NFLTeam.write_teams_to_file(team_data)

for team in team_data:  # prints dicts made from data.csv
    print(team)
