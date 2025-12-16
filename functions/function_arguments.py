"""
Topic: Function Arguments

Types:
1. Positional arguments
2. Keyword arguments
"""

# --------------------------------------------------
# POSITIONAL ARGUMENTS
# --------------------------------------------------

def student_info(name, age):
    print(name, age)

student_info("Sherine", 21)
# Output: Sherine 21


# --------------------------------------------------
# KEYWORD ARGUMENTS
# --------------------------------------------------

student_info(age=21, name="Sherine")
# Output: Sherine 21


# --------------------------------------------------
# RULES
# --------------------------------------------------
# 1. Positional arguments follow order
# 2. Keyword arguments use parameter names
# 3. Keyword arguments can be in any order
# 4. Positional arguments must come before keyword arguments

# --------------------------------------------------
# END OF FILE
# --------------------------------------------------
