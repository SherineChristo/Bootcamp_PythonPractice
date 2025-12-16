"""
Topic: Defining Functions and Return Values

A function is a reusable block of code that performs a specific task.
"""

# --------------------------------------------------
# FUNCTION DEFINITION
# --------------------------------------------------

def greet():
    print("Hello, Welcome to Python")

greet()
# Output: Hello, Welcome to Python


# --------------------------------------------------
# FUNCTION WITH RETURN VALUE
# --------------------------------------------------

def add(a, b):
    return a + b

result = add(10, 20)
print(result)
# Output: 30


# --------------------------------------------------
# RULES
# --------------------------------------------------
# 1. Use 'def' keyword to define a function
# 2. Function name should be meaningful
# 3. Code inside function must be indented
# 4. return sends value back to caller
# 5. Code after return will not execute

# --------------------------------------------------
# END OF FILE
# --------------------------------------------------
