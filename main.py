from data_handling import read_data, transform_data
from ratings import Ratings
from match import Match
from simulation import Simulator


df = read_data('sportsref_download.csv')
regular_season = transform_data(df)
print(regular_season)


ratings = Ratings(regular_season)
print(ratings.df.head(32))

match = Match(ratings)
simulator = Simulator(match, simulations=10000)

schedule = [
    ('Philadelphia Eagles', 'Detroit Lions'),
    ('Kansas City Chiefs', 'Arizona Cardinals')
]

print('-' * 100)
for team1, team2 in schedule:
    observations = simulator.simulate(team1, team2)

    t1 = round(observations['t1'] * 100, 2)
    t2 = round(observations['t2'] * 100, 2)

    print(f'{team1}: {t1}%')
    print(f'{team2}: {t2}%')
    print('-' * 100)