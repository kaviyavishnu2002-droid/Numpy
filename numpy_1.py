import numpy as np

print(f"path: {np.__file__}")

""" create an arrays """
# zeros, ones, empty, arange, linspace, full, eye, rand, asarray, dtype, zeros_like, ones_like
arr = np.array([10, 20, 30, 40])
zeros = np.zeros(5)
zeros2 = np.zeros((3, 4))
ones = np.ones(4)
ones2 = np.ones((2, 3))
empty = np.empty(5)  # Never use values from empty() before assigning your own data.
arange = np.arange(0, 10)  # np.arange(start, stop, step)
arange2 = np.arange(0, 10, 2)
arange3 = np.arange(0, 1, 0.2)
linspace = np.linspace(0, 10, 8)  # np.linspace(start, stop, num)
full = np.full((2, 3), 7)  # only 7
eye = np.eye(3)
rand = np.random.rand(3)
rand2 = np.random.rand(2, 3)
randint = np.random.randint(1, 10, size=(2, 3))  # Random integers
lst = [10, 20, 30]
asarray = np.asarray(lst)
dtype = np.array([1, 2, 3], dtype=float)
x = np.array([[1,2,3],[4,5,6]])
zeros_like = np.zeros_like(x)
ones_like = np.ones_like(x)

print(f"arr: {arr}")
print(f"arrtype: {type(arr)}")
print(f"zeroes: {zeros}")
print(f"zeroes2: {zeros2}")
print(f"ones: {ones}")
print(f"ones2: {ones2}")
print(f"empty: {empty}")
print(f"arange: {arange}")
print(f"arange2: {arange2}")
print(f"arange3: {arange3}")
print(f"linspace: {linspace}")
print(f"full: {full}")
print(f"eye: {eye}")
print(f"rand: {rand}")
print(f"rand2 {rand2}")
print(f"randint: {randint}")
print(f"asarray: {asarray}")
print(f"dtype: {dtype}")
print(f"zeros_like: {zeros_like}")
print(f"ones_like: {ones_like}")


""" dimensions, shape, size, data type """
arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(arr2.ndim) # number of dimensions
print(arr2.shape) # structure of the array
print(arr2.size)  # total numbers of element
print(arr2.dtype)  # data types of elemet

a = np.array([1,2,3])
b = np.array([4,5,6])
c = a + b
print(c) # [5 7 9]
