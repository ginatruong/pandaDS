# DATAFRAMES PART 2
import numpy as np
import pandas as pd 

from numpy.random import randn 
np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z']) 
df

booldf = df > 0
# returns DATAFRAME WITH true/false

df[booldf]
# returns dataframe with VALUES that are TRUE and NaN if it's FALSE

df[df>0]
# returns DF with values that are true and NaN if false 

df['W']>0
# returns a series of A-E/ROWS, true/false on right as values

df['W']
# returns series but data values

df[df['W']>0]
# returns dataframe with true values only, rows / A-E, columns w-z, and values
# passing in a series as a bracket notation, will only get back the rows that are true 
# no null / nan values

df[df['Z']<0]
# returns dataframe with rows and columns and values only that are true 

# renaming it in a variable so don't have to type out the equation
resultdf = df[df['W']>0]
resultdf 

resultdf['X']
# returns a series of X column values

df[df['W']>0]['X']

df[df['W']>0][['Y','X']]
# see broken steps below

boolser = df['W']>0 # returns true/false in a series
result = df[boolser] # returns dataframe with values that are true only from W>0, dataframe as in all other rows/columns
mycols = ['Y', 'X']
result[molcols]
# returns dataframe with X and Y columns

# -----------------
df[(df['W']>0) and (df['Y']>1)]
# COMMON MISTAKE, THIS WILL RETURN AN ERROR, AND OPERATOR NEEDS TO BE &

df[(df['W']>0) & (df['Y']>1)]
# WILL RETURN DATAFRAME, row E
# USE OR OPERATOR AS |

# RESETTING INDEX TO DEFAULT 0 THRU END#
df.reset_index()
# returns dataframe with index# 0-4
# returns original index/labels as a new column/ INDEX with values A-E
# WON'T AFFECT ORIGINAL dataframe, unless inplace=True

df.reset_index(inplace=True)

newind = 'CA NY WY OR CO'.split()
# returns array with comma in between states ['CA', 'NY', 'WY', 'OR', 'CO']

df['States'] = newind
df
# new column/States at end of list with state values

df.set_index('States', inplace=True)
# returns index# as states column values, it'll override the old index whereas reset index lets you create a new column with the original data









