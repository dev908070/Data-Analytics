the central data structure in Pandas are :
    
    1.Series
    2.DataFrame
    3.index

The first letter is capitalized hence we can assume that all the Pandas 
Data structure has been implemented using OOP's concept Series,DataFrame
and Index all are classes 

The second most difference between Numpy and Pandas is

1.Numpy array store hetrogenous elements
2.Pandas Data structure are desgined to work with hetrogenous elements



import numpy as np

import pandas as pd
from pandas import Series,DataFrame

obj = pd.Series([4,7,8,5,7])

obj

obj.index

obj.values

#### We can also prove indexs by our self but its not a good thing

obj2 = pd.Series([4,7,8,5,7],index = ['a','b','c','d','e'])

obj2
obj2.index

Note :--""" 1. All the Numpy and Pandas method returns a view 
            2. both are having interoperatablity avility numpy 
               k sare function me pandas ka argument chala jata h
               or  vise versa re possible"""

np.exp(obj2) ##e to the power 


'b'in obj2

'f' in obj2

sdata = {'UP':3500,'MP':3600,'Delhi':45000,'JK':34000}

obj3 = pd.Series(sdata)

obj3

## A defination of series is just like an ordered dect. like data structure

state = ['UP','UK','JK','MP']

state

obj4 = pd.Series(state)

obj4

obj5 = pd.Series(sdata,index=state)

obj5

pd.isnull(obj5).sum()

pd.notnull(obj5).sum()

"""the comman pandas functions can straigt way called upon the data structure 
by using the dot method"""

obj5.isnull()

obj4 + obj5

#we can add a new value with .name ='values'
obj5.name = 'population'

obj5

#we can give the name to or index 
obj5.index.name = 'state'

obj5

data = {'year':[2000,2001,2002,2006,2012,2016],
        'state':['UP','UP','Up','MP','MP','MP'],
        'pop':[1.2,2.2,3.4,5,4.5,8]}

frame = pd.DataFrame(data)
frame

frame.head() #We can pass here a number according to our requerment

frame.tail() #here is same as also

pd.DataFrame(data,columns=['pop','state','state']) # its also return a view object

frame

frame2 = pd.DataFrame(data,columns=['year','state','pop','debt'],
                      index=['one','two','three','four','five','six'])



frame2

frame2['state']
# We can also use . as like below
frame2.year

frame2.loc['three']

frame2['debt']= 16.5


frame2

frame2['debt'] =np.arange(6)

frame2

val = pd.Series([1.2,2.3,2.3],index=['one','four','five'])


frame2['debt'] = val

frame2

frame2['eastern']=frame2.state == 'UP'

    
del frame2['eastern']# deleting the column

pop = {"UP":{2000:1.2,2001:2.2},
       "MP":{2006:5.0,2016:8.0}}


pop

frame3 = pd.DataFrame(pop)
frame3












































