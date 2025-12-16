"""
Topic: if / elif / else in Python

Used for decision making based on conditions.
"""

# --------------------------------------------------
# REAL-TIME EXAMPLE: STUDENT GRADING SYSTEM
# --------------------------------------------------

marks = 78

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print(grade)
# Output: B


# --------------------------------------------------
# RULES
# --------------------------------------------------
# 1. Indentation is mandatory (4 spaces recommended)
# 2. elif can be used multiple times
# 3. else is optional but must be last
# 4. Conditions are evaluated top to bottom

# --------------------------------------------------
# END OF FILE
# --------------------------------------------------
