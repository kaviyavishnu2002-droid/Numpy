import numpy as np

# Mathematical operations & Universal Functions (ufuncs)
# Input arrays
a = np.array([1, 4, 9, 16])
b = np.array([10, 20, 30, 40])

print("a =", a)
print("b =", b)

print("\nnp.add(a, b)")
print(np.add(a, b))

print("\nnp.subtract(a, b)")
print(np.subtract(a, b))

print("\nnp.multiply(a, b)")
print(np.multiply(a, b))

print("\nnp.divide(a, b)")
print(np.divide(a, b))

print("\nnp.sqrt(a)")
print(np.sqrt(a))

print("\nnp.power(a, 2)")
print(np.power(a, 2))

print("\nnp.exp(a)")
print(np.exp(a))

print("\nnp.log(a)")
print(np.log(a))

print("\nnp.floor([1.2, 3.7, 5.0, 9.9])")
print(np.floor(np.array([1.2, 3.7, 5.0, 9.9])))

print("\nnp.ceil([1.2, 3.7, 5.0, 9.1])")
print(np.ceil(np.array([1.2, 3.7, 5.0, 9.1])))

print("\nnp.round([1.2, 1.5, 1.8, 2.5])")
print(np.round(np.array([1.2, 1.5, 1.8, 2.5])))

print("\nnp.logical_and(a > 5, b < 35)")
print(np.logical_and(a > 5, b < 35))

print("\nnp.logical_or(a > 5, b < 20)")
print(np.logical_or(a > 5, b < 20))

x = np.array([0, np.pi/2, np.pi])
np.sin(x)
np.cos(x)


# Aggregation functions
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Array a:\n", a)

print("\nnp.sum(a)")
print(np.sum(a))

print("\nnp.sum(a, axis=0)")
print(np.sum(a, axis=0))

print("\nnp.sum(a, axis=1)")
print(np.sum(a, axis=1))


print("\nnp.min(a)")
print(np.min(a))

print("\nnp.min(a, axis=0)")
print(np.min(a, axis=0))

print("\nnp.min(a, axis=1)")
print(np.min(a, axis=1))


print("\nnp.max(a)")
print(np.max(a))

print("\nnp.max(a, axis=0)")
print(np.max(a, axis=0))

print("\nnp.max(a, axis=1)")
print(np.max(a, axis=1))


print("\nnp.mean(a)")
print(np.mean(a))

print("\nnp.mean(a, axis=0)")
print(np.mean(a, axis=0))

print("\nnp.mean(a, axis=1)")
print(np.mean(a, axis=1))


print("\nnp.median(a)")
print(np.median(a))

print("\nnp.std(a)")
print(np.std(a))

print("\nnp.var(a)")
print(np.var(a))


print("\nnp.prod(a)")
print(np.prod(a))

print("\nnp.cumsum(a)")
print(np.cumsum(a))

print("\nnp.cumprod(a)")
print(np.cumprod(a))


print("\nnp.any(a > 45)")
print(np.any(a > 45))

print("\nnp.all(a > 5)")
print(np.all(a > 5))


print("\nnp.argmax(a)")
print(np.argmax(a))

print("\nnp.argmin(a)")
print(np.argmin(a))


print("\nnp.ptp(a)")
print(np.ptp(a))


print("\nnp.count_nonzero(a)")
print(np.count_nonzero(a))
