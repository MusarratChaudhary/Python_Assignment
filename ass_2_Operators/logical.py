# LOGICAL OPERATORS IN PYTHON
# Logical operators are used to combine conditional statements.
# These always return the result in True or False.
# Logical Operators only work with Boolean values (True/False).
# They always follow Binary Logic (0, 1).

# AND OPERATOR
# Returns True if both statements are true. 
# If even one statement is false among them, it will return False.
a = 10
b = 20

print(a > 5 and b > 15)  # Output: True (Both conditions are True)

# OR OPERATOR
# Returns True if at least one statement is true.
# If both conditions are False, it will return False.
a = 10
b = 5

print(a > 15 or b > 3)  # Output: True (One condition is True)

# NOT OPERATOR
# Reverse the result, returns False if the result is true & returns True if the result is false
a = 10

print(not(a > 5))  # Output: False (a > 5 is True but NOT makes it False)
