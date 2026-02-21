import numpy as np
# Data types & type conversion

a = np.zeros(1000000, dtype=np.float64)
b = np.zeros(1000000, dtype=np.float32)

print(a.nbytes) # Memory understanding
print(b.nbytes)

#  type conversion
a = np.array([1, 2, 3, 4])
b = a.astype(float)
print(b)
print(a.dtype)
print(b.dtype)

x = np.array([1.9, 2.2, 3.7])
y = x.astype(int) # x is still old type
print(y)
x = x.astype(int) # correct way
b = x.astype(bool)
print(b)

# reshape(), flatten(), ravel()
a = np.arange(1, 13)

b = a.reshape(3, 4)
f = b.flatten() # always copy
r = b.ravel() 
print(f)
print(r)
r[0] = 888
print(b)

# fancy indexing creates a copy
y = b[[0, 2]] # y is row 0 and 2
print(y)
y[0, 0] = 555
print(b) # b will NOT change.

print(np.shares_memory(b, x))
