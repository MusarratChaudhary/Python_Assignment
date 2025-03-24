# -----------FROZEN SET-----------
# Frozenset is just like a set, but it is immutable (unchangeable).
# Once created, you cannot add, remove, or change items in a frozenset.
# Used when you want a set but don't want it to be accidentally changed.
# The frozenset() function takes an optional parameter like a list, tuple, set, 
# or any iterable and converts it into an unchangeable frozenset.


# Creating a frozenset from a list
fruits = frozenset(['apple', 'banana', 'cherry'])
print("Frozen Set:", fruits)  
print(type(fruits))

# -------Try to add an element-----

# fruits.add("mango")
# print(fruits)                     # Output: AttributeError: 'frozenset' object has no attribute 'add'

# -------Try to remove an element-------

# fruits.remove("apple")
# print(fruits)                     # Output: AttributeError: 'frozenset' object has no attribute 'remove'

# Frozensets support set operations like union, intersection, difference, and symmetric difference
set_a = frozenset([1, 2, 3])
set_b = frozenset([3, 4, 5])

# -------Union: combines elements from both sets------

# Frozenset union can be done in two ways:
# 1) Using '|' (pipe) operator
union_set = set_a | set_b
print("Union:", union_set)                              # Output: Union: frozenset({1, 2, 3, 4, 5})

# 2) Using union() method
print("After union:",set_a.union(set_b))                # Output: After union: frozenset({1, 2, 3, 4, 5})
# NOTE:  Both return a new frozenset and do not modify original frozensets.                  

# --------Intersection: elements common to both sets--------

# Frozenset intersecton can be done in two ways:
# 1) Using & operator
intersection_set = set_a & set_b
print("Intersection:", intersection_set)                      # Output: Intersection: frozenset({3})

# 2) Using intersection() method
print("After intersection:",set_a.intersection(set_b))        # Output: After intersection: frozenset({3})

# --------Difference: elements in set_a but not in set_b---------

# Frozenset difference can be done in two ways:
# 1) Using - operator
difference_set = set_a - set_b           
print("Difference:", difference_set)                          # Output: Difference: frozenset({1, 2})

# 2) Using difference() method
print("After difference:",set_a.difference(set_b))             # Output: After difference: frozenset({1, 2})

# -------Symmetric Difference: elements in either set_a or set_b but not in both--------

# Frozenset symetric difference can be done in two ways:
# 1) Using ^ operator
symmetric_difference_set = set_a ^ set_b
print("Symmetric Difference:", symmetric_difference_set)        # Output: Symmetric Difference: frozenset({1, 2, 4, 5})

# 2) Using symmetric_difference() method
print("After symmetric_difference:",set_a.symmetric_difference(set_b))  # Output: After symmetric_difference: frozenset({1, 2, 4, 5})

