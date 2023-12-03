import pandas as pd

def read_data(file_path):
    return pd.read_csv(file_path)

def transform_data(df):
    regular_season = pd.concat(
        [
            df[['Week', 'Winner/tie', 'PtsW', 'PtsL']].rename(columns={
                'Week': 'week',
                'Winner/tie': 'team',
                'PtsW': 'pf',
                'PtsL': 'pa',
            }),
            df[['Week', 'Loser/tie', 'PtsW', 'PtsL']].rename(columns={
                'Week': 'week',
                'Loser/tie': 'team',
                'PtsW': 'pf',
                'PtsL': 'pa',
            }),
        ]
    ).sort_values(['week'])
    return regular_season
