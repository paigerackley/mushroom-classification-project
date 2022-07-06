import pandas as pd
import numpy as np



def get_mush_data():
    '''
    Returns CSV as Pandas Dataframe.
    '''
    url = 'https://github.com/paigerackley/mushroom-classification-project/blob/main/mushrooms.csv?raw=true'
    df = pd.read_csv(url, index_col=0)
    return df
