"""
Topic: Variables & Data Types in Python

This file explains:
1. Variables and naming rules
2. Basic data types (int, float, bool, str, None)
3. Type casting
4. Mutable vs Immutable data types

All examples are real-time and assignment-ready.
"""

# --------------------------------------------------
# 1. VARIABLES
# --------------------------------------------------

# A variable is a name that stores a value in memory.
# Python is dynamically typed, so no need to specify the type.

# Variable Naming Rules:
# 1. Must start with a letter or underscore (_)
# 2. Cannot start with a number
# 3. Can contain letters, numbers, and underscores
# 4. Case-sensitive
# 5. Cannot use Python keywords

user_name = "Sherine"
user_age = 21

print("User Name:", user_name)
print("User Age:", user_age)


# --------------------------------------------------
# 2. DATA TYPES
# --------------------------------------------------

# -------- int (Integer) --------
# Stores whole numbers
# Real-time example: Number of items in a cart

cart_items = 5
print("\nInteger Example:")
print(cart_items)
print(type(cart_items))


# -------- float (Floating Point) --------
# Stores decimal values
# Real-time example: Product price

product_price = 249.75
print("\nFloat Example:")
print(product_price)
print(type(product_price))


# -------- bool (Boolean) --------
# Stores True or False
# Real-time example: Login status

is_logged_in = True
print("\nBoolean Example:")
print(is_logged_in)
print(type(is_logged_in))


# -------- str (String) --------
# Stores text data
# Real-time example: User name

student_name = "Sherine Delphina"
print("\nString Example:")
print(student_name)
print(type(student_name))


# -------- None --------
# Represents no value
# Real-time example: Profile picture not uploaded yet

profile_picture = None
print("\nNone Example:")
print(profile_picture)
print(type(profile_picture))


# --------------------------------------------------
# 3. TYPE CASTING
# --------------------------------------------------

# Type casting converts one data type to another
# Common functions: int(), float(), str(), bool()

# Real-time example: User input is always a string

age_input = "21"
age = int(age_input)  # converting string to integer

print("\nType Casting Example:")
print(age)
print(type(age))


# Another example: int to string

price = 100
price_str = str(price)

print(price_str)
print(type(price_str))


# --------------------------------------------------
# 4. MUTABLE VS IMMUTABLE DATA TYPES
# --------------------------------------------------

# -------- IMMUTABLE TYPES --------
# Cannot be changed after creation
# Examples: int, float, bool, str, tuple

name = "Sherine"
# name[0] = "A"  # This will cause an error because strings are immutable
print("\nImmutable Example (String):")
print(name)


# -------- MUTABLE TYPES --------
# Can be changed after creation
# Examples: list, dict, set

subjects = ["Math", "Science", "English"]
subjects[1] = "Computer Science"

print("\nMutable Example (List):")
print(subjects)


# --------------------------------------------------
# 5. REAL-TIME COMBINED EXAMPLE
# --------------------------------------------------

# Student information system example

student_name = "Sherine"
student_age = 21
attendance_percentage = 92.5
is_present = True
remarks = None

enrolled_subjects = ["Math", "Physics"]
enrolled_subjects.append("AI")

print("\nReal-Time Student Example:")
print("Name:", student_name)
print("Age:", student_age)
print("Attendance:", attendance_percentage)
print("Present:", is_present)
print("Remarks:", remarks)
print("Subjects:", enrolled_subjects)


# --------------------------------------------------
# END OF FILE
# --------------------------------------------------
