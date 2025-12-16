"""
Topic: Operators in Python

This file explains:
1. Arithmetic operators
2. Comparison operators
3. Logical operators
4. Bitwise operators
5. Assignment operators
6. Identity and Membership operators

All examples are real-time and assignment-ready.
"""

# --------------------------------------------------
# 1. ARITHMETIC OPERATORS
# --------------------------------------------------

# Used to perform mathematical calculations
# Operators: +, -, *, /, %, //, **

# Real-time example: Shopping bill calculation

price = 500
quantity = 3

print("\nArithmetic Operators:")

print("Addition:", price + quantity)        # +
print("Subtraction:", price - quantity)     # -
print("Multiplication:", price * quantity)  # *
print("Division:", price / quantity)        # /
print("Modulus:", price % quantity)         # %
print("Floor Division:", price // quantity) # //
print("Exponent:", price ** 2)               # **


# --------------------------------------------------
# 2. COMPARISON OPERATORS
# --------------------------------------------------

# Used to compare two values
# Operators: ==, !=, >, <, >=, <=
# Output will always be True or False

age = 21

print("\nComparison Operators:")

print(age == 21)   # Equal to
print(age != 18)   # Not equal to
print(age > 18)    # Greater than
print(age < 30)    # Less than
print(age >= 21)   # Greater than or equal to
print(age <= 25)   # Less than or equal to


# --------------------------------------------------
# 3. LOGICAL OPERATORS
# --------------------------------------------------

# Used to combine conditional statements
# Operators: and, or, not

is_logged_in = True
has_permission = False

print("\nLogical Operators:")

print(is_logged_in and has_permission)  # True only if both are True
print(is_logged_in or has_permission)   # True if at least one is True
print(not is_logged_in)                 # Reverses the condition


# --------------------------------------------------
# 4. BITWISE OPERATORS
# --------------------------------------------------

# Used to perform operations at the binary level
# Operators: &, |, ^, ~, <<, >>

a = 5   # Binary: 0101
b = 3   # Binary: 0011

print("\nBitwise Operators:")

print("AND:", a & b)        # 0001
print("OR:", a | b)         # 0111
print("XOR:", a ^ b)        # 0110
print("NOT:", ~a)           # Bitwise NOT
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)


# --------------------------------------------------
# 5. ASSIGNMENT OPERATORS
# --------------------------------------------------

# Used to assign and update values
# Operators: =, +=, -=, *=, /=, %=, //=, **=

marks = 50

print("\nAssignment Operators:")

marks += 10
print("After += :", marks)

marks -= 5
print("After -= :", marks)

marks *= 2
print("After *= :", marks)

marks /= 5
print("After /= :", marks)

marks //= 2
print("After //= :", marks)

marks **= 2
print("After **= :", marks)


# --------------------------------------------------
# 6. IDENTITY OPERATORS
# --------------------------------------------------

# Used to compare memory locations
# Operators: is, is not

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("\nIdentity Operators:")

print(x is y)      # False (different memory)
print(x is z)      # True (same memory)
print(x is not y)  # True


# --------------------------------------------------
# 7. MEMBERSHIP OPERATORS
# --------------------------------------------------

# Used to check presence in a sequence
# Operators: in, not in

subjects = ["Math", "Physics", "AI"]

print("\nMembership Operators:")

print("AI" in subjects)
print("Biology" not in subjects)


# --------------------------------------------------
# END OF FILE
# --------------------------------------------------
