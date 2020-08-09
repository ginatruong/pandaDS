# GROUPBY - allows you to group together rows based off of a column and perform an aggregate function on them.
import numpy as np
import pandas as pd 

data = {
  'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
  'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
  'Sales':[200,120,340,124,243,350]
}

df=pd.DataFrame(data)

