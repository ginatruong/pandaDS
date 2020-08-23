# GROUPBY - allows you to group together rows based off of a column and perform an aggregate function on them.
import numpy as np
import pandas as pd 

data = {
  'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
  'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
  'Sales':[200,120,340,124,243,350]
}

df=pd.DataFrame(data)

df.groupby('Company')
# returns groupby object type

byComp = df.groupby('Company')
byComp
# returns groupby object type

byComp.mean()
# returns the mean for each company, it'll ignore all non-numerical values

byComp.sum()

byComp.std()

byComp.sum().loc['FB']

df.groupby('Company').sum().loc['FB']
# instead of using variable

df.groupby('Company').count()
# max()
# min()

df.groupby('Company').describe()
# provides aggregate details and values

df.groupby('Company').describe().transpose()
# switches rows to columns, and vice versa

df.groupby('Company').describe().transpose()['FB']

