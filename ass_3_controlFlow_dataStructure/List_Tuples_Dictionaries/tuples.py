# -------------------------------
# ------------TUPLES-------------
# -------------------------------

# Tuples are similar to lists, but they are unchangeable (immutable).
# In Tuples, multiple items are stored inside round brackets ( ).
# The order is fixed, duplicates are allowed, but items cannot be updated, changed, added or removed.

# --------- Why Use Tuple Instead of List?-----------

# When data needs to stay fixed, so no one accidentally changes it.
# Tuples are faster and more memory efficient than lists.

fruits = ("Apple", "Mango", "Banana", "Cherry", "Melon")
print(fruits)

print(len(fruits))                 # Shows how many items are in the tuple

# TUPLE INDEXING -> Items are indexed like lists, first item is [0], second is [1]
print(fruits[0])                   # First item
print(fruits[-1])                  # Last item (Negative indexing)

# TUPLE SLICING -> Access specific elements
print(fruits[1:4])                 # # Get elements from index 1 to 3 (4 is excluded)

# COUNT -> Count how many times an item appears
print(fruits.count("Apple"))       # Counts how many 'Apple' are in the tuple

# INDEX -> Find index position of item
print(fruits.index("Cherry"))      # Shows index of 'Cherry'

# CONVERT TUPLE TO LIST -> To make it changeable
fruits_list = list(fruits)
fruits_list.append("Orange")
print("After Convert to List and Append:", fruits_list)

# NESTED TUPLE -> Tuple inside tuple
nested = ("Fruit", ("Apple", "Banana"))
print(nested)

# SINGLE ITEM TUPLE -> Must add comma
single = ("Apple",)
print(type(single))                # <class 'tuple'>
