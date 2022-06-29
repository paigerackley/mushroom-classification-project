import pandas as pd
import numpy as np


def get_mush_data():
    '''
    Returns CSV as Pandas Dataframe.
    '''
    file = '/Users/cheese_enchilada/Desktop/Mushroom/mushrooms.csv'
    df = pd.read_csv(file)
    return df