class Ratings:
  def __init__(self, regular_season):
    self._ratings = regular_season.groupby('team').mean()[['pf', 'pa']]
    self._avg_points = regular_season['pf'].mean()
    self._std_points = regular_season['pf'].std()

  @property
  def df(self):
    return self._ratings

  @property
  def std_points(self):
    return self._std_points

  def get_team_data(self, team):
    return self._ratings.loc[team][['pf', 'pa']]

