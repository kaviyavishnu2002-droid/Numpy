"""
NUMPY MASKING & FILTERING
"""

import numpy as np

print("="*70)
print("ORIGINAL DATA")
print("="*70)

a = np.array([10, 15, 20, 25, 30, 35, 40])
b = np.array([[5, 12, 7],
              [20, 3, 25],
              [30, 18, 1]])

print("1D Array:", a)
print("2D Array:\n", b)

# -------------------------------------------------------------------
print("\n" + "="*70)
print("BOOLEAN MASKING (CONDITION BASED)")
print("="*70)

# 1. Simple boolean mask
mask = a > 25
print("\n1. Mask (a > 25):", mask)
print("Filtered values:", a[mask])

# 2. Direct condition filtering
print("\n2. Direct filtering (a <= 20):")
print(a[a <= 20])

# 3. Multiple conditions using logical operators
print("\n3. Multiple conditions (20 < a < 35):")
print(a[(a > 20) & (a < 35)])

# -------------------------------------------------------------------
print("\n" + "="*70)
print("MASKING WITH LOGICAL FUNCTIONS")
print("="*70)

# 4. np.logical_and
print("\n4. np.logical_and():")
print(a[np.logical_and(a >= 15, a <= 30)])

# 5. np.logical_or
print("\n5. np.logical_or():")
print(a[np.logical_or(a < 15, a > 35)])

# 6. np.logical_not
print("\n6. np.logical_not():")
print(a[np.logical_not(a > 25)])

# -------------------------------------------------------------------
print("\n" + "="*70)
print("WHERE-BASED FILTERING")
print("="*70)

# 7. np.where() – filtering values
print("\n7. np.where() – values > 25:")
print(np.where(a > 25, a, -1))

# 8. np.where() – indices
print("\n8. np.where() – indices where a == 25:")
print(np.where(a == 25))

# -------------------------------------------------------------------
print("\n" + "="*70)
print("FILTERING 2D ARRAYS")
print("="*70)

# 9. 2D condition filtering
print("\n9. Elements > 15:")
print(b[b > 15])

# 10. Row-wise filtering
print("\n10. Rows where sum > 40:")
row_mask = b.sum(axis=1) > 40
print(b[row_mask])

# -------------------------------------------------------------------
print("\n" + "="*70)
print("MEMBERSHIP & VALUE FILTERING")
print("="*70)

# 11. np.isin()
print("\n11. np.isin():")
print(a[np.isin(a, [15, 25, 35])])

# 12. np.in1d() (1D only)
# print("\n12. np.in1d():")
# print(a[np.in1d(a, [10, 40])]) # it's old version use isin

# -------------------------------------------------------------------
print("\n" + "="*70)
print("SPECIAL FILTERING METHODS")
print("="*70)

# 13. np.nonzero()
print("\n13. np.nonzero():")
c = np.array([0, 5, 0, 8, 0, 3])
print(np.nonzero(c))
print("Non-zero values:", c[np.nonzero(c)])

# 14. np.isnan()
print("\n14. np.isnan():")
d = np.array([1.0, np.nan, 2.5, np.nan, 4.0])
print("Without NaN:", d[~np.isnan(d)])

# 15. np.isfinite()
print("\n15. np.isfinite():")
e = np.array([1, np.inf, -np.inf, 5])
print("Finite values:", e[np.isfinite(e)])

# -------------------------------------------------------------------
print("\n" + "="*70)
print("BOOLEAN INDEX ARRAY (ADVANCED)")
print("="*70)

# 16. Boolean index array
bool_idx = np.array([True, True, True, False, True, False, True])
print("\n16. Boolean index array:")
print(a[bool_idx])

# -------------------------------------------------------------------
print("\n" + "="*70)
print("FILTERING USING FUNCTIONS")
print("="*70)

# 17. np.vectorize() filtering
print("\n17. Custom function filter:")

def is_even(x):
    return x % 2 == 0

even_mask = np.vectorize(is_even)(a)
print("Even numbers:", a[even_mask])

print("\n" + "="*70)
print("END OF FILE")
print("="*70)
