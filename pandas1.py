# command line to install
conda install pandas
pip install pandas

# --------------------------------------------------------
# SERIES
# PANDA series - series of axis labels meaning, indexed by a label
import numpy as np
import pandas as pd 

labels = ['a', 'b', 'c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

pd.Series(data = my_data)
# index/right 0-2, right/mydata 10-30

pd.Series(data=my_data, index=labels)

pd.Series(my_data,labels) 
# data and index are in the correct order

pd.Series(arr)
# index/right 0-2, data/right/arr 10-30

pd.Series(arr, labels)

pd.Series(d)
# index as a-c, data/10-30 from key/value dictionary

pd.Series(data=labels)
# index/right 0-2, data/labels/right/a-c

pd.Series(data=[sum,print,len])
# passing in functions
# never really use this but good to know for string functions

ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])
ser1 
# returns left index/as countries, and data as numbers/right

ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])
ser2 

# retrieving value using index
ser1['USA']
# index/USA, returns DATA VALUE: 1

ser3 = pd.Series(data=labels)
# index/right, 0-2, labels as data values/a-c, right

ser3[0]
# returns value a by using index:0

ser1 + ser2 
# try to match up based off from the index, and then calculate data/values
# USA 2
# GERMANY 4
# IF NO MATCH, RETURNS NULL
# IT'LL RETURN INTEGERS AS FLOAT 4.0

ser2

