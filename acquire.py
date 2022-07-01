import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split


def get_mush_data():
    '''
    Returns CSV as Pandas Dataframe.
    '''
    file = '/Users/cheese_enchilada/Desktop/Mushroom/mushrooms.csv'
    df = pd.read_csv(file)
    return df


