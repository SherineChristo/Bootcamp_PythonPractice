"""
Topic: Variable Scope in Python

Types:
1. Local
2. Global
3. Nonlocal
"""

# --------------------------------------------------
# LOCAL SCOPE
# --------------------------------------------------

def local_example():
    x = 10
    print(x)

local_example()
# Output: 10

# print(x)  ❌ Error (x is local)


# --------------------------------------------------
# GLOBAL SCOPE
# --------------------------------------------------

y = 20

def global_example():
    print(y)

global_example()
# Output: 20


# --------------------------------------------------
# MODIFY GLOBAL VARIABLE
# --------------------------------------------------

count = 0

def update_count():
    global count
    count += 1

update_count()
print(count)
# Output: 1


# --------------------------------------------------
# NONLOCAL SCOPE
# --------------------------------------------------

def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"

    inner()
    print(x)

outer()
# Output: inner


# --------------------------------------------------
# RULES
# --------------------------------------------------
# 1. Local variables exist inside functions
# 2. Global variables exist outside functions
# 3. global keyword modifies global variables
# 4. nonlocal modifies variable from outer function

# --------------------------------------------------
# END OF FILE
# --------------------------------------------------
