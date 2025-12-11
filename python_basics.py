"""
Python Basics – Assignment Notes
This file contains command-style explanations for:
1. What is Python?
2. Python interpreter & pip
3. Virtual environments (venv)
4. Running Python scripts
5. Comments & docstrings
"""

# -----------------------------------------------------------
# 1. WHAT IS PYTHON?
# -----------------------------------------------------------
"""
COMMAND:
Python is a high-level, interpreted programming language used for:
- Web development
- Data science
- Machine learning
- Scripting & automation
- Cybersecurity
- IoT and more

Python features:
- Easy syntax
- Large community
- Cross-platform
- Huge library support
"""


# -----------------------------------------------------------
# 2. PYTHON INTERPRETER & pip
# -----------------------------------------------------------

"""
COMMAND:
python --version             # Check Python version
which python                # (mac/Linux) Find Python interpreter path
where python                # (Windows) Find Python interpreter path

pip --version               # Check pip version
pip list                    # List installed packages
pip install <package>       # Install a package
pip uninstall <package>     # Uninstall a package
pip freeze                  # Show installed packages with versions
"""


# -----------------------------------------------------------
# 3. VIRTUAL ENVIRONMENTS (venv)
# -----------------------------------------------------------

"""
COMMAND:
python -m venv myenv        # Create a virtual environment

# Activate virtual environment
source myenv/bin/activate   # macOS / Linux
myenv\Scripts\activate      # Windows

pip install <package>       # Installs INSIDE venv only

deactivate                   # Exit virtual environment

# Delete environment simply by deleting the folder:
rm -rf myenv                # macOS / Linux
rmdir /s myenv              # Windows
"""


# -----------------------------------------------------------
# 4. RUNNING PYTHON SCRIPTS
# -----------------------------------------------------------

"""
COMMAND:
python file.py              # Run a Python script
python -c "print('Hello')"  # Run a single-line command
python                      # Open Python interactive shell (REPL)

Example script content:
print("Hello, Python!")
"""


# -----------------------------------------------------------
# 5. COMMENTS & DOCSTRINGS
# -----------------------------------------------------------

# Single-line comment:
# This is a single-line comment

# Multi-line comments (unofficial but used):
# Line 1
# Line 2
# Line 3

"""
Docstring Example:
A docstring provides documentation inside functions, classes, or modules.
Use triple quotes to write a docstring.
"""

def add(a, b):
    """
    Function: add
    Description: Returns the sum of two numbers.
    Parameters:
        a (int or float)
        b (int or float)
    Returns:
        Sum of a and b
    """
    return a + b


# Example call
result = add(5, 7)
print("Result of add(5,7):", result)
