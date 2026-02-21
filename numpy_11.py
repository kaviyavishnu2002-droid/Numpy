"""
NUMPY MEMORY LAYOUT, STRIDES & CONTIGUOUS ARRAYS
Single File Example
"""

import numpy as np

print("="*70)
print("1. BASIC ARRAY & MEMORY INFO")
print("="*70)

a = np.array([1, 2, 3, 4, 5])
b = np.arange(12).reshape(3, 4)
print("Array a:", a)
print("Array a.dtype:", a.dtype)
print("Shape:", a.shape)
print("Strides:", a.strides) # strides = (row_jump, column_jump)
print("Flags b:", b.flags)
print("C-contiguous:", a.flags['C_CONTIGUOUS'])
print("F-contiguous:", a.flags['F_CONTIGUOUS'])

# `C_CONTIGUOUS` | Row-major storage    
# `F_CONTIGUOUS` | Column-major storage 
# `OWNDATA`      | Owns memory          
# `WRITEABLE`    | Modifiable           
# `ALIGNED`      | CPU-friendly memory  

# --------------------------------------------------
print("\n" + "="*70)
print("2. C-ORDER (ROW-MAJOR) MEMORY LAYOUT")
print("="*70)

c_array = np.array([[1, 2, 3],
                    [4, 5, 6]], order='C')

print("C-order array:\n", c_array)
print("Array c.dtype:", c_array.dtype)
print("Strides:", c_array.strides)
print("C-contiguous:", c_array.flags['C_CONTIGUOUS'])
print("F-contiguous:", c_array.flags['F_CONTIGUOUS'])

# --------------------------------------------------
print("\n" + "="*70)
print("3. F-ORDER (COLUMN-MAJOR) MEMORY LAYOUT")
print("="*70)

f_array = np.array([[1, 2, 3],
                    [4, 5, 6]], order='F')

print("F-order array:\n", f_array)
print("Strides:", f_array.strides)
print("C-contiguous:", f_array.flags['C_CONTIGUOUS'])
print("F-contiguous:", f_array.flags['F_CONTIGUOUS'])

# --------------------------------------------------
print("\n" + "="*70)
print("4. STRIDES EXPLANATION")
print("="*70)

x = np.array([[10, 20, 30],
              [40, 50, 60]])

print("Array x:\n", x)
print("Strides:", x.strides)
print("Meaning:")
print("- Move 1 row ->", x.strides[0], "bytes")
print("- Move 1 column ->", x.strides[1], "bytes")

# --------------------------------------------------
print("\n" + "="*70)
print("5. VIEW (SHARED MEMORY)")
print("="*70)

view = x.view() # (SHARED MEMORY)
view[0, 0] = 999

print("Original array after view change:\n", x)
print("View array:\n", view)

# --------------------------------------------------
print("\n" + "="*70)
print("6. COPY (SEPARATE MEMORY)")
print("="*70)

copy_arr = x.copy()
copy_arr[0, 1] = 888

print("Original array:\n", x)
print("Copied array:\n", copy_arr)

# --------------------------------------------------
print("\n" + "="*70)
print("7. NON-CONTIGUOUS ARRAY (SLICING)")
print("="*70)

y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
sliced = y[::2]

print("Original y:", y)
print("Sliced y[::2]:", sliced)
print("y dtype:", y.dtype)
print("sliced dtype:", sliced.dtype)
print("Strides y:", y.strides)
print("Strides:", sliced.strides)
print("C-contiguous:", sliced.flags['C_CONTIGUOUS'])

# --------------------------------------------------
print("\n" + "="*70)
print("8. MAKING ARRAY CONTIGUOUS")
print("="*70)

contig = np.ascontiguousarray(sliced)
# ascontiguousarray() creates a copy only if needed

print("New array:", contig)
print("Strides:", contig.strides)
print("C-contiguous:", contig.flags['C_CONTIGUOUS'])

# --------------------------------------------------
print("\n" + "="*70)
print("9. TRANSPOSE & MEMORY LAYOUT")
print("="*70)

m = np.array([[1, 2, 3],
              [4, 5, 6]])

t = m.T  # transpose() creates a non-contiguous view

print(np.shares_memory(a, t))
print("Original:\n", m)
print("Transpose:\n", t)
print("m strides:", m.strides)
print("t strides:", t.strides)
print("m C-contiguous:", m.flags['C_CONTIGUOUS'])
print("t C-contiguous:", t.flags['C_CONTIGUOUS'])

# --------------------------------------------------
print("\n" + "="*70)
print("10. FLATTEN vs RAVEL")
print("="*70)

m = np.array([[1, 2, 3],
              [4, 5, 6]])

flat = m.flatten()
ravel = m.ravel()

flat[0] = 1000
ravel[1] = 2000

print("Original array:\n", m)
print("Flatten (copy):", flat)
print("Ravel (view when possible):", ravel)

# --------------------------------------------------
print("\n" + "="*70)
print("11. SUMMARY CHECK")
print("="*70)

print("m C-contiguous:", m.flags['C_CONTIGUOUS'])
print("m F-contiguous:", m.flags['F_CONTIGUOUS'])
print("t C-contiguous:", t.flags['C_CONTIGUOUS'])
print("t F-contiguous:", t.flags['F_CONTIGUOUS'])

print("\nEND OF FILE")
print("="*70)
