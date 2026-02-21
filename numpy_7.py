"""
NUMPY SORTING & SEARCHING 
"""

import numpy as np

print("="*60)
print("ORIGINAL ARRAYS")
print("="*60)

a = np.array([50, 10, 30, 20, 40])
b = np.array([[3, 1, 2],
              [6, 4, 5]])

print("1D Array:", a)
print("2D Array:\n", b)

# --------------------------------------------------
print("\n" + "="*60)
print("SORTING METHODS")
print("="*60)

# 1. np.sort() – returns sorted copy
print("\n1. np.sort()")
print(np.sort(a))

# 2. ndarray.sort() – sorts in-place
print("\n2. array.sort() (in-place)")
a_copy = a.copy()
a_copy.sort()
print(a_copy)

# 3. Sorting 2D array (axis)
print("\n3. Sorting 2D array by axis")
print("Axis=0 (column-wise):\n", np.sort(b, axis=0))
print("Axis=1 (row-wise):\n", np.sort(b, axis=1))

# 4. np.argsort() – returns indices
print("\n4. np.argsort()")
indices = np.argsort(a)
print("Indices:", indices)
print("Sorted using indices:", a[indices])

# 5. np.lexsort() – multiple key sorting
print("\n5. np.lexsort() (multiple keys)")
names = np.array(["John", "Alice", "Bob"])
ages = np.array([25, 22, 28])
order = np.lexsort((ages, names))  # high priority for names
print("Sorted order:", order)
print("Sorted names:", names[order])
print("Sorted ages:", ages[order])

# 6. np.partition() – partial sorting
print("\n6. np.partition()")
print(np.partition(a, 2))  # first 3 smallest elements in correct position

# 7. np.argpartition() – indices of partial sort
print("\n7. np.argpartition()")
print(np.argpartition(a, 2))

# --------------------------------------------------
print("\n" + "="*60)
print("SEARCHING METHODS")
print("="*60)

x = np.array([10, 20, 30, 40, 50, 30])

print("\nArray for searching:", x)

# 1. np.where()
print("\n1. np.where()")
print("Index of 30:", np.where(x == 30))

# 2. np.searchsorted() – binary search (sorted array)
print("\n2. np.searchsorted()")
sorted_x = np.array([10, 20, 30, 40, 50])
print("Insert position for 35:", np.searchsorted(sorted_x, 35, side="right")) # default --> left 
print("→ [10, 20, 30, 35, 40, 50]")

# 3. np.argmax() – index of max
print("\n3. np.argmax()")
print("Index of max:", np.argmax(x))

# 4. np.argmin() – index of min
print("\n4. np.argmin()")
print("Index of min:", np.argmin(x))

# 5. np.max() – maximum value
print("\n5. np.max()")
print("Max value:", np.max(x))

# 6. np.min() – minimum value
print("\n6. np.min()")
print("Min value:", np.min(x))

# 7. np.nonzero() – indices of non-zero values
print("\n7. np.nonzero()")
y = np.array([0, 5, 0, 3, 0])
print("Non-zero indices:", np.nonzero(y))

# 8. np.isin() – membership test
print("\n8. np.isin()")
print(np.isin(x, [20, 40]))

# 9. np.unique() – unique values + search info
print("\n9. np.unique()")
values, indices = np.unique(x, return_index=True)
print("Unique values:", values)
print("First indices:", indices)

print("\n" + "="*60)
print("END OF FILE")
print("="*60)
