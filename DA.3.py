import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = np.array([1,2,3,4,5])#data type is int32

b = np.array([1,2.5,3,"ram",4])#data type is String 

""" Numpy has automatically converted all the individuals 
    elements by the large data type given
   
for example a string can easily wrap integers 
 but vice versa is difficult """
    
c = np.array([1,2,3.5,5.6])#dat type is float


d = np.array([1,2,3.5,5.6], dtype=np.int32)

""" By Explicitly specifing the dtype perameter 
    we can set the default data type"""

e = np.array([1,2,3,'ram',[1,2,3]])#its data type is  array of object

f = np.array([[1,2,3],[4,5,6]]) #Its data type is int32 becouse the elements of the list is equal

g = np.array([[1,2,3],[1,2,3,4,5]])# its data type is array of object because of elements

h = np.array([[[1,2,],[3,4]],[[2,1],[4,3]]])
h
"""In h we have two  2-D array in a single 3-D array"""
[1,2,3] + [1,2,3]
#concatination operation is perform
np.array([1,2,3]) + np.array([1,2,3])
# in the numpy array elements wise operation are performed


mat = np.array([[1,2],[3,4]])
mat

mat1 = np.array([[2,1],[4,3]])
mat1

#Cross product
mat*mat1

#Dot product

mat@mat1

#Addition with elements wise operations

mat2 = mat + mat1
mat2


# Shape of The data
a.shape
b.shape
c.shape
h.shape

#Data type

a.dtype
h.dtype
g.dtype














































