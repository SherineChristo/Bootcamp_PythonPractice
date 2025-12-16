"""
Topic: Variable Arguments

*args  → multiple positional arguments
**kwargs → multiple keyword arguments
"""

# --------------------------------------------------
# *args EXAMPLE
# --------------------------------------------------

def add_numbers(*args):
    return sum(args)

print(add_numbers(10, 20, 30))
# Output: 60


# --------------------------------------------------
# **kwargs EXAMPLE
# --------------------------------------------------

def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_details(name="Sherine", age=21, dept="CSE")
# Output:
# name : Sherine
# age : 21
# dept : CSE


# --------------------------------------------------
# RULES
# --------------------------------------------------
# 1. *args stores values as a tuple
# 2. **kwargs stores values as a dictionary
# 3. Order: normal → *args → **kwargs

# --------------------------------------------------
# END OF FILE
# --------------------------------------------------
