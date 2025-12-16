"""
Topic: Arrays in Python

Arrays store elements of the SAME data type.
Python arrays are provided by the array module.
"""

from array import array

# --------------------------------------------------
# CREATING AN ARRAY
# --------------------------------------------------

# Syntax: array(typecode, elements)
# typecode 'i' → integer

marks = array('i', [85, 90, 78, 92])

print(marks)          # Output: array('i', [85, 90, 78, 92])
print(type(marks))    # Output: <class 'array.array'>


# --------------------------------------------------
# ARRAY OPERATIONS
# --------------------------------------------------

marks.append(88)
print(marks)          # Output: array('i', [85, 90, 78, 92, 88])

marks.remove(78)
print(marks)          # Output: array('i', [85, 90, 92, 88])

print(marks[1])       # Output: 90


# --------------------------------------------------
# RULES
# --------------------------------------------------
# 1. All elements must be of same data type
# 2. Faster than lists for numeric data
# 3. Less flexible than lists

# --------------------------------------------------
# END OF FILE
# --------------------------------------------------
