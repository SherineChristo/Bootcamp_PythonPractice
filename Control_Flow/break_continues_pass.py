"""
Topic: break, continue, pass in Python

Used to control loop execution.
"""

# --------------------------------------------------
# BREAK EXAMPLE
# --------------------------------------------------

for num in range(1, 6):
    if num == 4:
        break
    print(num)

# Output:
# 1
# 2
# 3


# --------------------------------------------------
# CONTINUE EXAMPLE
# --------------------------------------------------

for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# Output:
# 1
# 2
# 4
# 5


# --------------------------------------------------
# PASS EXAMPLE
# --------------------------------------------------

for num in range(1, 4):
    if num == 2:
        pass
    print(num)

# Output:
# 1
# 2
# 3


# --------------------------------------------------
# RULES
# --------------------------------------------------
# break → exits loop
# continue → skips iteration
# pass → placeholder (does nothing)

# --------------------------------------------------
# END OF FILE
# --------------------------------------------------
