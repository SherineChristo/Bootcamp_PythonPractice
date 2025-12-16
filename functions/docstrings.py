"""
Topic: Docstrings

Docstrings explain what a function does.
Used for documentation.
"""

# --------------------------------------------------
# DOCSTRING EXAMPLE
# --------------------------------------------------

def multiply(a, b):
    """
    This function multiplies two numbers
    and returns the result.
    """
    return a * b

print(multiply(4, 5))
# Output: 20

print(multiply.__doc__)
# Output:
# This function multiplies two numbers
# and returns the result.


# --------------------------------------------------
# RULES
# --------------------------------------------------
# 1. Written inside triple quotes
# 2. Placed immediately after function definition
# 3. Used by help() and documentation tools

# --------------------------------------------------
# END OF FILE
# --------------------------------------------------
