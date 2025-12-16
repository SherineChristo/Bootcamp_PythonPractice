"""
Topic: Default Arguments

Default arguments take a value if no argument is passed.
"""

# --------------------------------------------------
# DEFAULT ARGUMENT EXAMPLE
# --------------------------------------------------

def greet_user(name="User"):
    print("Hello", name)

greet_user()
# Output: Hello User

greet_user("Sherine")
# Output: Hello Sherine


# --------------------------------------------------
# RULES
# --------------------------------------------------
# 1. Default arguments must be at the end
# 2. They are optional while calling the function
# 3. Avoid mutable default arguments (list, dict)

# --------------------------------------------------
# END OF FILE
# --------------------------------------------------
