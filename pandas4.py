# DATAFRAMES PART 3
import numpy as import np 
import pandas as pd 

# INDEX LEVELS
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

outside
# returns array

inside 
# returns inside

list(zip(outside,inside))
# returns [('G1',1),etc.]

df = pd.Dataframe(randn(6,2),hier_index,['A','B'])
# 6,2 = rows and columns, x,y
# returns GROUP G1 with 1-3 rows/column a/b, GROUP G2 with 1-3 rows/column a/b, total of 6 rows and 2 columns

df.loc['G1']
# RETURNS SUBDATA OF G1

df.loc['G1'].loc[1]
# returns a series

df.index.names

df.index.names = ['Groups','Num']
df
# returns GROUPS ON THE OUTSIDE, NUM AS IN THE INSIDE ROW 1-3 

df.loc['G2'].loc[2]['B']
# returns group2, two rows, b column

df.xs('G1')
# returns a cross section, returns num/as index and not include the groups index/subset, ONLY RETURNS THE DATA INSIDE

df.xs(1,level='Num')
# doesn't return NUM/ROW, but returns GROUP INDEX




