import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


def hab_chart(train):

    hab_colors = train['habitat'].value_counts()
    h_height = hab_colors.values.tolist() #Provides numerical values
    hab_color_labels = hab_colors.axes[0].tolist() #Converts index object to list

    poisonous_cc = [] #Poisonous color cap list
    edible_cc = []    #Edible color cap list
    for hab in hab_color_labels:
        size = len(train[train['habitat'] == hab].index)
        edibles = len(train[(train['habitat'] == hab) & (train['mclass'] == 'e')].index)
        edible_cc.append(edibles)
        poisonous_cc.append(size-edibles)
                            
    #=====PLOT Preparations and Plotting====#
    ind = np.arange(7)  # the x locations for the groups
    width = 0.50
    fig, ax = plt.subplots(figsize=(12,7))
    edible_bars = ax.bar(ind, edible_cc , width, color='#dec521')
    poison_bars = ax.bar(ind+width, poisonous_cc , width, color='#8722dd')

    #Add some text for labels, title and axes ticks
    ax.set_xlabel("Habitat",fontsize=20)
    ax.set_ylabel('Quantity',fontsize=20)
    ax.set_title('Edible and Poisonous Mushrooms Based on Habitat',fontsize=22)
    ax.set_xticks(ind + width / 2) #Positioning on the x axis
    ax.set_xticklabels(('Urban', 'Grasses', 'Meadows', 'Woods', 'Paths', 'Waste', 'Leaves'),
                    fontsize = 12)
    ax.legend((edible_bars,poison_bars),('edible','poisonous'),fontsize=17)



def pop_chart(train):

    pop_colors = train['population'].value_counts()
    p_height = pop_colors.values.tolist() #Provides numerical values
    pop_color_labels = pop_colors.axes[0].tolist() #Converts index object to list

    poisonous_cc = [] #Poisonous color cap list
    edible_cc = []    #Edible color cap list
    for pop in pop_color_labels:
        size = len(train[train['population'] == pop].index)
        edibles = len(train[(train['population'] == pop) & (train['mclass'] == 'e')].index)
        edible_cc.append(edibles)
        poisonous_cc.append(size-edibles)
                            
    #=====PLOT Preparations and Plotting====#
    ind = np.arange(6)  # the x locations for the groups
    width = 0.50
    fig, ax = plt.subplots(figsize=(12,7))
    edible_bars = ax.bar(ind, edible_cc , width, color='#dec521')
    poison_bars = ax.bar(ind+width, poisonous_cc , width, color='#8722dd')

    #Add some text for labels, title and axes ticks
    ax.set_xlabel("Population",fontsize=20)
    ax.set_ylabel('Quantity',fontsize=20)
    ax.set_title('Edible and Poisonous Mushrooms Based on Population',fontsize=22)
    ax.set_xticks(ind + width / 2) #Positioning on the x axis
    ax.set_xticklabels(('Scattered', 'Numerous', 'Abundant', 'Several', 'Solitary', 'Clustered'),
                    fontsize = 12)
    ax.legend((edible_bars,poison_bars),('edible','poisonous'),fontsize=17)

def odor_chart(train):
    
    #Obtain total number of mushrooms for each 'odor' (Entire DataFrame)
    odors = train['odor'].value_counts()
    odor_height = odors.values.tolist() #Provides numerical values
    odor_labels = odors.axes[0].tolist() #Converts index labels object to list


    poisonous_od = [] #Poisonous odor list
    edible_od = []    #Edible odor list
    for odor in odor_labels:
        size = len(train[train['odor'] == odor].index)
        edibles = len(train[(train['odor'] == odor) & (train['mclass'] == 'e')].index)
        edible_od.append(edibles)
        poisonous_od.append(size-edibles)
                            
    #=====PLOT Preparations and Plotting====#
    width = 0.40
    ind = np.arange(9)  # the x locations for the groups
    fig, ax = plt.subplots(figsize=(12,7))
    edible_bars = ax.bar(ind, edible_od , width, color='#dec521')
    poison_bars = ax.bar(ind+width, poisonous_od , width, color='#8722dd')

    #Add some text for labels, title and axes ticks
    ax.set_xlabel("Odor",fontsize=20)
    ax.set_ylabel('Quantity',fontsize=20)
    ax.set_title('Edible and Poisonous Mushrooms Based on Odor',fontsize=22)
    ax.set_xticks(ind + width / 2) #Positioning on the x axis
    ax.set_xticklabels(('none', 'foul','fishy','spicy','almond','anise','pungent','creosote','musty'),
                    fontsize = 12)
    ax.legend((edible_bars,poison_bars),('edible','poisonous'),fontsize=17)
    plt.show()


def cap_chart(train):

    cap_colors = train['cap_color'].value_counts()
    m_height = cap_colors.values.tolist() #Provides numerical values
    cap_colors.axes #Provides row labels
    cap_color_labels = cap_colors.axes[0].tolist() #Converts index object to list

    poisonous_cc = [] #Poisonous color cap list
    edible_cc = []    #Edible color cap list
    for capColor in cap_color_labels:
        size = len(train[train['cap_color'] == capColor].index)
        edibles = len(train[(train['cap_color'] == capColor) & (train['mclass'] == 'e')].index)
        edible_cc.append(edibles)
        poisonous_cc.append(size-edibles)
                            
    #=====PLOT Preparations and Plotting====#
    ind = np.arange(10)  # the x locations for the groups
    width = 0.40
    fig, ax = plt.subplots(figsize=(12,7))
    edible_bars = ax.bar(ind, edible_cc , width, color='#dec521')
    poison_bars = ax.bar(ind+width, poisonous_cc , width, color='#8722dd')

    #Add some text for labels, title and axes ticks
    ax.set_xlabel("Cap Color",fontsize=20)
    ax.set_ylabel('Quantity',fontsize=20)
    ax.set_title('Edible and Poisonous Mushrooms Based on Cap Color',fontsize=22)
    ax.set_xticks(ind + width / 2) #Positioning on the x axis
    ax.set_xticklabels(('brown', 'gray','red','yellow','white','buff','pink','cinnamon','purple','green'),
                    fontsize = 12)
    ax.legend((edible_bars,poison_bars),('edible','poisonous'),fontsize=17)

