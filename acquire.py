import pandas as pd
import numpy as np
import os



def get_mush_data():
    '''
    Returns CSV as Pandas Dataframe.
    '''
    filename = 'mushrooms.csv'

    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    return df
