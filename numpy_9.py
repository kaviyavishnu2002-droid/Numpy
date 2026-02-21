"""
NUMPY RANDOM NUMBERS
"""

import numpy as np

# --------------------------------------------------
print("\n1. np.random.random()  → Uniform [0.0, 1.0)")
print(np.random.random())
print(np.random.random(5))
print(np.random.random((2, 3)))

# --------------------------------------------------
print("\n2. np.random.rand()  → Uniform [0.0, 1.0)")
print(np.random.rand())
print(np.random.rand(4))
print(np.random.rand(2, 3))

# --------------------------------------------------
print("\n3. np.random.randn()  → Standard Normal Distribution")
print(np.random.randn())
print(np.random.randn(5))
print(np.random.randn(2, 3))

# --------------------------------------------------
print("\n4. np.random.randint()  → Random Integers")
print(np.random.randint(10))          # 0 to 9
print(np.random.randint(10, 20))      # 10 to 19
print(np.random.randint(1, 100, 5))   # 5 numbers
print(np.random.randint(1, 10, (2, 3))) # shape

# --------------------------------------------------
print("\n5. np.random.uniform()  → Uniform Distribution")
print(np.random.uniform(5, 10))
print(np.random.uniform(1, 5, 4))
print(np.random.uniform(0, 1, (2, 3)))

# --------------------------------------------------
print("\n6. np.random.normal()  → Normal Distribution")
print(np.random.normal())
print(np.random.normal(0, 1, 5))
print(np.random.normal(50, 10, (2, 3)))  # values = 50 +or- 10

# --------------------------------------------------
print("\n7. np.random.choice()  → Random Selection")
arr = np.array([10, 20, 30, 40, 50])
print(np.random.choice(arr))
print(np.random.choice(arr, 3))
print(np.random.choice(arr, 3, replace=False)) # replace=False --> not repeat
print(np.random.choice(arr, 5, p=[0.1, 0.2, 0.3, 0.2, 0.2])) # Probability weights for each element.
#  10 has low probability and 30 has high probability.

# --------------------------------------------------
print("\n8. np.random.permutation()  → Random Permutation")
print(np.random.permutation(arr)) # [40 50 10 20 30]
print(np.random.permutation(10)) # [9 6 5 1 3 4 0 7 2 8]

# --------------------------------------------------
print("\n9. np.random.shuffle()  → In-place Shuffle")
arr2 = arr.copy()
np.random.shuffle(arr2)
print(arr2)

# --------------------------------------------------
print("\n10. np.random.seed()  → Reproducible Randomness")
np.random.seed(42)
print(np.random.randint(1, 100, 5))
np.random.seed(42)
print(np.random.randint(1, 100, 5))  # Same output

np.random.seed(45)
print(np.random.randint(1, 100, 5))
np.random.seed(42)
print(np.random.randint(1, 100, 5))

np.random.seed(44)
print(np.random.randint(1, 100, 5))
np.random.seed(42)
print(np.random.randint(1, 100, 5))

np.random.seed(44)
print(np.random.randint(1, 100, 5))
np.random.seed(45)
print(np.random.randint(1, 100, 5))

# --------------------------------------------------
print("\n11. np.random.exponential()  → Exponential Distribution")
print(np.random.exponential(1.0, 5))

# --------------------------------------------------
print("\n12. np.random.poisson()  → Poisson Distribution")
print(np.random.poisson(5, 5))

# --------------------------------------------------
print("\n13. np.random.binomial()  → Binomial Distribution")
print(np.random.binomial(10, 0.5, 5))

# --------------------------------------------------
print("\n14. np.random.beta()  → Beta Distribution")
print(np.random.beta(2, 5, 5))

# --------------------------------------------------
print("\n15. np.random.gamma()  → Gamma Distribution")
print(np.random.gamma(2, 2, 5))

# --------------------------------------------------
print("\n16. np.random.lognormal()  → Log-Normal Distribution")
print(np.random.lognormal(0, 1, 5))

# --------------------------------------------------
print("\n17. np.random.triangular()  → Triangular Distribution")
print(np.random.triangular(1, 5, 10, 5))

# --------------------------------------------------
print("\n18. np.random.weibull()  → Weibull Distribution")
print(np.random.weibull(1.5, 5))

# --------------------------------------------------
print("\n19. np.random.bytes()  → Random Bytes")
print(np.random.bytes(10))

# --------------------------------------------------
print("\n20. np.random.default_rng()  → New Generator API")
rng = np.random.default_rng(123)
print(rng.integers(1, 10, 5))
print(rng.random((2, 3)))

# --------------------------------------------------

print("\n" + "="*70)
print("END OF FILE")
print("="*70)
