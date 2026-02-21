import numpy as np

# Broadcasting (core NumPy concept)

a = np.array([1, 2, 3])
b = 10
print(a + b)
print(a + 5)

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
b = np.array([10, 20, 30])
c = np.array([[100],
              [200]])
print(a + b)
print(c.shape)
print(a+c)


# The axis concept (deep & correct)
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(np.sum(a, axis=0)) # axis=0 collapses rows
print(np.sum(a, axis=1)) # axis=1 collapses columns

b = np.arange(0, 3*4*5*6).reshape(3, 4, 5, 6)
print(b)

c = np.sum(b, axis=2)
print('c: ', c)
print('c_shape: ', c.shape)

# keepdims (small but important bonus)
print(np.mean(b, axis=1, keepdims=True))
# By default, axis is removed.
# But sometimes you want to keep dimensions.

