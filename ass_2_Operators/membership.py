# MEMBERSHIP OPERATORS:
# Membership operators are used to check if a value is present in a sequence or not.
# These always return the result in True or False.
# Membership operators only work with Sequences like (List, Tuple, String, Dictionary).


# IN OPERATOR
fruits = ["Apple", "Mango", "Banana"]

print("Apple" in fruits)         # Output: True (Apple present in fruits)
print("Cherry" in fruits)        # Output: False (Cherry is not present)

# NOT IN OPERATOR
num = [1, 2, 3, 4, 5]

print(1 not in num)              # Output: False (1 is present)
print(6 not in num)              # Output: True  (6 is not present)


# DICTIONARY EXAMPLE:
# It checks Keys in the dictionary, not Values.
my_dict = {"name": "XYZ", "course": "Python"}

print("name" in my_dict)         # Output: True (Key is present) 
print("XYZ" in my_dict)       # Output: False