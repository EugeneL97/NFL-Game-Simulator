# Sports Simulation Project

## Overview

This project simulates an NFL season game outcome based on previous scoring for the season. It includes modules for data handling, ratings computation, and match simulation.

## Project Structure

The project is organized into several modules:

- **data_handling.py**: Contains functions to read and transform the input data.
- **ratings.py**: Defines the Ratings class to compute team ratings based on historical performance.
- **match.py**: Implements the Match and AbstractMatch classes for generating simulated game scores.
- **simulation.py**: Includes the Simulator class for running simulations and obtaining win probabilities.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/sports-simulation-project.git
   ```

2. Install the required dependencies:

   ```bash
   pip install pandas matplotlib numpy scipy
   ```

3. Run the main script:

   ```bash
   python main.py
   ```

## Usage

1. **Update Data:**
   Update the `sportsref_download.csv` file with the current season scores. Follow these steps:

   - Go to [Pro Football Reference - 2023 Season Games](https://www.pro-football-reference.com/years/2023/games.htm).
   - Scroll down to "Week-by-Week Games."
   - To the right of this section, find "Share and Export."
   - Click the dropdown and select "Get Table as CSV (for Excel)."
   - Copy and paste that data and overwrite the `sportsref_download.csv` with the updated data.

2. **Run Simulation:**
   The `main.py` script demonstrates how to use the various modules to simulate game outcomes and print win probabilities for specified matchups. After updating the data, run the script using the following command:

   ```bash
   python main.py
   ```

   This will execute the simulation and display the win probabilities for the specified matchups in the console. Feel free to customize the project according to your specific sports data and simulation requirements.

```python

# Import modules
from data_handling import read_data, transform_data
from ratings import Ratings
from match import Match
from simulation import Simulator

# Load data
df = read_data('sportsref_download.csv')
regular_season = transform_data(df)

# Create objects
ratings = Ratings(regular_season)
match = Match(ratings)
simulator = Simulator(match, simulations=10000)

# Example usage
schedule = [
    ('Team1', 'Team2'),
    ('Team1', 'Team3')
]

print('-' * 100)
for team1, team2 in schedule:
    observations = simulator.simulate(team1, team2)

    t1 = round(observations['t1'] * 100, 2)
    t2 = round(observations['t2'] * 100, 2)

    print(f'{team1}: {t1}%')
    print(f'{team2}: {t2}%')
    print('-' * 100)
```

Feel free to tweak around the values or change up the algorithm!
