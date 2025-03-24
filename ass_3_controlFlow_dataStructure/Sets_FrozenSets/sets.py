# ------------------------------
# -------------SET--------------
# ------------------------------

# Set is a collection used to store multiple items.
# A set can contain different data types.
# Sets are:
# Unordered -> Set items have no fixed order, and can't be accessed by index or key.
# Unchangeable -> means you can't modify/update existing items, but you can add new or remove items.
# Duplicates -> Duplicate values will be ignored. 

# -----------BASIC SETS EXAMPLE-----------

info = {"Ali", 19 , True, 1, False, 0}
print("Set Info:",info)               # In sets, True and 1 are same, & False and 0 are same, treated as duplicates.

# Sets Length
print("Set Length:",len(info))

# Add
info.add("Ayan")
print("After Add:",info)

# Remove
info.remove("Ali")
print("After Remove:",info)

# Iterating over a sets
for val in info:
    print("Set through for loop:",val)

# Clear all items from the sets

info.clear()
print("After clear:",info)                     # Output: set()

# Empty Sets:
# {} -> Python by default treats this as an empty dictionary.
# For empty set -> must use set() because {} will confuse Python as a dictionary.

info = {}
print("Empty dict:",type(info))               # Output: <class 'dict'>

info = set()
print("Empty set:",type(info))               # Output: <class 'set'>


# ---------METHODS IN SETS------------

set1 = {1,4,6,7}
set2 = {3,4,5,8 }
print(set1,set2)

# Union -> Combining items from both sets, without duplicates
print("After union:",set1.union(set2))

# Intersection -> Items that are common in both sets
print("After intersection:",set1.intersection(set2))

# Update -> Updating set1 to keep only items found in both sets
set1.intersection_update(set2)
print("Intersection update:",set1)

# Symmetric Difference ->  Unique items from both sets (no duplicates, no common items).
print("symmetric difference:",set1.symmetric_difference(set2))

# Difference -> items in set2 but not in set1
print("Difference:",set1.difference(set2))

# Add ->  Adding an item to set1
set1.add(9)
print("After add 9:",set1)

# Remove/Discard
set2.remove(6)
print("After remove 6:",set2)                    # Removing an item from set2; raises KeyError if item not found

set2.discard(2)
print("After discard 2:",set2)                    # Discarding an item from set2; does nothing if item not found

# Pop -> pop() removes a random item, not predictable because set is unordered.
set1.pop()
print("After pop:",set1)

# Del -> Deleting set1 entirely
del set1 
print("After delete:",set1)                   # Output: Error -> This would raise a NameError as set1 no longer exists

# Clear ->  Clearing all items from set2
set2.clear()
print("After clear:",set2)                    # Output: set()

# ----------SETS RELATIONSHIPS----------

# 1. issubset() -> Check if all items of one set exist in another (subset).
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print(A.issubset(B))           # Output: True (All items of A are in B)
print(B.issubset(A))           # Output: False

# 2. issuperset() -> Check if one set contains all items of another (superset).
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}

print(A.issuperset(B))         # Output: True (A has all items of B)
print(B.issuperset(A))         # Output: False

# 3. isdisjoint() → Check if two sets have NO common items.
A = {1, 2, 3}
B = {4, 5, 6}
C = {2, 5}

print(A.isdisjoint(B))         # Output: True (No common items)
print(A.isdisjoint(C))         # Output: False (2 is common)
