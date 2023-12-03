class Simulator:
    def __init__(self, match, simulations = 10000):
      self._match = match
      self._simulations = simulations

    def simulate(self, t1, t2):
      scores = [
          self._match.generate_score(t1, t2)
          for _ in range(self._simulations)
      ]

      t1_wins = sum(t1_score > t2_score for t1_score, t2_score in scores)
      t1_win_percentage = t1_wins / self._simulations

      return {
          't1' : t1_win_percentage,
          't2' : 1 - t1_win_percentage
      }

