"""
Topic: Strings in Python (Very Important)

This file explains:
1. String indexing
2. String slicing
3. Common string methods
4. String formatting
5. Raw strings

All examples include outputs as comments.
"""

# --------------------------------------------------
# 1. STRING INDEXING
# --------------------------------------------------

# Indexing allows access to individual characters
# Index starts from 0 (left to right)
# Negative indexing starts from -1 (right to left)

text = "Python"

print(text[0])     # Output: P
print(text[3])     # Output: h
print(text[-1])    # Output: n
print(text[-4])    # Output: t


# --------------------------------------------------
# 2. STRING SLICING
# --------------------------------------------------

# Slicing extracts a part of the string
# Syntax: string[start : end : step]
# End index is not included

language = "Programming"

print(language[0:6])      # Output: Progra
print(language[3:8])      # Output: gramm
print(language[:7])       # Output: Program
print(language[7:])       # Output: ming
print(language[::2])      # Output: Pormig
print(language[::-1])     # Output: gnimmargorP


# --------------------------------------------------
# 3. STRING METHODS
# --------------------------------------------------

sentence = "python is very powerful"

# split() → splits string into a list
words = sentence.split(" ")
print(words)  
# Output: ['python', 'is', 'very', 'powerful']

# join() → joins list into a string
joined_sentence = " ".join(words)
print(joined_sentence)  
# Output: python is very powerful

# replace() → replaces part of a string
updated_sentence = sentence.replace("python", "Python")
print(updated_sentence)  
# Output: Python is very powerful

# upper() → converts to uppercase
print(sentence.upper())  
# Output: PYTHON IS VERY POWERFUL

# lower() → converts to lowercase
print("HELLO".lower())  
# Output: hello

# strip() → removes leading and trailing spaces
text_with_spaces = "  hello world  "
print(text_with_spaces.strip())  
# Output: hello world

# startswith() and endswith()
print(sentence.startswith("python"))  # Output: True
print(sentence.endswith("powerful"))  # Output: True


# --------------------------------------------------
# 4. STRING FORMATTING
# --------------------------------------------------

name = "Sherine"
age = 21
cgpa = 8.9

# f-strings (Recommended & Fast)
print(f"My name is {name}, age is {age}, CGPA is {cgpa}")
# Output: My name is Sherine, age is 21, CGPA is 8.9

# .format() method
print("My name is {}, age is {}, CGPA is {}".format(name, age, cgpa))
# Output: My name is Sherine, age is 21, CGPA is 8.9

# Indexed format
print("Name: {0}, Age: {1}".format(name, age))
# Output: Name: Sherine, Age: 21


# --------------------------------------------------
# 5. RAW STRINGS
# --------------------------------------------------

# Raw strings ignore escape characters
# Very useful for file paths and regex

normal_string = "C:\\new_folder\\test.txt"
raw_string = r"C:\new_folder\test.txt"

print(normal_string)
# Output: C:\new_folder\test.txt

print(raw_string)
# Output: C:\new_folder\test.txt


# --------------------------------------------------
# IMPORTANT RULES ABOUT STRINGS
# --------------------------------------------------

# 1. Strings are IMMUTABLE
# 2. Indexing starts from 0
# 3. Slicing does not modify the original string
# 4. Methods return a new string

word = "Hello"
# word[0] = "h"  # ❌ Error (Immutable)

print(word)
# Output: Hello


# --------------------------------------------------
# END OF FILE
# --------------------------------------------------
