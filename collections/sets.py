"""
Topic: Sets in Python

Sets store UNIQUE, unordered elements.
"""

# --------------------------------------------------
# CREATING A SET
# --------------------------------------------------

skills = {"Python", "Java", "Python", "SQL"}
print(skills)
# Output: {'Python', 'Java', 'SQL'}


# --------------------------------------------------
# SET OPERATIONS
# --------------------------------------------------

skills.add("AI")
print(skills)
# Output: {'Python', 'Java', 'SQL', 'AI'}

skills.remove("Java")
print(skills)
# Output: {'Python', 'SQL', 'AI'}


# --------------------------------------------------
# MATHEMATICAL OPERATIONS
# --------------------------------------------------

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))        # Output: {1, 2, 3, 4, 5}
print(a.intersection(b)) # Output: {3}
print(a.difference(b))   # Output: {1, 2}


# --------------------------------------------------
# RULES
# --------------------------------------------------
# 1. No duplicates
# 2. Unordered
# 3. Mutable but elements must be immutable

# --------------------------------------------------
# END OF FILE
# --------------------------------------------------
