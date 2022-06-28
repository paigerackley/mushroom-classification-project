import pandas as pd
import numpy as np
import os

from env import host, user, password


def get_mush_data():
    '''
    This function reads in iris data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('mushrooms.csv'):
        
        # If csv file exists read in data from csv file
        df = pd.read_csv('mushrooms.csv', index_col=0)

    return df 