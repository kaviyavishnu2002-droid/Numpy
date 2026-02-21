"""
NUMPY VECTORIZATION vs LOOPS
"""

import numpy as np
import time

print("="*70)
print("SETUP DATA")
print("="*70)

n = 1_000_000
a = np.random.rand(n)
b = np.random.rand(n)

print("a:", a)
print("b:", b)
# --------------------------------------------------
print("\n" + "="*70)
print("1. ADDITION")
print("="*70)

# LOOP
start = time.time()
c_loop = np.empty(n)
for i in range(n):
    c_loop[i] = a[i] + b[i]
loop_time = time.time() - start

# VECTORIZATION
start = time.time()
c_vec = a + b
vec_time = time.time() - start
print("c_loop:", c_loop)
print("c_vec:", c_vec)
print("Loop time:", loop_time)
print("Vectorized time:", vec_time)

# --------------------------------------------------
print("\n" + "="*70)
print("2. SUBTRACTION")
print("="*70)

# LOOP
c_loop = np.empty(n)
for i in range(n):
    c_loop[i] = a[i] - b[i]

# VECTORIZATION
c_vec = a - b

print("Done subtraction (loop vs vectorized)")

# --------------------------------------------------
print("\n" + "="*70)
print("3. MULTIPLICATION")
print("="*70)

# LOOP
c_loop = np.empty(n)
for i in range(n):
    c_loop[i] = a[i] * b[i]

# VECTORIZATION
c_vec = a * b

print("Done multiplication (loop vs vectorized)")

# --------------------------------------------------
print("\n" + "="*70)
print("4. DIVISION")
print("="*70)

# LOOP
c_loop = np.empty(n)
for i in range(n):
    c_loop[i] = a[i] / b[i]

# VECTORIZATION
c_vec = a / b

print("Done division (loop vs vectorized)")

# --------------------------------------------------
print("\n" + "="*70)
print("5. POWER OPERATION")
print("="*70)

# LOOP
c_loop = np.empty(n)
for i in range(n):
    c_loop[i] = a[i] ** 2

# VECTORIZATION
c_vec = a ** 2

print("Done power (loop vs vectorized)")

# --------------------------------------------------
print("\n" + "="*70)
print("6. CONDITIONAL OPERATION")
print("="*70)

# LOOP
c_loop = np.empty(n)
for i in range(n):
    if a[i] > 0.5:
        c_loop[i] = 1
    else:
        c_loop[i] = 0

# VECTORIZATION
c_vec = np.where(a > 0.5, 1, 0)
print("c_loop:", c_loop)
print("c_vec:", c_vec)
print("Done conditional operation")

# --------------------------------------------------
print("\n" + "="*70)
print("7. MATHEMATICAL FUNCTIONS (sin, log)")
print("="*70)

# LOOP
c_loop = np.empty(n)
for i in range(n):
    c_loop[i] = np.sin(a[i]) + np.log(a[i] + 1)

# VECTORIZATION
c_vec = np.sin(a) + np.log(a + 1)

print("Done math functions")

# --------------------------------------------------
print("\n" + "="*70)
print("8. SUM REDUCTION")
print("="*70)

# LOOP
total = 0.0
for i in range(n):
    total += a[i]

# VECTORIZATION
total_vec = np.sum(a)

print("Loop sum:", total)
print("Vectorized sum:", total_vec)

# --------------------------------------------------
print("\n" + "="*70)
print("9. MEAN CALCULATION")
print("="*70)

# LOOP
total = 0.0
for i in range(n):
    total += a[i]
mean_loop = total / n

# VECTORIZATION
mean_vec = np.mean(a)

print("Loop mean:", mean_loop)
print("Vectorized mean:", mean_vec)

# --------------------------------------------------
print("\n" + "="*70)
print("10. 2D ARRAY OPERATION")
print("="*70)

mat = np.random.rand(1000, 1000)

# LOOP
row_sums_loop = np.zeros(1000)
start_time = time.time()
for i in range(1000):
    for j in range(1000):
        row_sums_loop[i] += mat[i, j]
print("loop_time:", time.time() - start_time)

# VECTORIZATION
start_time = time.time()
row_sums_vec = mat.sum(axis=1)
print("vectorization time:", time.time() - start_time)

print("Done 2D row sum")

# --------------------------------------------------

print("="*70)
print("END OF FILE")
print("="*70)
