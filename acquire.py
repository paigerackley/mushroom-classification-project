import pandas as pd
import numpy as np


def get_mush_data():
    '''
    This function reads mushroom csv file and imports it in.
    '''
        
        # If csv file exists read in data from csv file
    df = pd.read_csv('mushrooms.csv', index_col=0)

    return df 