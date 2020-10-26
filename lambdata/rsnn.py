import pandas as pd
import numpy as np
import random


def numNull(df):
    return df.isnull().sum().sum()


def randomShuffle(df):
    df = df.copy()
    # Make a list to hold the indecies (sorted and random)
    indexNums = []
    randIndecies = []
    
    # Populate sorted indecies list
    for i in range(len(df)):
        indexNums.append(i)
    
    # Randomize index list
    for i in range(len(df)):
        randRow = random.choice(indexNums)
        # Add random index to the column
        randIndecies.append(randRow)
        # Remove that option from future indecies
        indexNums.remove(randrow)

    # Add the randomized list to the df as a new column
    df['randIndex'] = pd.Series(randIndecies)

    # Sort the dataframe by the new index and drop that 
    df = df.sort_values('randIndex').drop(columns='randIndex')

    # Reset the index column
    df = df.reset_index().drop(columns='index')

    # Return the updated dataframe
    return df
