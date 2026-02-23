import numpy as np

arr = np.array([10, 20, 30, 40])
dtype = np.array([1, 2, 3], dtype=float)  # with data type
zeros = np.zeros((3, 4))  # zeros((shape))
ones = np.ones((2, 3))   # ones((shape))
empty = np.empty(5)  # Never use values from empty() before assigning your own data.
arange = np.arange(0, 10, 2)  # np.arange(start, stop, step)
linspace = np.linspace(0, 10, 8)  # np.linspace(start, stop, num)
full = np.full((2, 3), 7)  # only 7 (shape, num)
eye = np.eye(3)
rand2 = np.random.rand(2, 3)  # rand(shape) [zero to one]
randint = np.random.randint(1, 10, size=(2, 3))  # Random integers
list = [10, 20, 30]
asarray = np.asarray(list)   # change as a array from list
zeros_like = np.zeros_like(arr)   # change into zeros
ones_like = np.ones_like(arr)   # change into ones
print(arr.ndim) # number of dimensions
print(arr.shape) # structure of the array
print(arr.size)  # total numbers of element
print(arr.dtype)  # data types of elemet
