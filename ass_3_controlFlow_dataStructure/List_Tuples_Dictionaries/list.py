# -----------------------------
# ------------LIST-------------
# -----------------------------

# Lists are used to store multiple items in one variable.
# Lists are ordered, changeable (mutable), and allow duplicate values.
# A list can store different data types like string, integer, float.
# Ex: my_list = ["abc", 10, True]
# List items are written inside square brackets [ ] and separated by commas (,).

fruits = ["Apple", "Mango", "Banana", "Cherry", "Melon"]
print(fruits)

# LIST LENGTH 
print(len(fruits))                 # Shows how many items are in the list

# LIST INDEXING -> List items are indexed, 1st item = [0], 2nd = [1], and so on.
print(fruits[0])
print(fruits[-1])                  # Right to left, -1 = last item.

# LIST SLCING -> Access specific elements easily from a list.
print(fruits[1:4])                 # # Get elements from index 1 to 3 (4 is excluded)

# APPEND -> Add item at the end
fruits.append("Orange")            # Adds 'Orange' at the end of the list
print("After Append:", fruits)

# INSERT -> Add item at specific position
fruits.insert(1, "Grapes")         # Adds 'Grapes' at index 1
print("After Insert:", fruits)

# REMOVE -> Remove specific item
fruits.remove("Mango")             # Removes 'Mango' from the list
print("After Remove:", fruits)

# POP -> Remove item by index (default: last item)
fruits.pop()                       # Removes last item ('Orange')
fruits.pop(2)                      # Removes item at index 2
print("After Pop:", fruits)

# SORT -> Arrange items in alphabetical order
fruits.sort()                  
print("After Sort:", fruits)

# REVERSE -> Reverse the list order
fruits.reverse()               
print("After Reverse:", fruits)

# COUNT -> Count how many times an item appears
print(fruits.count("Apple"))       # Counts how many 'Apple' are in the list

# INDEX -> Find index position of item
print(fruits.index("Cherry"))      # Shows index of 'Cherry'

# EXTEND -> Add another list to current list
seasonal_fruits = ["Strawberries", "Blueberries", "Apricots"]
fruits.extend(seasonal_fruits)
print("After Extend:", fruits)

# COPY -> Make a copy of the list
mix_fruits = fruits.copy()
print("Copy of List:", mix_fruits)

# # CLEAR -> Empty the list
fruits.clear()
print("After Clear:", fruits)      # Output will be []

# ITERATING OVER LIST
fruit = ['APPLE', 'MANGO', 'BANANA']
for item in fruit:
    print(item)
