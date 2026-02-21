# ==============================
# NumPy Stack & Split – Single File
# ==============================

import numpy as np

print("========== STACK EXAMPLES ==========")

# Base arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nOriginal Arrays:")
print("a =", a)
print("b =", b)

# 1. np.stack()
print("\n1. np.stack()")
print(np.stack((a, b)))

# 2. np.hstack()
print("\n2. np.hstack()")
print(np.hstack((a, b)))

# 3. np.vstack()
print("\n3. np.vstack()")
print(np.vstack((a, b)))

# 4. np.dstack()
print("\n4. np.dstack()")
print(np.dstack((a, b)))

# 5. np.column_stack()
print("\n5. np.column_stack()")
print(np.column_stack((a, b)))

# 6. np.row_stack()
print("\n6. np.row_stack()")
print(np.row_stack((a, b)))  # ❌ Old (deprecated)


print("\n========== SPLIT EXAMPLES ==========")

# 1D array
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("\nOriginal Array x:")
print(x)

# 1. np.split()
print("\n1. np.split(x, [3, 7])")
print(np.split(x, [3, 7]))

# 2. np.array_split()
print("\n2. np.array_split(x, 3)")
print(np.array_split(x, 3))


# 2D array for hsplit & vsplit
m = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8]])

print("\n2D Array m:")
print(m)

# 3. np.hsplit()
print("\n3. np.hsplit(m, 2)")
print(np.hsplit(m, 2))

# 4. np.vsplit()
print("\n4. np.vsplit(m, 2)")
print(np.vsplit(m, 2))


# 3D array for dsplit
n = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])

print("\n3D Array n:")
print(n)

# 5. np.dsplit()
print("\n5. np.dsplit(n, 2)")
print(np.dsplit(n, 2))

print("\n========== END ==========")
