"""
Topic: Dictionary in Python

Dictionary stores data in key-value pairs.
"""

# --------------------------------------------------
# CREATING A DICTIONARY
# --------------------------------------------------

student = {
    "name": "Sherine",
    "age": 21,
    "cgpa": 8.9
}

print(student)
# Output: {'name': 'Sherine', 'age': 21, 'cgpa': 8.9}


# --------------------------------------------------
# CRUD OPERATIONS
# --------------------------------------------------

# CREATE / UPDATE
student["department"] = "CSE"
student["age"] = 22

# READ
print(student["name"])   # Output: Sherine

# DELETE
del student["cgpa"]

print(student)
# Output: {'name': 'Sherine', 'age': 22, 'department': 'CSE'}


# --------------------------------------------------
# ITERATION
# --------------------------------------------------

for key in student:
    print(key, student[key])
# Output:
# name Sherine
# age 22
# department CSE


# --------------------------------------------------
# RULES
# --------------------------------------------------
# 1. Keys must be unique
# 2. Keys must be immutable
# 3. Values can be any type

# --------------------------------------------------
# END OF FILE
# --------------------------------------------------
