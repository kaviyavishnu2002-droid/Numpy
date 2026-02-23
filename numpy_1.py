import numpy as np

print(f"path: {np.__file__}")

""" create an arrays """
# zeros, ones, empty, arange, linspace, full, eye, rand, asarray, dtype, zeros_like, ones_like
arr = np.array([10, 20, 30, 40])
print(f"arr: {arr}")
print(f"arrtype: {type(arr)}")

zeros = np.zeros(5)
print(f"zeroes: {zeros}")

zeros2 = np.zeros((3, 4))
print(f"zeroes2: {zeros2}")

ones = np.ones(4)
print(f"ones: {ones}")

ones2 = np.ones((2, 3))
print(f"ones2: {ones2}")

empty = np.empty(5)  # Never use values from empty() before assigning your own data.
print(f"empty: {empty}")

arange = np.arange(0, 10, 2)  # np.arange(start, stop, step)
print(f"arange: {arange}")

linspace = np.linspace(0, 10, 8)  # np.linspace(start, stop, num)
print(f"linspace: {linspace}")

full = np.full((2, 3), 7)  # only 7
print(f"full: {full}")

eye = np.eye(3)
print(f"eye: {eye}")

rand = np.random.rand(3)
print(f"rand: {rand}")

rand2 = np.random.rand(2, 3)
print(f"rand2 {rand2}")

randint = np.random.randint(1, 10, size=(2, 3))  # Random integers
print(f"randint: {randint}")

lst = [10, 20, 30]
asarray = np.asarray(lst)
print(f"asarray: {asarray}")

dtype = np.array([1, 2, 3], dtype=float)
print(f"dtype: {dtype}")

x = np.array([[1,2,3],[4,5,6]])
zeros_like = np.zeros_like(x)   # change into zeros
print(f"zeros_like: {zeros_like}")

ones_like = np.ones_like(x)   # change into ones
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
