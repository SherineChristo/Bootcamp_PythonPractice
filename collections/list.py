"""
Topic: Lists in Python

Lists are ordered, mutable, and allow duplicate values.
"""

# --------------------------------------------------
# CREATING A LIST
# --------------------------------------------------

subjects = ["Math", "Physics", "Chemistry"]
print(subjects)
# Output: ['Math', 'Physics', 'Chemistry']


# --------------------------------------------------
# LIST OPERATIONS
# --------------------------------------------------

subjects.append("AI")
print(subjects)
# Output: ['Math', 'Physics', 'Chemistry', 'AI']

subjects.insert(1, "Python")
print(subjects)
# Output: ['Math', 'Python', 'Physics', 'Chemistry', 'AI']

subjects.remove("Chemistry")
print(subjects)
# Output: ['Math', 'Python', 'Physics', 'AI']

subjects.pop()
print(subjects)
# Output: ['Math', 'Python', 'Physics']


# --------------------------------------------------
# LIST SLICING
# --------------------------------------------------

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])   # Output: [20, 30, 40]
print(numbers[::-1])  # Output: [50, 40, 30, 20, 10]


# --------------------------------------------------
# LIST COMPREHENSION
# --------------------------------------------------

# Real-time example: square of marks
marks = [60, 70, 80]

squared_marks = [m * m for m in marks]
print(squared_marks)
# Output: [3600, 4900, 6400]


# --------------------------------------------------
# RULES
# --------------------------------------------------
# 1. Lists are mutable
# 2. Allow mixed data types
# 3. Indexing starts from 0

# --------------------------------------------------
# END OF FILE
# --------------------------------------------------
