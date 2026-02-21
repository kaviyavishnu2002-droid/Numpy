"""
NUMPY STRUCTURED ARRAYS
"""

import numpy as np

print("="*70)
print("1. BASIC STRUCTURED ARRAY")
print("="*70)

dtype_basic = [('id', 'i4'), ('name', 'U10'), ('salary', 'f8')]

data = np.array([
    (1, 'Alice', 50000.0),
    (2, 'Bob',   60000.0),
    (3, 'Carol', 55000.0)
], dtype=dtype_basic)

print(data)
print("Names:", data['name'])
print("Salaries:", data['salary'])

# --------------------------------------------------
print("\n" + "="*70)
print("2. STRUCTURED ARRAY WITH MULTIPLE DATA TYPES")
print("="*70)

dtype_multi = [
    ('emp_id', np.int32),
    ('dept', 'U10'),
    ('age', np.int8),
    ('active', np.bool_)
]

employees = np.array([
    (101, 'IT', 25, True),
    (102, 'HR', 30, False),
    (103, 'IT', 28, True)
], dtype=dtype_multi)

print(employees)

# --------------------------------------------------
print("\n" + "="*70)
print("3. ACCESSING FIELDS")
print("="*70)

print("Employee IDs:", employees['emp_id'])
print("Departments:", employees['dept'])
print("Active employees:", employees[employees['active']])

# --------------------------------------------------
print("\n" + "="*70)
print("4. UPDATING FIELDS")
print("="*70)

employees['age'] += 1
employees['active'] = False
print(employees)

# --------------------------------------------------
print("\n" + "="*70)
print("5. SORTING STRUCTURED ARRAYS")
print("="*70)

sorted_by_age = np.sort(employees, order='age')
print("Sorted by age:\n", sorted_by_age)

sorted_by_dept_age = np.sort(employees, order=['dept', 'age'])
print("Sorted by dept, then age:\n", sorted_by_dept_age)

# --------------------------------------------------
print("\n" + "="*70)
print("6. FILTERING (BOOLEAN MASK)")
print("="*70)

it_employees = employees[employees['dept'] == 'IT']
print(it_employees)

# --------------------------------------------------
print("\n" + "="*70)
print("7. STRUCTURED ARRAY WITH NESTED FIELDS")
print("="*70)

dtype_nested = [
    ('id', 'i4'),
    ('personal', [
        ('name', 'U10'),
        ('age', 'i4')
    ]),
    ('salary', 'f8')
]

nested_data = np.array([
    (1, ('Alice', 25), 50000),
    (2, ('Bob', 30),   60000)
], dtype=dtype_nested)

print(nested_data)
print("Names:", nested_data['personal']['name'])

# --------------------------------------------------
print("\n" + "="*70)
print("8. VIEW AS STRUCTURED ARRAY")
print("="*70)

raw = np.array([
    (1, 25, 50000.0),
    (2, 30, 60000.0)
])

dtype_view = [('id', 'i4'), ('age', 'i4'), ('salary', 'f8')]
# structured_view = raw.view(dtype=dtype_view)

# print(structured_view)

# --------------------------------------------------
print("\n" + "="*70)
print("9. CONVERT STRUCTURED ARRAY TO NORMAL ARRAY")
print("="*70)

# salary_only = structured_view['salary']
# print("Salary column:", salary_only)

# --------------------------------------------------
print("\n" + "="*70)
print("10. UNIQUE, SEARCH & CONDITIONS")
print("="*70)

print("Unique departments:", np.unique(employees['dept']))
print("Index of max age:", np.argmax(employees['age']))
print("Employees age > 26:", employees[employees['age'] > 26])

# --------------------------------------------------
print("\n" + "="*70)
print("11. STRUCTURED ARRAY FROM ZERO INITIALIZATION")
print("="*70)

zeros_struct = np.zeros(3, dtype=dtype_basic)
print(zeros_struct)

# --------------------------------------------------
print("\n" + "="*70)
print("12. RECORD ARRAYS (recarray)")
print("="*70)

rec = data.view(np.recarray)  # lets you access fields using dot notation
print(data['name'])
print(data['salary'])
print(rec.name)
print(rec.salary)

# --------------------------------------------------
print("\n" + "="*70)
print("MULTI FIELD DATAS")
print("="*70)

dtype = [
    ('date', 'U10'),
    ('open', 'f8'),
    ('high', 'f8'),
    ('low', 'f8'),
    ('close', 'f8')
]

data = np.array([
    ('2024-01-01', 100.0, 110.0, 95.0, 105.0),
    ('2024-01-02', 105.0, 115.0, 100.0, 110.0),
    ('2024-01-03', 110.0, 120.0, 108.0, 115.0)
], dtype=dtype)

result = data[['open', 'close']]
print(result)

print("="*70)
print("END OF FILE")
print("="*70)
