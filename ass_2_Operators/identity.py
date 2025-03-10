# IDENTITY OPERATORS IN PYTHON
# Identity operators are used to compare the memory location of two objects.
# These always return the result in True or False.

# IMPORTANT POINT:
# Immutable Data Types (like String, Numbers, Tuples) share the same memory location if their values are the same.
# Mutable Data Types (like List, Dictionary, Set) are always stored at different memory locations 
# even if their values are the same.

# The identity operator consists of "is" and "is not"

# IS OPERATOR
a = "abc"
b = "abc"

print(a is b)    # Output: True (same value means same memory location)

a = "abc"
b = "xyz"

print(a is b)    # Output: False (different value means different memory location)

# IS NOT OPERATOR
# EXAMPLE_1:
a = ["abc","xyz"]
b = ["abc","xyz"]

print(a is b)     # Output: False (same value but different memory location bcz list is mutuable)

# EXAMPLE_2:
a = 20
b = 30

print(a is not b)   # Output: True (because both have different values and different memory location)
