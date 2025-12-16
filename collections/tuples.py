"""
Topic: Tuples in Python

Tuples are ordered, immutable collections.
"""

# --------------------------------------------------
# CREATING A TUPLE
# --------------------------------------------------

coordinates = (10, 20)
print(coordinates)
# Output: (10, 20)


# --------------------------------------------------
# ACCESSING ELEMENTS
# --------------------------------------------------

print(coordinates[0])  # Output: 10
print(coordinates[1])  # Output: 20


# --------------------------------------------------
# IMMUTABILITY
# --------------------------------------------------

# coordinates[0] = 50  # ❌ Error (Tuples are immutable)


# --------------------------------------------------
# REAL-TIME USE CASE
# --------------------------------------------------

# Fixed configuration values
server_config = ("localhost", 8080)
print(server_config)
# Output: ('localhost', 8080)


# --------------------------------------------------
# RULES
# --------------------------------------------------
# 1. Tuples cannot be modified
# 2. Faster than lists
# 3. Used for fixed data

# --------------------------------------------------
# END OF FILE
# --------------------------------------------------
