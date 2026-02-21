"""
NUMPY + PANDAS
"""

import numpy as np
import pandas as pd

print("="*80)
print("1. CREATING PANDAS OBJECTS FROM NUMPY")
print("="*80)

# NumPy array → Series
arr_1d = np.array([10, 20, 30, 40])
s = pd.Series(arr_1d)
print("Series from NumPy:\n", s)

# NumPy array → DataFrame
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
df = pd.DataFrame(arr_2d, columns=["A", "B"])
print("\nDataFrame from NumPy:\n", df)

# --------------------------------------------------
print("\n" + "="*80)
print("2. DATAFRAME → NUMPY ARRAY")
print("="*80)

np_array = df.to_numpy()
print("DataFrame to NumPy array:\n", np_array)
print("dtype:", np_array.dtype)

# --------------------------------------------------
print("\n" + "="*80)
print("3. NUMPY FUNCTIONS ON PANDAS DATA")
print("="*80)

print("Mean (np.mean):", np.mean(df["A"]))
print("Sum (np.sum):", np.sum(df["B"]))
print("Max (np.max):", np.max(df))

# --------------------------------------------------
print("\n" + "="*80)
print("4. VECTORIZATION (NUMPY STYLE) IN PANDAS")
print("="*80)

df["C"] = df["A"] + df["B"]
df["D"] = np.sqrt(df["C"])
print(df)

# --------------------------------------------------
print("\n" + "="*80)
print("5. CONDITIONAL LOGIC (np.where)")
print("="*80)

df["Status"] = np.where(df["C"] > 5, "High", "Low")
print(df)

# --------------------------------------------------
print("\n" + "="*80)
print("6. BOOLEAN MASKING (NUMPY STYLE)")
print("="*80)

mask = df["A"].to_numpy() > 2
print("Mask:", mask)
print("Filtered rows:\n", df[mask])

# --------------------------------------------------
print("\n" + "="*80)
print("7. NUMPY AGGREGATION VS PANDAS")
print("="*80)

print("np.mean:", np.mean(df["A"]))
print("pd.mean:", df["A"].mean())

print("np.std:", np.std(df["A"]))
print("pd.std:", df["A"].std())

# --------------------------------------------------
print("\n" + "="*80)
print("8. NUMPY BROADCASTING WITH DATAFRAME")
print("="*80)

add_arr = np.array([100, 200])
df_broadcast = df[["A", "B"]] + add_arr
print(df_broadcast)

# --------------------------------------------------
print("\n" + "="*80)
print("9. NUMPY RANDOM DATA IN PANDAS")
print("="*80)

random_df = pd.DataFrame(
    np.random.randn(5, 3),
    columns=["X", "Y", "Z"]
)
print(random_df)

# --------------------------------------------------
print("\n" + "="*80)
print("10. NUMPY SORTING WITH PANDAS")
print("="*80)

sorted_df = df.iloc[np.argsort(df["C"].to_numpy())]
print(sorted_df)

# --------------------------------------------------
print("\n" + "="*80)
print("11. NUMPY SEARCHING IN PANDAS")
print("="*80)

positions = np.where(df["C"].to_numpy() > 5)
print("Positions where C > 5:", positions)

# --------------------------------------------------
print("\n" + "="*80)
print("12. NUMPY APPLY ALONG AXIS (ADVANCED)")
print("="*80)

values = df[["A", "B", "C"]].to_numpy()
row_sum = np.apply_along_axis(np.sum, axis=1, arr=values)
df["Row_Sum"] = row_sum
print(df)

# --------------------------------------------------
print("\n" + "="*80)
print("13. NUMPY + GROUPBY (HYBRID STYLE)")
print("="*80)

df_group = pd.DataFrame({
    "Dept": ["IT", "HR", "IT", "HR"],
    "Salary": [50000, 60000, 55000, 65000]
})

print(df_group)

group_mean = df_group.groupby("Dept")["Salary"].apply(np.mean)
print("\nGroup mean using NumPy:\n", group_mean)

# --------------------------------------------------
print("\n" + "="*80)
print("14. NUMPY CLIPPING & ROUNDING")
print("="*80)

df["Clipped"] = np.clip(df["C"], 4, 7)
df["Rounded"] = np.round(df["D"], 2)
print(df)

# --------------------------------------------------
print("\n" + "="*80)
print("15. NUMPY NAN HANDLING IN PANDAS")
print("="*80)

df_nan = pd.DataFrame({
    "A": [1, 2, np.nan, 4],
    "B": [5, np.nan, 7, 8]
})

print(df_nan)
print("np.isnan:\n", np.isnan(df_nan))
print("np.nanmean:", np.nanmean(df_nan.to_numpy()))

# --------------------------------------------------
print("\n" + "="*80)
print("SUMMARY")
print("="*80)

print("""
✔ Pandas is built on NumPy
✔ NumPy does heavy numerical computation
✔ Pandas handles labels, missing data, tables
✔ Best practice: Use NumPy inside Pandas operations
""")

print("="*80)
print("END OF FILE")
print("="*80)
