import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

np.add(a, b, out=a)

print(a) # [11 22 33]

# --------------------------------------------------

# Use boolean masks efficiently
# np.clip(array, min_value, max_value, out=None)

print(np.clip(a, 0, 100, out=a))

# like
a[a < 0] = 0
a[a > 100] = 100

# --------------------------------------------------
# np.select() is used to apply multiple conditions 
# to an array and choose different values for each condition.

# np.select(conditions, results, default=0)

returns = np.array([0.02, 0.005, -0.03, 0.0, -0.008])

signal = np.select(
    [returns > 0.01, returns < -0.01],
    [1, -1],
    default=0
)

print(signal)

# Pipeline mindset
prices = np.array([
    [100, 104,  99, 104],
    [104, 108, 102, 107],
    [107, 110, 105, 109]
], dtype=np.float32)

# returns
returns = (prices[:, 3] - prices[:, 0]) / prices[:, 0]

# signal
signal = np.where(returns > 0, 1, -1)

# risk control
signal = np.clip(signal, -1, 1)

# Axis + keepdims = professional pattern

X = np.array([
    [2, 4, 6],
    [1, 3, 5]
])
mean = X.mean(axis=1, keepdims=True)
X_norm = X - mean
print("mean:", mean)
print("x_norm:", X_norm)

# no reshape hacks
# broadcasting works cleanly
# fewer bugs