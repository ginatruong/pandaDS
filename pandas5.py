# Missing Data
import numpy as np
import pandas as pd 

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}

df = pd.DataFrame(d)
df

df.dropna()
# DELETE any rows that has a null value or NaN
# AXIS=0, ROWS/ X AXIS DEFAULT 

df.dropna(axis=1)
# DELETE any COLUMNS that has a null value or NaN 

df.dropna(thresh=2)
# shift tab lets you see documentation, thresh argument
# deletes last rows that have 2 NaN 
# kept the row that has one NaN

df.fillna(value='FILL VALUE')
# returns dataframe with FILL VALUE in cells that have a null value

df['A'].fillna(value=df['A'].mean())
# returns mean value in A column

