import pandas as pd
import numpy as np


def get_mush_data():
    '''
    # Read csv file into pandas DataFrame. 
    '''
file = “/Users/cheese_enchilada/Desktop/Mushroom/mushrooms.csv"
df = pd.read_csv(file)