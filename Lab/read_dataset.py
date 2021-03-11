import pandas as pd


def get_happieness_dataset():
    df = pd.read_csv(r'2019.csv')
    return df.drop('happieness', axis=1), df['happieness']
