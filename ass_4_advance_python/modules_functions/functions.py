# ------------FUNCTIONS IN PYTHON-------------
# A function is a block of code that is used to perform a specific task.
# Instead of writing the same code again and again, 
# we define it once inside a function and reuse it whenever needed.

# -----------Why do we use functions?----------
# 1) To reuse code, 2) To make code organized and clean, 3) To divide tasks into smaller parts (modules)

# ____________ 1) SIMPLE FUNCTION ______________
def say_hello():
    print("1) " + "Hello! Welcome to My World!")

# Calling the function
say_hello()

# ____________ 2) FUNCTION WITH PARAMETERS ____________
def greet(name):
    print("2) " + "Hello! " + name )

greet("Musarrat")

# ____________ 3) Function with Return Value _____________
def greet(name):
    return "Hello " + name + "!"

# Function call with return values
message = greet("Musarrat Chaudhary")
print("3)",message)

# ___________ 4) Function with Multiple Parameters ___________
def full_name(first, last):
    return first + last

print("4)",full_name("Musarrat ","Chaudhry"))

# ____________ 5) Default Arguments _____________
def info(name, age = 22):
    print("5)", name, age)
    return 
info("Musarrat")

# ____________ 6) Positional Arguments _______________
def info(name, age):
    print("6)", name, age)

"""These are the arguments that are passed in the same order as defined in the function.
Position matters!"""
info("musarrat",22)

"The function will run without error, BUT the values are in the wrong positions."
# info(22, "musarrat")

# _____________ 7) Positional-Only Arguments ______________
"All the arguments before this symbol will be treated as positional-only."
def info(name, age,/, education):
    print("7)", name, age, education)
"Position/Order matters for positional argument"
info("musarrat",22, education="b.com")

# ______________ 8) Keyword Arguments ___________________
def info(name, age, education, university):
    print("8)", name, age, education, university)
    "Python allows to pass function arguments in the form of keywords which are also called named arguments"
info(name="Musarrat",age=22, education="B.com", university="Karachi University")

"Use parameter names, order doesn’t matter"
# info(age=22, name="musarrat")

# _____________ 9) Keyword-Only Arguments _______________
"When we define a function and use an asterisk *, all the arguments that come after it must be passed using their names (as keyword arguments) only"
def full_info(name,*,age, education, university):
   print("9)", name + " is " + str(age) + " years old.I have completed my " + education + " from " + university)

"The arguments before the asterisk are positional, and after astrik argument must be passed as key-value pairs."
full_info("Musarrat",age=22, education="B.com", university="Karachi University")

# ______________ 10) Arbitrary Arguments _______________
# -------------- 1) *args --------------
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
" With *args, you pass positional arguments, and it comes in the form of a tuple."
def my_hobbies(*hobbies):
    print("9)",hobbies)

my_hobbies("Reading", "Drawing", "Gardening")

# --------------- 2) **kwargs ---------------
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
"2) With **kwargs, you pass keyword arguments, and it comes in the form of a dictionary."
def daily_routine(**routine):
    print("10)",routine)

daily_routine(morning = "home chores", afternoon = "study", night = "coding")

# _____________ 11) Types Of Functions ____________
# 1. Built-in Functions – (Already in Python)
# These are ready-made functions that come with Python. You don’t have to make or install them.
print("11)","Hello")      
len("Hello")        
type(5)              

# 2. User-Defined Functions – (Made by us)
# These are the functions we create ourselves to reuse code and make our program neat.
def greet(name):
    print("Hello " + name)

greet("Musarrat")

# 3. Third-Party Functions – (From other libraries)
# These functions come from outside libraries. We need to install them (like with pip) and then import them.
import math

print(math.sqrt(25))             # Finds square root

# ______________ 12) Variable Scope _____________
# In Python, variable scope refers to where a variable is accessible or visible in your program. There are mainly four types of variable scopes:

# 1. Local Scope
# A variable that is created inside a function is in the local scope.
# It can only be accessed within that function.
def my_function():
    x = 10                  # x is in local scope
    print("Local Scope:",x)

my_function()
# print(x)                  # This will give an error because x is not accessible outside the function.

# 2. Global Scope
# A variable that is created outside of any function is in the global scope.
# It can be accessed anywhere in the program, including inside functions.

x = 20                      # x is in global scope

def my_function():
    print("Global Scope:",x)                # Can access the global variable

my_function()                               # Output: 20
print("Global Scope:",x)                    # Output: 20

# 3. Enclosing Scope (Nonlocal)
# This scope exists in nested functions (i.e., functions inside functions).
# The variable is in the enclosing function's scope, and it can be accessed by the inner function.
def outer_function():
    x = 30                  # x is in the enclosing scope

    def inner_function():
        print("Enclosing Scope:",x)            # Accesses x from the enclosing scope

    inner_function()

outer_function()            # Output: 30

# 4. Built-in Scope
# This is the widest scope, and it contains all the built-in functions and objects provided by Python, 
# like print(), len(), etc.
# These are always available for use.

print("Built-in Scope:",len("Hello"))         # len() is from the built-in scope

# NOTE:
# Python uses the LEGB rule to determine the scope of a variable,
# If a variable isn't found in the local scope, Python looks for it in the enclosing, global, and built-in scopes, in that order.
