import numpy as np

Q. What is Standard Normal distribution
Ans. A normal distribution with mean =0 and standard deviation = 0

Q.What is simpling a distribution?
Ans. To get values fromthat distribution 

data = np.random.randn(2,3)
data

data*10

data + data

data

#Numpy mostly returns a view object and does not frequently changes the original Data

data.shape
data.dtype  


data1 = [1,2,3,4,5,4]
arr1 = np.array(data1)

data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)

#ndim method is use for checking the dimention of the data

arr1.ndim
arr2.ndim

"""spyder cant show array object of more than 3 dimenions as of now"""

np.zeros(10)

np.zeros(2,3) #it will generate an error
''' Numpy k kisi bhi function ko 2-d data pass karna hota h to usko 
    tuple form me pass kiya jata hai'''

np.zeros((2,3))

#empty Returns garbage values
np.empty((2,3,2))

'''numpy also overrides a lot of builtin python function numpy always adds
   'a' prefix to all the over riden''' 

range(15)
np.arange(15)


####################### comman data types of Numpy ##################



The default data type is float64
but it can be changes according to the perfrances
64 or 32 woh size hai memoray ka



Slicing :-  entire row or entire column or row/columns 
Dicing :- Some roe or sum columns dicing means cube

arr = np.arange(15)

arr[5:8]

arr[5:8] = 12 # Here it will change the original values of that array

arr_slice = arr[5:8]

arr_slice[1] = 12344 # it will aso change the original values of arr

arr_slice

arr

#### copy() function can help to prevent from this changes

arr2d = np.array([[1,2,3],[4,5,6],[8,9,7]])

arr2d

arr2d[2] #first row of the matrix

Numpy ka prefrenaces sabse pahle row ko jata h


arr2d[1][0]
&

arr2d[1,0]

arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

arr3d

arr3d[0]

arr3d[1]

old_values = arr3d[0].copy()

arr3d[0] = 23

arr3d

arr3d[0] = old_values

arr3d
arr3d[1,0]

















 
































































