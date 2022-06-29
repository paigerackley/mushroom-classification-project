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

def split_mush_data(df):
    '''
    This function performs split on mushroom data, stratify class.
    Returns train, validate, and test dfs. It is an all-in-all function.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        )
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                            )
    return train, validate, test


def prepare_mush(df):
    '''
    Returns cleaned and edited df
    '''
    # need to rename alot of these,unusable in coding
    df.rename(columns = {'class':'mclass'}, inplace = True)
    df.rename(columns = {'cap-shape':'cap_shape'}, inplace = True)
    df.rename(columns = {'cap-surface':'cap_surface'}, inplace = True)
    df.rename(columns = {'cap-color':'cap_color'}, inplace = True)
    df.rename(columns = {'gill-attachment':'gill_attachment'}, inplace = True)
    df.rename(columns = {'gill-spacing':'gill_spacing'}, inplace = True)
    df.rename(columns = {'gill-size':'gill_size'}, inplace = True)
    df.rename(columns = {'gill-color':'gill_color'}, inplace = True)
    df.rename(columns = {'stalk-shape':'stalk_shape'}, inplace = True)
    df.rename(columns = {'stalk-root':'stalk_root'}, inplace = True)
    df.rename(columns = {'stalk-surface-above-ring':'stalk_surface_above_ring'}, inplace = True)
    df.rename(columns = {'stalk-surface-below-ring':'stalk_surface_below_ring'}, inplace = True)
    df.rename(columns = {'stalk-color-above-ring':'stalk_color_above_ring'}, inplace = True)
    df.rename(columns = {'stalk-color-below-ring':'stalk_color_below_ring'}, inplace = True)
    df.rename(columns = {'veil-type':'veil_type'}, inplace = True)
    df.rename(columns = {'veil-color':'veil_color'}, inplace = True)
    df.rename(columns = {'ring-number':'ring_number'}, inplace = True)
    df.rename(columns = {'ring-type':'ring_type'}, inplace = True)
    df.rename(columns = {'spore-print-color':'spore_print_color'}, inplace = True)

    # Split the data
    train, validate, test = split_mush_data(df)

    return train, validate, test