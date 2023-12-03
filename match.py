from abc import ABC, abstractmethod
import random
from scipy.stats import norm

class AbstractMatch(ABC):
    @abstractmethod
    def generate_score(self, t1: str, t2: str):
      pass

class Match(AbstractMatch):
    def __init__(self, ratings):
      self._ratings = ratings

    def compute_expected_points(self, t1, t2):
      def compute_expected_points(off, opposing_def):
        return (off * opposing_def) / self._ratings._avg_points

      t1_pf, t1_pa = self._ratings.get_team_data(t1)
      t2_pf, t2_pa = self._ratings.get_team_data(t2)

      team1_mu = compute_expected_points(t1_pf, t2_pa)
      team2_mu = compute_expected_points(t2_pf, t1_pa)

      return team1_mu, team2_mu
    
    def generate_score(self, t1, t2):
      team1_mu, team2_mu = self.compute_expected_points(t1, t2)
      return (
          round(norm.ppf(random.random(), team1_mu, self._ratings.std_points), 2),
          round(norm.ppf(random.random(), team2_mu, self._ratings.std_points), 2),
      )

