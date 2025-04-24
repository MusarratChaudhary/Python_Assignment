# ---------MODULE---------
# A module in Python is just a file that contains some Python code.
# This code can have functions, variables, or classes inside it.
# We can reuse this module in other Python files by importing it.
# Modules help to keep the code organized, clean, and easy to understand.


# ----------TYPES OF MODULE IN PYTHON----------

# ---------- 1. Built-in Modules (Standard Library):
# Pre-installed modules in python.
# We don’t need to install them separately.

# => Examples: math, random, os, sys
# These built-in modules help us perform various tasks easily, 
# like doing math operations, working with files, or generating random numbers.

# => Code Example:
import random
print("Random number:",random.randint(2,10))

import math

number = 16
square_root = math.sqrt(number)
print("Square root of", number, "is:", square_root)

# -----------2. User-Defined Module in Python:
# A user-defined module is a Python file that we create ourselves to store functions, variables, or classes.
# We can use this module in other Python files by importing it.
# It helps us reuse our code and keep it organized.

# => Code Example:
def sum(a,b):
    return a + b

# ------------3. External Module in Python(Third Party Library):
# An external module is a module that is not built-in.
# We need to install external modules first using pip (Python’s package installer).
# External modules are mostly third-party libraries like: numpy, pandas, requests

# =>  Steps to Use an External Module:
#      1) Install the module using pip
#      2) Import the module in your Python file
#      3) Use the functions of that module

# Code Example:
import requests as req 
import pprint
response = req.get("https://www.asharib.xyz/api/profile")
pprint.pprint(response.json())

# -----------How to Import a Module in Python?-----------
# 1. Basic Import =>  We import the whole module and use its name to call functions.

import math                # importing the built-in math module
print("Basic Import: Sqrt of 25 is:",math.sqrt(25))       # using sqrt function from math module

# 2. Import with Alias (as) => We can give a short name (alias) to the module.

import math as m          # giving 'math' module a short name 'm'
print("Import with alias: Sqrt of 16 is:",m.sqrt(16))         # now we use m.sqrt instead of math.sqrt

# 3. Import Specific Function or Variable => We can import only the part we need from the module.

from math import pi, sqrt  # importing only 'pi' and 'sqrt' from math module

print(pi)                  # pi is a math constant (approx. 3.14), used in circle formulas
print(sqrt(9))             # prints the square root of 9

# 4. Import Everything => This imports all functions and variables from a module.

from math import *         # importing everything from math

print("Import everything:",cos(0))              # directly using functions without writing module name

# Note: Using 'from math import *' is not recommended in big projects 
# because it can confuse which functions are coming from where.
