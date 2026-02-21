"""
NUMPY LINEAR ALGEBRA (numpy.linalg)
"""

import numpy as np
from numpy.linalg import (
    det, inv, matrix_rank, eig, eigvals,
    solve, norm, svd, cond, pinv, qr, cholesky
)

print("="*70)
print("LINEAR ALGEBRA USING numpy.linalg")
print("="*70)

# --------------------------------------------------
print("\nORIGINAL MATRICES")
# --------------------------------------------------

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[2, 1],
              [1, 3]])

b = np.array([5, 11])

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Vector b:", b)

# --------------------------------------------------
print("\n1. DETERMINANT (det)")
print("det(A):", det(A))

# --------------------------------------------------
print("\n2. INVERSE (inv)")
A_inv = inv(A)
print("Inverse of A:\n", A_inv)

# --------------------------------------------------
print("\n3. MATRIX RANK (matrix_rank)")
print("Rank of A:", matrix_rank(A))

# --------------------------------------------------
print("\n4. SOLVING LINEAR EQUATIONS (solve)")
# Ax = b
x = solve(A, b)
print("Solution x for Ax=b:", x)

# --------------------------------------------------
print("\n5. EIGENVALUES & EIGENVECTORS (eig)")
eigenvalues, eigenvectors = eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# --------------------------------------------------
print("\n6. EIGENVALUES ONLY (eigvals)")
print("Eigenvalues of B:", eigvals(B))

# --------------------------------------------------
print("\n7. MATRIX NORM (norm)")
print("Frobenius norm of A:", norm(A))
print("L2 norm of A:", norm(A, ord=2))

# --------------------------------------------------
print("\n8. SINGULAR VALUE DECOMPOSITION (svd)")
# A = U Σ Vᵀ
U, S, Vt = svd(A)
print("U:\n", U)
print("Singular values:", S)
print("Vᵀ:\n", Vt)

# --------------------------------------------------
print("\n9. CONDITION NUMBER (cond)")
print("Condition number of A:", cond(A))

# --------------------------------------------------
print("\n10. PSEUDO-INVERSE (pinv)")
A_pinv = pinv(A)
print("Pseudo-inverse of A:\n", A_pinv)

# --------------------------------------------------
print("\n11. QR DECOMPOSITION (qr)")
# A = QR
Q, R = qr(A)
print("Q matrix:\n", Q)
print("R matrix:\n", R)

# --------------------------------------------------
print("\n12. CHOLESKY DECOMPOSITION (cholesky)")
# Only for symmetric positive-definite matrices
C = np.array([[4, 2],
              [2, 3]])

print("Matrix C:\n", C)
L = cholesky(C)
print("Cholesky decomposition (L):\n", L)

# --------------------------------------------------
print("\n13. TRACE (np.trace)")
print("Trace of A:", np.trace(A))

# --------------------------------------------------
print("\n14. MATRIX MULTIPLICATION (dot)")
print("A dot B:\n", np.dot(A, B))

# --------------------------------------------------
print("\n15. IDENTITY MATRIX (eye)")
I = np.eye(3)
print("Identity matrix:\n", I)

# --------------------------------------------------

print("\n" + "="*70)
print("END OF numpy.linalg DEMO")
print("="*70)
