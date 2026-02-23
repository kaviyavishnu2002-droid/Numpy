""" Array attributes """

import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(arr.ndim)  # number of dimensions
print(arr.shape)  # shape of data structure
print(arr.size)  # total number of elements
print(arr.dtype)  # data type

""" indexing and slicing """
a = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90,100,110,120]
])
# array[row_index, column_index]
print(a[0, 0]) # get one element
print(a[1])  # get one full row
print(a[:, 2])  # get one full column

# slicing
print("slicing"+ "-"*10)
print(a[0:2])  # slice row
print(a[:, 1:3])  #slice column
print(a[0:2, 1:3])  # slice row and column

x = a[0:2, 0:2] # This is a view, not a copy.
x[0,0] = 999 # If you modify, Original array a also changes.

# Fancy indexing: using a list / array of indices.
print(a[[0, 0]])
print(a[[0, 2]])
print(a[[0, 2], [1, 3]])# This means: (0,1) and (2,3)  # [ 20 120]

# Boolean indexing (most powerful)
print(a[a > 60])
mask = a > 60
print(mask)  
print((a > 77) & (a < 104))
a[a < 50] = 0
print(a)