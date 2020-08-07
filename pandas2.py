# DATAFRAME#1
import numpy as np
import pandas as pd 

from numpy.random import randn 
np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z']) 
df
# returns 5 rows, 4 columns. 
# A-E are row indexes, and W-Z are column names

df['W']
# returns the W column with a-e rows

type(df['W'])
# returns pandas.core.series 

type(df)
# returns pandas.core.frame.DataFrame

df.W 
# returns like df['W'] / column W with their rows / recommended to use [], bc the dot is used for other methods

df[['W','Z']]
# returns W and Z columns with A-E rows/
# MULTIPLE COLUMN - DATAFRAME
# SINGLE COLUMN - RETURNS A SERIES 

# df['new'] - returns keyerror

df['new'] = df['W'] + df['Y']
# created a new last column with W + Y values 

df.drop('new', axis=1, inplace=True)
# axis = 0 means it's referring to the INDEX / X AXIS
# if want to refer to column, axis = 1 /Y AXIS
# it will return with the new column if you don't specify ARGUMENT inplace=True bc it's defaulted to FALSE
# DEFAULTED TO FALSE so changes are made by mistake

df.drop('E',axis=0)
# axis=0 is defaulted so you don't have to specify it
# it'll delete ROW E / x axis

df.shape
# returns (5,4) 2 dimensional 5 ROWS/ 4 COLUMNS (X = 0,Y = 1)

df['Y']
# returns single column 

df[['Z','X']]
# returns multiple columns

df.loc['A']
# returns index A
# location of INDEX / ROW YOU WANT
# shift tab in jupyter will show information
# RETURNS SERIES of A index, COLUMN W-Z AS INDEX SERIES/LEFT AND VALUE OF A WILL BE ON RIGHT SIDE

df.iloc[2]
# location index position# NUMERICAL/INTEGER ONLY
# C IS INDEX 2

df.loc['B','Y']
# returns a single value
# row B, column Y = single value

df.loc[['A','B'], ['W','Y']]
# returns a subset of rows A and B with Columns W and Y /values 










