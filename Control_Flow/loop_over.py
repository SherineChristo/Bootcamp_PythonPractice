"""
Topic: Looping over Lists, Tuples, and Dictionaries
"""

# --------------------------------------------------
# LOOP OVER LIST
# --------------------------------------------------

languages = ["Python", "Java", "C"]

for lang in languages:
    print(lang)

# Output:
# Python
# Java
# C


# --------------------------------------------------
# LOOP OVER TUPLE
# --------------------------------------------------

coordinates = (10, 20, 30)

for value in coordinates:
    print(value)

# Output:
# 10
# 20
# 30


# --------------------------------------------------
# LOOP OVER DICTIONARY
# --------------------------------------------------

student = {
    "name": "Sherine",
    "age": 21,
    "dept": "CSE"
}

# Loop over keys
for key in student:
    print(key)

# Output:
# name
# age
# dept


# Loop over values
for value in student.values():
    print(value)

# Output:
# Sherine
# 21
# CSE


# Loop over key-value pairs
for key, value in student.items():
    print(key, ":", value)

# Output:
# name : Sherine
# age : 21
# dept : CSE


# --------------------------------------------------
# RULES
# --------------------------------------------------
# 1. Lists and tuples preserve order
# 2. Dictionaries iterate over keys by default
# 3. items() gives key-value pairs

# --------------------------------------------------
# END OF FILE
# --------------------------------------------------
