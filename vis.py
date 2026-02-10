import numpy as np

print(np.__file__)

arr = np.array([10, 20, 30, 40])   # create array
print(arr)
print(type(arr))

# 1-D array
a = np.array([1, 2, 3])

# 2-D array
b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# 3-D array
c = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

""" dimensions, shape, size, data type """
arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(arr2.ndim) # number of dimensions
print(arr2.shape) # structure of the array
print(arr2.size)  # total numbers of element
print(arr2.dtype)  # data types of elemet

""" zeros, ones, empty, arange, linspace """
a = np.zeros(5)
b = np.zeros((3, 4))

print(a)
print(b)

a = np.ones(4)
b = np.ones((2, 3))

print(a)
print(b)

a = np.empty(5)  # Never use values from empty() before assigning your own data.
print(a)

# np.arange(start, stop, step)
a = np.arange(0, 10)
print(a)
b = np.arange(0, 10, 2)
print(b)
c = np.arange(0, 1, 0.2)
print(c)

# np.linspace(start, stop, num)
a = np.linspace(0, 10, 8)
print(a)